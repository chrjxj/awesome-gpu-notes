#! /bin/bash

patch /etc/nvidia-container-runtime/config.toml  << 'EOF'
11a12
> no-cgroups = true
16a18
> debug = "~/.local/nvidia-container-runtime.log"
EOF
