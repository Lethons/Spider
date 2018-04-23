from bs4 import BeautifulSoup


class ParseHtml():
    def __init__(self):
        pass

    def get_news_title(self, html):
        title_list = []
        soup = BeautifulSoup(html, 'lxml')
        titles = soup.find_all('h3', class_='c-title')
        for title in titles:
            title_list.append(title.find('a').get_text())
        return title_list
