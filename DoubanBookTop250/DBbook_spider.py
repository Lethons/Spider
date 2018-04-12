import requests
import json
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


base_url = 'https://book.douban.com/top250?start='

headrs = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
    + '(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}


def get_url():
    for i in range(10):
        page = i * 25
        url = base_url + str(page)
        yield url


def get_html(url):
    try:
        response = requests.get(url, headrs)
        print(response.status_code)
        response.encoding = 'utf-8'
        return response.text
    except RequestException:
        print("Get Html Error!")


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    books = soup.select('.pl2 a')
    publishs = soup.select('.pl')
    rating = soup.select('.rating_nums')
    eva = soup.select('.star.clearfix .pl')
    quotes = soup.select('.inq')
    for i in range(len(quotes)):
        yield {
            'book': books[i].get_text().replace(' ', '').replace('\n', ''),
            'publish': publishs[i].get_text().replace(' ', ''),
            'rating': rating[i].get_text(),
            'evaluation': eva[i].get_text().replace(' ', '').replace('\n', ''),
            'quote': quotes[i].get_text(),
        }


def save_data(book):
    with open('book_top250.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(book, ensure_ascii=False) + '\n')


def main():
    count = 1
    for url in get_url():
        print("----------正在爬取第%d页----------" % count)
        html = get_html(url)
        for book in parse_html(html):
            save_data(book)
        count += 1
    print("crawl success!")


if __name__ == '__main__':
    main()
