# NVidia Codec

## Codecs (Encoding & Decoding) Basics

* [H.264 Encoding & Decoding Basics](https://youtu.be/J9RemuYxA4s)
* [video-encoding-decoding-and-transcoding](https://www.haivision.com/blog/all/the-beginners-guide-to-video-encoding-decoding-and-transcoding/)
* [What is Video Encoding? Codecs and Compression Techniques](https://blog.video.ibm.com/streaming-video-tips/what-is-video-encoding-codecs-compression-techniques/)
* [Video Formats, Codecs and Containers (Explained)](https://youtu.be/XvoW-bwIeyY)
* [Video: Formats, Codecs & Containers](https://youtu.be/-4NXxY4maYc)

## NVidia video technologies and Codec

- https://developer.nvidia.com/nvidia-video-codec-sdk
- turing-h264-video-encoding-speed-and-quality, [blog](https://developer.nvidia.com/blog/turing-h264-video-encoding-speed-and-quality/)
- detailed-overview-nvenc-encoder-api, [slides](https://on-demand.gputechconf.com/gtc/2014/presentations/S4654-detailed-overview-nvenc-encoder-api.pdf)
and [video](TBA)
- gpu-video-technologies-overview, [slides](https://developer.download.nvidia.com/video/gputechconf/gtc/2019/presentation/s9331-nvidia-gpu-video-technologies-overview-applications-and-optimization-techniques.pdf)
and [video](TBA)
- [Test codec performance](perf-codec.md)

- [Decode performance in FPS](https://developer.nvidia.com/sites/default/files/akamai/designworks/images-videocodec/nvedec_9.1_1080p_002.png)
  reported in official website

![Decode performance in FPS](https://developer.nvidia.com/sites/default/files/akamai/designworks/images-videocodec/nvedec_9.1_1080p_002.png)

GPU hardware capabilities

![GPU hardware capabilities](https://developer.nvidia.com/blog/wp-content/uploads/2019/07/image5.png)



## FFMPEG with NV Codec

* Compile ffmpeg with CUDA, refer to the [setup guide](setup-ffmpeg.md)


Transcoding pipeline with FFmpeg using NVIDIA hardware acceleration
![Transcoding pipeline](https://developer.nvidia.com/blog/wp-content/uploads/2019/07/image1.png)

