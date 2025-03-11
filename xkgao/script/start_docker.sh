# # 拉取镜像
# docker pull pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel
# # 保存到本地
# docker save -o pytorch_image.tar pytorch/pytorch:latest-cuda12.1
# # 从本地加载镜像
# docker load -i pytorch_image.tar

# 容器打包成镜像
# docker commit xkgao_torch pytorch2.5.1-cuda12.1-cudnn9-devel:v1

docker run --gpus all -it \
    -v /data:/data \
    --name xkgao_torch \
    docker.io/pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel bash
