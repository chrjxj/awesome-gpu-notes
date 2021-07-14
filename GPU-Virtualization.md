# GPU Virtualization


### NV Docs

* vGPU对物理GPU的算力的分配 ([doc](https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#grid-vgpu-introduction))

    * vGPU v11.1 之前，算力的分配仅支持 time-sliced basis;
        * time-sliced basis [计算资源调度策略](https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#changing-vgpu-scheduling-policy)（参见 vGPU SW guide, section 8）
        * Best efforts （默认选项，支持Maxwell architecture以及之后）
        * Equal share scheduler (Maxwell architecture 之后)
        * Fixed share scheduler (Maxwell architecture 之后)

    * vGPU v11.1 以及之后，额外增加 vGPU MIG支持 （需要物理GPU支持MIG，如A100）
        * 关于MIG：请参见 MIG User Guide “introduction” https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#introduction

* 其他

    * GPU管理功能 https://docs.nvidia.com/grid/latest/grid-management-sdk-user-guide/index.html
    * [NVIDIA vGPU试用License全新申请流程介绍](https://mp.weixin.qq.com/s?__biz=MzUyNTE2MzUyNQ==&mid=2247484991&idx=1&sn=a207ffcef55bf896f366d899e9c3f1bc&chksm=fa230b55cd54824354e72f7681b908d6a5a85473145f50585c83a6e0a456c5ada1272c846d83&token=2085931763&lang=zh_CN#rd)

### Tech blogs

* 2018年阿里云郑晓，龙欣推出的 《浅谈GPU虚拟化技术》 系列博客，很系统的总结了Intel、Nvidia、AMD三大厂商的硬件虚拟化技术。
    
    * 阿里云郑晓：浅谈GPU虚拟化技术（第一章）-GPU虚拟化发展史
    * 阿里云郑晓：浅谈GPU虚拟化技术（第二章）-GPU直通模式
    * 第三章 浅谈GPU虚拟化技术（三）GPU SRIOV及vGPU调度
    * 浅谈GPU虚拟化技术（四）- GPU分片虚拟化
    * 浅谈GPU虚拟化技术（五）：GPU图形渲染虚拟化的业界难题-VDI的用户体验

* 爱奇艺 [爱奇艺 vGPU 的探索与实践](https://mp.weixin.qq.com/s/nXggFCcZ_uKxKj-PGtcppw)

* 腾讯技术工程: [GPU虚拟化，算力隔离，和qGPU](https://mp.weixin.qq.com/s/3VjGpyXZSkJhy6sFPUsZzw)

* [硬件支持的GPU虚拟化技术](http://juniorprincewang.github.io/2018/06/18/%E7%A1%AC%E4%BB%B6%E6%94%AF%E6%8C%81%E7%9A%84GPU%E8%99%9A%E6%8B%9F%E5%8C%96%E6%8A%80%E6%9C%AF/)



