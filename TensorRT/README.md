# TensorRT

## General

#### GTC Talks and Workshops

- S31828 – TensorRT Quick Start Guide; [link](https://gtc21.event.nvidia.com/media/TensorRT%20Quick%20Start%20Guide%20%5BS31828%5D/1_8ebzdf11)
- CWES1737 – Accelerate Deep Learning Inference with TensorRT 8.0; [link](https://gtc21.event.nvidia.com/media/Accelerate+Deep+Learning+Inference+with+TensorRT+8.0+%5BS31876%5D/1_rhhv5aiq)

- S31552 – Making the Most of Structured Sparsity in the NVIDIA Ampere Architecture
- S31653 – Quantization Aware Training in PyTorch with TensorRT 8.0; [link](https://gtc21.event.nvidia.com/media/Quantization%20Aware%20Training%20in%20PyTorch%20with%20TensorRT%208.0%20%5BS31653%5D/1_qdvvff64)
 
- S31732 – Inference with Tensorflow2 Integrated with TensorRT
- S31864 – New Features in TRTorch, a PyTorch/TorchScript Compiler Targeting NVIDIA GPUs Using TensorRT
- S32224 – Accelerating Deep Learning Inference with ONNXRuntime-TensorRT
- S31695 – Prototyping and Debugging Deep Learning Inference Models Using TensorRT’s ONNX-Graphsurgeon and Polygraphy Tools

#### Source code

Official 

- [TRT quickstart](https://github.com/NVIDIA/TensorRT/tree/master/quickstart)
- [Pytorch Quantization](https://github.com/NVIDIA/TensorRT/tree/master/tools/pytorch-quantization): PyTorch-Quantization is a toolkit for training and evaluating PyTorch models with simulated quantization. Quantization can be added to the model automatically, or manually, allowing the model to be tuned for accuracy and performance. Quantization is compatible with NVIDIAs high performance integer kernels which leverage integer Tensor Cores. The quantized model can be exported to ONNX and imported by TensorRT 8.0 and later.
- [Polygraphy](https://github.com/NVIDIA/TensorRT/tree/master/tools/Polygraphy): A Deep Learning Inference Prototyping and Debugging Toolkit
- [ONNX GraphSurgeon](https://github.com/NVIDIA/TensorRT/tree/master/tools/onnx-graphsurgeon): a tool to easily generate new ONNX graphs, or modify existing ones.
- [torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt): PyTorch to TensorRT converter

Third-party  

- [tensorrtx](https://github.com/wang-xinyu/tensorrtx): Implementation of popular deep learning networks with TensorRT network definition API
- [pytorch-YOLOv4](https://github.com/Tianxiaomo/pytorch-YOLOv4): PyTorch ,ONNX and TensorRT implementation of YOLOv4
- [tensorrt_demos](https://github.com/jkjung-avt/tensorrt_demos): TensorRT MODNet, YOLOv4, YOLOv3, SSD, MTCNN, and GoogLeNet
- [Inference with TensorRT and Jetson](https://github.com/dusty-nv/): Hello AI World guide to deploying deep-learning inference networks and deep vision primitives with TensorRT and NVIDIA Jetson.



## Reduced Precision


1. Quantization basics:
    * INTEGER QUANTIZATION FOR DEEP LEARNING INFERENCE: PRINCIPLES AND EMPIRICAL EVALUATION, [paper](https://arxiv.org/pdf/2004.09602.pdf)

1. PTQ
    * TensorRT developer guide: [chapter 5](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#mixed_precision) and [chapter 10](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#work-with-qat-networks)  
1. QAT
    * Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference introduces quantization-aware training: [paper](https://arxiv.org/pdf/1712.05877.pdf)
    * Pytorch: [quantization](https://pytorch.org/docs/stable/quantization.html), [Quantized Transfer Learning for Computer Vision Tutorial](https://pytorch.org/tutorials/intermediate/quantized_transfer_learning_tutorial.html)
    * Tensorflow QAT [Blog](https://www.tensorflow.org/model_optimization/guide/quantization/training)

GTC sessions

* GTC talks for [quantization](https://www.nvidia.com/en-us/gtc/on-demand/?search=quantization)
* GTC21 – QAT in PyTorch with TensorRT 8.0: [link](https://gtc21.event.nvidia.com/media/Quantization%20Aware%20Training%20in%20PyTorch%20with%20TensorRT%208.0%20%5BS31653%5D/1_qdvvff64)
