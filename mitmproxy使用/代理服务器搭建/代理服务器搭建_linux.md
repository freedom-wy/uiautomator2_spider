# 代理服务器搭建 
## 在linux服务器中使用tinyproxy服务搭建代理服务器 
```bash
yum install -y epel-release
yum update
yum -y install tinyproxy
#修改Allow 127.0.0.1为自己IP,只允许自己使用,或者在Allow前面打#注释,允许任何IP都可以连接
vi /etc/tinyproxy/tinyproxy.conf
service tinyproxy restart
#chkconfig --level 345 tinyproxy on
#centos7如下设置:
systemctl restart  tinyproxy.service
systemctl enable tinyproxy.service
```  

#### bug:dazhuang_python@sina.com
