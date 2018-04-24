import json
import os


class SaveData():
    def __init__(self):
        self.path = os.getcwd()[:-11]
        self.filename = 'news.txt'

    def save_to_txt(self,data):
        datapath = self.path + '/data/'
        if not os.path.exists(datapath):
            os.mkdir(datapath)
        datafile = datapath + self.filename
        with open(datafile, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4) + '\n')