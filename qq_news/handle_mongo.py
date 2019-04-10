import pymongo
from pymongo.collection import Collection


class Handle_ad_to_mongo(object):
    def __init__(self):
        mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db_data = mongo_client['ad_data']

    def insert_item_in_db(self, collection_name, item):
        print('当前保存的item为%s:' % item)
        db_collections = Collection(self.db_data, collection_name)
        db_collections.update({'ad_id':item['ad_id']},item,True)


ad_mongo = Handle_ad_to_mongo()
