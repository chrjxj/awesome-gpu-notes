# LLAMA 2

### Prepare before start

1. DGX A100 40G, suggest 1 or 4 GPUs. Installed docker and GPU plugin for docker;
2. download docker image, source code, and dataset

    ```bash
    ### in host OS ###
    docker pull nvcr.io/ea-bignlp/nemofw-training:23.07-py3

    # Download source code
    git clone https://github.com/facebookresearch/llama.git
    git clone https://github.com/facebookresearch/llama-recipes.git

    # download alpaca_data dataset
    cd llama-recipes/
    wget -P ft_datasets https://raw.githubusercontent.com/tatsu-lab/stanford_alpaca/main/alpaca_data.json
    ```

3. Download LLAMA Model files

    ```bash
    # before download script, you must go to https://ai.meta.com/resources/models-and-libraries/llama-downloads/, 
    # follow steps and apply for llama 2 access; you will get a email with link
    wget https://raw.githubusercontent.com/facebookresearch/llama/main/download.sh

    chmod +x download.sh
    # don't use sh download.sh
    ./download.sh

    ```


### Convert model

Use following steps to convert LLAMA model to pytorch format

1. Start container: `docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864  -v /home:/home -v /your/path:/your/path nvcr.io/ea-bignlp/nemofw-training:23.07-py3 bash`

1. insdie docker, install python packages: `pip install -r llama-recipes-requirements.txt`
   * reference: https://github.com/facebookresearch/llama-recipes/blob/main/requirements.txt

1. convert LLAMA model to pytorch format
    ```bash
    # following inside the container
    cd /paht/to/your/workspace
    cd llama-recipes

    # transformers is installed in `nvcr.io/ea-bignlp/nemofw-training:23.07-py3`; we can use convert_llama_weights_to_hf.py directly
    pip freeze | grep transformers ## verify it is version 4.31.0 or higher

    wget https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/models/llama/convert_llama_weights_to_hf.py

    ll ../Models-llama-2/
            ./
            ../
            13B/
            LICENSE
            USE_POLICY.md
            download.sh*
            gpt2-merges.txt
            gpt2-vocab.json
            tokenizer.model
            tokenizer_checklist.chk

    python src/transformers/models/llama/convert_llama_weights_to_hf.py \
    --input_dir /path/to/downloaded/llama/weights --model_size 13B --output_dir /output/path
    ```


### SFT

TBA

### PEFT


#### 1. LoRA


**Train with 1*GPU**

Commands:

```bash
# following inside the container
cd /paht/to/your/workspace
cd llama-recipes

export CUDA_VISIBLE_DEVICES=0
python llama_finetuning.py  --use_peft --peft_method lora --quantization  --dataset alpaca_dataset --model_name ./llama-2-13b-pytoch/ --output_dir ./PEFT_Model_Outputs

```

Training logs:

```bash
 step 582 is completed and loss is 0.6818716526031494
Training Epoch0:   4%|████▋                                                                                                   | 583/13000 [15:04<5:19:52,  1.55s/it]
 step 583 is completed and loss is 0.5822356343269348

...

Training Epoch0:   5%|████▊                                                                                                   | 605/13000 [15:38<5:20:56,  1.55s/it]
 step 605 is completed and loss is 0.8930172324180603
Training Epoch0:   5%|████▊                                                                                                   | 606/13000 [15:40<5:21:24,  1.56s/it]
 step 606 is completed and loss is 1.4484190940856934
Training Epoch0:   5%|████▊                                                                                                   | 607/13000 [15:41<5:21:31,  1.56s/it]T
```

Training Thoughput: 1.55 s/it

Notes: 
* Seems no speedup after adding `--use_fast_kernels`


**Train with 1*GPU**

Commands:

```bash
# following inside the container
cd /paht/to/your/workspace
cd llama-recipes

export CUDA_VISIBLE_DEVICES=4,5,6,7
torchrun --nnodes 1 --nproc_per_node 4  llama_finetuning.py --enable_fsdp --use_fast_kernels --use_peft --peft_method lora --model_name ./llama-2-13b-pytoch/  --pure_bf16 --output_dir ./PEFT_Model_Outputs 

```


Training logs:

```bash
...

Training Epoch2: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 97/97 [10:27<00:00,  6.47s/it]

Max CUDA memory allocated was 32 GB
Max CUDA memory reserved was 38 GB
Peak active CUDA memory was 32 GB
Cuda Malloc retires : 579
CPU Total Peak Memory consumed during the train (max): 2 GB
evaluating Epoch: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21/21 [00:09<00:00,  2.12it/s]
 eval_ppl=tensor(5.0186, device='cuda:0') eval_epoch_loss=tensor(1.6131, device='cuda:0')
we are about to save the PEFT modules
PEFT modules are saved in ./PEFT_Model_Outputs directory
best eval loss on epoch 2 is 1.6131418943405151
Epoch 3: train_perplexity=4.9403, train_epoch_loss=1.5974, epcoh time 628.8528654070105s
Key: avg_train_prep, Value: 5.124361038208008
Key: avg_train_loss, Value: 1.6331899166107178
Key: avg_eval_prep, Value: 5.062094688415527
Key: avg_eval_loss, Value: 1.6217451095581055
Key: avg_epoch_time, Value: 822.4309747720448
Key: avg_checkpoint_time, Value: 0.6152872766833752

ls -lh ./PEFT_Model_Outputs

-rw-r--r-- 1 root root 129 Aug 12 02:24 README.md
-rw-r--r-- 1 root root 443 Aug 12 02:24 adapter_config.json
-rw-r--r-- 1 root root 26M Aug 12 02:24 adapter_model.bin

```


### Resource

