from BaikeSpider import html_download, parse_html, url_manager


class MainSpider():
    def __init__(self):
        self.url = url_manager.UrlManager()
        self.download = html_download.HtmlDownload()
        self.parse = parse_html.ParseHtml()

    def spider(self, url):
        html = self.download.download_page_html(url)
        urls = self.parse.parse_new_url(html)
        self.url.add_new_urls(urls)
        while self.url.has_new_urls():
            new_url = self.url.get_new_url()
            html = self.download.download_page_html(new_url)
            title = self.parse.get_page_title(html)
            para = self.parse.get_page_para(html)
            print(title)
            print(para.strip())
            for index in self.parse.get_page_index(html):
                print(index)
            info = self.parse.get_page_info(html)
            print(info)
            print('-' * 80)


if __name__ == '__main__':
    keyword = input("Please input Keyword: ")
    base_url = 'https://baike.baidu.com/search/none?word=' + keyword
    spider = MainSpider()
    spider.spider(base_url)
