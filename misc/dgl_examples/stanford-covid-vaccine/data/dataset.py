# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import collections.abc
import math
import pickle
import shutil
import sys
import tempfile
import threading
import time
import warnings
from copy import copy, deepcopy
from multiprocessing.pool import ThreadPool
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, Callable, Dict, List, Optional, Sequence, Union

import numpy as np
import torch
from torch.serialization import DEFAULT_PROTOCOL
from torch.utils.data import Dataset as _TorchDataset
from torch.utils.data import Subset


if TYPE_CHECKING:
    from tqdm import tqdm

    has_tqdm = True
else:
    has_tqdm = False


class Dataset(_TorchDataset):
    """
    A generic dataset with a length property and an optional callable data transform
    when fetching a data sample.
    If passing slicing indices, will return a PyTorch Subset, for example: `data: Subset = dataset[1:4]`,
    for more details, please check: https://pytorch.org/docs/stable/data.html#torch.utils.data.Subset

    For example, typical input data can be a list of dictionaries::

        [{                            {                            {
             'img': 'image1.nii.gz',      'img': 'image2.nii.gz',      'img': 'image3.nii.gz',
             'seg': 'label1.nii.gz',      'seg': 'label2.nii.gz',      'seg': 'label3.nii.gz',
             'extra': 123                 'extra': 456                 'extra': 789
         },                           },                           }]
    """

    def __init__(self, data: Sequence, transform: Optional[Callable] = None) -> None:
        """
        Args:
            data: input data to load and transform to generate dataset for model.
            transform: a callable data transform on input data.

        """
        self.data = data
        self.transform = transform

    def __len__(self) -> int:
        return len(self.data)

    def _transform(self, index: int):
        """
        Fetch single data item from `self.data`.
        """
        data_i = self.data[index]
        return apply_transform(self.transform, data_i) if self.transform is not None else data_i

    def __getitem__(self, index: Union[int, slice, Sequence[int]]):
        """
        Returns a `Subset` if `index` is a slice or Sequence, a data item otherwise.
        """
        if isinstance(index, slice):
            # dataset[:42]
            start, stop, step = index.indices(len(self))
            indices = range(start, stop, step)
            return Subset(dataset=self, indices=indices)
        if isinstance(index, collections.abc.Sequence):
            # dataset[[1, 3, 4]]
            return Subset(dataset=self, indices=index)
        return self._transform(index)


class DatasetFunc(Dataset):
    """
    Execute function on the input dataset and leverage the output to act as a new Dataset.
    It can be used to load / fetch the basic dataset items, like the list of `image, label` paths.
    Or chain together to execute more complicated logic, like `partition_dataset`, `resample_datalist`, etc.
    The `data` arg of `Dataset` will be applied to the first arg of callable `func`.
    Usage example::

        data_list = DatasetFunc(
            data="path to file",
            func=monai.data.load_decathlon_datalist,
            data_list_key="validation",
            base_dir="path to base dir",
        )
        # partition dataset for every rank
        data_partition = DatasetFunc(
            data=data_list,
            func=lambda **kwargs: monai.data.partition_dataset(**kwargs)[torch.distributed.get_rank()],
            num_partitions=torch.distributed.get_world_size(),
        )
        dataset = Dataset(data=data_partition, transform=transforms)

    Args:
        data: input data for the func to process, will apply to `func` as the first arg.
        func: callable function to generate dataset items.
        kwargs: other arguments for the `func` except for the first arg.

    """

    def __init__(self, data: Any, func: Callable, **kwargs) -> None:
        super().__init__(data=None, transform=None)  # type:ignore
        self.src = data
        self.func = func
        self.kwargs = kwargs
        self.reset()

    def reset(self, data: Optional[Any] = None, func: Optional[Callable] = None, **kwargs):
        """
        Reset the dataset items with specified `func`.

        Args:
            data: if not None, execute `func` on it, default to `self.src`.
            func: if not None, execute the `func` with specified `kwargs`, default to `self.func`.
            kwargs: other arguments for the `func` except for the first arg.

        """
        src = self.src if data is None else data
        self.data = self.func(src, **self.kwargs) if func is None else func(src, **kwargs)



# class CacheDataset(Dataset):
#     """
#     Dataset with cache mechanism that can load data and cache deterministic transforms' result during training.

#     By caching the results of non-random preprocessing transforms, it accelerates the training data pipeline.
#     If the requested data is not in the cache, all transforms will run normally
#     (see also :py:class:`monai.data.dataset.Dataset`).

#     Users can set the cache rate or number of items to cache.
#     It is recommended to experiment with different `cache_num` or `cache_rate` to identify the best training speed.

