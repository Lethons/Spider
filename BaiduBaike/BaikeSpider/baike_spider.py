from BaikeSpider import html_download, parse_html, url_manager, data_save


class MainSpider():
    def __init__(self):
        self.url = url_manager.UrlManager()
        self.download = html_download.HtmlDownload()
        self.parse = parse_html.ParseHtml()
        self.save = data_save.SaveData()

    def baike_spider(self, url):
        html = self.download.download_page_html(url)
        urls = self.parse.parse_new_url(html)
        self.url.add_new_urls(urls)
        while self.url.has_new_urls():
            new_url = self.url.get_new_url()
            print(new_url)
            html = self.download.download_page_html(new_url)
            all_text = self.parse.get_page_all(html)
            self.save.save_as_json(all_text)


if __name__ == '__main__':
    keyword = input("Please input Keyword: ")
    base_url = 'https://baike.baidu.com/search/none?word=' + keyword
    spider = MainSpider()
    spider.baike_spider(base_url)
