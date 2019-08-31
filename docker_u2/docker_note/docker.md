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
4、```docker push<hub-user>/<repo-name>:<tag>``` 上传image  
***
### 更改docker toolbox的vitualbox到vmware workstation
1、下载docker-machine-driver-vmwareworkstation(docker vmware的驱动)  
2、复制docker-machine-driver-vmwareworkstation.exe 到Docker Toolbox下  
3、修改start.sh脚本  
```shell
#!/bin/bash

export PATH="$PATH:/c/Program Files (x86)/VMware/VMware Workstation"

trap '[ "$?" -eq 0 ] || read -p "Looks like something went wrong in step ´$STEP´... Press any key to continue..."' EXIT

VM=${DOCKER_MACHINE_NAME-default}
DOCKER_MACHINE=./docker-machine.exe

BLUE='\033[1;34m'
GREEN='\033[0;32m'
NC='\033[0m'


if [ ! -f "${DOCKER_MACHINE}" ]; then
  echo "Docker Machine is not installed. Please re-run the Toolbox Installer and try again."
  exit 1
fi

vmrun.exe list | grep "${VM}" &> /dev/null
VM_EXISTS_CODE=$?

set -e

STEP="Checking if machine $VM exists"
if [ $VM_EXISTS_CODE -eq 1 ]; then
  "${DOCKER_MACHINE}" rm -f "${VM}" &> /dev/null || :
  rm -rf ~/.docker/machine/machines/"${VM}"
  #set proxy variables if they exists
  if [ -n ${HTTP_PROXY+x} ]; then
    PROXY_ENV="$PROXY_ENV --engine-env HTTP_PROXY=$HTTP_PROXY"
  fi
  if [ -n ${HTTPS_PROXY+x} ]; then
    PROXY_ENV="$PROXY_ENV --engine-env HTTPS_PROXY=$HTTPS_PROXY"
  fi
  if [ -n ${NO_PROXY+x} ]; then
    PROXY_ENV="$PROXY_ENV --engine-env NO_PROXY=$NO_PROXY"
  fi  
  "${DOCKER_MACHINE}" create -d vmwareworkstation $PROXY_ENV "${VM}"
fi

STEP="Checking status on $VM"
VM_STATUS="$(${DOCKER_MACHINE} status ${VM} 2>&1)"
if [ "${VM_STATUS}" != "Running" ]; then
  "${DOCKER_MACHINE}" start "${VM}"
  yes | "${DOCKER_MACHINE}" regenerate-certs "${VM}"
fi

STEP="Setting env"
eval "$(${DOCKER_MACHINE} env --shell=bash ${VM})"

STEP="Finalize"
clear
cat << EOF


                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/

EOF
echo -e "${BLUE}docker${NC} is configured to use the ${GREEN}${VM}${NC} machine with IP ${GREEN}$(${DOCKER_MACHINE} ip ${VM})${NC}"
echo "For help getting started, check out the docs at https://docs.docker.com"
echo
cd

docker () {
  MSYS_NO_PATHCONV=1 docker.exe "$@"
}
export -f docker

if [ $# -eq 0 ]; then
  echo "Start interactive shell"
  exec "$BASH" --login -i
else
  echo "Start shell with command"
  exec "$BASH" -c "$*"
```  
4、启动vmware workstation  
5、查看当前docker环境中的虚拟主机,在cmd命令行中输入docker-machine ls(一般能看到default,是在vitualbox中创建的)  
6、删除虚拟主机docker-machine stop default && docker-machine rm default  
7、此时即可卸载vitualbox虚拟机软件了  
8、双击打开Docker Quickstart Terminal或在cmd命令行中输入docker-machine create --driver=vmwareworkstation default 创建一个名称为default的虚拟主机  

#### bug:dazhuang_python@sina.com
