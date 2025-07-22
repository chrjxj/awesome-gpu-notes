# README


## NV AI dynamo

dynamo https://github.com/ai-dynamo/dynamo

NVIDIA Inference Xfer Library (NIXL) https://github.com/ai-dynamo/nixl/tree/main?tab=readme-ov-file

Throughput is Not All You Need: Maximizing Goodput in LLM Serving using Prefill-Decode Disaggregation: https://hao-ai-lab.github.io/blogs/distserve/



Understanding the LLM Inference Workload - Mark Moyou, NVIDIA https://www.youtube.com/watch?v=z2M8gKGYws4

How To Reduce LLM Decoding Time With KV-Caching https://www.youtube.com/watch?v=sNv5jpAwkcU

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

## genai-perf


```bash
usage: genai-perf [-h] [-m MODEL] [--backend {tensorrtllm,vllm}]
                  [--endpoint ENDPOINT] [--endpoint-type {chat,completions}]
                  [--service-kind {triton,openai}] [--streaming] [-u URL]
                  [--extra-inputs EXTRA_INPUTS]
                  [--input-dataset {openorca,cnn_dailymail} | --input-file INPUT_FILE]
                  [--num-prompts NUM_PROMPTS]
                  [--output-tokens-mean OUTPUT_TOKENS_MEAN]
                  [--output-tokens-mean-deterministic]
                  [--output-tokens-stddev OUTPUT_TOKENS_STDDEV]
                  [--random-seed RANDOM_SEED]
                  [--synthetic-input-tokens-mean SYNTHETIC_INPUT_TOKENS_MEAN]
                  [--synthetic-input-tokens-stddev SYNTHETIC_INPUT_TOKENS_STDDEV]
                  [--concurrency CONCURRENCY]
                  [--measurement-interval MEASUREMENT_INTERVAL]
                  [--request-rate REQUEST_RATE] [-s STABILITY_PERCENTAGE]
                  [--generate-plots]
                  [--profile-export-file PROFILE_EXPORT_FILE]
                  [--artifact-dir ARTIFACT_DIR] [--tokenizer TOKENIZER] [-v]
                  [--version]
                  {compare} ...

CLI to profile LLMs and Generative AI models with Perf Analyzer

positional arguments:
  {compare}             List of subparser commands.

options:
  -h, --help            show this help message and exit

Endpoint:
  -m MODEL, --model MODEL
                        The name of the model to benchmark. (default: None)
  --backend {tensorrtllm,vllm}
                        When using the "triton" service-kind, this is the
                        backend of the model. For the TENSORRT-LLM backend,
                        you currently must set 'exclude_input_in_output' to
                        true in the model config to not echo the input tokens
                        in the output. (default: tensorrtllm)
  --endpoint ENDPOINT   Set a custom endpoint that differs from the OpenAI
                        defaults. (default: None)
  --endpoint-type {chat,completions}
                        The endpoint-type to send requests to on the server.
                        This is only used with the "openai" service-kind.
                        (default: None)
  --service-kind {triton,openai}
                        The kind of service perf_analyzer will generate load
                        for. In order to use "openai", you must specify an api
                        via --endpoint-type. (default: triton)
  --streaming           An option to enable the use of the streaming API.
                        (default: False)
  -u URL, --url URL     URL of the endpoint to target for benchmarking.
                        (default: None)

Input:
  --extra-inputs EXTRA_INPUTS
                        Provide additional inputs to include with every
                        request. You can repeat this flag for multiple inputs.
                        Inputs should be in an input_name:value format.
                        (default: None)
  --input-dataset {openorca,cnn_dailymail}
                        The HuggingFace dataset to use for prompts. (default:
                        None)
  --input-file INPUT_FILE
                        The input file containing the single prompt to use for
                        profiling. (default: None)
  --num-prompts NUM_PROMPTS
                        The number of unique prompts to generate as stimulus.
                        (default: 100)
  --output-tokens-mean OUTPUT_TOKENS_MEAN
                        The mean number of tokens in each output. Ensure the
                        --tokenizer value is set correctly. (default: -1)
  --output-tokens-mean-deterministic
                        When using --output-tokens-mean, this flag can be set
                        to improve precision by setting the minimum number of
                        tokens equal to the requested number of tokens. This
                        is currently supported with the Triton service-kind.
                        Note that there is still some variability in the
                        requested number of output tokens, but GenAi-Perf
                        attempts its best effort with your model to get the
                        right number of output tokens. (default: False)
  --output-tokens-stddev OUTPUT_TOKENS_STDDEV
                        The standard deviation of the number of tokens in each
                        output. This is only used when --output-tokens-mean is
                        provided. (default: 0)
  --random-seed RANDOM_SEED
                        The seed used to generate random values. (default: 0)
  --synthetic-input-tokens-mean SYNTHETIC_INPUT_TOKENS_MEAN
                        The mean of number of tokens in the generated prompts
                        when using synthetic data. (default: 550)
  --synthetic-input-tokens-stddev SYNTHETIC_INPUT_TOKENS_STDDEV
                        The standard deviation of number of tokens in the
                        generated prompts when using synthetic data. (default:
                        0)

Profiling:
  --concurrency CONCURRENCY
                        The concurrency value to benchmark. (default: None)
  --measurement-interval MEASUREMENT_INTERVAL, -p MEASUREMENT_INTERVAL
                        The time interval used for each measurement in
                        milliseconds. Perf Analyzer will sample a time
                        interval specified and take measurement over the
                        requests completed within that time interval.
                        (default: 10000)
  --request-rate REQUEST_RATE
                        Sets the request rate for the load generated by PA.
                        (default: None)
  -s STABILITY_PERCENTAGE, --stability-percentage STABILITY_PERCENTAGE
                        The allowed variation in latency measurements when
                        determining if a result is stable. The measurement is
                        considered as stable if the ratio of max / min from
                        the recent 3 measurements is within (stability
                        percentage) in terms of both infer per second and
                        latency. (default: 999)

Output:
  --generate-plots      An option to enable the generation of plots. (default:
                        False)
  --profile-export-file PROFILE_EXPORT_FILE
                        The path where the perf_analyzer profile export will
                        be generated. By default, the profile export will be
                        to profile_export.json. The genai-perf file will be
                        exported to <profile_export_file>_genai_perf.csv. For
                        example, if the profile export file is
                        profile_export.json, the genai-perf file will be
                        exported to profile_export_genai_perf.csv. (default:
                        profile_export.json)
  --artifact-dir ARTIFACT_DIR
                        The directory to store all the (output) artifacts
                        generated by GenAI-Perf and Perf Analyzer. (default:
                        artifacts)

Other:
  --tokenizer TOKENIZER
                        The HuggingFace tokenizer to use to interpret token
                        metrics from prompts and responses. (default: hf-
                        internal-testing/llama-tokenizer)
  -v, --verbose         An option to enable verbose mode. (default: False)
  --version             An option to print the version and exit.


```


