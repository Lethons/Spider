from bs4 import BeautifulSoup


class ParseHtml():

    def __init__(self):
        pass


    def getNewUrl(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', class_='result-title')
        urls = set()
        for link in links:
            urls.add(link['href'])
        return urls


    def getData(self, html):
        pass

