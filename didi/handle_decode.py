import json
import time
from handle_mongo import mongo





#通过mitmdump解析数据
def response(flow):
    #详情页
    if 'c.rlab.net.cn/shop/index' in flow.request.url:
        result = json.loads(flow.response.text)
        if result['errmsg'] == '你操作得太频繁啦, 休息一下吧':
            mongo.save_flag('didi_flag',{'flag':1})
            return
        else:
            result_dict = result['data']
            shop_id_result = mongo.find_data('didi_waimai_data',result_dict['shopId'])
            if shop_id_result is None:
                print('未找到商店ID')
                pass
            else:
                if '_id' in shop_id_result:
                    shop_id_result.pop('_id')
                print('当前查找到的数据为:',shop_id_result)
                shop_id_result['crawl_url'] = flow.request.url
                shop_id_result['shop_logo'] = result_dict['logoImg']
                shop_id_result['shop_addr'] = result_dict['addr']
                shop_id_result['business_hours'] = result_dict['bizTime']
                shop_id_result['phone_num'] = result_dict['phone']
                # 经度
                shop_id_result['longitude'] = result_dict['lng']
                # 纬度
                shop_id_result['latitude'] = result_dict['lat']
                # 平均服务时间
                try:
                    shop_id_result['average_service_time'] = result_dict['deliveryDesc']
                except:
                    shop_id_result['average_service_time'] = '当前无服务时间'
                # 商品信息
                shop_id_result['commodity'] = result_dict['cates']
                shop_id_result['crawl_time'] = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
                mongo.insert_data('didi_waimai_data',shop_id_result)
                # print(shop_id_result)
    #列表页
    elif 'c.rlab.net.cn/feed/index' in flow.request.url:
        result = json.loads(flow.response.text)
        if result['errmsg'] == '你操作得太频繁啦, 休息一下吧':
            mongo.save_flag('didi_flag',{'flag':1})
            return
        print('开始保存列表页数据')
        for shop in result['data']['shops']['data']:
            shop_id_result = mongo.find_data('didi_waimai_data', shop['shopId'])
            if shop_id_result is None:
                info = {}
                #当前城市
                # info['city'] = ''
                info['shop_id'] = shop['shopId']
                info['shop_name'] = shop['shopName']
                try:
                    info['sale_values'] = shop['saleByMonthMists']
                except:
                    info['sale_values'] = '当前无销售数量数据'
                mongo.insert_data('didi_waimai_data',info)
            else:
                continue

    #商家说明页
    elif 'c.rlab.net.cn/shop/detail' in flow.request.url:
        result = json.loads(flow.response.text)
        if result['errmsg'] == '你操作得太频繁啦, 休息一下吧':
            mongo.save_flag('didi_flag',{'flag':1})
            return
        result_dict = result['data']
        shop_id_result = mongo.find_data('didi_waimai_data', result_dict['shopId'])
        if shop_id_result is None:
            print('未找到商店ID')
            pass
        else:
            print('查找到商店ID：', shop_id_result['shop_id'])
            try:
                shop_id_result['licenses_info'] = result_dict['licenses']
            except:
                pass
            try:
                shop_id_result['tips_info'] = result_dict['tips']
            except:
                pass
            mongo.insert_data('didi_waimai_data',shop_id_result)
