# LSTM模型在PyTorch和TensorRT上的推理

### 准备工作

- 一台Linux操作系统的GPU服务器, 安装GPU驱动:
- 安装Docker, 详见: https://docs.docker.com/engine/install/ubuntu/
- 安装 NVIDIA Container Toolkit, 详见: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

- 免费注册NVIDIA NGC: https://ngc.nvidia.com
  - 申请NGC API Key https://ngc.nvidia.com/setup/api-key
  - 在服务器端登录NGC

```bash
sudo docker login nvcr.io
Username: $oauthtoken
Password: 请填写第二步申请的API Key
```

### 使用Pytorch容器


```bash
docker pull nvcr.io/nvidia/pytorch:23.10-py3

docker run -it --gpus all --ipc=host  \
    --network=host \
    --shm-size=32g   --ulimit memlock=-1 --ulimit stack=67108864 \
    -v /workspace:/workspace \
    nvcr.io/nvidia/pytorch:23.10-py3    \
    bash
```

容器中主要软件的对应版本:

```
tensorrt                  8.6.1
torch                     2.1.0a0+32f93b1
```

以下步骤在容器内完成


### 创建、导出 LSTM模型

在 `/workspace`目录下，创建文件 `export_lstm_model.py` (如下示例代码)


```python
import torch
import onnx
from torch import nn
import numpy as np
import onnxruntime.backend as backend
import numpy as np
import time


torch.manual_seed(0)

num_layers = 10

model = nn.LSTM(10, 20, num_layers=num_layers, bidirectional=True)
model.eval()

with torch.no_grad():
    input = torch.randn(1, 3, 10)
    h0 = torch.randn(num_layers * 2, 3, 20)
    c0 = torch.randn(num_layers * 2, 3, 20)
    output, (hn, cn) = model(input, (h0, c0))


# export model to onnx
torch.onnx.export(model, (input, (h0, c0)), "lstm.onnx")
onnx_model = onnx.load("lstm.onnx")
# input shape [5, 3, 10]
print(onnx_model.graph.input[0])

# export with `dynamic_axes`
torch.onnx.export(
    model,
    (input, (h0, c0)),
    "lstm.onnx",
    input_names=["input", "h0", "c0"],
    output_names=["output", "hn", "cn"],
    dynamic_axes={"input": {0: "sequence"}, "output": {0: "sequence"}},
)

#
# run onnx inference and check output results
#

onnx_model = onnx.load("lstm.onnx")
# input shape ['sequence', 3, 10]

t0 = time.time()
for i in range(10):
    output, (hn, cn) = model(input, (h0, c0))
print("on cpu, time for 10 iter: {} sec".format(time.time() - t0))

# Check results between pytorch model and onnx model
y, (hn, cn) = model(input, (h0, c0))
y_onnx, hn_onnx, cn_onnx = backend.run(
    onnx_model, [input.numpy(), h0.numpy(), c0.numpy()], device="CPU"
)

np.testing.assert_almost_equal(y_onnx, y.detach(), decimal=5)
np.testing.assert_almost_equal(hn_onnx, hn.detach(), decimal=5)
np.testing.assert_almost_equal(cn_onnx, cn.detach(), decimal=5)


```


并执行该脚本导出 LSTM模型文件为 onnx格式: `python3 export_lstm_model.py`; Sample output:

```bash
name: "input"
type {
  tensor_type {
    elem_type: 1
    shape {
      dim {
        dim_value: 1
      }
      dim {
        dim_value: 3
      }
      dim {
        dim_value: 10
      }
    }
  }
}

on cpu, time for 10 iter: 11.87377643585205 sec

```

### Inference using Pytorch and GPU

save the following sample code to `run_pytorch_gpu.py` in your `/worskspace` folder.

```python
import torch
import onnx
from torch import nn
import numpy as np
import onnxruntime.backend as backend
import numpy as np
import time

num_layers = 10


model = nn.LSTM(10, 20, num_layers=num_layers, bidirectional=True)
model.eval()
model.to("cuda")

with torch.no_grad():
    input = torch.randn(1, 3, 10, device="cuda")
    h0 = torch.randn(num_layers * 2, 3, 20, device="cuda")
    c0 = torch.randn(num_layers * 2, 3, 20, device="cuda")
    output, (hn, cn) = model(input, (h0, c0))

t0 = time.time()

for i in range(100):
    output, (hn, cn) = model(input, (h0, c0))

print("time for 100 iter: {} sec".format(time.time()-t0))

```

