# NVIDIA常用工具和命令

## nvidia-smi

#### `nvidia-smi` 常用命令

```bash

# print GPU's FULL name
nvidia-smi --query-gpu=name --format=csv,noheader

nvidia-smi --query-gpu=timestamp,name,pci.bus_id,driver_version,pstate,pcie.link.gen.max, pcie.link.gen.current,temperature.gpu,utilization.gpu,utilization.memory, memory.total,memory.free,memory.used --format=csv -l 5


nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory, --format=csv -lms 1000


nvidia-smi --query-gpu=timestamp,name,pci.bus_id,driver_version,pstate,pcie.link.gen.max, pcie.link.gen.current,temperature.gpu,utilization.gpu,utilization.memory, memory.total,memory.free,memory.used --format=csv -lms 5
```

#### `nvidia-smi pmon` 常用命令

进程监控命令，以滚动条形式显示GPU进程状态信息。附加选项：

   ```bash
   # 指定刷新时间（默认为1秒，最大为10秒）
   nvidia-smi pmon –d xxx
   # 显示指定数目的统计信息并退出
   nvidia-smi pmon –c xxx

   #指定显示哪些监控指标（默认为u），其中：u：GPU使用率  m：FB内存使用情况
   nvidia-smi pmon –s xxx

   nvidia-smi pmon –o D/T  #指定显示的时间格式D：YYYYMMDD，THH:MM:SS
   nvidia-smi pmon –f xxx #将查询的信息输出到具体的文件中，不在终端显示
   ```

#### 设备监控命令 (`nvidia-smi dmon`)

设备监控命令，以滚动条形式显示GPU设备统计信息。监控最多4个GPU，如果没有指定任何GPU，则默认监控GPU0-GPU3（GPU索引从0开始）。

```
nvidia-smi dmon -s "pucet" -i 0 -o "DT" -d 2
#Date       Time        gpu   pwr gtemp mtemp    sm   mem   enc   dec  mclk  pclk sbecc dbecc   pci rxpci txpci
#YYYYMMDD   HH:MM:SS    Idx     W     C     C     %     %     %     %   MHz   MHz  errs  errs  errs  MB/s  MB/s
 20210102   19:12:31      0    37    19     -     0     0     0     0  4006   582     -     -     0     0     1
 20210102   19:12:33      0    39    19     -     0     0     0     0  4006  1582     -     -     0     0     0
 20210102   19:12:35      0    39    19     -     0     0     0     0  4006  1582     -     -     0     0     0
```

- 附加选项:

| Command      | Description |
|:---:|:----|     
|nvidia-smi dmon -i          |                                                     |
|nvidia-smi dmon -d xxx		 |  指定刷新时间（默认为1秒）                                      |
|nvidia-smi dmon -c xxx 	|	显示指定数目的统计信息并退出                                     |
|nvidia-smi dmon -o "DT" 	|	指定显示的时间格式D YYYYMMDD，TH                             |
|nvidia-smi dmon -f log.txt |		将查询的信息输出到具体的文件中，不在终端显示                         |
|nvidia-smi dmon -s "puc"    |  指定显示哪些监控指标（默认为puc），其中                              |

| metrics for `-s`     | Description |
| :---:        |    :----  |
|p | 电源使用情况和温度（pwr 功耗，temp 温度）                          |
|u | GPU使用率（sm 流处理器，mem 显存，enc 编码资源，dec 解码资源）           |
|c | GPU处理器和GPU内存时钟频率（mclk 显存频率，pclk 处理器频率）             |
|v | 电源和热力异常                                            |
|m | FB内存和Bar1内存                                        |
|e | ECC错误和PCIe重显错误个数                                   |
|t | PCIe读写带宽                                           |


| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

#### 和时钟和电源相关命令

![时钟和电源相关命令](./images/1.png)

详见: http://nvidia.custhelp.com/app/answers/detail/a_id/3751/~/useful-nvidia-smi-queries

#### nvidia-smi 查询

