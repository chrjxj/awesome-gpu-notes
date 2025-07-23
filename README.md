# Awesome GPU Notes

## GPU and CUDA Documents

GPU architecture

- [nvidia-ampere-architecture-whitepaper](https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf)
- [TESLA V100 GPU ARCHITECTURE](https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf)

CUDA

- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)
- [CUDA Best Practice Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)
- CUDA Sample Code

    * [sgemm](https://github.com/cwpearson/nvidia-performance-tools/tree/90890e807ef9fc1532ee08938de6689444701686/sgemm)


Topics

* https://developer.nvidia.com/blog/inside-volta/
* https://developer.nvidia.com/blog/cuda-pro-tip-optimized-filtering-warp-aggregated-atomics/
* https://developer.nvidia.com/blog/cooperative-groups/


## Inference


[TensorRT](https://github.com/NVIDIA/TensorRT)

https://github.com/NVIDIA/TensorRT-LLM

https://github.com/NVIDIA/tensorrt-model-optimizer

[Triton](https://github.com/triton-inference-server)

* https://github.com/triton-inference-server/server
* https://github.com/triton-inference-server/client
* https://github.com/triton-inference-server/tensorrtllm_backend
* https://github.com/triton-inference-server/perf_analyzer


**ai-dynamo - LLM Inference "OS"**

https://github.com/ai-dynamo/dynamo
NVIDIA Inference Xfer Library (NIXL): https://github.com/ai-dynamo/nixl

![dynamo](https://github.com/ai-dynamo/dynamo/blob/main/docs/images/architecture.png)

## Training

- [distributed training](distributed-training/README.md)

## Tools


#### NVIDIA System Management (nvidia-smi and NVML)

TBA

#### NVIDIA Nsight Systems

- [official site](https://developer.nvidia.com/nsight-systems)
- [Document home](https://docs.nvidia.com/nsight-systems/index.html)


Videos:

- University of Illinois ECE 408 - Nsight Compute and Nsight Systems:

    * https://www.youtube.com/watch?v=uN2qju175aE
    * https://www.youtube.com/watch?v=yI137sSOlkU
    * https://www.youtube.com/watch?v=YHrmnaPgFfY
    * https://www.youtube.com/watch?v=UNX0KNMQlW8

- NV: [what the profiler is telling you](https://youtu.be/kKANP0kL_hk)


## Modulus, AI for science

* [Deep Learning for Science and Engineering](https://www.nvidia.com/en-us/on-demand/deep-learning-for-science-and-engineering/), George Karniadakis, Professor, Brown University
* [DLI](https://github.com/openhackathons-org/End-to-End-AI-for-Science)
* [End-to-End AI for Science](https://github.com/openhackathons-org/End-to-End-AI-for-Science)



## Various Softwares

#### NVIDIA cuNumeric


* cunumeric [home page](https://developer.nvidia.com/cunumeric) and [github](https://github.com/nv-legate/cunumeric)
* blog: https://developer.nvidia.com/blog/accelerating-python-applications-with-cunumeric-and-legate/
* About [legion](https://legion.stanford.edu)
  

## Storage

Portus: Efficient DNN Checkpointing to Persistent Memory with Zero-Copy

* paper: https://www.tianyuanwu.com/files/portus.pdf
* https://kms.shanghaitech.edu.cn/handle/2MSLDSTB/414241



