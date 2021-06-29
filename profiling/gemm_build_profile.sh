#!/bin/bash
GPU_ID=1


cd ./nvidia-performance-tools/sgemm/ && mkdir -p build && cd build && rm -rf ./ \
	&& cmake .. && make -j8

# nsys profile  --gpu-metrics-device=$GPU_ID  -o  1-1-pinned-basic         1-1-pinned-basic
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  1-2-pinned-tiled         1-2-pinned-tiled
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  1-3-pinned-joint         1-3-pinned-joint
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  2-1-pageable-basic       2-1-pageable-basic
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  2-2-pinned-basic         2-2-pinned-basic
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  2-3-pinned-tiled         2-3-pinned-tiled
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  2-4-pinned-tiled-overlap 2-4-pinned-tiled-overlap
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  2-5-pinned-joint         2-5-pinned-joint
# nsys profile  --gpu-metrics-device=$GPU_ID  -o  2-6-pinned-joint-overlap 2-6-pinned-joint-overlap


nsys profile   -o  1-1-pinned-basic         1-1-pinned-basic
nsys profile   -o  1-2-pinned-tiled         1-2-pinned-tiled
nsys profile   -o  1-3-pinned-joint         1-3-pinned-joint
nsys profile   -o  2-1-pageable-basic       2-1-pageable-basic
nsys profile   -o  2-2-pinned-basic         2-2-pinned-basic
nsys profile   -o  2-3-pinned-tiled         2-3-pinned-tiled
nsys profile   -o  2-4-pinned-tiled-overlap 2-4-pinned-tiled-overlap
nsys profile   -o  2-5-pinned-joint         2-5-pinned-joint
nsys profile   -o  2-6-pinned-joint-overlap 2-6-pinned-joint-overlap


nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  1-1-pinned-basic         1-1-pinned-basic
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  1-2-pinned-tiled         1-2-pinned-tiled
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  1-3-pinned-joint         1-3-pinned-joint
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  2-1-pageable-basic       2-1-pageable-basic
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  2-2-pinned-basic         2-2-pinned-basic
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  2-3-pinned-tiled         2-3-pinned-tiled
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  2-4-pinned-tiled-overlap 2-4-pinned-tiled-overlap
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  2-5-pinned-joint         2-5-pinned-joint
nv-nsight-cu-cli --kernel-id ::mygemm:6 --section ".*"  -o  2-6-pinned-joint-overlap 2-6-pinned-joint-overlap
