import uiautomator2 as u2
import time





class Handle_QQ_news(object):
    def __init__(self):
        #连接设备
        self.qq_news_device = u2.connect('S07187307509')
        #启动app
        self.qq_news_device.app_start("com.tencent.news")

    def stop_app(self):
        #退出app
        self.qq_news_device.app_stop_all()
        #清除缓存
        self.qq_news_device.app_clear("com.tencent.news")

    #获取屏幕大小
    def get_size(self):
        size = self.qq_news_device.window_size()
        return size

    def handle_slide(self):
        #左右滑动
        l = self.get_size()
        x1 = int(l[0] * 0.95)
        y1 = int(l[1] * 0.8)
        x2 = int(l[1] * 0.05)
        #判断是否进入首页
        if self.qq_news_device(resourceId = "com.tencent.news:id/main_navigation_bar").exists(timeout=20):
            #遍历三次
            for i in range(0,3):
                sum = 1
                #21个栏目
                while sum <= 21:
                    #点击三次
                    for i1 in range(0,3):
                        time.sleep(3)
                        #点击新闻按钮
                        self.qq_news_device.xpath("//android.widget.TextView[@text='新闻']").click()
                        time.sleep(3)
                    #向右滑动
                    self.qq_news_device.swipe(x1,y1,x2,y1,0.1)
                    sum = sum + 1
                while sum > 1:
                    for i2 in range(0,3):
                        time.sleep(3)
                        self.qq_news_device.xpath("//android.widget.TextView[@text='新闻']").click()
                        time.sleep(3)
                    #向左滑动
                    self.qq_news_device.swipe(x2,y1,x1,y1,0.1)
                    sum = sum - 1
                    #判断是否进入搜索页
                    if self.qq_news_device(resourceId="com.tencent.news:id/search_daily_header_title").exists(timeout=2):
                        self.qq_news_device.press("back")
                        self.qq_news_device.press("back")
                        break




#启动三次
for i in range(0,3):
    aishangtianqi = Handle_QQ_news()
    aishangtianqi.handle_slide()
    aishangtianqi.stop_app()
