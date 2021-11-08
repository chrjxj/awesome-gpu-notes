# Perf GPT-2 with FasterTransformer

### Goal


* Test GPT 1.5B inference performance with FasterTransformer 4.0

* Reference: https://github.com/NVIDIA/FasterTransformer/blob/v4.0/docs/gpt_guide.md

  * checkpoint of OpenAI GPT-2 model (TensorFlow); including 124M, 355M, 774M and 1558M
  * checkpoint of Megatron (which is trained by pytorch) - only 345M model in NV NGC
  * Use TensorFlow 

### Steps


- Start docker container:

```
docker pull nvcr.io/nvidia/tensorflow:20.12-tf1-py3

docker run -it --gpus all --network=host --ipc=host -v /home:/local -v /raid:/raid nvcr.io/nvidia/tensorflow:20.12-tf1-py3 /bin/bash
```

- run following steps inside docker container
- Download and build FasterTransformer

```
https://github.com/NVIDIA/FasterTransformer/archive/refs/heads/v4.0.zip
unzip v4.0.zip
mv FasterTransformer-4.0 FasterTransformer
cd FasterTransformer
mkdir -p build
cd build

# xx --> 60 (P40) or 61 (P4) or 70 (V100) or 75(T4) or 80 (A100).
cmake -DSM=xx -DCMAKE_BUILD_TYPE=Release ..
make -j16

```

- In `FasterTransformer` folder, edit requirement.txt for tensorflow, and install python packages: `pip install -r requirement.txt`

- In `FasterTransformer` folder, Download vocab and merge table; download gpt model

```
wget https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-vocab.json -P models
wget https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-merges.txt -P models
python  sample/tensorflow/utils/download_gpt2_model.py 1558M
```

- convert 1558M model (`-g 1` means using 1 GPU for inference; [code](https://github.com/NVIDIA/FasterTransformer/blob/v4.0/sample/tensorflow/utils/openai_gpt_ckpt_convert.py#L175))

    *  `python sample/tensorflow/utils/openai_gpt_ckpt_convert.py -o models/openai-gpt-models/c-model/1558M/ -i models/1558M/model.ckpt -g 1`


- Go `FasterTransformer/build` folder
- Generate the decoding_gemm_config.in

```
./bin/gpt_gemm <local_batch_size> <context_local_batch_size> <head_number> <size_per_head> <vocab_size> <start_len> <tensor_para_size> <is_fp16>
E.g., ./bin/gpt_gemm 8 8 12 64 50257 32 1 1

```

- edit `../sample/cpp/gpt_config.ini` for `./bin/gpt_sample`
- run inference test: `./bin/gpt_sample`