#     The transforms which are supposed to be cached must implement the `monai.transforms.Transform`
#     interface and should not be `Randomizable`. This dataset will cache the outcomes before the first
#     `Randomizable` `Transform` within a `Compose` instance.
#     So to improve the caching efficiency, please always put as many as possible non-random transforms
#     before the randomized ones when composing the chain of transforms.
#     If passing slicing indices, will return a PyTorch Subset, for example: `data: Subset = dataset[1:4]`,
#     for more details, please check: https://pytorch.org/docs/stable/data.html#torch.utils.data.Subset

#     For example, if the transform is a `Compose` of::

#         transforms = Compose([
#             LoadImaged(),
#             AddChanneld(),
#             Spacingd(),
#             Orientationd(),
#             ScaleIntensityRanged(),
#             RandCropByPosNegLabeld(),
#             ToTensord()
#         ])

#     when `transforms` is used in a multi-epoch training pipeline, before the first training epoch,
#     this dataset will cache the results up to ``ScaleIntensityRanged``, as
#     all non-random transforms `LoadImaged`, `AddChanneld`, `Spacingd`, `Orientationd`, `ScaleIntensityRanged`
#     can be cached. During training, the dataset will load the cached results and run
#     ``RandCropByPosNegLabeld`` and ``ToTensord``, as ``RandCropByPosNegLabeld`` is a randomized transform
#     and the outcome not cached.

#     During training call `set_data()` to update input data and recompute cache content, note that it requires
#     `persistent_workers=False` in the PyTorch DataLoader.

#     Note:
#         `CacheDataset` executes non-random transforms and prepares cache content in the main process before
#         the first epoch, then all the subprocesses of DataLoader will read the same cache content in the main process
#         during training. it may take a long time to prepare cache content according to the size of expected cache data.
#         So to debug or verify the program before real training, users can set `cache_rate=0.0` or `cache_num=0` to
#         temporarily skip caching.

#     """

#     def __init__(
#         self,
#         data: Sequence,
#         transform: Optional[Union[Sequence[Callable], Callable]] = None,
#         cache_num: int = sys.maxsize,
#         cache_rate: float = 1.0,
#         num_workers: Optional[int] = 1,
#         progress: bool = True,
#         copy_cache: bool = True,
#         as_contiguous: bool = True,
#         hash_as_key: bool = False,
#         hash_func: Callable[..., bytes] = pickle_hashing,
#     ) -> None:
#         """
#         Args:
#             data: input data to load and transform to generate dataset for model.
#             transform: transforms to execute operations on input data.
#             cache_num: number of items to be cached. Default is `sys.maxsize`.
#                 will take the minimum of (cache_num, data_length x cache_rate, data_length).
#             cache_rate: percentage of cached data in total, default is 1.0 (cache all).
#                 will take the minimum of (cache_num, data_length x cache_rate, data_length).
#             num_workers: the number of worker threads to use.
#                 If num_workers is None then the number returned by os.cpu_count() is used.
#                 If a value less than 1 is speficied, 1 will be used instead.
#             progress: whether to display a progress bar.
#             copy_cache: whether to `deepcopy` the cache content before applying the random transforms,
#                 default to `True`. if the random transforms don't modify the cached content
#                 (for example, randomly crop from the cached image and deepcopy the crop region)
#                 or if every cache item is only used once in a `multi-processing` environment,
#                 may set `copy=False` for better performance.
#             as_contiguous: whether to convert the cached NumPy array or PyTorch tensor to be contiguous.
#                 it may help improve the performance of following logic.
#             hash_as_key: whether to compute hash value of input data as the key to save cache,
#                 if key exists, avoid saving duplicated content. it can help save memory when
#                 the dataset has duplicated items or augmented dataset.
#             hash_func: if `hash_as_key`, a callable to compute hash from data items to be cached.
#                 defaults to `monai.data.utils.pickle_hashing`.

#         """
#         if not isinstance(transform, Compose):
#             transform = Compose(transform)
#         super().__init__(data=data, transform=transform)
#         self.set_num = cache_num  # tracking the user-provided `cache_num` option
#         self.set_rate = cache_rate  # tracking the user-provided `cache_rate` option
#         self.progress = progress
#         self.copy_cache = copy_cache
#         self.as_contiguous = as_contiguous
#         self.hash_as_key = hash_as_key
#         self.hash_func = hash_func
#         self.num_workers = num_workers
#         if self.num_workers is not None:
#             self.num_workers = max(int(self.num_workers), 1)
#         self.cache_num = 0
#         self._cache: Union[List, Dict] = []
#         self.set_data(data)

