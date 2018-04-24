from NewsSpider import get_html, parse_html, save_data

class MainSpider():
    def __init__(self):
        self.download = get_html.GetHtml()
        self.parse = parse_html
        self.save = save_data.SaveData()

    def analy_payload(self, keyword, page=0):
        payload = {
            'word': keyword,
            'pn': page,
            'ct': '1',
            'tn': 'news',
            'ie': 'utf-8',
            'bt': '0',
            'et': '0',
        }
        return payload

    def spider_main(self, url, params):
        global keyword
        html = self.download.download_html(url, params)
        base_parse = self.parse.ParseHtml(html)
        total = base_parse.get_news_total()
        print(total)
        pages = int(input("How many pages do you want get?\n"))
        for pn in range(pages):
            real_pn = pn + 1
            print("正在爬取第%d页" % real_pn)
            page = pn * 10
            payload = self.analy_payload(keyword, page)
            html = self.download.download_html(url, payload)
            page_parse = self.parse.ParseHtml(html)
            for data in page_parse.get_parse_all():
                self.save.save_to_txt(data)


if __name__ == '__main__':
    keyword = input("What news do you want to search?\n")
    spider = MainSpider()
    base_url = 'http://news.baidu.com/ns'
    payload = spider.analy_payload(keyword)
    spider.spider_main(base_url, payload)