| Term      | Description |
| :---:        |    :----  |
|Fan                |      风扇转速（0%--100%），N/A表示没有风扇                                          |
|Temp               |   GPU温度（GPU温度过高会导致GPU频率下降）                                             |
|Perf               |      性能状态，从P0（最大性能）到P12（最小性能）                                          |
|Pwr                |      GPU功耗                                                             |
|Persistence-M    	|	持续模式的状态（持续模式耗能大，但在新的GPU应用启动时花费时间更少）             |
|Bus-Id             |   	GPU总线，domain:bus:device.function                                 |
|Disp.A             |    Display Active，表示GPU的显示是否初始化                                        |
|Memory-Usage 		|	显存使用率                                                                |
|Volatile GPU-Util 	|	GPU使用率                                                               |
|ECC                |    是否开启错误检查和纠正技术，0/DISABLED, 1/ENABLED                          |
|Compute M.      	|	计算模式，0/DEFAULT,1/EXCLUSIVE_PROCESS,2/PROHIBITED |



| Command      | Description |
| :---:        |    :----  |
|nvidia-smi -q -i xxx -f xxx  |     指定具体的GPU或unit信息;将查询的信息输出到具体的文件中，不在终端显示 |
|nvidia-smi -q -d xxx         |   指定显示GPU卡某些信息，xxx参数可以为MEMORY, UTILIZATION, ECC, TEMPERATURE, POWER,CLOCK, COMPUTE, PIDS, PERFORMANCE, SUPPORTED_CLOCKS, PAGE_RETIREMENT,ACCOUNTING |
|nvidia-smi -q -l xxx         |   动态刷新信息，可指定刷新频率，以秒为单位 |
|nvidia-smi --query-gpu=gpu_name,gpu_bus_id,vbios_version--format=csv     |       选择性查询选项，可以指定显示的属性选项 可查看的属性有 timestamp，driver_version，pci.bus，pcie.link.width.current等。（可查看nvidia-smi--help-query-gpu来查看有哪些属性）|

 

#### 设置GPU卡设备的状态选项

| Command      | Description |   
| :---:        |    :----  |     
|nvidia-smi -pm 0/1    |          设置持久模式 0/DISABLED,1/ENABLED                                |
|nvidia-smi -e 0/1     |          切换ECC支持 0/DISABLED, 1/ENABLED                              |
|nvidia-smi -p 0/1     |      重置ECC错误计数 0/VOLATILE, 1/AGGREGATE                              |
|nvidia-smi -c.        |      设置计算应用模式 0/DEFAULT,1/EXCLUSIVE_PROCESS,2/PROHIBITED            |
|nvidia-smi -r         |      GPU复位                                                          |
|nvidia-smi -vm.       |      设置GPU虚拟化模式                                                     |
|nvidia-smi -ac xxx,xxx|      设置GPU运行的工作频率。e.g. nvidia-smi -ac2000,800                       |
|nvidia-smi -rac 	|			将时钟频率重置为默认值                                                  |
|nvidia-smi -acp 0/1   |  切换-ac和-rac的权限要求，0/UNRESTRICTED, 1/RESTRICTED                       |
|nvidia-smi -pl  	   | 指定最大电源管理限制（瓦特）                                                      |
|nvidia-smi -am 0/1.   |  启用或禁用计数模式，0/DISABLED,1/ENABLED                                     |
|nvidia-smi -caa.      |  清除缓冲区中的所有已记录PID，0/DISABLED,1/ENABLED                               |




#### 在Windows上使用 `nvidia-smi`

- nvidia-smi所在的位置为：`C:\Program Files\NVIDIA Corporation\NVSMI`
- 建议添加路径到系统的 `PATH` 变量进行编辑

## NVIDIA Management Library (NVML)

```
----------------------------------------------------------
| nvidia-smi | python binding | 						 |
----------------------------------------------------------
|		NVIDIA Management Library (NVML)				 |
----------------------------------------------------------
```

