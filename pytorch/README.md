# README


### CUSTOM C++ AND CUDA EXTENSIONS


* [CUSTOM C++ AND CUDA EXTENSIONS](https://pytorch.org/tutorials/advanced/cpp_extension.html) tutorials
* source code in the tutorials: [github repo](https://github.com/pytorch/extension-cpp) or local copy



* start docker container

```
docker run --gpus '"device=3"' -it --ipc=host -p 18888:8888 -v /your/path:/local  nvcr.io/nvidia/pytorch:21.03-py3 /bin/bash
```

* run experiements inside docker container: 

```
cd /path/to/extension-cpp-master
export MAX_JOBS=16
cd ./cpp && python setup.py install
cd ../cuda && python setup.py install
cd ..
```

* Known issues:

In the [CUSTOM C++ AND CUDA EXTENSIONS](https://pytorch.org/tutorials/advanced/cpp_extension.html), the  `auto gates = gate_weights.reshape({batch_size, 3, state_size});` line in `lltm_cuda_forward` kernel is a bug, causing shape mismatch.

