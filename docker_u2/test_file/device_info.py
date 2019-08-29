import uiautomator2 as u2


#设备连接，如果在本地，可以不写设备号
d = u2.connect('192.168.1.6')
#获取设备信息
print(d.info)