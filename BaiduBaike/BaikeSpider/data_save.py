import os
import json


class SaveData():
    def __init__(self):
        self.path = os.getcwd()[:-12]

    def save_as_json(self, data):
        filename = str(data['title']) + '.json'
        datapath = self.path + '/data/'
        if not os.path.exists(datapath):
            os.mkdir(datapath)
        datafile = datapath + filename
        with open(datafile, 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)