Run `python3 run_pytorch_gpu.py`. Sample output (you may get different results depending on your GPU)

```
time for 100 iter: 0.043291568756103516 sec
```

### Convert LSTM Model to TensorRT

We use command line tool `trtexec` to test model conversion and out of box performance.

Run `trtexec --onnx=lstm.onnx --saveEngine=lstm_trt_fp32.engine --verbose`

Sample output (you may get different results depending on your GPU)

```bash

...

[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.226392 ms - Host latency: 0.256519 ms (enqueue 0.180469 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.225391 ms - Host latency: 0.255737 ms (enqueue 0.179907 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.226001 ms - Host latency: 0.256567 ms (enqueue 0.18064 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.225464 ms - Host latency: 0.25564 ms (enqueue 0.179883 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.225708 ms - Host latency: 0.257739 ms (enqueue 0.18208 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.225391 ms - Host latency: 0.256079 ms (enqueue 0.179321 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.225171 ms - Host latency: 0.256763 ms (enqueue 0.180664 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.225366 ms - Host latency: 0.255054 ms (enqueue 0.179468 ms)
[03/16/2024-13:35:03] [I] Average on 10 runs - GPU latency: 0.225391 ms - Host latency: 0.255322 ms (enqueue 0.179736 ms)

...

[03/16/2024-13:35:03] [I]
[03/16/2024-13:35:03] [I] === Performance summary ===
[03/16/2024-13:35:03] [I] Throughput: 4300.33 qps
[03/16/2024-13:35:03] [I] Latency: min = 0.250122 ms, max = 1.62878 ms, mean = 0.2559 ms, median = 0.255371 ms, percentile(90%) = 0.258057 ms, percentile(95%) = 0.258789 ms, percentile(99%) = 0.260254 ms
[03/16/2024-13:35:03] [I] Enqueue Time: min = 0.170959 ms, max = 1.60791 ms, mean = 0.179284 ms, median = 0.179565 ms, percentile(90%) = 0.181519 ms, percentile(95%) = 0.182861 ms, percentile(99%) = 0.1875 ms
[03/16/2024-13:35:03] [I] H2D Latency: min = 0.0151367 ms, max = 1.31348 ms, mean = 0.0162684 ms, median = 0.0161133 ms, percentile(90%) = 0.0164795 ms, percentile(95%) = 0.0169678 ms, percentile(99%) = 0.0177002 ms
[03/16/2024-13:35:03] [I] GPU Compute Time: min = 0.222168 ms, max = 1.59949 ms, mean = 0.225527 ms, median = 0.225281 ms, percentile(90%) = 0.226318 ms, percentile(95%) = 0.227295 ms, percentile(99%) = 0.227417 ms
[03/16/2024-13:35:03] [I] D2H Latency: min = 0.0109863 ms, max = 0.0217285 ms, mean = 0.0141102 ms, median = 0.013916 ms, percentile(90%) = 0.0166016 ms, percentile(95%) = 0.0170898 ms, percentile(99%) = 0.0184326 ms
[03/16/2024-13:35:03] [I] Total Host Walltime: 3.00047 s
[03/16/2024-13:35:03] [I] Total GPU Compute Time: 2.90997 s
[03/16/2024-13:35:03] [W] * GPU compute time is unstable, with coefficient of variance = 7.41713%.
[03/16/2024-13:35:03] [W]   If not already in use, locking GPU clock frequency or adding --useSpinWait may improve the stability.
[03/16/2024-13:35:03] [I] Explanations of the performance metrics are printed in the verbose logs.
[03/16/2024-13:35:03] [V]
[03/16/2024-13:35:03] [V] === Explanations of the performance metrics ===
[03/16/2024-13:35:03] [V] Total Host Walltime: the host walltime from when the first query (after warmups) is enqueued to when the last query is completed.
[03/16/2024-13:35:03] [V] GPU Compute Time: the GPU latency to execute the kernels for a query.
[03/16/2024-13:35:03] [V] Total GPU Compute Time: the summation of the GPU Compute Time of all the queries. If this is significantly shorter than Total Host Walltime, the GPU may be under-utilized because of host-side overheads or data transfers.
[03/16/2024-13:35:03] [V] Throughput: the observed throughput computed by dividing the number of queries by the Total Host Walltime. If this is significantly lower than the reciprocal of GPU Compute Time, the GPU may be under-utilized because of host-side overheads or data transfers.
[03/16/2024-13:35:03] [V] Enqueue Time: the host latency to enqueue a query. If this is longer than GPU Compute Time, the GPU may be under-utilized.
[03/16/2024-13:35:03] [V] H2D Latency: the latency for host-to-device data transfers for input tensors of a single query.
[03/16/2024-13:35:03] [V] D2H Latency: the latency for device-to-host data transfers for output tensors of a single query.
[03/16/2024-13:35:03] [V] Latency: the summation of H2D Latency, GPU Compute Time, and D2H Latency. This is the latency to infer a single query.
[03/16/2024-13:35:03] [I]
&&&& PASSED TensorRT.trtexec [TensorRT v8601] # trtexec --onnx=lstm.onnx --verbose

```


