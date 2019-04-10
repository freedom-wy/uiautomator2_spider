import json
from handle_mongo import ad_mongo
import hashlib
import urllib
import time





def response(flow):
    #qq新闻app广告api
    if 'getQQNewsUnreadList' in flow.request.url:
        data_dict = json.loads(flow.response.text)['adList']
        data_list = json.loads(data_dict)['order']
        for i in data_list:
            info = {}
            #视频广告
            if 'video_url' in i:
                info['img_url'] = [i['video_url']]
                info['ad_id'] = handle_encode_data(info['img_url'])
                info['ad_name'] = i['title']
                info['ad_luodi_url'] = i['url']
                info['api_url'] = flow.request.url
                info['ad_source_data'] = i
                info['crawl_time'] = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
                ad_mongo.insert_item_in_db('qq_news_task',info)
            #广告
            elif 'resource_url0' in i:
                info['img_url'] = [i['resource_url0']]
                info['ad_id'] = handle_encode_data(info['img_url'])
                info['ad_name'] = i['title']
                info['ad_luodi_url'] = i['url']
                info['api_url'] = flow.request.url
                info['ad_source_data'] = i
                info['crawl_time'] = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
                ad_mongo.insert_item_in_db('qq_news_task',info)
            #广告
            elif 'resource_urlList' in i:
                img_list = []
                for img in i['resource_urlList']:
                    img_list.append(img['url'])
                info['img_url'] = img_list
                info['ad_id'] = handle_encode_data(info['img_url'])
                info['ad_name'] = i['title']
                info['ad_luodi_url'] = i['url']
                info['api_url'] = flow.request.url
                info['ad_source_data'] = i
                info['crawl_time'] = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
                ad_mongo.insert_item_in_db('qq_news_task', info)


#对URL进行hash，生成广告ID
def handle_encode_data(data):
    if isinstance(data,list):
        hash_info = hashlib.md5()
        for i in data:
            hash_info.update(i.encode())
        return hash_info.hexdigest()
    else:
        hash_info = hashlib.md5()
        hash_info.update(data.encode())
        return hash_info.hexdigest()
