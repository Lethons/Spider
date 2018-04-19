from bs4 import BeautifulSoup


class ParseHtml():
    def __init__(self):
        pass

    def parse_new_url(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', class_='result-title')
        urls = set()
        for link in links:
            urls.add(link['href'])
        return urls

    def get_page_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string
        return title

    def get_page_para(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        para = soup.find('div', class_='para')
        return para.get_text()

    def get_page_index(self, html):
        index_list = []
        soup = BeautifulSoup(html, 'html.parser')
        indexs = soup.find_all('h2', class_='title-text')
        for index in indexs:
            index_list.append(index.get_text())
        return index_list

    def get_page_menu(self, html):
        menu_list = []
        soup = BeautifulSoup(html, 'html.parser')
        menus = soup.find_all('dl')
        for menu in menus:
            menu_list.append(menu.get_text())
        return menu_list

    def get_page_info(self, html):
        key_list = []
        val_list = []
        info = {}
        soup = BeautifulSoup(html, 'html.parser')
        keys = soup.find_all('dt', class_='basicInfo-item name')
        for key in keys:
            key_list.append(key.get_text())
        vals = soup.find_all('dd', class_='basicInfo-item value')
        for val in vals:
            val_list.append(val.get_text())
        for i in range(len(val_list)):
            info[key_list[i]] = val_list[i].strip('\n')
        if not info:
            return None
        return info

    def getPageText(self, html):
        title = self.get_page_title(html)
        para = self.get_page_para(html)
        info = self.get_page_info(html)
        menu = self.get_page_menu(html)
