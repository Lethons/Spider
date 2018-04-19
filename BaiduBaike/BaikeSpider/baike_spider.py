from BaikeSpider import html_download, parse_html, url_manager


class BaikeSpider():

    def __init__(self):
        self.url = url_manager.UrlManager()
        self.download = html_download.HtmlDownload()
        self.parse = parse_html.ParseHtml()


    def spider(self,url):
        html = self.download.htmlDownload(url)
        urls = self.parse.getNewUrl(html)
        self.url.addNewUrls(urls)
        while self.url.hasNewUrls():
            new_url = self.url.getNewUrl()
            print(new_url)




if __name__ == '__main__':
    keyword = input("Please input Keyword: ")
    base_url = 'https://baike.baidu.com/search/none?word=' + keyword
    spider = BaikeSpider()
    spider.spider(base_url)