#     def set_data(self, data: Sequence):
#         """
#         Set the input data and run deterministic transforms to generate cache content.

#         Note: should call this func after an entire epoch and must set `persistent_workers=False`
#         in PyTorch DataLoader, because it needs to create new worker processes based on new
#         generated cache content.

#         """

#         def _compute_cache():
#             self.cache_num = min(int(self.set_num), int(len(self.data) * self.set_rate), len(self.data))
#             return self._fill_cache()

#         if self.hash_as_key:
#             # only compute cache for the unique items of dataset
#             mapping = {self.hash_func(v): v for v in data}
#             self.data = list(mapping.values())
#             cache_ = _compute_cache()
#             self._cache = dict(zip(list(mapping)[: self.cache_num], cache_))
#             self.data = data
#         else:
#             self.data = data
#             self._cache = _compute_cache()

#     def _fill_cache(self) -> List:
#         if self.cache_num <= 0:
#             return []
#         if self.progress and not has_tqdm:
#             warnings.warn("tqdm is not installed, will not show the caching progress bar.")
#         with ThreadPool(self.num_workers) as p:
#             if self.progress and has_tqdm:
#                 return list(
#                     tqdm(
#                         p.imap(self._load_cache_item, range(self.cache_num)),
#                         total=self.cache_num,
#                         desc="Loading dataset",
#                     )
#                 )
#             return list(p.imap(self._load_cache_item, range(self.cache_num)))

#     def _load_cache_item(self, idx: int):
#         """
#         Args:
#             idx: the index of the input data sequence.
#         """
#         item = self.data[idx]
#         for _transform in self.transform.transforms:  # type:ignore
#             # execute all the deterministic transforms
#             if isinstance(_transform, Randomizable) or not isinstance(_transform, Transform):
#                 break
#             _xform = deepcopy(_transform) if isinstance(_transform, ThreadUnsafe) else _transform
#             item = apply_transform(_xform, item)
#         if self.as_contiguous:
#             item = convert_to_contiguous(item, memory_format=torch.contiguous_format)
#         return item

#     def _transform(self, index: int):
#         index_: Any = index
#         if self.hash_as_key:
#             key = self.hash_func(self.data[index])
#             if key in self._cache:
#                 # if existing in cache, get the index
#                 index_ = key  # if using hash as cache keys, set the key

#         if isinstance(index_, int) and index_ % len(self) >= self.cache_num:  # support negative index
#             # no cache for this index, execute all the transforms directly
#             return super()._transform(index_)
#         # load data from cache and execute from the first random transform
#         start_run = False
#         if self._cache is None:
#             self._cache = self._fill_cache()
#         data = self._cache[index_]
#         if not isinstance(self.transform, Compose):
#             raise ValueError("transform must be an instance of monai.transforms.Compose.")
#         for _transform in self.transform.transforms:
#             if start_run or isinstance(_transform, Randomizable) or not isinstance(_transform, Transform):
#                 # only need to deep copy data on first non-deterministic transform
#                 if not start_run:
#                     start_run = True
#                     if self.copy_cache:
#                         data = deepcopy(data)
#                 data = apply_transform(_transform, data)
#         return data


class CacheDataset(Dataset):

    def __init__(self, data: Sequence,
        cache_num: int = sys.maxsize,
        cache_rate: float = 1.0,
        num_workers: Optional[int] = 1,
        progress: bool = True,   
    ):
        self.data = data
        self.num_workers = 1
        self.progress = progress
        self.set_data(data)

    def set_data(self, data: Sequence):
        """
        Set the input data and run deterministic transforms to generate cache content.

        Note: should call this func after an entire epoch and must set `persistent_workers=False`
        in PyTorch DataLoader, because it needs to create new worker processes based on new
        generated cache content.

        """

        def _compute_cache():
            #self.cache_num = min(int(self.set_num), int(len(self.data) * self.set_rate), len(self.data))
            self.cache_num = len(self.data)
            return self._fill_cache()

        self.data = data
        self._cache = _compute_cache()


    def _fill_cache(self) -> List:
        if self.cache_num <= 0:
            return []

        with ThreadPool(self.num_workers) as p:
            if self.progress and has_tqdm:
                return list(
                    tqdm(
                        p.imap(self._load_cache_item, range(self.cache_num)),
                        total=self.cache_num,
                        desc="Loading dataset",
                    )
                )
            return list(p.imap(self._load_cache_item, range(self.cache_num)))

    def _load_cache_item(self, idx: int):
        """
        Args:
            idx: the index of the input data sequence.
        """
        raise NotImplementedError

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        if self._cache is None:
            self._cache = self._fill_cache()
        data = self._cache[idx]
        return data
