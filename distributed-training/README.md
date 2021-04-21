# Distributed Training


## Data Parallel and Misc 


* baidu-allreduce: [code](https://github.com/baidu-research/baidu-allreduce) and [article](https://www.tomshardware.com/news/baidu-svail-ring-allreduce-library,33691.html) 
* [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473)
* [Optimizing Network Performance for Distributed DNN Training on GPU Clusters: ImageNet/AlexNet Training in 1.5 Minutes ](https://arxiv.org/abs/1902.06855)


* [Horovod: fast and easy distributed deep learning in TensorFlow](https://arxiv.org/pdf/1802.05799.pdf)
* [PyTorch Distributed: Experiences on Accelerating Data Parallel Training](https://arxiv.org/abs/2006.15704)

## NVidia Megatron-LM


* 2021, Efficient Large-Scale Language Model Training on GPU Clusters, [paper](https://arxiv.org/abs/2104.04473), [blog](https://developer.nvidia.com/blog/scaling-language-model-training-to-a-trillion-parameters-using-megatron)  
* 2020, Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism, [paper](https://arxiv.org/pdf/1909.08053v4.pdf) 
* code, https://github.com/NVIDIA/Megatron-LM


## Google SWITCH TRANSFORMERS and Mix of Experts

* [Hierarchical mixtures of experts and the em algorithm. Micahel Jordan, 1994. ](https://www.cs.toronto.edu/~hinton/absps/hme.pdf)
* [GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism](https://arxiv.org/abs/1811.06965)
* [Pipedream: Fast and efficient pipeline parallel dnn training.2018](https://arxiv.org/abs/1806.03377)
* [SWITCH TRANSFORMERS: SCALING TO TRILLION PARAMETER MODELS WITH SIMPLE AND EFFICIENT SPARSITY ](https://arxiv.org/abs/2101.03961)


## DeepSpeed


#### Documentation and Article

DeepSpeed documentation can be found on: [deepspeed.ai](https://www.deepspeed.ai/)


* [2020/09/10] [DeepSpeed v0.3: Extreme-scale model training for everyone](https://www.microsoft.com/en-us/research/blog/deepspeed-extreme-scale-model-training-for-everyone/)
  * [Powering 10x longer sequences and 6x faster execution through DeepSpeed Sparse Attention](https://www.deepspeed.ai/news/2020/09/08/sparse-attention-news.html)
  * [Training a trillion parameters with pipeline parallelism](https://www.deepspeed.ai/news/2020/09/08/pipeline-parallelism.html)
  * [Up to 5x less communication and 3.4x faster training through 1-bit Adam](https://www.deepspeed.ai/news/2020/09/08/onebit-adam-news.html)
  * [10x bigger model training on a single GPU with ZeRO-Offload](https://www.deepspeed.ai/news/2020/09/08/ZeRO-Offload.html)
* [2020/08/07] [DeepSpeed Microsoft Research Webinar](https://note.microsoft.com/MSR-Webinar-DeepSpeed-Registration-On-Demand.html) is now available on-demand


#### Publications

1. (2019) ZeRO: memory optimizations toward training trillion parameter models. [arXiv:1910.02054](https://arxiv.org/abs/1910.02054) and [In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '20)](https://dl.acm.org/doi/10.5555/3433701.3433727).
2. (2020) DeepSpeed: System Optimizations Enable Training Deep Learning Models with Over 100 Billion Parameters. [In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD '20, Tutorial)](https://dl.acm.org/doi/10.1145/3394486.3406703).
3. (2020) Accelerating Training of Transformer-Based Language Models with Progressive Layer Dropping. [arXiv:2010.13369](https://arxiv.org/abs/2010.13369) and [NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/a1140a3d0df1c81e24ae954d935e8926-Abstract.html).
4. (2021) ZeRO-Offload: Democratizing Billion-Scale Model Training. [arXiv:2101.06840](https://arxiv.org/abs/2101.06840).
5. (2021) 1-bit Adam: Communication Efficient Large-Scale Training with Adam's Convergence Speed. [arXiv:2102.02888](https://arxiv.org/abs/2102.02888).

#### Videos

1. DeepSpeed KDD 2020 Tutorial
    1. [Overview](https://www.youtube.com/watch?v=CaseqC45DNc&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=29)
    2. [ZeRO + large model training](https://www.youtube.com/watch?v=y4_bCiAsIAk&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=28)
    3. [17B T-NLG demo](https://www.youtube.com/watch?v=9V-ZbP92drg&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=27)
    4. [Fastest BERT training + RScan tuning](https://www.youtube.com/watch?v=o1K-ZG9F6u0&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=26)
    5. DeepSpeed hands on deep dive: [part 1](https://www.youtube.com/watch?v=_NOk-mBwDYg&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=92), [part 2](https://www.youtube.com/watch?v=sG6_c4VXLww&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=94), [part 3](https://www.youtube.com/watch?v=k9yPkBTayos&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=93)
    6. [FAQ](https://www.youtube.com/watch?v=nsHu6vEgPew&list=PLa85ZdUjfWS21mgibJ2vCvLziprjpKoW0&index=24)

2. Microsoft Research Webinar
    * Registration is free and all videos are available on-demand.
    * [ZeRO & Fastest BERT: Increasing the scale and speed of deep learning training in DeepSpeed](https://note.microsoft.com/MSR-Webinar-DeepSpeed-Registration-On-Demand.html).

