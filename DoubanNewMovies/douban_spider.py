import json
import requests
import pymongo
from bs4 import BeautifulSoup
from config import *


client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


headrs = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/59.0'
}


def get_html(url):
    '''得到页面HTML'''
    try:
        response = requests.get(url, headrs)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
    except requests.RequestException as e:
        print("request error!!!", e.args)


def parse_html(html):
    '''解析HTML得到想要的信息'''
    soup = BeautifulSoup(html, 'lxml')
    names = soup.select('.pl2 a')
    actors = soup.select('.pl2 p')
    rates = soup.select('.rating_nums')
    comments = soup.select('.star.clearfix .pl')
    for index in range(len(names)):
        yield {
            'index': index + 1,
            'name': names[index].get_text().replace(' ', '').replace('\n', ''),
            'stars': actors[index].get_text().replace(' ', ''),
            'rate': rates[index].get_text(),
            'comment_nums': comments[index].get_text().replace('(', '').replace(')', ''),
            }


def save_data_file(data):
    '''将数据保存到文件中'''
    with open('DoubanNewMovies.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')


def save_data_mongo(data):
    if db[MONGO_TABLE].insert(data):
        print('存储到MongoDB成功！！！', data)
        return True
    else:
        return False



def main():
    url = 'https://movie.douban.com/chart'
    html = get_html(url)
    for data in parse_html(html):
        save_data_file(data)
        save_data_mongo(data)


if __name__ == '__main__':
    main()

