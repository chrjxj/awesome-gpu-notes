# Recommender Systems and NVIDIA Merlin

[toc]

## Dataset

### criteo-kaggle

Kaggle的[展示广告竞赛](https://www.kaggle.com/c/criteo-display-ad-challenge/)中所使用的Criteo数据集。该数据包含数百万展示广告的特征值和点击反馈，目的是对点击率（CTR）的预测做基准预测。

- 背景：Criteo是在线效果类数字营销厂商，核心业务是重定向广告（retargeting）。Criteo的核心产品主要包括访客广告、流失客户广告、移动应用内效果型广告和AD-X
  移动广告跟踪分析产品等。Criteo拥有世界领先的自主学习式推荐引擎和预测引擎，能够通过其对于市场的洞察提供可评估的结果，因而能够在正确的时间通过推送广告，将对的产品推荐给对的用户。

- 下载
    - https://www.kaggle.com/datasets/mrkmakr/criteo-dataset
    - 到 https://ailab.criteo.com/ressources 上的 `Kaggle Display Advertising dataset`;
      直接下载: `wget -c -i 0 http://go.criteo.net/criteo-research-kaggle-display-advertising-challenge-dataset.tar.gz`
    - https://s3-eu-west-1.amazonaws.com/kaggle-display-advertising-challenge-dataset/dac.tar.gz

- 数据格式：

      - 格式：<label> <integer feature 1>  <integer feature 13> <categorical feature 1> ... <categorical feature 26>  。共计39个特征，13个数值特征（int），26个类别特征。若value为空值，则为空白

    - 训练数据：train.txt：Criteo
      公司在七天内的部分流量。每行对应的是Critio的展示广告，第一列代表该广告是否被点击。我们对正样本（已点击）的和负样本（未点击）均做了子采样来减少数据量。类别特征的值已经过哈希处理为64位来进行脱敏。特征的语义没有公开，并且有些特征有缺失值。行按照时间排序。

        - 示例：

  | label | f1   | f2   | f3   | f4   | f5    | f6   | f7   | f8   | f9   | f10  | f11  | f12  | f13  | f14      | f15      | f16      | f17      | f18      | f19      | f20      | f21      | f22      | f23      | f24      | f25      | f26      | f27      | f28      | f29      | f30      | f31      | f32      | f33      | f34      | f35      | f36      | f37      | f38      | f39      |
    | ----- | ---- | ---- | ---- | ---- | ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
  | 0     | 1    | 1    | 5    | 0    | 1382  | 4    | 15   | 2    | 181  | 1    | 2    |      | 2    | 68fd1e64 | 80e26c9b | fb936136 | 7b4723c4 | 25c83c98 | 7e0ccccf | de7995b8 | 1f89b562 | a73ee510 | a8cd5504 | b2cb9c98 | 37c9c164 | 2824a5f6 | 1adce6ef | 8ba8b39a | 891b62e7 | e5ba7672 | f54016b9 | 21ddcdc9 | b1252a9d | 07b5194c |          | 3a171ecb | c5c50484 | e8b83407 | 9727dd16 |
  | 0     | 2    | 0    | 44   | 1    | 102   | 8    | 2    | 2    | 4    | 1    | 1    |      | 4    | 68fd1e64 | f0cf0024 | 6f67f7e5 | 41274cd7 | 25c83c98 | fe6b92e5 | 922afcc0 | 0b153874 | a73ee510 | 2b53e5fb | 4f1b46f3 | 6.23E+11 | d7020589 | b28479f6 | e6c5b5cd | c92f3b61 | 07c540c4 | b04e4670 | 21ddcdc9 | 5840adea | 60f6221e |          | 3a171ecb | 43f13e8b | e8b83407 | 731c3655 |
  | 1     | 1    | 4    | 2    | 0    | 0     | 0    | 1    | 0    | 0    | 1    | 1    |      | 0    | 68fd1e64 | 2c16a946 | 503b9dbc | e4dbea90 | f3474129 | 13718bbd | 38eb9cf4 | 1f89b562 | a73ee510 | 547c0ffe | bc8c9f21 | 60ab2f07 | 46f42a63 | 07d13a8f | 18231224 | e6b6bdc7 | e5ba7672 | 74ef3502 |          |          | 5316a17f |          | 32c7478e | 9117a34a |          |          |


- 测试数据：test.txt：测试集于训练集的计算方式相同，但对应的是训练集时间段的后一天的事件。并且第一列（label）已被移除。

    - 示例：

  | label | f1   | f2   | f3   | f4   | f5   | f6   | f7   | f8   | f9   | f10  | f11  | f12  | f13  | f14      | f15      | f16      | f17      | f18      | f19      | f20      | f21      | f22      | f23      | f24      | f25      | f26      | f27      | f28      | f29      | f30      | f31      | f32      | f33      | f34      | f35      | f36      | f37      | f38      | f39      |
      | ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
  |       |      | 29   | 50   | 5    | 7260 | 437  | 1    | 4    | 14   |      | 1    | 0    | 6    | 5a9ed9b0 | a0e12995 | a1e14474 | 08a40877 | 25c83c98 |          | 964d1fdd | 5b392875 | a73ee510 | de89c3d2 | 59cd5ae7 | 8d98db20 | 8b216f7b | 1adce6ef | 78c64a1d | 3ecdadf7 | 3486227d | 1616f155 | 21ddcdc9 | 5840adea | 2c277e62 |          | 423fab69 | 54c91918 | 9b3e8820 | e75c9ae9 |
  |       | 27   | 17   | 45   | 28   | 2    | 28   | 27   | 29   | 28   | 1    | 1    |      | 23   | 68fd1e64 | 960c983b | 9fbfbfd5 | 38c11726 | 25c83c98 | 7e0ccccf | fe06fd10 | 062b5529 | a73ee510 | ca53fc84 | 67360210 | 895d8bbb | 4f8e2224 | f862f261 | b4cc2435 | 4c0041e5 | e5ba7672 | b4abdd09 | 21ddcdc9 | 5840adea | 36a7ab86 |          | 32c7478e | 85e4d73f | 010f6491 | ee63dd9b |
  |       | 1    | 1    | 19   | 7    | 1    | 3    | 1    | 7    | 7    | 1    | 1    |      | 2    | 09ca0b81 | 8947f767 | a87e61f7 | c4ba2a67 | 25c83c98 | 7e0ccccf | ce6020cc | 062b5529 | a73ee510 | b04d3cfe | 70dcd184 | 899eb56b | aca22cf9 | b28479f6 | a473257f | 88f592e4 | d4bb7bd8 | bd17c3da | 1d04f4a4 | a458ea53 | 82bdc0bb |          | 32c7478e | 5bdcd9c4 | 010f6491 | cca57dcc |

### MovieLens

MovieLens数据集由GroupLens研究组在 University of Minnesota中组织的。 最大的数据集使用约14万用户的数据，并覆盖27,000部电影。
除了评分之外，MovieLens数据还包含类似“Western”的流派信息和用户应用的标签，如“over the top”和“Arnold Schwarzenegger”。
这些流派标记和标签在构建内容向量方面是有用的。内容向量对项目的信息进行编码，例如颜色，形状，流派或真正的任何其他属性 - 可以是用于基于内容的推荐算法的任何形式。

MovieLens 25M Dataset

* About [dataset](https://files.grouplens.org/datasets/movielens/ml-25m-README.html)
* Download: `wget https://files.grouplens.org/datasets/movielens/ml-25m.zip`
* Permalink: https://grouplens.org/datasets/movielens/25m/
* https://movielens.org/

### Avazu 广告点击率预估数据集

* kaggle比赛官方网站：https://www.kaggle.com/c/avazu-ctr-prediction/overview
* 下载：https://www.kaggle.com/c/avazu-ctr-prediction/data
* 各个模型效果：https://paperswithcode.com/sota/click-through-rate-prediction-on-avazu

## NVIDIA Merlin

- Overview:[Merlin Overview](https://developer.nvidia.com/nvidia-merlin)
- Even Oldridge – NVIDIA Merlin Recommender Systems at Scale on the
  GPU: [video](https://www.bilibili.com/video/BV1q34y1E7sq/)

### ETL with NVIDIA NVTabular

### Dataloader with NVIDIA NVTabular

### Training using HugeCTR

### Training using TensorFlow

* Training Transformers4Rec (Tensorflow or Pytorch)
    * 什么是Transformers4Rec [介绍](./Merlin_Transformers4Rec.md)
    * Transformers4Rec[使用范例](./Merlin_Transformers4Rec.md)

Transformers4Rec: Bridging the Gap between NLP and Sequential / Session-Based Recommendation

* Source code on github: [link](https://github.com/NVIDIA-Merlin/Transformers4Rec/)
* [Document](https://nvidia-merlin.github.io/Transformers4Rec/main/index.html)
* Presentation of the paper "Transformers4Rec": [video](https://www.bilibili.com/video/BV1X3411G78H/)
* build an end-to-end session-based recommender system: [demo video](https://www.bilibili.com/video/BV1d5411Q7Yf/)
* Paper: https://dl.acm.org/doi/10.1145/3460231.3474255

### Inference with Triton

### Merlin Source code

- Open-source Merlin GitHub Repo -[Merlin Repo](https://github.com/NVIDIA-Merlin/Merlin)
    - NVTabular Github Repo - [NVTabular Repo](https://github.com/NVIDIA/NVTabular)
    - HugeCTR Github Repo - [HugeCTR Repo](https://github.com/NVIDIA/HugeCTR)


- Example Notebooks: [NVTabular Examples](https://github.com/NVIDIA/NVTabular/tree/main/examples)
  , [HugeCTR Examples](https://github.com/NVIDIA/HugeCTR/tree/master/notebooks)
    - [Getting Started with Movie Lens Dataset](https://github.com/NVIDIA/NVTabular/tree/main/examples/getting-started-movielens)
    - [Scaling Rec Sys Workload to Multi-GPU and Multi-Nodes](https://github.com/NVIDIA/NVTabular/tree/main/examples/scaling-criteo)
    - [Accelerated TF embeddings with HugeCTR Sparse Operation Kit](https://github.com/NVIDIA/HugeCTR/blob/master/notebooks/sparse_operation_kit_demo.ipynb)

- Reference Applications:
    - [DLRM](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Recommendation/DLRM) (PyTorch Training
      and Triton Inference)

    - [Wide &amp; Deep](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow/Recommendation) (
      TensorFlow Training),
    - [VAE-CF](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow/Recommendation) (TensorFlow
      Training),
    - [NCF](https://github.com/NVIDIA/DeepLearningExamples/tree/master/) (TensorFlow and PyTorch Training)

### Developer Blogs

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

### GTC talks

- GTC 2021 Sessions
    - Intro Blogs
        - [Learn how Spotify, Walmart, Tencent and Postmates are scaling and accelerating their recommender systems on GPU during GTC 2021](https://medium.com/nvidia-merlin/learn-how-spotify-walmart-tencent-and-postmates-are-scaling-and-accelerating-their-recommender-371ee4904cd4)
        - [NVIDIA Deepens Commitment to Streamlining Recommender Workflows with GTC Spring Sessions](https://developer.nvidia.com/blog/nvidia-deepens-commitment-to-streamlining-recommender-workflows-with-gtc-spring-sessions/)
    - [Accelerated ETL, Training and Inference of Recommender Systems on the GPU with Merlin, HugeCTR, NVTabular, and Triton](https://gtc21.event.nvidia.com/media/Accelerated%20ETL%2C%20Training%20and%20Inference%20of%20Recommender%20Systems%20on%20the%20GPU%20with%20Merlin%2C%20HugeCTR%2C%20NVTabular%2C%20and%20Triton%20%5BS31830%5D/1_6v5scqwv)
    - [Merlin HugeCTR: Deep Dive Into Performance Optimization](https://gtc21.event.nvidia.com/media/Merlin%20HugeCTR%3A%20Deep%20Dive%20Into%20Performance%20Optimization%20%5BS31269%5D/1_owz82snn)
    - [Training and Deploying Recommender Systems on the GPU: Merlin, HugeCTR, NVTabular, and Triton](https://gtc21.event.nvidia.com/media/Training%20and%20Deploying%20Recommender%20Systems%20on%20the%20GPU%3A%20Merlin%2C%20HugeCTR%2C%20NVTabular%2C%20and%20Triton%20%5BCWES1184%5D/1_udu6553p)

- GTC Spring 2022 Sessions

    - Building and Deploying Recommender Systems Quickly and Easily with NVIDIA
      Merlin [S41119](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1639106562192001FMKc)
    - Tutorial: Building Recommender Systems More Easily using Merlin
      Models [DLIT2043](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1639106562192001FMKc)
    - Building Next-gen Class Recommendations at Peloton with NVIDIA
      Merlin [S41259](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1634926177530001lfnt)
    - Scaling Real-time Deep Learning Recommendation Inference at a 150M+ User
      Scale [S42547](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&search.primarytopic=162464136458604127og#/session/1642819675389001aEvU)
    