### `perf_analyzer`

```bash
perf_analyzer: invalid option -- 'h'
Usage: perf_analyzer [options]
==== SYNOPSIS ====
 
	--version 
	--service-kind <"triton"|"tfserving"|"torchserve"|"triton_c_api">
	-m <model name>
	-x <model version>
	--bls-composing-models=<string>
	--model-signature-name <model signature name>
	-v

I. MEASUREMENT PARAMETERS: 
	--async (-a)
	--sync
	--measurement-interval (-p) <measurement window (in msec)>
	--concurrency-range <start:end:step>
	--periodic-concurrency-range <start:end:step>
	--request-period <number of responses>
	--request-rate-range <start:end:step>
	--request-distribution <"poisson"|"constant">
	--request-intervals <path to file containing time intervals in microseconds>
	--serial-sequences
	--binary-search
	--num-of-sequences <number of concurrent sequences>
	--latency-threshold (-l) <latency threshold (in msec)>
	--max-threads <thread counts>
	--stability-percentage (-s) <deviation threshold for stable measurement (in percentage)>
	--max-trials (-r)  <maximum number of measurements for each profiling>
	--percentile <percentile>
	DEPRECATED OPTIONS
	-t <number of concurrent requests>
	-c <maximum concurrency>
	-d

II. INPUT DATA OPTIONS: 
	-b <batch size>
	--input-data <"zero"|"random"|<path>>
	--shared-memory <"system"|"cuda"|"none">
	--output-shared-memory-size <size in bytes>
	--shape <name:shape>
	--sequence-length <length>
	--sequence-length-variation <variation>
	--sequence-id-range <start:end>
	--string-length <length>
	--string-data <string>
	--input-tensor-format=[binary|json]
	--output-tensor-format=[binary|json]
	DEPRECATED OPTIONS
	-z
	--data-directory <path>

III. SERVER DETAILS: 
	-u <URL for inference service>
	-i <Protocol used to communicate with inference service>
	--ssl-grpc-use-ssl <bool>
	--ssl-grpc-root-certifications-file <path>
	--ssl-grpc-private-key-file <path>
	--ssl-grpc-certificate-chain-file <path>
	--ssl-https-verify-peer <number>
	--ssl-https-verify-host <number>
	--ssl-https-ca-certificates-file <path>
	--ssl-https-client-certificate-file <path>
	--ssl-https-client-certificate-type <string>
	--ssl-https-private-key-file <path>
	--ssl-https-private-key-type <string>

IV. OTHER OPTIONS: 
	-f <filename for storing report in csv format>
	--profile-export-file <path>
	-H <HTTP header>
	--streaming
	--grpc-compression-algorithm <compression_algorithm>
	--trace-file
	--trace-level
	--trace-rate
	--trace-count
	--log-frequency
	--collect-metrics
	--metrics-url
	--metrics-interval

==== OPTIONS ==== 
 
 --version: print the current version of Perf Analyzer.
 --service-kind: Describes the kind of service perf_analyzer to generate load
	 for. The options are "triton", "triton_c_api", "tfserving" and
	 "torchserve". Default value is "triton". Note in order to use
	 "torchserve" backend --input-data option must point to a json file holding data
	 in the following format {"data" : [{"TORCHSERVE_INPUT" :
	 ["<complete path to the content file>"]}, {...}...]}. The type of file here
	 will depend on the model. In order to use "triton_c_api" you must
	 specify the Triton server install path and the model repository path via
	 the --triton-server-directory and --model-repository flags
 -m:     This is a required argument and is used to specify the model against
	 which to run perf_analyzer.
 -x:     The version of the above model to be used. If not specified the most
	 recent version (that is, the highest numbered version) of the model
	 will be used.
 --model-signature-name: The signature name of the saved model to use. Default
	 value is "serving_default". This option will be ignored if
	 --service-kind is not "tfserving".
 -v:     Enables verbose mode.
 -v -v:  Enables extra verbose mode.

I. MEASUREMENT PARAMETERS: 
 --async (-a): Enables asynchronous mode in perf_analyzer. By default,
	 perf_analyzer will use synchronous API to request inference. However, if
	 the model is sequential then default mode is asynchronous. Specify
	 --sync to operate sequential models in synchronous mode. In synchronous
	 mode, perf_analyzer will start threads equal to the concurrency
	 level. Use asynchronous mode to limit the number of threads, yet
	 maintain the concurrency.
 --sync: Force enables synchronous mode in perf_analyzer. Can be used to
	 operate perf_analyzer with sequential model in synchronous mode.
 --measurement-interval (-p): Indicates the time interval used for each
	 measurement in milliseconds. The perf analyzer will sample a time interval
	 specified by -p and take measurement over the requests completed
	 within that time interval. The default value is 5000 msec.
 --measurement-mode <"time_windows"|"count_windows">: Indicates the mode used
	 for stabilizing measurements. "time_windows" will create windows
	 such that the length of each window is equal to --measurement-interval.
	 "count_windows" will create windows such that there are at least
	 --measurement-request-count requests in each window.
 --measurement-request-count: Indicates the minimum number of requests to be
	 collected in each measurement window when "count_windows" mode is
	 used. This mode can be enabled using the --measurement-mode flag.
 --concurrency-range <start:end:step>: Determines the range of concurrency
	 levels covered by the perf_analyzer. The perf_analyzer will start from
	 the concurrency level of 'start' and go till 'end' with a stride of
	 'step'. The default value of 'end' and 'step' are 1. If 'end' is not
	 specified then perf_analyzer will run for a single concurrency
	 level determined by 'start'. If 'end' is set as 0, then the concurrency
	 limit will be incremented by 'step' till latency threshold is met.
	 'end' and --latency-threshold can not be both 0 simultaneously. 'end'
	 can not be 0 for sequence models while using asynchronous mode.
--periodic-concurrency-range <start:end:step>: Determines the range of
	 concurrency levels in the similar but slightly different manner as the
	 --concurrency-range. Perf Analyzer will start from the concurrency level
	 of 'start' and increase by 'step' each time. Unlike
	 --concurrency-range, the 'end' indicates the *total* number of concurrency since
	 the 'start' (including) and will stop increasing once the cumulative
	 number of concurrent requests has reached the 'end'. The user can
	 specify *when* to periodically increase the concurrency level using the
	 --request-period option. The concurrency level will periodically
	 increase for every n-th response specified by --request-period. Since
	 this disables stability check in Perf Analyzer and reports response
	 timestamps only, the user must provide --profile-export-file to
	 specify where to dump all the measured timestamps. The default values of
	 'start', 'end', and 'step' are 1.
--request-period <n>: Indicates the number of responses that each request must
	 receive before new, concurrent requests are sent when
	 --periodic-concurrency-range is specified. Default value is 10.
--request-parameter <name:value:type>: Specifies a custom parameter that can
	 be sent to a Triton backend as part of the request. For example,
	 providing '--request-parameter max_tokens:256:int' to the command line
	 will set an additional parameter 'max_tokens' of type 'int' to 256 as
	 part of the request. The --request-parameter may be specified
	 multiple times for different custom parameters.
 --request-rate-range <start:end:step>: Determines the range of request rates
	 for load generated by analyzer. This option can take floating-point
	 values. The search along the request rate range is enabled only when
	 using this option. If not specified, then analyzer will search
	 along the concurrency-range. The perf_analyzer will start from the
	 request rate of 'start' and go till 'end' with a stride of 'step'. The
	 default values of 'start', 'end' and 'step' are all 1.0. If 'end' is
	 not specified then perf_analyzer will run for a single request rate
	 as determined by 'start'. If 'end' is set as 0.0, then the request
	 rate will be incremented by 'step' till latency threshold is met.
	 'end' and --latency-threshold can not be both 0 simultaneously.
 --request-distribution <"poisson"|"constant">: Specifies the time interval
	 distribution between dispatching inference requests to the server.
	 Poisson distribution closely mimics the real-world work load on a
	 server. This option is ignored if not using --request-rate-range. By
	 default, this option is set to be constant.
 --request-intervals: Specifies a path to a file containing time intervals in
	 microseconds. Each time interval should be in a new line. The
	 analyzer will try to maintain time intervals between successive generated
	 requests to be as close as possible in this file. This option can be
	 used to apply custom load to server with a certain pattern of
	 interest. The analyzer will loop around the file if the duration of
	 execution exceeds to that accounted for by the intervals. This option can
	 not be used with --request-rate-range or --concurrency-range.
--binary-search: Enables the binary search on the specified search range. This
	 option requires 'start' and 'end' to be expilicitly specified in
	 the --concurrency-range or --request-rate-range. When using this
	 option, 'step' is more like the precision. Lower the 'step', more the
	 number of iterations along the search path to find suitable
	 convergence. By default, linear search is used.
--num-of-sequences: Sets the number of concurrent sequences for sequence
	 models. This option is ignored when --request-rate-range is not
	 specified. By default, its value is 4.
 --latency-threshold (-l): Sets the limit on the observed latency. Analyzer
	 will terminate the concurrency search once the measured latency
	 exceeds this threshold. By default, latency threshold is set 0 and the
	 perf_analyzer will run for entire --concurrency-range.
 --max-threads: Sets the maximum number of threads that will be created for
	 providing desired concurrency or request rate. However, when runningin
	 synchronous mode with concurrency-range having explicit 'end'
	 specification,this value will be ignored. Default is 4 if
	 --request-rate-range is specified otherwise default is 16.
 --stability-percentage (-s): Indicates the allowed variation in latency
	 measurements when determining if a result is stable. The measurement is
	 considered as stable if the ratio of max / min from the recent 3
	 measurements is within (stability percentage)% in terms of both infer
	 per second and latency. Default is 10(%).
 --max-trials (-r): Indicates the maximum number of measurements for each
	 concurrency level visited during search. The perf analyzer will take
	 multiple measurements and report the measurement until it is stable.
	 The perf analyzer will abort if the measurement is still unstable
	 after the maximum number of measurements. The default value is 10.
 --percentile: Indicates the confidence value as a percentile that will be
	 used to determine if a measurement is stable. For example, a value of
	 85 indicates that the 85th percentile latency will be used to
	 determine stability. The percentile will also be reported in the results.
	 The default is -1 indicating that the average latency is used to
	 determine stability
 --serial-sequences: Enables serial sequence mode where a maximum of one
	 request is outstanding at a time for any given sequence. The default is
	 false.

II. INPUT DATA OPTIONS: 
 -b:     Batch size for each request sent.
 --input-data: Select the type of data that will be used for input in
	 inference requests. The available options are "zero", "random", path to a
	 directory or a json file. If the option is path to a directory then
	 the directory must contain a binary/text file for each
	 non-string/string input respectively, named the same as the input. Each file must
	 contain the data required for that input for a batch-1 request. Each
	 binary file should contain the raw binary representation of the
	 input in row-major order for non-string inputs. The text file should
	 contain all strings needed by batch-1, each in a new line, listed in
	 row-major order. When pointing to a json file, user must adhere to the
	 format described in the Performance Analyzer documentation. By
	 specifying json data users can control data used with every request.
	 Multiple data streams can be specified for a sequence model and the
	 analyzer will select a data stream in a round-robin fashion for every
	 new sequence. Multiple json files can also be provided (--input-data
	 json_file1 --input-data json-file2 and so on) and the analyzer will
	 append data streams from each file. When using
	 --service-kind=torchserve make sure this option points to a json file. Default is
	 "random".
 --shared-memory <"system"|"cuda"|"none">: Specifies the type of the shared
	 memory to use for input and output data. Default is none.
 --output-shared-memory-size: The size in bytes of the shared memory region to
	 allocate per output tensor. Only needed when one or more of the
	 outputs are of string type and/or variable shape. The value should be
	 larger than the size of the largest output tensor the model is
	 expected to return. The analyzer will use the following formula to
	 calculate the total shared memory to allocate: output_shared_memory_size *
	 number_of_outputs * batch_size. Defaults to 100KB.
 --shape: The shape used for the specified input. The argument must be
	 specified as 'name:shape' where the shape is a comma-separated list for
	 dimension sizes, for example '--shape input_name:1,2,3' indicate tensor
	 shape [ 1, 2, 3 ]. --shape may be specified multiple times to
	 specify shapes for different inputs.
 --sequence-length: Indicates the base length of a sequence used for sequence
	 models. A sequence with length X will be composed of X requests to
	 be sent as the elements in the sequence. The actual length of the
	 sequencewill be within +/- Y% of the base length, where Y defaults to
	 20% and is customizable via `--sequence-length-variation`. If
	 sequence length is unspecified and input data is provided, the sequence
	 length will be the number of inputs in the user-provided input data.
	 Default is 20.
 --sequence-length-variation: The percentage variation in length of sequences.
	 This flag is only valid when not using user-provided input data or
	 when `--sequence-length` is specified while using user-provided
	 input data. Default is 20.
 --sequence-id-range <start:end>: Determines the range of sequence id used by
	 the perf_analyzer. The perf_analyzer will start from the sequence id
	 of 'start' and go till 'end' (excluded). If 'end' is not specified
	 then perf_analyzer will use new sequence id without bounds. If 'end'
	 is specified and the concurrency setting may result in maintaining
	 a number of sequences more than the range of available sequence id,
	 perf analyzer will exit with error due to possible sequence id
	 collision. The default setting is start from sequence id 1 and without
	 bounds
 --string-length: Specifies the length of the random strings to be generated
	 by the analyzer for string input. This option is ignored if
	 --input-data points to a directory. Default is 128.
 --string-data: If provided, analyzer will use this string to initialize
	 string input buffers. The perf analyzer will replicate the given string
	 to build tensors of required shape. --string-length will not have any
	 effect. This option is ignored if --input-data points to a
	 directory.
 --input-tensor-format=[binary|json]: Specifies Triton inference request input
	 tensor format. Only valid when HTTP protocol is used. Default is
	 'binary'.
 --output-tensor-format=[binary|json]: Specifies Triton inference response
	 output tensor format. Only valid when HTTP protocol is used. Default is
	 'binary'.

III. SERVER DETAILS: 
 -u:                                  Specify URL to the server. When using triton default is "localhost:8000" if using HTTP and
	 "localhost:8001" if using gRPC. When using tfserving default is
	 "localhost:8500". 
 -i:                                  The communication protocol to use. The available protocols are gRPC and HTTP. Default is HTTP.
 --ssl-grpc-use-ssl:                  Bool (true|false) for whether to use encrypted channel to the server. Default false.
 --ssl-grpc-root-certifications-file: Path to file containing the PEM encoding of the server root certificates.
 --ssl-grpc-private-key-file:         Path to file containing the PEM encoding of the client's private key.
 --ssl-grpc-certificate-chain-file:   Path to file containing the PEM encoding of the client's certificate chain.
 --ssl-https-verify-peer:             Number (0|1) to verify the peer's SSL certificate. See
	 https://curl.se/libcurl/c/CURLOPT_SSL_VERIFYPEER.html for the meaning of each value. Default is 1.
 --ssl-https-verify-host:             Number (0|1|2) to verify the certificate's name against host. See
	 https://curl.se/libcurl/c/CURLOPT_SSL_VERIFYHOST.html for the meaning of each value. Default is 2.
 --ssl-https-ca-certificates-file:    Path to Certificate Authority (CA) bundle.
 --ssl-https-client-certificate-file: Path to the SSL client certificate.
 --ssl-https-client-certificate-type: Type (PEM|DER) of the client SSL certificate. Default is PEM.
 --ssl-https-private-key-file:        Path to the private keyfile for TLS and SSL client cert.
 --ssl-https-private-key-type:        Type (PEM|DER) of the private key file. Default is PEM.

IV. OTHER OPTIONS: 
 -f:     The latency report will be stored in the file named by this option.
	 By default, the result is not recorded in a file.
 --profile-export-file: Specifies the path that the profile export will be generated at. By
	 default, the profile export will not be generated.
 -H:     The header will be added to HTTP requests (ignored for GRPC
	 requests). The header must be specified as 'Header:Value'. -H may be
	 specified multiple times to add multiple headers.
 --streaming: Enables the use of streaming API. This flag is only valid with
	 gRPC protocol. By default, it is set false.
 --grpc-compression-algorithm: The compression algorithm to be used by gRPC
	 when sending request. Only supported when grpc protocol is being used.
	 The supported values are none, gzip, and deflate. Default value is
	 none.
 --trace-file: Set the file where trace output will be saved. If
	 --log-frequency is also specified, this argument value will be the prefix of the
	 files to save the trace output. See --log-frequency for details.
	 Only used for service-kind of triton. Default value is none.
 --trace-level: Specify a trace level. OFF to disable tracing, TIMESTAMPS to
	 trace timestamps, TENSORS to trace tensors. It may be specified
	 multiple times to trace multiple information. Default is OFF.
 --trace-rate: Set the trace sampling rate. Default is 1000.
 --trace-count: Set the number of traces to be sampled. If the value is -1,
	 the number of traces to be sampled will not be limited. Default is -1.
 --log-frequency:  Set the trace log frequency. If the value is 0, Triton will
	 only log the trace output to <trace-file> when shutting down.
	 Otherwise, Triton will log the trace output to <trace-file>.<idx> when it
	 collects the specified number of traces. For example, if the log
	 frequency is 100, when Triton collects the 100-th trace, it logs the
	 traces to file <trace-file>.0, and when it collects the 200-th trace,
	 it logs the 101-th to the 200-th traces to file <trace-file>.1.
	 Default is 0.
 --triton-server-directory: The Triton server install path. Required by and
	 only used when C API is used (--service-kind=triton_c_api).
	 eg:--triton-server-directory=/opt/tritonserver.
 --model-repository: The model repository of which the model is loaded.
	 Required by and only used when C API is used
	 (--service-kind=triton_c_api). eg:--model-repository=/tmp/host/docker-data/model_unit_test.
 --verbose-csv: The csv files generated by perf analyzer will include
	 additional information.
 --collect-metrics: Enables collection of server-side inference server
	 metrics. Outputs metrics in the csv file generated with the -f option. Must
	 enable `--verbose-csv` option to use the `--collect-metrics`.
 --metrics-url: The URL to query for server-side inference server metrics.
	 Default is 'localhost:8002/metrics'.
 --metrics-interval: How often in milliseconds, within each measurement
	 window, to query for server-side inference server metrics. Default is
	 1000.
 --bls-composing-models: A comma separated list of all BLS composing models
	 (with optional model version number after a colon for each) that may
	 be called by the input BLS model. For example, 'modelA:3,modelB'
	 would specify that modelA and modelB are composing models that may be
	 called by the input BLS model, and that modelA will use version 3,
	 while modelB's version is unspecified

```



