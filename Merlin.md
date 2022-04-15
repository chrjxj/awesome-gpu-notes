# Merlin 

- Overview:[Merlin Overview](https://developer.nvidia.com/nvidia-merlin)
  

## Source code

- Open-source Merlin GitHub Repo -[Merlin Repo](https://github.com/NVIDIA-Merlin/Merlin)
  - NVTabular Github Repo - [NVTabular Repo](https://github.com/NVIDIA/NVTabular)
  - HugeCTR Github Repo - [HugeCTR Repo](https://github.com/NVIDIA/HugeCTR)

- NGC Containers: [HugeCTR](https://ngc.nvidia.com/catalog/containers/nvidia:hugectr),[NVTabular](https://ngc.nvidia.com/catalog/containers/nvidia:nvtabular),[Merlin Inference](https://ngc.nvidia.com/containers/nvstaging:merlin:merlin-inference),[Merlin Training](https://ngc.nvidia.com/containers/nvstaging:merlin:merlin-training),[Merlin Pytorch Training](https://ngc.nvidia.com/containers/nvstaging:merlin:merlin-pytorch-training),[Merlin Tensorflow Training](https://ngc.nvidia.com/containers/nvstaging:merlin:merlin-tensorflow-training)

- Example Notebooks: [NVTabular Examples](https://github.com/NVIDIA/NVTabular/tree/main/examples), [HugeCTR Examples](https://github.com/NVIDIA/HugeCTR/tree/master/notebooks)
  - [Getting Started with Movie Lens Dataset](https://github.com/NVIDIA/NVTabular/tree/main/examples/getting-started-movielens)
  - [Scaling Rec Sys Workload to Multi-GPU and Multi-Nodes](https://github.com/NVIDIA/NVTabular/tree/main/examples/scaling-criteo)
  - [Accelerated TF embeddings with HugeCTR Sparse Operation Kit](https://github.com/NVIDIA/HugeCTR/blob/master/notebooks/sparse_operation_kit_demo.ipynb)

- Reference Applications: 
    - [DLRM](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Recommendation/DLRM) (PyTorch Training and Triton Inference), 
     
    - [Wide &amp; Deep](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow/Recommendation) (TensorFlow Training),
    - [VAE-CF](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow/Recommendation) (TensorFlow Training),    
    - [NCF](https://github.com/NVIDIA/DeepLearningExamples/tree/master/) (TensorFlow and PyTorch Training)

##  Developer Blogs

  - [Accelerating Wide &amp; Deep Recommender Inference on GPUs](https://devblogs.nvidia.com/accelerating-wide-deep-recommender-inference-on-gpus/)
  - [Announcing the NVIDIA NVTabular Open Beta with Multi-GPU Support and New Data Loaders](https://developer.nvidia.com/blog/announcing-the-nvtabular-open-beta-with-multi-gpu-support-and-new-data-loaders/)
  - [Accelerating ETL for Recommender Systems on NVIDIA GPUs with NVTabular](https://developer.nvidia.com/blog/accelerating-etl-for-recsys-on-gpus-with-nvtabular/)
  - [Announcing the NVIDIA NVTabular Open Beta with Multi-GPU Support and New Data Loaders](https://developer.nvidia.com/blog/announcing-the-nvtabular-open-beta-with-multi-gpu-support-and-new-data-loaders/)
  - [Accelerating Recommender Systems Training with NVIDIA Merlin Open Beta](https://developer.nvidia.com/blog/accelerating-recommender-systems-training-with-nvidia-merlin-open-beta/)
  - [Training Deep Learning Based Recommender Systems 9x Faster with TensorFlow](https://medium.com/nvidia-merlin/training-deep-learning-based-recommender-systems-9x-faster-with-tensorflow-cc5a2572ea49)
  - [A New API for NVTabular and Inference support are coming with Merlin&#39;s 0.4 release](https://medium.com/nvidia-merlin/a-new-api-for-nvtabular-and-inference-support-are-coming-with-merlins-0-4-release-b3ef2c5aa8f3)
  - [MLPerf v1.0 Training Benchmarks: Insights into a Record-Setting NVIDIA Performance](https://developer.nvidia.com/blog/mlperf-v1-0-training-benchmarks-insights-into-a-record-setting-performance/)
  - [Continuously Improving Recommender Systems for Competitive Advantage Using NVIDIA Merlin and MLOps](https://developer.nvidia.com/blog/continuously-improving-recommender-systems-for-competitive-advantage-with-merlin-and-mlops/)
  - [Using Neural Networks for Your Recommender System](https://developer.nvidia.com/blog/using-neural-networks-for-your-recommender-system/)

## GTC

- GTC 2021 Sessions
  - Intro Blogs
    - [Learn how Spotify, Walmart, Tencent and Postmates are scaling and accelerating their recommender systems on GPU during GTC 2021](https://medium.com/nvidia-merlin/learn-how-spotify-walmart-tencent-and-postmates-are-scaling-and-accelerating-their-recommender-371ee4904cd4)
    - [NVIDIA Deepens Commitment to Streamlining Recommender Workflows with GTC Spring Sessions](https://developer.nvidia.com/blog/nvidia-deepens-commitment-to-streamlining-recommender-workflows-with-gtc-spring-sessions/)
  - [Accelerated ETL, Training and Inference of Recommender Systems on the GPU with Merlin, HugeCTR, NVTabular, and Triton](https://gtc21.event.nvidia.com/media/Accelerated%20ETL%2C%20Training%20and%20Inference%20of%20Recommender%20Systems%20on%20the%20GPU%20with%20Merlin%2C%20HugeCTR%2C%20NVTabular%2C%20and%20Triton%20%5BS31830%5D/1_6v5scqwv)
  - [Merlin HugeCTR: Deep Dive Into Performance Optimization](https://gtc21.event.nvidia.com/media/Merlin%20HugeCTR%3A%20Deep%20Dive%20Into%20Performance%20Optimization%20%5BS31269%5D/1_owz82snn)
  - [Training and Deploying Recommender Systems on the GPU: Merlin, HugeCTR, NVTabular, and Triton](https://gtc21.event.nvidia.com/media/Training%20and%20Deploying%20Recommender%20Systems%20on%20the%20GPU%3A%20Merlin%2C%20HugeCTR%2C%20NVTabular%2C%20and%20Triton%20%5BCWES1184%5D/1_udu6553p)

- GTC Spring 2022 Sessions
    
    - Building and Deploying Recommender Systems Quickly and Easily with NVIDIA Merlin [S41119](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1639106562192001FMKc)
    - Tutorial: Building Recommender Systems More Easily using Merlin Models [DLIT2043](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1639106562192001FMKc)
    - Building Next-gen Class Recommendations at Peloton with NVIDIA Merlin [S41259](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1634926177530001lfnt)
    - Scaling Real-time Deep Learning Recommendation Inference at a 150M+ User Scale [S42547](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1642819675389001aEvU)
    


