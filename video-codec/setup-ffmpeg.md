# ffmpeg with CUDA

## Setup ffmpeg

Prerequisites

- ffmpeg requires separate git repository nvcodec-headers for NV-accelerated ffmpeg build.
- To compile ffmpeg, the CUDA toolkit must be installed on the system, though the CUDA toolkit is not needed to run the ffmpeg compiled binary.


#### Compiling ffmpeg for Linux

run the following commands with `sudo`:

```
# Install necessary packages.
sudo apt-get update && sudo apt-get install -y build-essential yasm cmake libtool libc6 libc6-dev unzip wget libnuma1 libnuma-dev

# Clone ffnvcodec
git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git
# Clone ffmpeg's public GIT repository.
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg/

# Install ffnvcodec
cd nv-codec-headers && sudo make install && cd -

# Configure ffmpeg
# check `ffbuild/config.log` if running into issues
# make sure the nvccflags matches with your GPU device arch
cd ffmpeg/
./configure --enable-nonfree --enable-cuda-sdk --enable-libnpp --extra-cflags=-I/usr/local/cuda/include \
                --extra-ldflags=-L/usr/local/cuda/lib64 \
                --nvccflags='-gencode arch=compute_70,code=sm_70'
# Compile ffmpeg
make -j 8
# Install the libraries.
sudo make install
```

or, run the following commands without `sudo`:

```
# Install necessary packages.
apt-get update && apt-get install -y build-essential yasm cmake libtool libc6 libc6-dev unzip wget libnuma1 libnuma-dev

# Clone ffnvcodec
git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git
# Clone ffmpeg's public GIT repository.
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg/

# Install ffnvcodec
cd nv-codec-headers && make install && cd -

# Configure ffmpeg
# check `ffbuild/config.log` if running into issues
# make sure the nvccflags matches with your GPU device arch
cd ffmpeg/
./configure --enable-nonfree --enable-cuda-sdk --enable-libnpp --extra-cflags=-I/usr/local/cuda/include \
                --extra-ldflags=-L/usr/local/cuda/lib64 \
                --nvccflags='-gencode arch=compute_70,code=sm_70'
# Compile ffmpeg
make -j 8
# Install the libraries.
make install
```


## Use ffmpeg

 
ffmpeg cli option "-hwaccel cuda -hwaccel_output_format cude": automatically detect NV-accelerated video codec and keep video frames in GPU memory for transcoding


* software 1:1 transcode (without GPU's codec): `ffmpeg -i input.mp4 -c:a copy -c:v h264 -b:v 5M output.mp4`
* 1:1 HWACCEL Transcode without Scaling (reads file input.mp4 and transcodes it to output.mp4 with H.264 video at the same resolution)

    `CUDA_VISIBLE_DEVICES=0 ffmpeg -y -vsync 0 -hwaccel cuda -hwaccel_output_format cuda -i input.mp4 -c:a copy -c:v h264_nvenc -b:v 5M output.mp4`

* 1:1 HWACCEL Transcode with Scaling (reads file input.mp4 and transcodes it to output.mp4 with H.264 video at 720p resolution)
    
    `CUDA_VISIBLE_DEVICES=0 ffmpeg -y -vsync 0 -hwaccel cuda -hwaccel_output_format cuda –resize 1280x720 -i input.mp4 -c:a copy -c:v h264_nvenc -b:v 5M output.mp4`


`CUDA_VISIBLE_DEVICES=0 ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i src_video_file.avi -c:a copy -c:v h264 -b:v 5M output.mp4`


```
-c:a copy	            copies the audio stream without any re-encoding
-c:v h264	            selects the software H.264 encoder for the output stream
-b:v 5M	                sets the output bitrate to 5Mb/s

-hwaccel cuda	        chooses appropriate hw accelerator
-hwaccel_output_format  cuda	keeps the decoded frames in GPU memory
-c:v h264_nvenc	        selects the NVIDIA hardware accelerated H.264 encoder
```

## Reference

* [ffmpeg-with-nvidia-gpu](https://docs.nvidia.com/video-technologies/video-codec-sdk/ffmpeg-with-nvidia-gpu)
* [blog: nvidia-ffmpeg-transcoding-guide](https://developer.nvidia.com/blog/nvidia-ffmpeg-transcoding-guide/)
* [ffmpeg Compilation Guide](https://trac.ffmpeg.org/wiki/CompilationGuide)

