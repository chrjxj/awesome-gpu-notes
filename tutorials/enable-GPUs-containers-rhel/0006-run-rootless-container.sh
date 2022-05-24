#! /bin/bash

podman run --security-opt=no-new-privileges --cap-drop=ALL --security-opt \
label=type:nvidia_container_t --hooks-dir=/usr/share/containers/oci/hooks.d/ \
docker.io/nvidia/cuda:10.2-base nvidia-smi
