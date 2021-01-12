# README

A shared memory Implementation of matrix multiply in CUDA.

### build 

```
mkdir -p bin
make
```

### test

| Input Size      | Globalmem Implementation (sec) | Sharedmem Implementation (sec) |
| :---:        |    :----:  |    :----:  |
| A: 320x320, B:  320x320               | 0.001806 |0.00032 |
| A: 640x640, B:  640x640               | 0.0125 |0.00184 |
| A: 1024x1024, B:  1024x1024             | 0.05 |0.0069 |

MatMulKernel execution time: 0.006932


note: 

- test ran in a GTX 1070.
- latency is measured on kernel function execution only


### Profiling

1. In the target system, run `nsys profile -o your-output-filename ./matMul` and generate profiling file.
2. In the host system, use `nsight system` to open the *.qdrep file
