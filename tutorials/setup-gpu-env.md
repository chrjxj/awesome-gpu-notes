# Setup Env for DataCenter GPU

以Ubuntu为例

[toc]

## 1. 安装GPU驱动


* 准备工作

    * 查看是否安装了NVIDIA GPU: `lspci | grep -i nvidia`
    * 【重要】根据GPU的型号，OS的版本，从官网下载*对应*的驱动程序 https://www.nvidia.com/Download/index.aspx?lang=en-us
      * 以安装 NVIDIA Tesla 驱动为例的详细[步骤](https://cloud.tencent.com/document/product/560/8048)
    
    * 如已知需要下载的驱动版本，也可以命令行下直接下载
    ```bash
    BASE_URL=https://us.download.nvidia.com/tesla
    DRIVER_VERSION=450.80.02
    curl -fSsl -O $BASE_URL/$DRIVER_VERSION/NVIDIA-Linux-x86_64-$DRIVER_VERSION.run
    ```    
    * 安装必要的软件: `sudo apt update && apt install -y build-essential libglvnd-dev pkg-config`

* 安装驱动

    * 运行以下命令禁用当前驱动程序: `sudo telinit 3`
    * 安装方法1 - 使用 Runfile Installers

    ```bash
    sudo apt purge nvidia-*
    sudo chmod +x NVIDIA-Linux-x86_64-xxx.xx.run
    sudo ./NVIDIA-Linux-x86_64-xxx.xx.run
    ```

    * 安装方法2 - 使用OS的 package managers; 参见: [link](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#package-manager); 例如: 

    ```bash
    sudo apt purge nvidia-*
    sudo add-apt-repository ppa:graphics-drivers/ppa
    sudo apt update && sudo apt install nvidia-driver-xxx
    ```

    * 安装完成后重启机器

* 安装后检查

    ```bash
    nvidia-smi
    cat /proc/driver/nvidia/version
    ```

参考文档:

* https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html
* https://www.nvidia.com/Download/Find.aspx?lang=en-us 


(可选) 建议使用以预装CUDA的容器；作为可选项，在主机的OS上，也可以安装CUDA，居然步骤请参见: https://cloud.tencent.com/document/product/560/8064


## 2. 安装容器环境


* 卸载老版本或者其他(非Docker-CE)发行版的 Docker环境

* 安装Docker-CE. 详见[link](https://docs.docker.com/engine/install/)

```bash
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
sudo systemctl status docker
sudo docker container run hello-world
```
* 安装nvidia-docker2

    * 说明: 如果OS里的`/etc/os-release`文件被修改，请手动设置 `distribution`变量

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

参考文档:

* NVIDIA Container Toolkit github [repo](https://github.com/NVIDIA/nvidia-docker)
* NVIDIA Container Toolkit [Overview](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html)
* [setup NVIDIA Container Toolkit on Ubuntu](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)
* https://docs.docker.com/engine/install/



## 3. 使用NGC


1. 到 https://ngc.nvidia.com 注册账号，并登陆
2. 登录后，点击右上角账户名称，在下拉菜单中选择 `Setup`后，选择 `GetAPI Key`
3. 进入API Key页面后，单击 `Generate API Key`，生成您的API密钥
4. 到你的服务器上（假定容器环境已经安装完成）登陆 nvcr.io

```
$ docker login nvcr.io

Username ($oauthtoken): 【这里输入 $oauthtoken】
Password: 【这里输入在网站生成的 API密钥】

```

5. 到网站 https://catalog.ngc.nvidia.com 找到需要的容器, 拉取镜像, 如: `docker pull nvcr.io/nvidia/pytorch:22.02-py3`

详见: [基于GPU实例部署NGC环境](https://cloud.baidu.com/doc/GPU/s/fkppdq6rd)

## 4. 其他Linux发行版

#### RHEL 7 or RHEL 8

在RHEL 7 or RHEL 8 上安装、配置NVIDIA GPU 驱动程序、CUDA和 nvidia-container-toolkit: 

* [教程](https://www.redhat.com/en/blog/how-use-gpus-containers-bare-metal-rhel-8)
* [配置脚本](./enable-GPUs-containers-rhel); 来源于 Github [repo](https://github.com/openshift-psap/blog-artifacts/tree/master/how-to-enable-GPUs-containers-rhel)

## 5. 常见问题


#### GPG Repository Key

Updating the CUDA Linux GPG Repository Key: https://developer.nvidia.com/blog/updating-the-cuda-linux-gpg-repository-key/

Fix Nvidia Apt Repository Public Key Error
2022-05-05

When running apt-get update inside Ubuntu 18.04, I have the following error:
```
W: GPG error: https://developer.download.nvidia.cn/compute/cuda/repos/ubuntu1804/x86_64 InRelease: The following signatures couldn’t be verified because the public key is not available: NO_PUBKEY A4B469963BF863CC
E: The repository ‘https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 InRelease’ is no longer signed.
N: Updating from such a repository can’t be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

This is because Nvidia is changing their public keys for their repositories, see the details here. The instructions in the original post does not work for me. I still see errors after running the command. Since I am building a Docker image, I followed the instructions here and it works:

```bash
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-key del 7fa2af80
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub
```

The two rm commands are crucial to fix the issue. The directory /etc/apt/sources.list.d/ stores the apt repository list for some packages, so that you do not need to touch the main source list file /etc/apt/sources.list. Files under this directory has the same format as the main sources.list file, and they are usually added by automated tools.

The command `apt-key del 7fa2af80` will delete the old public key for Nvidia. The `apt-key adv --fetch-keys` commands is used to add the new public keys for Nvidia.

References

  * The use of directory sources.list.d
    * https://stackoverflow.com/a/26021071/6064933
    * https://stackoverflow.com/a/22969010/6064933
  * update public key using apt-key: https://askubuntu.com/a/865494/768311
  * apt-key doc: http://manpages.ubuntu.com/manpages/bionic/man8/apt-key.8.html