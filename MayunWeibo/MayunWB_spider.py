import requests
import json
from urllib.parse import urlencode
from pyquery import PyQuery as pq


base_url = 'https://m.weibo.cn/api/container/getIndex?'


def get_page(page):
    if page > 1:
        params = {
            'display': '0',
            'retcode': '6102',
            'type': 'uid',
            'value': '2145291155',
            'containerid': '1076032145291155',
            'page': page,
        }
    else:
        params = {
            'display': '0',
            'retcode': '6102',
            'type': 'uid',
            'value': '2145291155',
            'containerid': '1076032145291155',
        }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print("Requests Error", e.args)


def parse_page(html):
    text = json.loads(html)
    data = text.get('data')
    cards = data.get('cards')
    for card in cards:
        item = card.get('mblog')
        weibo = {}
        weibo['id'] = item.get('id')
        weibo['text'] = pq(item.get('text')).text()
        weibo['attitudes'] = item.get('attitudes_count')
        weibo['comments'] = item.get('comments_count')
        weibo['reposts'] = item.get('reposts_count')
        print(weibo)
        print('-' * 80)
        yield weibo


def save_data(data):
    with open('mayunweibo.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')


def main():
    for page in range(1, 17):
        print(page)
        html = get_page(page)
        for data in parse_page(html):
            save_data(data)


if __name__ == '__main__':
    main()
