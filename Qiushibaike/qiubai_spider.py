import requests
import json
from pyquery import PyQuery as pq
from requests.exceptions import RequestException


def get_url(page_num):
    base_url = 'https://www.qiushibaike.com/8hr/page/'
    url = base_url + str(page_num)
    return url


def get_html(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        response.encoding = 'utf-8'
        return response.text
    except RequestException:
        print("get html error")


def get_article_id(html):
    doc = pq(html)
    duanzis = doc('#content .content-block.clearfix #content-left div').items()
    for duanzi in duanzis:
        id = duanzi.attr.id
        if id:
            yield id[-9:]


def get_article_url(id):
    base_url = "https://www.qiushibaike.com/article/"
    article_url = base_url + str(id)
    return article_url


def parse_article_html(article_html):
    doc = pq(article_html)
    article = doc('#content #single-next-link div')
    author = doc('#content .author.clearfix h2')
    stats = doc('#content .stats .stats-vote i')
    return {
        'article': article.text(),
        'author': author.text(),
        'stats': stats.text(),
    }


def save_data(data):
    with open('qiubai.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')


def qiubai_spider():
    '''
    pn = input("Please input page numbers: ")
    pn = int(pn) + 1
    '''
    for page_num in range(1, 11):
        url = get_url(page_num)
        print("----------正在爬取第%d页----------" % page_num)
        html = get_html(url)
        ids = []
        for id in get_article_id(html):
            ids.append(id)
            ids = set(ids)
            ids = list(ids)
        for id in ids:
            article_url = get_article_url(id)
            article_html = get_html(article_url)
            article = parse_article_html(article_html)
            save_data(article)
    print("crawl success")


if __name__ == '__main__':
    qiubai_spider()
