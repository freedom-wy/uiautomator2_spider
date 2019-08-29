# docker_u2 
## docker笔记

**docker run hello-world**  运行hello-world容器,若本地没有该镜像，则直接下载  
**docker version** 查看docker版本  
**docker run -it ubuntu bash**  以bash模式启动ubuntu容器，若本地没有ubuntu镜像，则直接下载  
**docker ps -a**  查看本地所有容器  
**docker images**  查看本地所有镜像  
**docker search 镜像名称**  在terminal中查看Hub中的镜像  
**docker pull 镜像名称**  在docker hub中下载centos镜像  
**docker run --name 容器名称 -it 镜像名称 /bin/bash**  使用centos镜像启动一个容器  
**docker rm 容器名称或容器ID**  删除容器  
**docker rmi 镜像名称**  删除镜像  
**docker ps -l**  查看当前机器中运行的容器  
**docker run -d centos /bin/bash -c "循环语句"**  -d参数为在后台运行，否则会占用一个terminal窗口  
**docker stop 容器名称或容器短ID**  停止容器  
**docker kill 容器名称或容器短ID**  停止容器  
**docker attach 长ID**  进入启动的容器内部  
**docker exec -it 短ID bash** 进入启动的容器内部  
**docker start 容器名称或ID**  启动容器  
**docker restart 容器名称或ID**  重启一个在运行的容器  
**docker pause 容器ID**  暂停一个容器  
**docker unpause 容器ID**  启动一个暂停的容器  
**docker rm -v $(docker ps -aq -f status=exited)**  批量删除状态为退出的容器  
**docker run -d -p 80 httpd** 启动一个httpd容器,使用随机端口  
**docker run -d -p 80:80 httpd** 启动一个80端口的容器，并进行端口映射
**docker commit --author "昵称<邮箱>" --message "备注信息" 容器名称 镜像名称:版本号**  将当前容器封装成镜像  
**docker history**  查看镜像历史命令  
**docker diff webserver**  查看容器内有哪些变化  
**docker info**  查看账号信息  
**docker tag 镜像名称:版本号 远程仓库名称:版本号**  上传前需要更改标签  
**docker push 镜像名称:版本号**  上传镜像到docker hub
***
### 构建docker image步骤  
1、创建目录 如创建docker  
2、编辑Dockerfile文件，文件内容  
```dockerfile
FROM sgrio/ubuntu-python
MAINTAINER dazhuang <dazhuang_python@sina.com>

EXPOSE 8080 8081

RUN apt-get update && \
    apt-get install \
        --no-install-recommends -y \
        build-essential \
        libssl-dev \
        python3-dev && \
    pip3 install \
        --no-cache-dir \
        mitmproxy pymongo Appium-Python-Client requests selenium flask pymysql sqlalchemy uiautomator2 weditor&& \
    apt-get remove --purge -y \
        build-essential \
        libssl-dev \
        python3-dev && \
    apt-get autoclean && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```  
3、构建docker images：docker build -t imooc_python .  
***
### 上传docker image到hub
1、首先docker login 验证信息  
2、查看当前已生成好的docker images  
3、在docker hub上创建仓库，如果REPOITORY的名不是你Docker hub账号和仓库，即Docker ID/仓库名，是上传不成功的，当然可以使用docker tag 镜像ID 用户名称/镜像源名(repository name):新的标签名(tag)来更改  
4、docker push<hub-user>/<repo-name>:<tag> 上传image

#### bug:dazhuang_python@sina.com
