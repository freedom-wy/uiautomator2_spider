# docker_u2 
## docker笔记

docker run hello-world  运行hello-world容器,若本地没有该镜像，则直接下载  
docker version 查看docker版本  
docker run -it ubuntu bash  以bash模式启动ubuntu容器，若本地没有ubuntu镜像，则直接下载  
docker ps -a  查看本地所有容器  
docker images  查看本地所有镜像  
docker search 镜像名称  在terminal中查看Hub中的镜像  
docker pull 镜像名称  在docker hub中下载centos镜像  
docker run --name 容器名称 -it 镜像名称 /bin/bash  使用centos镜像启动一个容器  
docker rm 容器名称或容器ID  删除容器  
docker rmi 镜像名称  删除镜像  
docker ps -l  查看当前机器中运行的容器  
docker run -d centos /bin/bash -c "循环语句"  -d参数为在后台运行，否则会占用一个terminal窗口  
docker stop 容器名称或容器短ID  停止容器  
docker kill 容器名称或容器短ID  停止容器  
docker attach 长ID  进入启动的容器内部  
docker exec -it 短ID bash 进入启动的容器内部  



#### bug:dazhuang_python@sina.com
