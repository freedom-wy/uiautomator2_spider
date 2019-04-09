import pymongo
from pymongo.collection import Collection

class Handle_mongo_db(object):
    def __init__(self):
        mongo_client = pymongo.MongoClient(host='10.70.120.162', port=27017)
        self.db_data = mongo_client['didi']

    def save_flag(self,collection_name,item):
        db_collections = Collection(self.db_data,collection_name)
        db_collections.update({'flag':item['flag']},item,True)

    def delete_flag(self,collection_name):
        db_collections = Collection(self.db_data,collection_name)
        return db_collections.find_one_and_delete({})

    def delete_all_flag(self):
        db_collections = Collection(self.db_data,'didi_flag')
        db_collections.remove({})



    def insert_data(self,collection_name,item):
        db_collections = Collection(self.db_data,collection_name)
        db_collections.update({'shop_id':item['shop_id']},item,True)

    def find_data(self,collection_name,item):
        db_collections = Collection(self.db_data,collection_name)
        shop_id_result = db_collections.find_one({'shop_id':item})
        return shop_id_result

mongo = Handle_mongo_db()