- 安装Python包 `pip install nvidia-ml-py`
- NVML API[手册](https://docs.nvidia.com/deploy/nvml-api/nvml-api-reference.html)


## GPU Test Tools

#### GPU Stree Test on Linux

GPU burn

* Multi-GPU CUDA stress test http://wili.cc/blog/gpu-burn.html
* source code: https://github.com/wilicc/gpu-burn


## MPS

Enable or disable MPS:

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

## Use Multi-Instance GPU (MIG)

Multi-Instance GPU (MIG) is a feature on the A100/A30 GPU (and  Next-Gen Hopper GPUs) to slice it into GPU instances and GPU instances into compute instances. Note that many of the commands listed below might need to be run as sudo.

### Config MIG with `nvidia-smi`

To enable or disable MIG mode on all GPUs or a certain GPU:

```bash
sudo nvidia-smi -mig 1
sudo nvidia-smi -mig 0

sudo nvidia-smi -i 3 -mig 1
sudo nvidia-smi -i 3 -mig 0
```


To list all possible GPU instance placements:

```bash
$ sudo nvidia-smi mig -lgip
+--------------------------------------------------------------------------+
| GPU instance profiles:                                                   |
| GPU   Name          ID    Instances   Memory     P2P    SM    DEC   ENC  |
|                           Free/Total   GiB              CE    JPEG  OFA  |
|==========================================================================|
|   0  MIG 1g.5gb     19     7/7        4.75       No     14     0     0   |
|                                                          1     0     0   |
+--------------------------------------------------------------------------+
|   0  MIG 2g.10gb    14     3/3        9.75       No     28     1     0   |
|                                                          2     0     0   |
+--------------------------------------------------------------------------+
|   0  MIG 3g.20gb     9     2/2        19.62      No     42     2     0   |
|                                                          3     0     0   |
+--------------------------------------------------------------------------+
|   0  MIG 4g.20gb     5     1/1        19.62      No     56     2     0   |
|                                                          4     0     0   |
+--------------------------------------------------------------------------+
|   0  MIG 7g.40gb     0     1/1        39.50      No     98     5     0   |
|                                                          7     1     1   |
+--------------------------------------------------------------------------+


$ sudo nvidia-smi mig -lgipp
GPU  0 Profile ID 19 Placements: {0,1,2,3,4,5,6}:1
GPU  0 Profile ID 14 Placements: {0,2,4}:2
GPU  0 Profile ID  9 Placements: {0,4}:4
GPU  0 Profile ID  5 Placement : {0}:4
GPU  0 Profile ID  0 Placement : {0}:8
```

To create GPU instances on a MIG-enabled GPU:

```bash
$ sudo nvidia-smi mig -cgi 19,19,19,19,19,19,19 -i 3
Successfully created GPU instance ID 13 on GPU  0 using profile MIG 1g.5gb (ID 19)
Successfully created GPU instance ID 11 on GPU  0 using profile MIG 1g.5gb (ID 19)
Successfully created GPU instance ID 12 on GPU  0 using profile MIG 1g.5gb (ID 19)
Successfully created GPU instance ID  7 on GPU  0 using profile MIG 1g.5gb (ID 19)
Successfully created GPU instance ID  8 on GPU  0 using profile MIG 1g.5gb (ID 19)
Successfully created GPU instance ID  9 on GPU  0 using profile MIG 1g.5gb (ID 19)
Successfully created GPU instance ID 10 on GPU  0 using profile MIG 1g.5gb (ID 19)
```

To create compute instances on a MIG-enabled GPU:

```bash
$ sudo nvidia-smi mig -cci -i 3
Successfully created compute instance ID  0 on GPU  0 GPU instance ID  7 using profile MIG 1g.5gb (ID  0)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID  8 using profile MIG 1g.5gb (ID  0)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID  9 using profile MIG 1g.5gb (ID  0)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID 10 using profile MIG 1g.5gb (ID  0)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID 11 using profile MIG 1g.5gb (ID  0)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID 12 using profile MIG 1g.5gb (ID  0)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID 13 using profile MIG 1g.5gb (ID  0)
```


To view the created MIG instances:

```bash
$ nvidia-smi
(...)
$ nvidia-smi -L
GPU 0: A100-PCIE-40GB (UUID: GPU-0069414c-9f30-41f9-d5d8-87890423f0c4)
  MIG 1g.5gb Device 0: (UUID: MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/7/0)
  MIG 1g.5gb Device 1: (UUID: MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/8/0)
  MIG 1g.5gb Device 2: (UUID: MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/9/0)
  MIG 1g.5gb Device 3: (UUID: MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/10/0)
  MIG 1g.5gb Device 4: (UUID: MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/11/0)
  MIG 1g.5gb Device 5: (UUID: MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/12/0)
  MIG 1g.5gb Device 6: (UUID: MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/13/0)
```

To list GPU instances:  `$ sudo nvidia mig -lgi`
To list compute instances: `$ sudo nvidia mig -lci`

```bash
+-------------------------------------------------------+
| Compute instances:                                    |
| GPU     GPU       Name             Profile   Instance |
|       Instance                       ID        ID     |
|         ID                                            |
|=======================================================|
|   0      7       MIG 1g.5gb           0         0     |
+-------------------------------------------------------+
|   0      8       MIG 1g.5gb           0         0     |
+-------------------------------------------------------+
|   0      9       MIG 1g.5gb           0         0     |
+-------------------------------------------------------+
|   0     11       MIG 1g.5gb           0         0     |
+-------------------------------------------------------+
|   0     12       MIG 1g.5gb           0         0     |
+-------------------------------------------------------+
|   0     13       MIG 1g.5gb           0         0     |
+-------------------------------------------------------+
|   0     14       MIG 1g.5gb           0         0     |
+-------------------------------------------------------+
```

To destroy compute instances:

```bash
$ sudo nvidia-smi mig -dci -i 3
Successfully destroyed compute instance ID  0 from GPU  0 GPU instance ID  7
Successfully destroyed compute instance ID  0 from GPU  0 GPU instance ID  8
Successfully destroyed compute instance ID  0 from GPU  0 GPU instance ID  9
Successfully destroyed compute instance ID  0 from GPU  0 GPU instance ID 10
Successfully destroyed compute instance ID  0 from GPU  0 GPU instance ID 11
Successfully destroyed compute instance ID  0 from GPU  0 GPU instance ID 12
Successfully destroyed compute instance ID  0 from GPU  0 GPU instance ID 13
```

To destroy GPU instances:
```bash
$ sudo nvidia-smi mig -dgi -i 3
Successfully destroyed GPU instance ID  7 from GPU  0
Successfully destroyed GPU instance ID  8 from GPU  0
Successfully destroyed GPU instance ID  9 from GPU  0
Successfully destroyed GPU instance ID 10 from GPU  0
Successfully destroyed GPU instance ID 11 from GPU  0
Successfully destroyed GPU instance ID 12 from GPU  0
Successfully destroyed GPU instance ID 13 from GPU  0
```

### Use MIG with Docker container

To expose a MIG instance to a Docker container, add --gpus='"device=MIG-GPU-0069414c-9f30-41f9-d5d8-87890423f0c4/7/0"' to your docker --runtime=nvidia ... command.

Multiple MIG instances can be specified by separating with commas, like --gpus='"device=0:0,0:1"' for example.

### MIG Documentation

See [NVIDIA_MIG_User_Guide](https://docs.nvidia.com/datacenter/tesla/pdf/NVIDIA_MIG_User_Guide.pdf) for more information.

## Nsight System

```bash
nsys profile --trace=cuda,cudnn,cublas,osrt,nvtx --delay=60 --duration 60 -o your_output_file python train.py 

nsys profile --trace=cuda,osrt,nvtx --delay=60 --duration 60 -o your_output_file python train.py
```

## 附录

#### nvidia-smi manual

```
NVIDIA System Management Interface -- v418.67

NVSMI provides monitoring information for Tesla and select Quadro devices.
The data is presented in either a plain text or an XML format, via stdout or a file.
NVSMI also provides several management operations for changing the device state.

Note that the functionality of NVSMI is exposed through the NVML C-based
library. See the NVIDIA developer website for more information about NVML.
Python wrappers to NVML are also available.  The output of NVSMI is
not guaranteed to be backwards compatible; NVML and the bindings are backwards
compatible.

http://developer.nvidia.com/nvidia-management-library-nvml/
http://pypi.python.org/pypi/nvidia-ml-py/
Supported products:
- Full Support
    - All Tesla products, starting with the Kepler architecture
    - All Quadro products, starting with the Kepler architecture
    - All GRID products, starting with the Kepler architecture
    - GeForce Titan products, starting with the Kepler architecture
- Limited Support
    - All Geforce products, starting with the Kepler architecture
nvidia-smi [OPTION1 [ARG1]] [OPTION2 [ARG2]] ...

    -h,   --help                Print usage information and exit.

  LIST OPTIONS:

    -L,   --list-gpus           Display a list of GPUs connected to the system.

    -B,   --list-blacklist-gpus Display a list of blacklisted GPUs in the system.

  SUMMARY OPTIONS:

    <no arguments>              Show a summary of GPUs connected to the system.

    [plus any of]

    -i,   --id=                 Target a specific GPU.
    -f,   --filename=           Log to a specified file, rather than to stdout.
    -l,   --loop=               Probe until Ctrl+C at specified second interval.

  QUERY OPTIONS:

    -q,   --query               Display GPU or Unit info.

    [plus any of]

    -u,   --unit                Show unit, rather than GPU, attributes.
    -i,   --id=                 Target a specific GPU or Unit.
    -f,   --filename=           Log to a specified file, rather than to stdout.
    -x,   --xml-format          Produce XML output.
          --dtd                 When showing xml output, embed DTD.
    -d,   --display=            Display only selected information: MEMORY,
                                    UTILIZATION, ECC, TEMPERATURE, POWER, CLOCK,
                                    COMPUTE, PIDS, PERFORMANCE, SUPPORTED_CLOCKS,
                                    PAGE_RETIREMENT, ACCOUNTING, ENCODER_STATS, FBC_STATS
                                Flags can be combined with comma e.g. ECC,POWER.
                                Sampling data with max/min/avg is also returned
                                for POWER, UTILIZATION and CLOCK display types.
                                Doesn't work with -u or -x flags.
    -l,   --loop=               Probe until Ctrl+C at specified second interval.

    -lms, --loop-ms=            Probe until Ctrl+C at specified millisecond interval.

  SELECTIVE QUERY OPTIONS:

    Allows the caller to pass an explicit list of properties to query.

    [one of]

    --query-gpu=                Information about GPU.
                                Call --help-query-gpu for more info.
    --query-supported-clocks=   List of supported clocks.
                                Call --help-query-supported-clocks for more info.
    --query-compute-apps=       List of currently active compute processes.
                                Call --help-query-compute-apps for more info.
    --query-accounted-apps=     List of accounted compute processes.
                                Call --help-query-accounted-apps for more info.
    --query-retired-pages=      List of device memory pages that have been retired.
                                Call --help-query-retired-pages for more info.

    [mandatory]

    --format=                   Comma separated list of format options:
                                  csv - comma separated values (MANDATORY)
                                  noheader - skip the first line with column headers
                                  nounits - don't print units for numerical
                                             values

    [plus any of]

    -i,   --id=                 Target a specific GPU or Unit.
    -f,   --filename=           Log to a specified file, rather than to stdout.
    -l,   --loop=               Probe until Ctrl+C at specified second interval.
    -lms, --loop-ms=            Probe until Ctrl+C at specified millisecond interval.

  DEVICE MODIFICATION OPTIONS:

    [any one of]

    -pm,  --persistence-mode=   Set persistence mode: 0/DISABLED, 1/ENABLED
    -e,   --ecc-config=         Toggle ECC support: 0/DISABLED, 1/ENABLED
    -p,   --reset-ecc-errors=   Reset ECC error counts: 0/VOLATILE, 1/AGGREGATE
    -c,   --compute-mode=       Set MODE for compute applications:
                                0/DEFAULT, 1/EXCLUSIVE_PROCESS,
                                2/PROHIBITED
          --gom=                Set GPU Operation Mode:
                                    0/ALL_ON, 1/COMPUTE, 2/LOW_DP
    -r    --gpu-reset           Trigger reset of the GPU.
                                Can be used to reset the GPU HW state in situations
                                that would otherwise require a machine reboot.
                                Typically useful if a double bit ECC error has
                                occurred.
                                Reset operations are not guarenteed to work in
                                all cases and should be used with caution.
    -vm   --virt-mode=          Switch GPU Virtualization Mode:
                                Sets GPU virtualization mode to 3/VGPU or 4/VSGA
                                Virtualization mode of a GPU can only be set when
                                it is running on a hypervisor.
    -lgc  --lock-gpu-clocks=    Specifies <minGpuClock,maxGpuClock> clocks as a
                                    pair (e.g. 1500,1500) that defines the range
                                    of desired locked GPU clock speed in MHz.
                                    Setting this will supercede application clocks
                                    and take effect regardless if an app is running.
                                    Input can also be a singular desired clock value
                                    (e.g. <GpuClockValue>).
    -rgc  --reset-gpu-clocks
                                Resets the Gpu clocks to the default values.
    -ac   --applications-clocks= Specifies <memory,graphics> clocks as a
                                    pair (e.g. 2000,800) that defines GPU's
                                    speed in MHz while running applications on a GPU.
    -rac  --reset-applications-clocks
                                Resets the applications clocks to the default values.
    -acp  --applications-clocks-permission=
                                Toggles permission requirements for -ac and -rac commands:
                                0/UNRESTRICTED, 1/RESTRICTED
    -pl   --power-limit=        Specifies maximum power management limit in watts.
    -cc   --cuda-clocks=        Overrides or restores default CUDA clocks.
                                In override mode, GPU clocks higher frequencies when running CUDA applications.
                                Only on supported devices starting from the Volta series.
                                Requires administrator privileges.
                                0/RESTORE_DEFAULT, 1/OVERRIDE
    -am   --accounting-mode=    Enable or disable Accounting Mode: 0/DISABLED, 1/ENABLED
    -caa  --clear-accounted-apps
                                Clears all the accounted PIDs in the buffer.
          --auto-boost-default= Set the default auto boost policy to 0/DISABLED
                                or 1/ENABLED, enforcing the change only after the
                                last boost client has exited.
          --auto-boost-permission=
                                Allow non-admin/root control over auto boost mode:
                                0/UNRESTRICTED, 1/RESTRICTED
   [plus optional]

    -i,   --id=                 Target a specific GPU.

  UNIT MODIFICATION OPTIONS:

    -t,   --toggle-led=         Set Unit LED state: 0/GREEN, 1/AMBER

   [plus optional]

    -i,   --id=                 Target a specific Unit.

  SHOW DTD OPTIONS:

          --dtd                 Print device DTD and exit.

     [plus optional]

    -f,   --filename=           Log to a specified file, rather than to stdout.
    -u,   --unit                Show unit, rather than device, DTD.

    --debug=                    Log encrypted debug information to a specified file.

 STATISTICS: (EXPERIMENTAL)
    stats                       Displays device statistics. "nvidia-smi stats -h" for more information.

 Device Monitoring:
    dmon                        Displays device stats in scrolling format.
                                "nvidia-smi dmon -h" for more information.

    daemon                      Runs in background and monitor devices as a daemon process.
                                This is an experimental feature. Not supported on Windows baremetal
                                "nvidia-smi daemon -h" for more information.

    replay                      Used to replay/extract the persistent stats generated by daemon.
                                This is an experimental feature.
                                "nvidia-smi replay -h" for more information.

 Process Monitoring:
    pmon                        Displays process stats in scrolling format.
                                "nvidia-smi pmon -h" for more information.

 TOPOLOGY:
    topo                        Displays device/system topology. "nvidia-smi topo -h" for more information.

 DRAIN STATES:
    drain                       Displays/modifies GPU drain states for power idling. "nvidia-smi drain -h" for more information.

 NVLINK:
    nvlink                      Displays device nvlink information. "nvidia-smi nvlink -h" for more information.

 CLOCKS:
    clocks                      Control and query clock information. "nvidia-smi clocks -h" for more information.

 ENCODER SESSIONS:
    encodersessions             Displays device encoder sessions information. "nvidia-smi encodersessions -h" for more information.

 FBC SESSIONS:
    fbcsessions                 Displays device FBC sessions information. "nvidia-smi fbcsessions -h" for more information.

 GRID vGPU:
    vgpu                        Displays vGPU information. "nvidia-smi vgpu -h" for more information.

Please see the nvidia-smi(1) manual page for more detailed information.

```

#### nvidia-smi manual for MIG


Run `$ nvidia-smi mig -h` to dump full usage information:

```bash
    mig -- Multi Instance GPU management.

    Usage: nvidia-smi mig [options]

    Options include:
    [-h | --help]: Display help information.
    [-i | --id]: Enumeration index, PCI bus ID or UUID.
                 Provide comma separated values for more than one device.
    [-gi | --gpu-instance-id]: GPU instance ID.
                               Provide comma separated values for more than one GPU instance.
    [-ci | --compute-instance-id]: Compute instance ID.
                                   Provide comma separated values for more than one compute
                                   instance.
    [-lgip | --list-gpu-instance-profiles]: List supported GPU instance profiles.
                                            Option -i can be used to restrict the command to
                                            run on a specific GPU.
    [-lgipp | --list-gpu-instance-possible-placements]: List possible GPU instance placements
                                                        in the following format, {Start}:Size.
                                                        Option -i can be used to restrict the
                                                        command to run on a specific GPU.
    [-C | --default-compute-instance]: Create compute instance with the default profile when used
                                       with the option to create a GPU instance (-cgi).
    [-cgi | --create-gpu-instance]: Create GPU instance for the given profile names or IDs.
                                    Provide comma separated values for more than one profile.
                                    Option -i can be used to restrict the command to run on
                                    a specific GPU.
    [-dgi | --destroy-gpu-instance]: Destroy GPU instances.
                                     Options -i and -gi can be used individually or combined
                                     to restrict the command to run on a specific GPU or GPU
                                     instance.
    [-lgi | --list-gpu-instances]: List GPU instances.
                                   Option -i can be used to restrict the command to run on a
                                   specific GPU.
    [-lcip | --list-compute-instance-profiles]: List supported compute instance profiles.
                                                Options -i and -gi can be used individually or
                                                combined to restrict the command to run on a
                                                specific GPU or GPU instance.
    [-cci | --create-compute-instance]: Create compute instance for the given profile name or IDs.
                                        Provide comma separated values for more than one profile.
                                        If no profile name or ID is given, then the default*
                                        compute instance profile ID will be used. Options -i and
                                        -gi can be used individually or combined to restrict the
                                        command to run on a specific GPU or GPU instance.
    [-dci | --destroy-compute-instance]: Destroy compute instances.
                                         Options -i, -gi and -ci can be used individually or
                                         combined to restrict the command to run on a specific
                                         GPU or GPU instance or compute instance.
    [-lci | --list-compute-instances]: List compute instances.
                                       Options -i and -gi can be used individually or combined
                                       to restrict the command to run on a specific GPU or GPU
                                       instance.
```


#### Reference


- https://blog.csdn.net/C_chuxin/article/details/82993350