#### Triton server

```bash

Usage: tritonserver [options]
  --help
	Print usage

Server:
  --id <string>
	Identifier for this server.
  --exit-timeout-secs <integer>
	Timeout (in seconds) when exiting to wait for in-flight
	inferences to finish. After the timeout expires the server exits even if
	inferences are still in flight.

Logging:
  --log-verbose <integer>
	Set verbose logging level. Zero (0) disables verbose logging
	and values >= 1 enable verbose logging.
  --log-info <boolean>
	Enable/disable info-level logging.
  --log-warning <boolean>
	Enable/disable warning-level logging.
  --log-error <boolean>
	Enable/disable error-level logging.
  --log-format <string>
	Set the logging format. Options are "default" and "ISO8601".
	The default is "default". For "default", the log severity (L) and
	timestamp will be logged as "LMMDD hh:mm:ss.ssssss". For "ISO8601",
	the log format will be "YYYY-MM-DDThh:mm:ssZ L".
  --log-file <string>
	Set the name of the log output file. If specified, log
	outputs will be saved to this file. If not specified, log outputs will
	stream to the console.

Model Repository:
  --model-store <string>
	Equivalent to --model-repository.
  --model-repository <string>
	Path to model repository directory. It may be specified
	multiple times to add multiple model repositories. Note that if a model
	is not unique across all model repositories at any time, the model
	will not be available.
  --exit-on-error <boolean>
	Exit the inference server if an error occurs during
	initialization.
  --disable-auto-complete-config
	If set, disables the triton and backends from auto
	completing model configuration files. Model configuration files must be
	provided and all required configuration settings must be specified.
  --strict-readiness <boolean>
	If true /v2/health/ready endpoint indicates ready if the
	server is responsive and all models are available. If false
	/v2/health/ready endpoint indicates ready if server is responsive even if
	some/all models are unavailable.
  --model-control-mode <string>
	Specify the mode for model management. Options are "none",
	"poll" and "explicit". The default is "none". For "none", the server
	will load all models in the model repository(s) at startup and will
	not make any changes to the load models after that. For "poll", the
	server will poll the model repository(s) to detect changes and will
	load/unload models based on those changes. The poll rate is
	controlled by 'repository-poll-secs'. For "explicit", model load and unload
	is initiated by using the model control APIs, and only models
	specified with --load-model will be loaded at startup.
  --repository-poll-secs <integer>
	Interval in seconds between each poll of the model
	repository to check for changes. Valid only when --model-control-mode=poll is
	specified.
  --load-model <string>
	Name of the model to be loaded on server startup. It may be
	specified multiple times to add multiple models. To load ALL models
	at startup, specify '*' as the model name with --load-model=* as the
	ONLY --load-model argument, this does not imply any pattern
	matching. Specifying --load-model=* in conjunction with another
	--load-model argument will result in error. Note that this option will only
	take effect if --model-control-mode=explicit is true.
  --model-config-name <string>
	The custom configuration name for models to load.The name
	should not contain any space character.For example:
	--model-config-name=h100. If --model-config-name is not set, Triton will use the
	default config.pbtxt.
  --model-load-thread-count <integer>
	The number of threads used to concurrently load models in
	model repositories. Default is 4.
  --model-load-retry-count <integer>
	The number of retry to load a model in model repositories.
	Default is 0.
  --model-namespacing <boolean>
	Whether model namespacing is enable or not. If true, models
	with the same name can be served if they are in different namespace.

HTTP:
  --allow-http <boolean>
	Allow the server to listen for HTTP requests.
  --http-address <string>
	The address for the http server to bind to. Default is
	0.0.0.0
  --http-port <integer>
	The port for the server to listen on for HTTP requests.
	Default is 8000.
  --reuse-http-port <boolean>
	Allow multiple servers to listen on the same HTTP port when
	every server has this option set. If you plan to use this option as
	a way to load balance between different Triton servers, the same
	model repository or set of models must be used for every server.
  --http-header-forward-pattern <string>
	The regular expression pattern that will be used for
	forwarding HTTP headers as inference request parameters.
  --http-thread-count <integer>
	Number of threads handling HTTP requests.
  --http-restricted-api <<string>:<string>=<string>>
	Specify restricted HTTP api setting. The format of this flag
	is --http-restricted-api=<apis>,<key>=<value>. Where <api> is a
	comma-separated list of apis to be restricted. <key> will be additional
	header key to be checked when a HTTP request is received, and
	<value> is the value expected to be matched. Allowed APIs: health,
	metadata, inference, shared-memory, model-config, model-repository,
	statistics, trace, logging

GRPC:
  --allow-grpc <boolean>
	Allow the server to listen for GRPC requests.
  --grpc-address <string>
	The address for the grpc server to binds to. Default is
	0.0.0.0
  --grpc-port <integer>
	The port for the server to listen on for GRPC requests.
	Default is 8001.
  --reuse-grpc-port <boolean>
	Allow multiple servers to listen on the same GRPC port when
	every server has this option set. If you plan to use this option as
	a way to load balance between different Triton servers, the same
	model repository or set of models must be used for every server.
  --grpc-header-forward-pattern <string>
	The regular expression pattern that will be used for
	forwarding GRPC headers as inference request parameters.
  --grpc-infer-allocation-pool-size <integer>
	The maximum number of inference request/response objects
	that remain allocated for reuse. As long as the number of in-flight
	requests doesn't exceed this value there will be no
	allocation/deallocation of request/response objects.
  --grpc-use-ssl <boolean>
	Use SSL authentication for GRPC requests. Default is false.
  --grpc-use-ssl-mutual <boolean>
	Use mututal SSL authentication for GRPC requests. This
	option will preempt '--grpc-use-ssl' if it is also specified. Default is
	false.
  --grpc-server-cert <string>
	File holding PEM-encoded server certificate. Ignored unless
	--grpc-use-ssl is true.
  --grpc-server-key <string>
	File holding PEM-encoded server key. Ignored unless
	--grpc-use-ssl is true.
  --grpc-root-cert <string>
	File holding PEM-encoded root certificate. Ignore unless
	--grpc-use-ssl is false.
  --grpc-infer-response-compression-level <string>
	The compression level to be used while returning the infer
	response to the peer. Allowed values are none, low, medium and high.
	By default, compression level is selected as none.
  --grpc-keepalive-time <integer>
	The period (in milliseconds) after which a keepalive ping is
	sent on the transport. Default is 7200000 (2 hours).
  --grpc-keepalive-timeout <integer>
	The period (in milliseconds) the sender of the keepalive
	ping waits for an acknowledgement. If it does not receive an
	acknowledgment within this time, it will close the connection. Default is
	20000 (20 seconds).
  --grpc-keepalive-permit-without-calls <boolean>
	Allows keepalive pings to be sent even if there are no calls
	in flight (0 : false; 1 : true). Default is 0 (false).
  --grpc-http2-max-pings-without-data <integer>
	The maximum number of pings that can be sent when there is
	no data/header frame to be sent. gRPC Core will not continue sending
	pings if we run over the limit. Setting it to 0 allows sending pings
	without such a restriction. Default is 2.
  --grpc-http2-min-recv-ping-interval-without-data <integer>
	If there are no data/header frames being sent on the
	transport, this channel argument on the server side controls the minimum
	time (in milliseconds) that gRPC Core would expect between receiving
	successive pings. If the time between successive pings is less than
	this time, then the ping will be considered a bad ping from the peer.
	Such a ping counts as a ‘ping strike’. Default is 300000 (5
	minutes).
  --grpc-http2-max-ping-strikes <integer>
	Maximum number of bad pings that the server will tolerate
	before sending an HTTP2 GOAWAY frame and closing the transport.
	Setting it to 0 allows the server to accept any number of bad pings.
	Default is 2.
  --grpc-max-connection-age <integer>
	Maximum time that a channel may exist in
	milliseconds.Default is undefined.
  --grpc-max-connection-age-grace <integer>
	Grace period after the channel reaches its max age. Default
	is undefined.
  --grpc-restricted-protocol <<string>:<string>=<string>>
	Specify restricted GRPC protocol setting. The format of this
	flag is --grpc-restricted-protocol=<protocols>,<key>=<value>. Where
	<protocol> is a comma-separated list of protocols to be restricted.
	<key> will be additional header key to be checked when a GRPC
	request is received, and <value> is the value expected to be matched.
	Allowed protocols: health, metadata, inference, shared-memory,
	model-config, model-repository, statistics, trace, logging

Sagemaker:
  --allow-sagemaker <boolean>
	Allow the server to listen for Sagemaker requests. Default
	is false.
  --sagemaker-port <integer>
	The port for the server to listen on for Sagemaker requests.
	Default is 8080.
  --sagemaker-safe-port-range <<integer>-<integer>>
	Set the allowed port range for endpoints other than the
	SageMaker endpoints.
  --sagemaker-thread-count <integer>
	Number of threads handling Sagemaker requests. Default is 8.

Vertex:
  --allow-vertex-ai <boolean>
	Allow the server to listen for Vertex AI requests. Default
	is true if AIP_MODE=PREDICTION, false otherwise.
  --vertex-ai-port <integer>
	The port for the server to listen on for Vertex AI requests.
	Default is AIP_HTTP_PORT if set, 8080 otherwise.
  --vertex-ai-thread-count <integer>
	Number of threads handling Vertex AI requests. Default is 8.
  --vertex-ai-default-model <string>
	The name of the model to use for single-model inference
	requests.

Metrics:
  --allow-metrics <boolean>
	Allow the server to provide prometheus metrics.
  --allow-gpu-metrics <boolean>
	Allow the server to provide GPU metrics. Ignored unless
	--allow-metrics is true.
  --allow-cpu-metrics <boolean>
	Allow the server to provide CPU metrics. Ignored unless
	--allow-metrics is true.
  --metrics-address <string>
	The address for the metrics server to bind to. Default is
	the same as --http-address if built with HTTP support. Otherwise,
	default is 0.0.0.0
  --metrics-port <integer>
	The port reporting prometheus metrics. Default is 8002.
  --metrics-interval-ms <float>
	Metrics will be collected once every <metrics-interval-ms>
	milliseconds. Default is 2000 milliseconds.
  --metrics-config <<string>=<string>>
	Specify a metrics-specific configuration setting. The format
	of this flag is --metrics-config=<setting>=<value>. It can be
	specified multiple times.

Tracing:
  --trace-config <<string>,<string>=<string>>
	Specify global or trace mode specific configuration setting.
	The format of this flag is --trace-config <mode>,<setting>=<value>.
	Where <mode> is either "triton" or "opentelemetry". The default is
	"triton". To specify global trace settings (level, rate, count, or
	mode), the format would be --trace-config <setting>=<value>. For
	"triton" mode, the server will use Triton's Trace APIs. For
	"opentelemetry" mode, the server will use OpenTelemetry's APIs to generate,
	collect and export traces for individual inference requests.

Backend:
  --backend-directory <string>
	The global directory searched for backend shared libraries.
	Default is '/opt/tritonserver/backends'.
  --backend-config <<string>,<string>=<string>>
	Specify a backend-specific configuration setting. The format
	of this flag is --backend-config=<backend_name>,<setting>=<value>.
	Where <backend_name> is the name of the backend, such as 'tensorrt'.

Repository Agent:
  --repoagent-directory <string>
	The global directory searched for repository agent shared
	libraries. Default is '/opt/tritonserver/repoagents'.

Response Cache:
  --cache-config <<string>,<string>=<string>>
	Specify a cache-specific configuration setting. The format
	of this flag is --cache-config=<cache_name>,<setting>=<value>. Where
	<cache_name> is the name of the cache, such as 'local' or 'redis'.
	Example: --cache-config=local,size=1048576 will configure a 'local'
	cache implementation with a fixed buffer pool of size 1048576 bytes.
  --cache-directory <string>
	The global directory searched for cache shared libraries.
	Default is '/opt/tritonserver/caches'. This directory is expected to
	contain a cache implementation as a shared library with the name
	'libtritoncache.so'.

Rate Limiter:
  --rate-limit <string>
	Specify the mode for rate limiting. Options are
	"execution_count" and "off". The default is "off". For "execution_count", the
	server will determine the instance using configured priority and the
	number of time the instance has been used to run inference. The
	inference will finally be executed once the required resources are
	available. For "off", the server will ignore any rate limiter config and
	run inference as soon as an instance is ready.
  --rate-limit-resource <<string>:<integer>:<integer>>
	The number of resources available to the server. The format
	of this flag is
	--rate-limit-resource=<resource_name>:<count>:<device>. The <device> is optional and if not listed will be applied to
	every device. If the resource is specified as "GLOBAL" in the model
	configuration the resource is considered shared among all the devices
	in the system. The <device> property is ignored for such resources.
	This flag can be specified multiple times to specify each resources
	and their availability. By default, the max across all instances
	that list the resource is selected as its availability. The values for
	this flag is case-insensitive.

Memory/Device Management:
  --pinned-memory-pool-byte-size <integer>
	The total byte size that can be allocated as pinned system
	memory. If GPU support is enabled, the server will allocate pinned
	system memory to accelerate data transfer between host and devices
	until it exceeds the specified byte size. If 'numa-node' is configured
	via --host-policy, the pinned system memory of the pool size will be
	allocated on each numa node. This option will not affect the
	allocation conducted by the backend frameworks. Default is 256 MB.
  --cuda-memory-pool-byte-size <<integer>:<integer>>
	The total byte size that can be allocated as CUDA memory for
	the GPU device. If GPU support is enabled, the server will allocate
	CUDA memory to minimize data transfer between host and devices
	until it exceeds the specified byte size. This option will not affect
	the allocation conducted by the backend frameworks. The argument
	should be 2 integers separated by colons in the format <GPU device
	ID>:<pool byte size>. This option can be used multiple times, but only
	once per GPU device. Subsequent uses will overwrite previous uses for
	the same GPU device. Default is 64 MB.
  --cuda-virtual-address-size <<integer>:<integer>>
	The total CUDA virtual address size that will be used for
	each implicit state when growable memory is used. This value
	determines the maximum size of each implicit state. The state size cannot go
	beyond this value. The argument should be 2 integers separated by
	colons in the format <GPU device ID>:<CUDA virtual address size>. This
	option can be used multiple times, but only once per GPU device.
	Subsequent uses will overwrite previous uses for the same GPU device.
	Default is 1 GB.
  --min-supported-compute-capability <float>
	The minimum supported CUDA compute capability. GPUs that
	don't support this compute capability will not be used by the server.
  --buffer-manager-thread-count <integer>
	The number of threads used to accelerate copies and other
	operations required to manage input and output tensor contents.
	Default is 0.
  --host-policy <<string>,<string>=<string>>
	Specify a host policy setting associated with a policy name.
	The format of this flag is
	--host-policy=<policy_name>,<setting>=<value>. Currently supported settings are 'numa-node', 'cpu-cores'.
	Note that 'numa-node' setting will affect pinned memory pool behavior,
	see --pinned-memory-pool for more detail.
  --model-load-gpu-limit <<device_id>:<fraction>>
	Specify the limit on GPU memory usage as a fraction. If
	model loading on the device is requested and the current memory usage
	exceeds the limit, the load will be rejected. If not specified, the
	limit will not be set.

DEPRECATED:
  --strict-model-config <boolean>
	DEPRECATED: If true model configuration files must be
	provided and all required configuration settings must be specified. If
	false the model configuration may be absent or only partially specified
	and the server will attempt to derive the missing required
	configuration.
  --response-cache-byte-size <integer>
	DEPRECATED: Please use --cache-config instead.
  --trace-file <string>
	DEPRECATED: Please use --trace-config
	triton,file=<path/to/your/file> Set the file where trace output will be saved. If
	--trace-log-frequency is also specified, this argument value will be the
	prefix of the files to save the trace output. See --trace-log-frequency
	for detail.
  --trace-level <string>
	DEPRECATED: Please use --trace-config
	level=<OFF|TIMESTAMPS|TENSORS>Specify a trace level. OFF to disable tracing, TIMESTAMPS to
	trace timestamps, TENSORS to trace tensors. It may be specified
	multiple times to trace multiple information. Default is OFF.
  --trace-rate <integer>
	DEPRECATED: Please use --trace-config rate=<rate value>Set
	the trace sampling rate. Default is 1000.
  --trace-count <integer>
	DEPRECATED: Please use --trace-config count=<count value>Set
	the number of traces to be sampled. If the value is -1, the number
	of traces to be sampled will not be limited. Default is -1.
  --trace-log-frequency <integer>
	DEPRECATED: Please use --trace-config
	triton,log-frequency=<value>Set the trace log frequency. If the value is 0, Triton will
	only log the trace output to <trace-file> when shutting down.
	Otherwise, Triton will log the trace output to <trace-file>.<idx> when it
	collects the specified number of traces. For example, if the log
	frequency is 100, when Triton collects the 100-th trace, it logs the
	traces to file <trace-file>.0, and when it collects the 200-th trace, it
	logs the 101-th to the 200-th traces to file <trace-file>.1.
	Default is 0.


```