If we build and run TensorRT engine in FP16 precision, latency is similar with FP32 situtation.
Run: `trtexec --onnx=lstm.onnx --saveEngine=lstm_trt_fp16.engine --fp16 --verbose`, sample output:

```bash

...
[03/20/2024-08:42:44] [I] Average on 10 runs - GPU latency: 0.227856 ms - Host latency: 0.256812 ms (enqueue 0.224561 ms)
[03/20/2024-08:42:44] [I] Average on 10 runs - GPU latency: 0.228247 ms - Host latency: 0.255933 ms (enqueue 0.218604 ms)
[03/20/2024-08:42:44] [I] Average on 10 runs - GPU latency: 0.297095 ms - Host latency: 0.325732 ms (enqueue 0.290894 ms)
[03/20/2024-08:42:44] [I] Average on 10 runs - GPU latency: 0.228955 ms - Host latency: 0.257642 ms (enqueue 0.219531 ms)
[03/20/2024-08:42:44] [I] Average on 10 runs - GPU latency: 0.229053 ms - Host latency: 0.256494 ms (enqueue 0.220898 ms)
[03/20/2024-08:42:44] [I]
[03/20/2024-08:42:44] [I] === Performance summary ===
[03/20/2024-08:42:44] [I] Throughput: 3491.54 qps
[03/20/2024-08:42:44] [I] Latency: min = 0.251892 ms, max = 4.15649 ms, mean = 0.263016 ms, median = 0.25708 ms, percentile(90%) = 0.263855 ms, percentile(95%) = 0.276123 ms, percentile(99%) = 0.352783 ms
[03/20/2024-08:42:44] [I] Enqueue Time: min = 0.187683 ms, max = 4.08435 ms, mean = 0.224477 ms, median = 0.219543 ms, percentile(90%) = 0.227295 ms, percentile(95%) = 0.23584 ms, percentile(99%) = 0.294189 ms
[03/20/2024-08:42:44] [I] H2D Latency: min = 0.0148926 ms, max = 0.274414 ms, mean = 0.0170437 ms, median = 0.0166016 ms, percentile(90%) = 0.0185547 ms, percentile(95%) = 0.019043 ms, percentile(99%) = 0.020752 ms
[03/20/2024-08:42:44] [I] GPU Compute Time: min = 0.225098 ms, max = 4.11542 ms, mean = 0.233777 ms, median = 0.228394 ms, percentile(90%) = 0.231323 ms, percentile(95%) = 0.244751 ms, percentile(99%) = 0.296997 ms
[03/20/2024-08:42:44] [I] D2H Latency: min = 0.0109863 ms, max = 0.208008 ms, mean = 0.0121948 ms, median = 0.0119629 ms, percentile(90%) = 0.0129395 ms, percentile(95%) = 0.0145264 ms, percentile(99%) = 0.0198364 ms
[03/20/2024-08:42:44] [I] Total Host Walltime: 3.00068 s
[03/20/2024-08:42:44] [I] Total GPU Compute Time: 2.44928 s
[03/20/2024-08:42:44] [W] * Throughput may be bound by Enqueue Time rather than GPU Compute and the GPU may be under-utilized.
[03/20/2024-08:42:44] [W]   If not already in use, --useCudaGraph (utilize CUDA graphs where possible) may increase the throughput.
[03/20/2024-08:42:44] [W] * GPU compute time is unstable, with coefficient of variance = 28.1311%.
[03/20/2024-08:42:44] [W]   If not already in use, locking GPU clock frequency or adding --useSpinWait may improve the stability.
[03/20/2024-08:42:44] [I] Explanations of the performance metrics are printed in the verbose logs.
[03/20/2024-08:42:44] [I]
&&&& PASSED TensorRT.trtexec [TensorRT v8601] # trtexec --onnx=lstm.onnx --saveEngine=lstm_trt_fp16.engine --fp16
```
