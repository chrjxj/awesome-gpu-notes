# NVidia RAPIDS SDKs

- [RAPIDS入门介绍](https://www.bilibili.com/video/BV1WT4y197AT)

- 如何在 GPU 上进行海量数据流的 ETL 处理, [video](https://www.nvidia.cn/gtc/on-demand/archived-sessions/?id=c16333c2-0ebd-4e8a-939a-e67139a291dd) and [slides](https://live.nvidia.cn/gtc-od/attachments/CNS20699.pdf)
    * RAPIDS CUDA Dataframe（cuDF）将 ETL 性能提高了 60 倍。直接将数据流传输到 cuDF 中，可确保用户可以充分利用 RAPIDS 提供的性能优势，同时最大程度地减少数据准备带来的延迟。我们将介绍如何创建用户定义的 cuDF 的数据源以将数据从第三方系统直接传递到 GPU dataframe 的。我们还将介绍架构设计模式，并展示开发人员如何编写有效的代码来将数据从外部系统直接传递到 GPU 中的。

- RAPIDS概览和更新, [video](https://www.bilibili.com/video/BV1Qy4y1x7gE/?share_source=copy_web&vd_source=d36d329e5f8cf03e67975cd6b0e18089) and [slides](https://live.nvidia-china.com/gtc-od/attachments/CNS20597.pdf)
    
    * 全面的介绍 RAPIDS 软件库，涵盖了 RAPIDS 核心库 cuDF 、 cuML 、 cuGraph，加速 GIS 工作流的 cuSpatial，加速信号处理的 cuSignal 和用于视觉化的 cuxfilter，以及各个组件最新的软件内容和更新。最后通过本研讨还可以了解到 RAPIDS 与头部软件库的集成情况

## cuDF


- Code: https://github.com/rapidsai/cudf
- Document: https://docs.rapids.ai/api/cudf/stable/
- Worshops

    - GTC Silicon Valley-2019 ID:S9793:cuDF: RAPIDS GPU-Accelerated Data Frame Library:  [video](https://developer.nvidia.com/gtc/2019/video/s9793) and [slides](https://developer.download.nvidia.cn/video/gputechconf/gtc/2019/presentation/s9793-cudf-rapids-gpu-accelerated-data-frame-library.pdf)



#### `Fraud Detection with RAPIDS` - performance benchmark between CPU and GPU

See details in the [notebook](./fraud-detection-with-rapids-hands-on.ipynb)

| Stage | Time on CPU (sec)  | Time on A100 GPU (sec)|
| ------ | ----------- | ------ | 
| load data   | 30.1 | 4.5 | 
| training | 62 | 9 |
| evaluation | 2.2 | 0.5 |



## Dask

dask是一个python编写的，灵活的大数据并行计算库(框架)，是一个比spark更轻盈的分布式计算框架，能在分布式集群中进行分布式并行计算，也可以在单机(多核心)中进行伪分布式并行计算。
与spark这些大数据处理引擎(框架)相比较，dask更轻。dask更侧重与其他库(比如numpy，pandas，Scikit-learn)相结合来使用，从而使这些库能更加方便进行分布式并行计算。

目前dask支持5种主要的数据结构，分别是：

* Array（用于存放类numpy的多维数组），
* DataFrame（不用多说，类pandas的二维表结构的数据帧），
* Bag（更简单的一个数组），
* Delayed（对函数的异步处理封装，针对本地多进程与多线程），
* Futures（对函数的分布式异步提交处理封装，比delayed多提供网络api）。

Workshops

- Scalable Machine Learning with Dask, [vidoe](https://www.bilibili.com/video/BV1jE411o7fX)
- RAPIDS: Dask and cuDF NYCTaxi: [video](https://youtu.be/gV0cykgsTPM)

