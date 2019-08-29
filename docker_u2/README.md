# docker_u2 
## 集成uiautomator2到docker 
### 调试手机
#### 1、首先将真实手机设备连接到本地电脑上  
#### 2、adb devices可以识别到设备后，执行python -m uiautomator2 init 进行uiautomator2初始化  
#### 3、设置vitualbox的共享文件夹  
#### 4、下载docker镜像:docker pull 450120127/imooc_python:v3
#### 5、挂载共享文件夹到docker host ：sudo mount -t vboxsf test_file /home/docker/share_file  
#### 6、创建带有Python环境的容器：docker run -it -v /home/docker/share_file:/root/ --name python 450120127/imooc_python:v3 /bin/bash
#### 7、进入相应的目录执行python文件

#### bug:dazhuang_python@sina.com
