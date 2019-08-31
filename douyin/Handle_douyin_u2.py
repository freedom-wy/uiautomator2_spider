#email:dazhuang_python@sina.com
#time:20190414

import uiautomator2 as u2
import time


#使用uiautomator2抓取抖音粉丝数据
#1、uiautomator2模块的安装
    # pip install --upgrade --pre uiautomator2
    # pip install pillow
#2、weditor模块的安装,作用同uiautomator viewer
    #pip install -U weditor
#3、初始化手机agent
    #python -m uiautomator2 init

class Handle_douyin(object):
    """
    使用uiautomator2模拟滑动抖音app,由于抖音app版本更新，修改了控件元素ID等值
    修复部分bug
    """
    #初始化设备
    def __init__(self):
        #连接手机
        self.d = u2.connect("MBC6OBPJSSG6IJSW")
        #启动抖音app
        self.d.app_start("com.ss.android.ugc.aweme")

    #获取手机显示尺寸
    def get_size(self):
        size = self.d.window_size()
        return size

    #滑动逻辑
    def handle_swipe(self):
        #点击搜索
        # if self.d(resourceId="com.ss.android.ugc.aweme:id/aft").exists(timeout=10):
        #     self.d(resourceId="com.ss.android.ugc.aweme:id/aft").click()
        if self.d(resourceId="com.ss.android.ugc.aweme:id/ah1").exists(timeout=10):
            self.d(resourceId="com.ss.android.ugc.aweme:id/ah1").click()
        #定位到搜索框
        # if self.d(resourceId="com.ss.android.ugc.aweme:id/jt").exists(timeout=10):
        #     self.d(resourceId="com.ss.android.ugc.aweme:id/jt").click()
        if self.d(resourceId="com.ss.android.ugc.aweme:id/ci6").exists(timeout=10):
            self.d(resourceId="com.ss.android.ugc.aweme:id/ci6").click()
            time.sleep(1)
        #发送要搜索的id
        self.d.send_keys("191433445", clear=True)
        # self.d(resourceId="com.ss.android.ugc.aweme:id/ci6").set_text("191433445")
        # while self.d(resourceId="com.ss.android.ugc.aweme:id/ci6").get_text() != "191433445":
        #     self.d(resourceId="com.ss.android.ugc.aweme:id/ci6").set_text("191433445")
        #     time.sleep(1)
        #点击搜索
        # self.d(resourceId="com.ss.android.ugc.aweme:id/a8w").click()
        self.d(resourceId="com.ss.android.ugc.aweme:id/dq8").click()
        #点击用户标签
        if self.d(resourceId="android:id/text1", text=u"用户").exists(timeout=10):
            self.d(resourceId="android:id/text1", text=u"用户").click()
            time.sleep(1)
        #点击明星头像,使用坐标点击
        self.d.click(0.104, 0.211)
        #点击粉丝标签
        if self.d(text=u"粉丝").exists(timeout=10):
            self.d(text=u"粉丝").click()

        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.15)
        while True:
            self.d.swipe(x1, y1, x1, y2)
            time.sleep(0.2)

if __name__ == '__main__':
    douyin = Handle_douyin()
    douyin.handle_swipe()
