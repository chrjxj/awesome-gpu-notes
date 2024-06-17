# README

## Commands


##### `trtllm-build`

```bash
root@sys-521ge-node1:/local/TASK010_BenchmarkIssue# trtllm-build -h
[TensorRT-LLM] TensorRT-LLM version: 0.10.0
usage: trtllm-build [-h] [--checkpoint_dir CHECKPOINT_DIR] [--model_config MODEL_CONFIG] [--build_config BUILD_CONFIG] [--model_cls_file MODEL_CLS_FILE]
                    [--model_cls_name MODEL_CLS_NAME] [--input_timing_cache INPUT_TIMING_CACHE] [--output_timing_cache OUTPUT_TIMING_CACHE] [--log_level LOG_LEVEL]
                    [--profiling_verbosity {layer_names_only,detailed,none}] [--enable_debug_output] [--output_dir OUTPUT_DIR] [--workers WORKERS]
                    [--max_batch_size MAX_BATCH_SIZE] [--max_input_len MAX_INPUT_LEN] [--max_output_len MAX_OUTPUT_LEN] [--max_beam_width MAX_BEAM_WIDTH]
                    [--max_num_tokens MAX_NUM_TOKENS] [--opt_num_tokens OPT_NUM_TOKENS] [--tp_size TP_SIZE] [--pp_size PP_SIZE]
                    [--max_prompt_embedding_table_size MAX_PROMPT_EMBEDDING_TABLE_SIZE] [--use_fused_mlp] [--gather_all_token_logits] [--gather_context_logits]
                    [--gather_generation_logits] [--strongly_typed] [--builder_opt BUILDER_OPT] [--logits_dtype {float16,float32}] [--weight_only_precision {int8,int4}]
                    [--weight_sparsity] [--max_draft_len MAX_DRAFT_LEN] [--lora_dir LORA_DIR [LORA_DIR ...]] [--lora_ckpt_source {hf,nemo}]
                    [--lora_target_modules {attn_qkv,attn_q,attn_k,attn_v,attn_dense,mlp_h_to_4h,mlp_4h_to_h,mlp_gate,cross_attn_qkv,cross_attn_q,cross_attn_k,cross_attn_v,cross_attn_dense,moe_h_to_4h,moe_4h_to_h,moe_gate,moe_router} [{attn_qkv,attn_q,attn_k,attn_v,attn_dense,mlp_h_to_4h,mlp_4h_to_h,mlp_gate,cross_attn_qkv,cross_attn_q,cross_attn_k,cross_attn_v,cross_attn_dense,moe_h_to_4h,moe_4h_to_h,moe_gate,moe_router} ...]]
                    [--max_lora_rank MAX_LORA_RANK] [--auto_parallel AUTO_PARALLEL] [--gpus_per_node GPUS_PER_NODE]
                    [--cluster_key {A100-SXM-80GB,A100-SXM-40GB,A100-PCIe-80GB,A100-PCIe-40GB,H100-SXM,H100-PCIe,H20,V100-PCIe-16GB,V100-PCIe-32GB,V100-SMX-16GB,V100-SMX-32GB,V100S-PCIe,A40,A30,A10,A10G,L40S,L40,L20,L4,L2}]
                    [--strip_plan] [--max_encoder_input_len MAX_ENCODER_INPUT_LEN] [--visualize_network] [--dry_run]
                    [--speculative_decoding_mode {draft_tokens_external,medusa}] [--weight_streaming] [--bert_attention_plugin {float16,float32,bfloat16,disable}]
                    [--gpt_attention_plugin {float16,float32,bfloat16,disable}] [--gemm_plugin {float16,float32,bfloat16,disable}]
                    [--nccl_plugin {float16,float32,bfloat16,disable}] [--lookup_plugin {float16,float32,bfloat16,disable}]
                    [--lora_plugin {float16,float32,bfloat16,disable}] [--moe_plugin {float16,float32,bfloat16,disable}]
                    [--mamba_conv1d_plugin {float16,float32,bfloat16,disable}] [--context_fmha {enable,disable}] [--context_fmha_fp32_acc {enable,disable}]
                    [--paged_kv_cache {enable,disable}] [--remove_input_padding {enable,disable}] [--use_custom_all_reduce {enable,disable}]
                    [--multi_block_mode {enable,disable}] [--enable_xqa {enable,disable}] [--attention_qk_half_accumulation {enable,disable}]
                    [--tokens_per_block TOKENS_PER_BLOCK] [--use_paged_context_fmha {enable,disable}] [--use_fp8_context_fmha {enable,disable}]
                    [--use_context_fmha_for_generation {enable,disable}] [--multiple_profiles {enable,disable}] [--paged_state {enable,disable}]
                    [--streamingllm {enable,disable}]

options:
  -h, --help            show this help message and exit
  --checkpoint_dir CHECKPOINT_DIR
  --model_config MODEL_CONFIG
  --build_config BUILD_CONFIG
  --model_cls_file MODEL_CLS_FILE
  --model_cls_name MODEL_CLS_NAME
  --input_timing_cache INPUT_TIMING_CACHE
                        The path to read timing cache, will be ignored if the file does not exist
  --output_timing_cache OUTPUT_TIMING_CACHE
                        The path to write timing cache
  --log_level LOG_LEVEL
  --profiling_verbosity {layer_names_only,detailed,none}
                        The profiling verbosity for the generated TRT engine. Set to detailed can inspect tactic choices and kernel parameters.
  --enable_debug_output
  --output_dir OUTPUT_DIR
                        The path to save the serialized engine files and model configs
  --workers WORKERS     The number of workers for building in parallel
  --max_batch_size MAX_BATCH_SIZE
  --max_input_len MAX_INPUT_LEN
  --max_output_len MAX_OUTPUT_LEN
  --max_beam_width MAX_BEAM_WIDTH
  --max_num_tokens MAX_NUM_TOKENS
  --opt_num_tokens OPT_NUM_TOKENS
                        It equals to max_batch_size*max_beam_width by default, set this value as close as possible to the actual number of tokens on your workload. Note
                        that this argument might be removed in the future.
  --tp_size TP_SIZE
  --pp_size PP_SIZE
  --max_prompt_embedding_table_size MAX_PROMPT_EMBEDDING_TABLE_SIZE, --max_multimodal_len MAX_PROMPT_EMBEDDING_TABLE_SIZE
                        Setting to a value > 0 enables support for prompt tuning or multimodal input.
  --use_fused_mlp       Enable horizontal fusion in GatedMLP, reduces layer input traffic and potentially improves performance. For FP8 PTQ, the downside is slight
                        reduction of accuracy because one of the quantization scaling factors is discarded. (An example for reference only: 0.45734 vs 0.45755 for
                        LLaMA-v2 7B using `modelopt/examples/hf/instruct_eval/mmlu.py`).
  --gather_all_token_logits
                        Enable both gather_context_logits and gather_generation_logits
  --gather_context_logits
                        Gather context logits
  --gather_generation_logits
                        Gather generation logits
  --strongly_typed      This option is introduced with TensorRT 9.1.0.1+ and will reduce the engine building time. It's not expected to see performance or accuracy
                        regression after enable this flag. Note that, we may remove this flag in the future, and enable the feature by default.
  --builder_opt BUILDER_OPT
  --logits_dtype {float16,float32}
  --weight_only_precision {int8,int4}
  --weight_sparsity
  --max_draft_len MAX_DRAFT_LEN
                        Maximum lengths of draft tokens for speculative decoding target model.
  --lora_dir LORA_DIR [LORA_DIR ...]
                        The directory of LoRA weights. Use config from the first directory if multiple directories are provided.
  --lora_ckpt_source {hf,nemo}
                        The source of lora checkpoint.
  --lora_target_modules {attn_qkv,attn_q,attn_k,attn_v,attn_dense,mlp_h_to_4h,mlp_4h_to_h,mlp_gate,cross_attn_qkv,cross_attn_q,cross_attn_k,cross_attn_v,cross_attn_dense,moe_h_to_4h,moe_4h_to_h,moe_gate,moe_router} [{attn_qkv,attn_q,attn_k,attn_v,attn_dense,mlp_h_to_4h,mlp_4h_to_h,mlp_gate,cross_attn_qkv,cross_attn_q,cross_attn_k,cross_attn_v,cross_attn_dense,moe_h_to_4h,moe_4h_to_h,moe_gate,moe_router} ...]
                        Add lora in which modules. Only be activated when use_lora_plugin is enabled.
  --max_lora_rank MAX_LORA_RANK
                        maximum lora rank for different lora modules. It is used to compute the workspace size of lora plugin.
  --auto_parallel AUTO_PARALLEL
                        MPI world size for auto parallel.
  --gpus_per_node GPUS_PER_NODE
                        Number of GPUs each node has in a multi-node setup. This is a cluster spec and can be greater/smaller than world size
  --cluster_key {A100-SXM-80GB,A100-SXM-40GB,A100-PCIe-80GB,A100-PCIe-40GB,H100-SXM,H100-PCIe,H20,V100-PCIe-16GB,V100-PCIe-32GB,V100-SMX-16GB,V100-SMX-32GB,V100S-PCIe,A40,A30,A10,A10G,L40S,L40,L20,L4,L2}
                        Unique name for target GPU type. Inferred from current GPU type if not specified.
  --strip_plan          Whether to strip weights from the final TRT engine under the assumption that the refit weights will be identical to those provided at build time.
  --max_encoder_input_len MAX_ENCODER_INPUT_LEN
                        Specify max encoder input length when using enc-dec models. Set max_input_len to 1 to start generation from decoder_start_token_id of length 1.
  --visualize_network   TRT Networks will be exported to ONNX prior to Engine build for debugging.
  --dry_run             Run through the build process except the actual Engine build for debugging.
  --speculative_decoding_mode {draft_tokens_external,medusa}
                        Mode of speculative decoding.
  --weight_streaming    Specify whether offloading weights to CPU and streaming loading at runtime.

plugin_config:
  --bert_attention_plugin {float16,float32,bfloat16,disable}
  --gpt_attention_plugin {float16,float32,bfloat16,disable}
  --gemm_plugin {float16,float32,bfloat16,disable}
  --nccl_plugin {float16,float32,bfloat16,disable}
  --lookup_plugin {float16,float32,bfloat16,disable}
  --lora_plugin {float16,float32,bfloat16,disable}
  --moe_plugin {float16,float32,bfloat16,disable}
  --mamba_conv1d_plugin {float16,float32,bfloat16,disable}
  --context_fmha {enable,disable}
  --context_fmha_fp32_acc {enable,disable}
  --paged_kv_cache {enable,disable}
  --remove_input_padding {enable,disable}
  --use_custom_all_reduce {enable,disable}
  --multi_block_mode {enable,disable}
  --enable_xqa {enable,disable}
  --attention_qk_half_accumulation {enable,disable}
  --tokens_per_block TOKENS_PER_BLOCK
  --use_paged_context_fmha {enable,disable}
  --use_fp8_context_fmha {enable,disable}
  --use_context_fmha_for_generation {enable,disable}
  --multiple_profiles {enable,disable}
  --paged_state {enable,disable}
  --streamingllm {enable,disable}

```

