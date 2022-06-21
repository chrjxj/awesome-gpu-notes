FROM nvcr.io/nvidia/tritonserver:21.12-py3

# Install base utilities
RUN apt-get update || true && \ 
    apt-get install -y libssl-dev wget tar  rapidjson-dev libarchive-dev zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

RUN cd ~ && wget https://cmake.org/files/v3.17/cmake-3.17.3.tar.gz && \
    tar xfz cmake-3.17.3.tar.gz && cd cmake-3.17.3 && \
    ./bootstrap && make -j$(nproc) && make install

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH 
RUN conda create -n monai python=3.8  && \
    echo "source activate monai" > ~/.bashrc
ENV PATH /opt/conda/envs/monai/bin:$PATH

RUN /bin/bash -c "source activate monai"

RUN export PYTHONNOUSERSITE=True && \
    pip install torch==1.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html && \
    BUILD_MONAI=1 pip install --no-build-isolation git+https://github.com/Project-MONAI/MONAI#egg=monai && \                    
    pip install nibabel scikit-image pillow tensorboard gdown ignite torchvision itk tqdm lmdb psutil cucim  pandas einops transformers mlflow matplotlib tensorboardX tifffile cupy
