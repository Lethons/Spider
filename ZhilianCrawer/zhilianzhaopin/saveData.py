from zhilianzhaopin.config import MONGO_DB, MONGO_TABLE, MONGO_URL
import pymongo
import json


client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


class SaveData():
    def __init__(self):
        self.txt = 'data.txt'

    def save_to_mongodb(self,data):
        if db[MONGO_TABLE].insert(data):
            print('存储到MongoDB成功', data)

    def save_to_txt(self, data):
        with open(self.txt, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4) + '\n')
