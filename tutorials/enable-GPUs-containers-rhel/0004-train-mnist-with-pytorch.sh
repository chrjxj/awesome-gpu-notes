#! /bin/bash

mkdir pytorch_mnist_ex && cd pytorch_mnist_ex
wget https://raw.githubusercontent.com/pytorch/examples/master/mnist/main.py

sed -i '98 s/("cuda.*$/("cuda")/' main.py

podman run  --rm --net=host -v $(pwd):/workspace:Z \
              --security-opt=no-new-privileges \
              --cap-drop=ALL --security-opt label=type:nvidia_container_t \
              docker.io/pytorch/pytorch:latest \
              python3 main.py --epochs=3

