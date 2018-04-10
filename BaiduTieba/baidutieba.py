import requests
import re
import json
from requests.exceptions import RequestException


def get_url(page_numbers):
    base_url = "http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="
    pn = page_numbers * 50
    url = base_url + str(pn)
    return url


def get_one_page(url):
    try:
        re = requests.get(url)
        re.encoding = 'utf-8'
        print(re.status_code)
        return re.text
    except RequestException:
        print("Request Error")
        return None


def parse_html(html):
    pattern = re.compile(
        'target="_blank" class="j_th_tit ">(.*?)</a>.*? title="主题作者: (.*?)"'
        + '.*?title="创建时间">(.*?)</span>.*?<div class="threadlist_abs '
        + 'threadlist_abs_onlyline ">(.*?)</div>', re.S)
    items = re.findall(pattern, html)
    if items:
        for item in items[1:]:
            yield{
                'title': item[0],
                'author': item[1],
                'date': item[2],
                'text': item[3].strip(),
            }
    else:
        print("Re Error")


def save_data(content):
    with open('tiebadata.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    pages = input("Please input how many pages do you want get: ")
    pages = int(pages)
    for pn in range(pages):
        url = get_url(pn)
        html = get_one_page(url)
        for item in parse_html(html):
            save_data(item)
    print("Crawl Success")


if __name__ == '__main__':
    main()
