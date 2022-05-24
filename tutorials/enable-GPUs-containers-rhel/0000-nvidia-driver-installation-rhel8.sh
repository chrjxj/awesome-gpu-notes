#! /bin/bash

yum -y install kernel-devel-`uname -r` kernel-headers-`uname -r`

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum -y install dkms

yum -y install http://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-repo-rhel8-10.2.89-1.x86_64.rpm

modprobe -r nouveau

yum -y install cuda

nvidia-modprobe && nvidia-modprobe -u

echo "Verifying driver installation"
nvidia-smi --query-gpu=gpu_name --format=csv,noheader --id=0 | sed -e 's/ /-/g'
