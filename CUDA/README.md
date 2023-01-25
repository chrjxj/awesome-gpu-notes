# CUDA Resources


## Documents

- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)
- [CUDA Best Practice Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)


## Lecture







- CUDA初级教程视频, NVIDIA Fellow 周斌博士: [B站](https://www.bilibili.com/video/BV1kx411m7Fk), [iQiyi](http://www.iqiyi.com/a_19rrhbvoe9.html)

- CSci 360 Computer Architecture, Prof. Stewart Weiss 

	* [home page](http://compsci.hunter.cuny.edu/~sweiss/course_materials/csci360/csci360_f14.php)
	* [assets](./cuny-sweiss-csci360/)

Books

- Professional CUDA C Programming; CUDA C编程权威指南 (John Cheng; Ty McKercher): 
[pdf (en)](https://www.cs.utexas.edu/~rossbach/cs380p/papers/cuda-programming.pdf);   [links (cn)](https://developer.aliyun.com/article/109432?spm=a2c6h.12873639.article-detail.58.745186b8BHLDE0&scm=20140722.ID_community@@article@@109432._.ID_community@@article@@109432-OR_rec-V_1)

- CUDA for Engineers, An Introduction to High-Performance Parallel Computing; Duane Storti
- GPU Gems 3, [book](https://developer.nvidia.com/gpugems/gpugems3/part-i-geometry) and [CD](https://http.download.nvidia.com/developer/GPU_Gems_3/CD)


## Topics

#### Multi-GPUs

The following are for students with time and interest to do additional study on topics related to this workshop.

* data paralle when using multi-GPUs: depth-first vs breadth-first approach: this [stack overflow answer](https://stackoverflow.com/questions/11673154/concurrency-in-cuda-multi-gpu-executions) provides several examples of CUDA code using both depth-first and breadth-first approaches.
* peer to peer memory transfers;  multiple GPUs on multiple nodes:  [This Supercomputing Conference Presentation](https://www.nvidia.com/docs/IO/116711/sc11-multi-gpu.pdf) will give you a good starting point


#### cuda-python

CUDA Python provides uniform APIs and bindings for CuPy, Numba, and CUDA:

* CuPy:aa NumPy/SciPy compatible Array library for GPU  
* Numba: a Python compiler that can compile Python code for execution on CUDA-capable GPUs



Resources:

* home page: https://developer.nvidia.com/cuda-python
* https://nvidia.github.io/cuda-python and [API reference](https://nvidia.github.io/cuda-python/api.html)
* GitHub: https://github.com/NVIDIA/cuda-python


## CUDA Sample Code


- [NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples) and its [release note](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
- [cude-code-101](./cude-code-101/)
- [sgemm](https://github.com/cwpearson/nvidia-performance-tools/tree/90890e807ef9fc1532ee08938de6689444701686/sgemm)

