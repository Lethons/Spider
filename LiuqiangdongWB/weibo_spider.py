import requests
import json
import re
import os
from urllib.parse import urlencode
from time import sleep


def get_page_url(page):
    '''得到微博每个页面的url'''
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    if page < 2:
        params = {
            'display': '0',
            'retcode': '6102',
            'type': 'uid',
            'value': '1866402485',
            'containerid': '1076031866402485',
        }
    else:
        params = {
            'display': '0',
            'retcode': '6102',
            'type': 'uid',
            'value': '1866402485',
            'containerid': '1076031866402485',
            'page': str(page)
        }
    url = base_url + urlencode(params)
    return url


def get_page_text(url):
    '''得到当前页面所有微博的信息'''
    headrs = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
        + '(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    }
    try:
        response = requests.get(url, headrs)
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
    except requests.RequestException as e:
        print("Requests Error", e.args)


def get_weibo_scheme(text):
    '''从文本解析出每条微博的url'''
    json_text = json.loads(text)
    cards = json_text.get('data').get('cards')
    for card in cards:
        yield {
            'scheme': card.get('scheme'),
            'id': card.get('itemid')[-16:],
        }


def get_weibo_data(id):
    '''得到微博各项数据'''
    if id:
        base_wb_url = 'https://m.weibo.cn/statuses/extend?id='
        wb_url = base_wb_url + id
        text = get_page_text(wb_url)
        json_text = json.loads(text)
        data = json_text.get('data')
        return {
            'weibo': data.get('longTextContent'),
            'attitudes': data.get('attitudes_count'),
            'comments': data.get('comments_count'),
            'reposts': data.get('reposts_count'),
        }
    else:
        print("id = None")


def get_pictures_url(scheme):
    '''得到微博图片的地址'''
    if scheme:
        html = get_page_text(scheme)
        pattern = re.compile('"url": "(.*?)",')
        pic_urls = re.findall(pattern, html)
        for pic_url in pic_urls:
            yield pic_url
    else:
        print("scheme = None")


def save_weibo_data(data):
    '''保存爬取的微博信息'''
    if data:
        with open('liuqiangdong.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
    else:
        print("NO DATA!!!")


def save_picture(pic_url, count):
    '''保存微博图片'''
    if pic_url:
        root = 'pictures//' + str(count) + '//'
        pic_name = pic_url.split('/')[-1][:-4]
        if not os.path.exists(root):
            os.mkdir(root)
        path = root + pic_name + '.jpg'
        if not os.path.exists(path):
            response = requests.get(pic_url)
            if response.status_code == 200:
                print("正在爬取图片： %s" % pic_name)
                with open(path, 'wb') as f:
                    f.write(response.content)
            else:
                print(response.status_code)
        else:
            print("文件已存在！")
    else:
        print("NO pic_url!!!")


def main():
    count = 0
    page = 1
    while page < 52:
        print("----------正在爬取第%d页----------" % page)
        url = get_page_url(page)
        text = get_page_text(url)
        for scheme in get_weibo_scheme(text):
            sleep(1)
            count += 1
            print('\n')
            print('正在爬取第%d篇微博' % count)
            print('\n')
            data = get_weibo_data(scheme['id'])
            save_weibo_data(data)
            try:
                for pic_url in get_pictures_url(scheme['scheme']):
                    save_picture(pic_url, count)
            except:
                print("图片爬取失败")
        page += 1
        sleep(1)

    print("***************爬取完成***************")


if __name__ == '__main__':
    main()
