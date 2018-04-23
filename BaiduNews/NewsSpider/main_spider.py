from NewsSpider import get_html, parse_html

class MainSpider():
    def __init__(self):
        self.download = get_html.GetHtml()
        self.parse = parse_html.ParseHtml()

    def analy_payload(self):
        keyword = input("What news do you want to search?\n")
        page = 0
        payload = {
            'word': keyword,
            'pn': page,
            'cl': '2',
            'ct': '1',
            'tn': 'news',
            'rn': '20',
            'ie': 'utf-8',
            'bt': '0',
            'et': '0',
        }
        return payload

    def spider_main(self, url, params):
        html = self.download.download_html(url, params)
        title = self.parse.get_news_title(html)
        print(title)
        print(len(title))


if __name__ == '__main__':
    spider = MainSpider()
    base_url = 'http://news.baidu.com/ns'
    payload = spider.analy_payload()
    spider.spider_main(base_url, payload)