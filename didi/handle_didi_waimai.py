import time
from handle_mongo import mongo
import uiautomator2 as u2




#启动前先删除flag
mongo.delete_all_flag()
#连接手机
device = u2.connect('127.0.0.1:62001')
#启动app
sess = device.session('com.xiaojukeji.didi.customer')
#点击销量
sess.xpath("//android.widget.TextView[@text='销量']").click()
#循环点击
while True:
    #已滑动到结束
    if sess.xpath("//android.widget.TextView[@text='更多商家入驻中^_^']").exists:
        print('结尾')
        break
    try:
        #判断是否操作过快
        flag = mongo.delete_flag('didi_flag')['flag']
        if flag == 1:
            print('操作过快')
            time.sleep(300)
            mongo.delete_all_flag()
            sess.press("back")
    except Exception as e:
        pass
    # 获取当前页面item条目数
    count_value = sess(resourceId="com.xiaojukeji.didi.customer:id/tv_business_name").count
    for i in range(2,int(count_value)-1):
        #点击条目
        try:
            sess(resourceId="com.xiaojukeji.didi.customer:id/tv_business_name",instance=i).click(timeout=5)
            print('执行列表页点击')
            time.sleep(1)
            try:
                flag = mongo.delete_flag('didi_flag')['flag']
                if flag == 1:
                    print('操作过快')
                    time.sleep(300)
                    mongo.delete_all_flag()
            except:
                pass
                    # sess.press("back")
        except Exception as e:
            print('未执行列表页点击',e)
            if sess(resourceId="com.xiaojukeji.didi.customer:id/iv_business_back").exists:
                #点击返回
                print('正常返回')
                time.sleep(2)
                sess.press("back")
            continue
        else:
            try:
                sess(resourceId="com.xiaojukeji.didi.customer:id/tv_business_name").click(timeout=5)
                print('执行商家信息点击')
                time.sleep(1)
                try:
                    flag = mongo.delete_flag('didi_flag')['flag']
                    if flag == 1:
                        print('操作过快')
                        time.sleep(300)
                        mongo.delete_all_flag()
                except:
                    pass
            except Exception as e:
                print('未执行商家信息点击', e)
                if sess(resourceId="com.xiaojukeji.didi.customer:id/iv_close").exists:
                    # 点击返回
                    print('正常返回')
                    time.sleep(2)
                    sess.press("back")
                    time.sleep(1)
                    sess.press("back")
                continue

        print('执行判断')
        try:
            if sess.xpath("//android.widget.EditText[@text='输入商家或商品名称']").exists:
                time.sleep(1)
                sess.press("back")
            if sess.xpath("//android.widget.TextView[@text='休息中']").exists:
                time.sleep(5)
            if sess.xpath("//android.widget.TextView[@text='骑手繁忙，暂停配送']").exists:
                time.sleep(5)
            #判断是否有返回按钮
            if sess(resourceId="com.xiaojukeji.didi.customer:id/iv_business_back").exists:
                #点击返回
                print('正常返回')
                time.sleep(2)
                sess.press("back")
            #判断是否点击到地址选择页面
            if sess.xpath("//android.widget.TextView[@text='送到']").exists:
                time.sleep(1)
                sess.press("back")
        except:
            print('准备返回')
            time.sleep(2)
            sess.press("back")
            time.sleep(1)
            sess.press("back")
        else:
            print('准备返回')
            time.sleep(2)
            sess.press("back")
            time.sleep(1)
            sess.press("back")


    #滑动
    time.sleep(2)
    x1 = int(480 * 0.5)
    y1 = int(853 * 0.75)
    y2 = int(853 * 0.25)
    print('滑动')
    sess.swipe(x1, y1, x1, y2)
