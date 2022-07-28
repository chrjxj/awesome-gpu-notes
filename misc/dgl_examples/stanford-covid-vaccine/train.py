# -*- coding: utf-8 -*-
"""
"""

import os
import time

import warnings
from copy import copy, deepcopy

import pandas as pd
import numpy as np
import time

import random
from tqdm.notebook import tqdm

from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, Callable, Dict, List, Optional, Sequence, Union

import torch
import torch.nn as nn
from torch.utils import data
from torch.nn import functional as F
from torch.optim import lr_scheduler

import dgl

from model import GCN
from data import CacheDataset

'''
Utils for parsing the RNA data
'''
pred_cols = ['reactivity', 'deg_Mg_pH10', 'deg_pH10', 'deg_Mg_50C', 'deg_50C']

token_to_idx = {
    'sequence': {x:i for i, x in enumerate('ACGU')}, # residue_to_idx
    'structure': {x:i for i, x in enumerate('().')},
    'predicted_loop_type': {x:i for i, x in enumerate('BEHIMSX')},
}

def get_couples(structure):
    """
    For each closing parenthesis, I find the matching opening one and store their index in the couples list.
    The assigned list is used to keep track of the assigned opening parenthesis
    """
    opened = [idx for idx, i in enumerate(structure) if i == '(']
    closed = [idx for idx, i in enumerate(structure) if i == ')']

    assert len(opened) == len(closed)
    assigned = []
    couples = []

    for close_idx in closed:
        for open_idx in opened:
            if open_idx < close_idx:
                if open_idx not in assigned:
                    candidate = open_idx
            else:
                break
        assigned.append(candidate)
        couples.append([candidate, close_idx])
        
    assert len(couples) == len(opened)
    return couples


def build_edge_list(couples: list, size: int) -> tuple:
    '''
    Build edge list representation of the grap from `couples`, the output 
    of `get_couples`. The output of this function will be used to for 
    constructing dgl graph. 
    '''
    src, dst = [], []
    for i in range(size):
        if i < size - 1:
            # neigbouring bases are linked as well
            src.append(i), 
            dst.append(i + 1)
        if i > 0:
            src.append(i)
            dst.append(i - 1)
    
    for i, j in couples:
        src.extend([i, j])
        dst.extend([j, i])
    
    return src, dst

def row_to_graph(row: pd.Series) -> dgl.DGLGraph:
    '''
    Process a row in the RNA data frame and convert to
    a dgl.DGLGraph object.
    '''
    couples = get_couples(row['structure'])
    edge_list = build_edge_list(couples, len(row['structure']))
    # build a dgl.graph
    g = dgl.graph(edge_list)
    # one-hot encoding for three types of node features
    node_features = []
    for node_feature_col in token_to_idx:
        # for each node, perform categorical encoding 
        node_feature = torch.tensor([token_to_idx[node_feature_col][x] for x in row[node_feature_col]])
        # then convert to one-hot
        node_feature = F.one_hot(node_feature, num_classes=len(token_to_idx[node_feature_col]))
        node_features.append(node_feature)
    node_features = torch.cat(node_features, axis=1)
    # attach as node features 
    g.ndata['h'] = node_features.to(torch.float32)
    return g

class RNADataset(CacheDataset):
    '''mRNA stability prediction dataset'''
    def __init__(self, data: Sequence,
        num_workers=8,
        is_train=True):

        self.data = data
        self.pred_cols = ['reactivity', 'deg_Mg_pH10', 'deg_pH10', 'deg_Mg_50C', 'deg_50C']
        self.n_outputs = len(self.pred_cols)
        self.is_train = is_train
        super().__init__(data, num_workers=num_workers, progress=True)

        self.set_data(data)

    def _load_cache_item(self, idx: int):
        """
        Args:
            idx: the index of the input data sequence.
        """
        row = self.data[idx]
        g = row_to_graph(row)
        
        if self.is_train:
            target = np.array(row[self.pred_cols].values.tolist()).T
            target = torch.tensor(target, dtype=torch.float32) # shape: (n_labeled_nodes, len(pred_cols))

            n_labeled_nodes = target.shape[0]
            n_nodes = g.num_nodes()

            node_labels = torch.zeros([n_nodes, len(self.pred_cols)], dtype=torch.float32)        
            node_labels[:n_labeled_nodes] = target
            g.ndata['target'] = node_labels # shape: (n_nodes, len(pred_cols))

            train_mask = torch.zeros(n_nodes, dtype=torch.bool)
            train_mask[:n_labeled_nodes] = True        
            g.ndata['train_mask'] = train_mask # shape: (n_nodes, )        
        return g

    @property
    def feature_dim(self):
        g = self.__getitem__(0)
        return g.ndata['h'].shape[1]

