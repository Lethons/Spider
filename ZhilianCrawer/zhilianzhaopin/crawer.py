from zhilianzhaopin import getHtml, parseHtml, saveData
from zhilianzhaopin.config import POSITION, PLACE, SAVE_TO_MONGODB
from multiprocessing import Pool

class Crawer():
    def __init__(self):
        self.html = getHtml.GetHtml()
        self.parse = parseHtml
        self.save = saveData.SaveData()

    def get_baseurl(self):
        baseurl = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
        url = baseurl + 'jl=' + PLACE + '&kw=' + POSITION
        return url

    def figure_all_page(self):
        base_url = self.get_baseurl()
        html = self.html.get_html(base_url)
        parse = self.parse.ParseHtml(html)
        position_num = parse.get_positions_total()
        all_page = int(position_num)//60 + 1
        print(all_page)
        return all_page

    def crawer(self, page):
        base_url = self.get_baseurl()
        url = base_url + '&p=' + str(page)
        html = self.html.get_html(url)
        parse = self.parse.ParseHtml(html)
        print('正在爬取第%d页' % page)
        for data in parse.get_positions_text():
            if SAVE_TO_MONGODB:
                self.save.save_to_mongodb(data)
            else:
                self.save.save_to_txt(data)


def main(page):
    craw = Crawer()
    craw.crawer(page)

if __name__ == '__main__':
    pool = Pool()
    craw = Crawer()
    page_num = craw.figure_all_page()
    if SAVE_TO_MONGODB:
        pool.map(main, [i for i in range(1, page_num + 1)])
    else:
        for page in range(1, page_num+1):
            main(page)

