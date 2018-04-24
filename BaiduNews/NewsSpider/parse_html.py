import re
from bs4 import BeautifulSoup


class ParseHtml():
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'lxml')

    def get_news_total(self):
        total = self.soup.find('span', class_='nums').get_text()
        pattern = re.compile('找.*?闻(.*?)篇')
        nums = re.match(pattern, total).groups()
        return nums[0]

    def get_news_title(self):
        title_list = []
        titles = self.soup.find_all('h3', class_='c-title')
        for title in titles:
            title_list.append(title.find('a').get_text())
        return title_list

    def get_news_author(self):
        author_list = []
        authors = self.soup.find_all('p', class_='c-author')
        for author in authors:
            author_list.append(author.get_text().replace('\xa0', ' '))
        return author_list

    def get_news_summary(self):
        summary_list = []
        summarys = self.soup.find_all('div', class_='c-summary')
        for summary in summarys:
            summary_list.append(summary.get_text().replace('\xa0', ' '))
        return summary_list

    def get_news_href(self):
        href_list = []
        hrefs = self.soup.find_all('a', class_='c-cache')
        for href in hrefs:
            href_list.append(href['href'])
        return href_list

    def get_parse_all(self):
        titles = self.get_news_title()
        summarys = self.get_news_summary()
        hrefs = self.get_news_href()
        for i in range(len(titles)):
            yield {
                '标题': titles[i],
                '简介': summarys[i],
                '链接': hrefs[i],
                }
