# DGL Examples

Before start, please go to https://developer.nvidia.com/dgl-container-early-access and apply DGL EA, so that you can pull dgl docker images from [NGC](https://ngc.nvidia.com/).

## 1. OpenVaccine

See OpenVaccine's [README](./stanford-covid-vaccine/README.md) file.

## SE3Transformer

1. Download SE3Transformer from [DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples/tree/master/DGLPyTorch/DrugDiscovery/SE3Transformer); (only need `SE3Transformer` folder)

2. in your host machine, run `se3-transformer` docker container: 

```bash
docker run --gpus '"device=0,1,2,3"' -it --rm --network=host --shm-size=24g --ulimit memlock=-1 --ulimit stack=67108864 \
    -v /your/path:/xxx  \
    nvcr.io/nvdlfwea/dgl/se3-transformer:21.10 /bin/bash
```

3. in container, go to `SE3Transformer` folder, and run: `sh scripts/benchmark_train.sh`

    * Training perf on 1*V100: 63 sec/epoch
