#! /bin/bash

distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | tee /etc/yum.repos.d/nvidia-docker.repo

yum -y install nvidia-container-toolkit

wget https://raw.githubusercontent.com/NVIDIA/dgx-selinux/master/bin/RHEL7/nvidia-container.pp
semodule -i nvidia-container.pp

nvidia-container-cli -k list | restorecon -v -f -

restorecon -Rv /dev

