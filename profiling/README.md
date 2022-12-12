# Profile with Nsight System and Nsight Compute


## Nsight Systems


Nsight Systems Documentation: https://docs.nvidia.com/nsight-systems


Nvidia Developer Blog

*  Nsight Systems Exposes GPU Optimization (May 30 2018): https://devblogs.nvidia.com/nsight-systems-exposes-gpu-optimization/
*  Using Nvidia Nsight Systems in Containers and the Cloud (Jan 29 2020): https://devblogs.nvidia.com/nvidia-nsight-systems-containers-cloud/
* [how to get the same system-wide actionable insights from the NVIDIA Visual Profiler and nvprof with Nsight Systems.](https://developer.nvidia.com/blog/transitioning-nsight-systems-nvidia-visual-profiler-nvprof/)

GTC: 

- [Profile NN with nvidia-nsight-systems](https://www.slideshare.net/JaeGeunHan/profiling-deep-learning-network-using-nvidia-nsight-systems)
- GTC2019, [s9339-profiling-deep-learning-networks](https://developer.download.nvidia.com/video/gputechconf/gtc/2019/presentation/s9339-profiling-deep-learning-networks.pdf)

## Nsight Compute


Nsight Compute Documentation: https://docs.nvidia.com/nsight-compute

Nsight Compute Command Line Interface User Manual: https://docs.nvidia.com/nsight-systems/pdf/Nsight-Systems-User-Guide.pdf


Nvidia Developer Blog

1. Using Nsight Compute to Inspect your Kernels (Sep 16 2019): https://devblogs.nvidia.com/using-nsight-compute-to-inspect-your-kernels/

## Common topics

Workload Memory Analysis

1. CUDA Memory Model: https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#memory-hierarchy
1. Device Memory Access Performance Guidelines: https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#device-memory-accesses


Stall Reasons

1. Nsight Graphics Docs: Stall Reasons: https://docs.nvidia.com/drive/drive_os_5.1.12.0L/nsight-graphics/activities/#shaderprofiler_stallreasons
1. Issue Efficiency Nsight Visual Studio Edition: https://docs.nvidia.com/gameworks/content/developertools/desktop/analysis/report/cudaexperiments/kernellevel/issueefficiency.htm


Occupancy

* Nsight Visual Studio Edition: https://docs.nvidia.com/gameworks/content/developertools/desktop/analysis/report/cudaexperiments/kernellevel/achievedoccupancy.htm




## DLProf
- blog: https://developer.nvidia.com/blog/profiling-and-optimizing-deep-neural-networks-with-dlprof-and-pyprof/


- [dlprof-user-guide](https://docs.nvidia.com/deeplearning/frameworks/dlprof-user-guide/index.html)

- [Profiling and Optimizing Deep Neural Networks with DLProf and PyProf](https://developer.nvidia.com/blog/profiling-and-optimizing-deep-neural-networks-with-dlprof-and-pyprof/)


## Reference



#### Some Opitions in Nsight Systems CMD line


```bash
# Breakdown of options:
nsys profile
-w true # Don't suppress app's console output.
-t cuda,nvtx,osrt,cudnn,cublas # Instrument, and show timeline bubbles for, cuda api calls, nvtx ranges,
                               # os runtime functions, cudnn library calls, and cublas library calls.
                               # These options do not require -s cpu nor do they silently enable -s cpu.
-s cpu # Sample the cpu stack periodically.  Stack samples show up as little tickmarks on the cpu timeline.
       # Last time i checked they were orange, but still easy to miss.
       # Mouse over them to show the backtrace at that point.
       # -s cpu can increase cpu overhead substantially (I've seen 2X or more) so be aware of that distortion.
       # -s none disables cpu sampling.  Without cpu sampling, the profiling overhead is reduced.
       # Use -s none if you want the timeline to better represent a production job (api calls and kernels will
       # still appear on the profile, but profiling them doesn't distort the timeline nearly as much).
-o nsight_report # output file
-f true # overwrite existing output file
--capture-range=cudaProfilerApi # Only start profiling when the app calls cudaProfilerStart...
--stop-on-range-end=true # ...and end profiling when the app calls cudaProfilerStop.
--cudabacktrace=true # Collect a cpu stack sample for cuda api calls whose runtime exceeds some threshold.
                     # When you mouse over a long-running api call on the timeline, a backtrace will
                     # appear, and you can identify which of your functions invoked it.
                     # I really like this feature.
                     # Requires -s cpu.
--cudabacktrace-threshold=10000 # Threshold (in nanosec) that determines how long a cuda api call
                                # must run to trigger a backtrace.  10 microsec is a reasonable value
                                # (most kernel launches should take less than 10 microsec) but you
                                # should retune if you see a particular api call you'd like to investigate.
                                # Requires --cudabacktrace=true and -s cpu.
--osrt-threshold=10000 # Threshold (in nanosec) that determines how long an os runtime call (eg sleep)
                       # must run to trigger a backtrace.
                       # Backtrace collection for os runtime calls that exceed this threshold should
                       # occur by default if -s cpu is enabled.
-x true # Quit the profiler when the app exits.
python script.py args...
```

#### DLProf

- DLProf Command:

```

usage: dlprof [<args>] [application]

usage: dlprof --nsys_database=[nsys.sqlite] [<args>]

    -h, --help
       Print help message.

    -V, --version
       Print version information.

    -f, --force=
       Possible values are 'true' or 'false'.
       If true, overwrite all existing result files
       with the same output filename (QDSTREM, QDREP, 
       SQLITE, CSV, JSON).
       Default is 'false'.

    -v, --verbosity=
       Possible values are 'quiet', 'minimal', 'normal',
       'detailed', 'diagnostic'.
       Specify the output verbosity level.
       Default is 'normal'.

    -m, --mode=
       Possible values are `simple', 'pytorch'.
       Specify the target framework being profiled. Use
       'simple' to generate only high level metrics agnostic
       to any framework. Use all other options to
       generate detailed metrics and reports specific to
       the framework.
       Default is 'pytorch'.

Nsight System Options
---------------------

    --nsys_database=
       Input SQLITE file generated by Nsight Systems.
       When specified, DLProf will aggregate profile data
       directly from the database. This option can be used to
       evaluate different aggregation options or generate
       new reports.
       If specified, additional application commands are
       ignored and the application will not be 
       profiled.
       Default option is ignored and application commands
       are expected.

    --nsys_base_name=
       Specify the base name for all Nsight Systems output
       files.
       Default is 'nsys_profile'.

    --nsys_opts=
       Specify nsys args within quotes '"[<nsys args>]"'.
       Customize the args passed to Nsight Systems.
       Option must include the default for DLProf to
       operate correctly.
       Default arguments are '"-t cuda,nvtx -s none"'.

    -y, --delay=
       Collection start delay in seconds.
       Default is 0.

    -d, --duration=
       Collection duration in seconds.
       A value of 0 will profile the entire application.
       Default is 0.

Data Aggregation Options
------------------------

    --key_node=
       Expects the name of a valid operation node in the model.
       Iteration intervals are determined from the NVTX end
       times of each key node instance. If DLProf is not
       detecting intervals correctly, try specifying a 
       different key node.
       Default is 'global_step'.

    --key_op=
       Expects the name of a valid operation in the model.
       This option is aliased to '--key_node' and performs the 
       same functionality.
       Default is ''.

    --iter_start=
       Set the iteration interval to start aggregating data.
       Profile data from iteration intervals less than the
       starting interval are excluded from all aggregated
       reports.
       Default is 0.

    --iter_stop=
       Set the iteration interval to stop aggregating data.
       Profile data from iteration intervals greater than the
       stoping interval are excluded from all aggregated
       reports.
       Default is last found interval.

Output Report Options
---------------------

    --output_path=
       Specify the output path to all aggregated collatoral.
       Default is '.'.

    --profile_name=
       Specify a name for the profile that is prepended to all
       generated report file names and displayed in TensorBoard.
       Default profile name is 'dlprof'.

    --reports=
       Possible values are 'all', 'summary', 'detail', 'kernel', 'iteration', 'tensor', 'op_type', 'group_node', 'expert_systems'.
       Select the aggregated report(s) to generate. Multiple 
       reports can be selected, separated by commas only (no spaces).
       No reports are generated by default.

    --formats=
       Possible values are 'csv', 'json'.
       Specify output file format(s). Multiple formats can be
       selected, separated by commas only (no spaces). A 
       separate report is created for each file format.
       Default is 'csv'.

    --domains=
       Specify NVTX domains to aggregate. Multiple domains can
       selected, separated by commas only (no spaces). A 
       separate report is created for each specified domain.
       Default is all domains.

    --dump_model_data=
       Possible values are 'true' or 'false'.
       If true, a json file is created that contains the 
       raw, correlated model data.
       Default is 'false'.

    --tb_dir=
       Specify the output directory for all generated TensorBoard
       event files.
       Default is 'event_files'.

    -b, --suppress_tb_files=
       Possible values are 'true' or 'false'.
       If true, TensorBoard event files will not be created.
       Default is `false`.
```