##### `gptManagerBenchmark`


```
$ ./cpp/build/benchmarks/gptManagerBenchmark  -h

TensorRT-LLM BatchManager Benchmark for GPT and GPT-like models.
Usage:
  TensorRT-LLM BatchManager Benchmark [OPTION...]

  -h, --help                    Print usage
      --engine_dir arg          Directory that store the engines.
      --api arg                 API type: gptManager or executor. (default:
                                gptManager)
      --type arg                Batching type: IFB, UIFB (unfused IFB) or
                                V1 (non-IFB) batching. (default: IFB)
      --dataset arg             Dataset that is used for benchmarking
                                BatchManager. (default: "")
      --output_csv arg          Write output metrics to CSV (default: "")
      --max_num_samples arg     maximum number of samples to use from
                                dataset/generate (default: 100000)
      --beam_width arg          Specify beam width you want to benchmark.
                                (default: 1)
      --warm_up arg             Specify warm up iterations before benchmark
                                starts. (default: 2)
      --eos_id arg              Specify the end-of-sequence token id.
                                (default: -1)
      --pad_id arg              Specify the padding token id.
      --max_tokens_in_paged_kvcache arg
                                Max tokens in paged K-V Cache.
      --max_attention_window arg
                                Max KV cache length per sequence
      --random_seed arg         integer random seed for exponential time
                                delays. (default: 420)
      --kv_cache_free_gpu_mem_fraction arg
                                K-V Cache Free Gpu Mem Fraction.
      --request_rate arg        request rate in reqs/sec. Skipping this arg
                                or negative value will trigger
                                offline/0-delay.
      --enable_trt_overlap      Overlap TRT context preparation and
                                execution
      --enable_exp_delays       Enables exponential delay distr to mimic
                                real world request arrival
      --streaming               Operate in streaming mode
      --enable_kv_cache_reuse   Enables the KV cache reuse.
      --enable_chunked_context  Whether to enable context chunking.
      --return_context_logits   Whether to return context logits.
      --return_generation_logits
                                Whether to return generation logits.
      --scheduler_policy arg    Choose scheduler policy between
                                max_utilization/guaranteed_no_evict.
                                (default: guaranteed_no_evict)
      --first_batch_delay arg   Delay before submitting the first batch of
                                requests. This can be used to increase the
                                size of the first batch.
      --static_emulated_batch_size arg
                                Emulate static batching performance with
                                the provided batch size.
      --static_emulated_timeout arg
                                Timeout (ms) before launching a partial
                                batch in emulated static batching mode
                                (default: 500)
      --log_level arg           Choose log level between
                                verbose/info/warning/error/internal_error.
                                (default: error)
      --log_iteration_data      On each decoder iteration, print batch
                                state metadata.
      --wait_sleep arg          Specify how many milliseconds to sleep each
                                iteration of waitForEmpty loop. (default:
                                25)
      --lora_dir arg            Directory containing LoRAs (default: "")
      --lora_host_cache_bytes arg
                                LoRA host cache memory in bytes
      --lora_num_device_mod_layers arg
                                LoRA number 1d cache rows
      --kv_host_cache_bytes arg
                                Size of secondary memory pool used for
                                offloading kv cache blocks (in bytes).
                                (default: 0)
      --kv_dont_onboard_blocks  If offloaded blocks should be onboarded to
                                primary memory before reuse
      --exclude_input_in_output_seq
                                When enabled, GptManager will exclude the
                                input sequence from output. (Only works if
                                --api is gptManager)
      --responses_json_file arg
                                When specified, dumps the responses to JSON
                                file. (only works if --api is gptManager)
                                (default: "")
      --max_prompt_len arg      Truncate all prompts from dataset to the
                                length specified.
      --dump_profile            Print profile information per layer.
      --gpu_weights_percent arg
                                Specify the percentage of weights that
                                reside on GPU (from 0.0 to 1.0). (default:
                                1.0)

```