def train_epoch(model, train_loader, criterion, optimizer, device):
    '''Train model for one epoch'''
    model.train()
    model.zero_grad()
    train_loss = []
    
    for index, graphs in enumerate(train_loader):
        graphs = graphs.to(device)
        preds = model(graphs, graphs.ndata['h'])
        train_mask = graphs.ndata['train_mask']
        targets = graphs.ndata['target']
        
        loss = criterion(preds[train_mask], targets[train_mask])
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        train_loss.append(loss.item())
    
    train_loss_avg = np.mean(train_loss)
    print(f"Train loss {train_loss_avg}")
    return train_loss_avg
    
def eval(model, valid_loader, criterion, device):
    '''Evaluate model'''
    model.eval()
    eval_loss = []
    
    for index, graphs in enumerate(valid_loader):
        graphs = graphs.to(device)
        preds = model(graphs, graphs.ndata['h'])
        train_mask = graphs.ndata['train_mask']
        targets = graphs.ndata['target']
        
        loss = criterion(preds[train_mask], targets[train_mask])
        eval_loss.append(loss.item())
    
    eval_loss_avg = np.mean(eval_loss)
    print(f"Valid loss {eval_loss_avg}")
    return eval_loss_avg


def train(amp=False):

    train_file = 'OpenVaccine/train.json'
    model_config = {
        'num_layers': 2,
        'hidden_feats': 8,
        'dropout': 0.2,
        'residual': False,
        'batchnorm': False,
    }

    train_config = {
        'frac_train': 0.8,
        'lr': 1e-3,
        'n_epochs': 40,
        'batch_size': 128,
        'num_workers': 0,
        'seed': 42
    }

    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu') 

    t0 = time.time()
    # parse the data into data frames
    train = pd.read_json(train_file, lines=True)

    N = train.shape[0]
    train_idx = np.random.choice(N, int(train_config['frac_train'] * N), replace=False)
    valid_idx = np.setdiff1d(np.arange(N), train_idx)
    print(train_idx.shape, valid_idx.shape)

    _, train_list_series = zip(*train.iloc[train_idx].iterrows())
    _, valid_list_series = zip(*train.iloc[valid_idx].iterrows())
    
    train_list_series
    train_dataset = RNADataset(train_list_series)
    train_loader = data.DataLoader(train_dataset, 
                                   batch_size=train_config['batch_size'], 
                                   shuffle=True, 
                                   pin_memory=True,
                                   num_workers=train_config['num_workers'], 
                                   collate_fn=dgl.batch
                                  )

    valid_dataset = RNADataset(valid_list_series)
    valid_loader = data.DataLoader(valid_dataset, 
                                   batch_size=train_config['batch_size'], 
                                   shuffle=False, 
                                   pin_memory=True,
                                   num_workers=train_config['num_workers'], 
                                   collate_fn=dgl.batch
                                  )

    t1 = time.time()
    print("Loaded {} training and {} valid data in {} sec".format(len(train_dataset), len(valid_dataset), t1-t0))

    model = GCN(
        in_feats=train_dataset.feature_dim,
        hidden_feats=[model_config['hidden_feats'] for _ in range(model_config['num_layers'] - 1)] + [train_dataset.n_outputs],
        activation=[F.relu for _ in range(model_config['num_layers'] - 1)] + [None],
        residual=[model_config['residual'] for _ in range(model_config['num_layers'])],
        batchnorm=[model_config['batchnorm'] for _ in range(model_config['num_layers'])],
        dropout=[model_config['dropout'] for _ in range(model_config['num_layers'] - 1)] + [0]
    ).to(device)

    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(params=model.parameters(), lr=train_config['lr'], weight_decay=0.0)

    train_losses = []
    eval_losses = []


    for epoch in range(train_config['n_epochs']):
        print('###Epoch:', epoch)
        train_loss = train_epoch(model, train_loader, criterion, optimizer, device)
        eval_loss = eval(model, valid_loader, criterion, device)
        train_losses.append(train_loss)
        eval_losses.append(eval_loss)
    t2 = time.time()

    print("trained {} epoches in {} sec; avg: {} sec".format(train_config['n_epochs'], t2-t1, (t2-t1)/train_config['n_epochs']))


if __name__ == "__main__":
    train()

