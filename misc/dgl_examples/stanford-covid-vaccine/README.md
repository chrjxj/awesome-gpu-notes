# DGL Example - OpenVaccine

## Prepare

- Download OpenVaccine dataset from its [kaggle page](https://www.kaggle.com/competitions/stanford-covid-vaccine/overview)

```bash
ls ./OpenVaccine
bpps  post_deadline_files  sample_submission.csv  test.json  train.json
```
- Apply DGL access, and then pull DGL container from NGC: `docker pull nvcr.io/nvdlfwea/dgl/dgl:22.04-pytorch-py3`

- start docker container: `docker run --gpus '"device=0"' -it --rm --network=host --shm-size=24g --ulimit memlock=-1 --ulimit stack=67108864 -v /your/path:/workspace nvcr.io/nvdlfwea/dgl/dgl:22.04-pytorch-py3 /bin/bash`

## GNN Training

1. Baseline

- the `train_baseline.py` script is adapted from: https://github.com/dglai/Graph-Neural-Networks-in-Life-Sciences/blob/main/3_macro_molecules/2-RNA_stability_prediction.ipynb

- in the docker container, run the test: `python train_baseline.py`; performance on 1 * V100 GPU: 
    * trained 40 epoches in 186.52 sec; avg: 4.66 sec


2. Precomputed version

- to avoid duplicated computing in data ETL stage every epoch, improved the script and saved as `train.py` 

- in the docker container, run the test: `python train.py`; performance on 1 * V100 GPU: 
    * precomputing: 8.48 sec for 1920 training and 480 valid samples
    * training: 40 epoches in 8.8 sec; avg 0.22 sec/epoch

