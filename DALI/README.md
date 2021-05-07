# DALI

## Resource

- home page:  https://developer.nvidia.com/DALI 
- Blog Posts: https://developer.nvidia.com/blog/tag/dali

- GTC 2019: [slides](https://developer.download.nvidia.com/video/gputechconf/gtc/2019/presentation/s9925-fast-ai-data-pre-processing-with-nvidia-dali.pdf), [video](https://developer.nvidia.com/gtc/2019/video/S9925/video), 
- GTC 2020: [slides](), [video](https://developer.nvidia.com/gtc/2020/video/s21139), 
- GTC 2021: [slides](), [video](https://gtc21.event.nvidia.com/media/1_j4dk7w7q), 




## Examples and Tutorials


build docker image, and start a docker container

```
docker build -t dali_examples -f ./Dockerfile.pytorch .

docker run -it --gpus all --network=host -p 10000:10000 dali_examples:latest /bin/bash

```

inside the docker container

```
jupyter lab --port 10000 --ip 0.0.0.0
```