# Test NVidia Codec Performance

 


## Guide 


Must do: use `nvidia-smi` to check GPU/drive/CUDA versions, and software SDK version and version matches. 


#### 1. lock the GPU clock

- check supported clocks and clock the working frequency: 

```
nvidia-smi -q -i 0 -d SUPPORTED_CLOCKS

# mem clock, graphic clock; require sudo
sudo nvidia-smi -ac 877,1312 -i 0
```

- monitor codec hardware utility: `nvidia-smi dmon -i 0`


#### 2. Get video files

TBA

#### 3. Test with FFmpeg

``

1. install ffmpeg 


```bash
docker pull nvcr.io/nvidia/cuda:11.0-devel-ubuntu18.04
docker run -it --name codec-test --gpus all --runtime nvidia -e NVIDIA_DRIVER_CAPABILITIES=video,compute,utility -v /raid:/raid nvcr.io/nvidia/cuda:11.0-devel-ubuntu18.04 /bin/bash
```

[compile ffmpeg for linux](https://docs.nvidia.com/video-technologies/video-codec-sdk/ffmpeg-with-nvidia-gpu/#software-setup)

https://docs.nvidia.com/video-technologies/video-codec-sdk/ffmpeg-with-nvidia-gpu/

#### 4. Test with `DeepStream`


- in the host machine: 

```bash
docker pull nvcr.io/nvidia/deepstream:5.0.1-20.09-devel
docker run -it --gpus all -v /raid:/raid nvcr.io/nvidia/deepstream:5.0.1-20.09-devel /bin/bash
```

- check Deepstream config [file](deepstream-config.txt)

- inside Deepstream docker container: 

```bash
deepstream-app -c test.txt
```


#### 5. Test with `video-sdk-samples`

- get source code  

    * download `Video_Codec_SDK_11.0.10` from XXX
    * git clone: `git clone https://github.com/NVIDIA/video-sdk-samples.git`

- compile: TBA

- run: TBA

https://github.com/NVIDIA/video-sdk-samples/tree/master/Samples/AppDecode/AppDecPerf


## Reference

* [ffmpeg-with-nvidia-gpu](https://docs.nvidia.com/video-technologies/video-codec-sdk/ffmpeg-with-nvidia-gpu)
* [blog: nvidia-ffmpeg-transcoding-guide](https://developer.nvidia.com/blog/nvidia-ffmpeg-transcoding-guide/)
* [ffmpeg Compilation Guide](https://trac.ffmpeg.org/wiki/CompilationGuide)
