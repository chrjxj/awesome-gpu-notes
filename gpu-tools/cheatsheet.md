# Cheatsheet



### Use MPS


```bash
# ====== 启动 =========
export CUDA_VISIBLE_DEVICES=0         # 这里以GPU0为例，其他卡类似
nvidia-smi -i 0 -c EXCLUSIVE_PROCESS  # 让GPU0变为独享模式。
nvidia-cuda-mps-control -d            # 开启mps服务 
# ====== 查看 =========
ps -ef | grep mps                     # 启动成功后能看到相应的进程
# ====== 停止 =========
nvidia-smi -i 0 -c DEFAULT       # 让GPU恢复为默认模式。
echo quit | nvidia-cuda-mps-control   # 关闭mps服务      
```


### Nsight System

nsys profile --trace=cuda,cudnn,cublas,osrt,nvtx --delay=60 --duration 60 -o your_output_file python train.py 

nsys profile --trace=cuda,osrt,nvtx --delay=60 --duration 60 -o your_output_file python train.py
