from bs4 import BeautifulSoup
from lxml import etree


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
        return para.get_text().strip()

    def get_page_index(self, html):
        index_list = []
        soup = BeautifulSoup(html, 'html.parser')
        indexs = soup.find_all('h2', class_='title-text')
        for index in indexs:
            index_list.append(index.get_text())
        return index_list

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

    def get_page_text(self, html):
        text_list = []
        page = etree.HTML(html)
        page_data = page.xpath('//div[@class="main-content"]/div[starts-with(@class,"para")]/text()')
        for text in page_data:
            if '\n' in text and text not in text_list:
                text_list.append(text)
            else:
                text_list[-1] = text_list[-1] + '\n' + text
        for text in text_list:
            if text.strip() == '':
                text_list.remove(text)
        return text_list

    def get_page_all(self,html):
        text_dict = {}
        title = self.get_page_title(html)
        para = self.get_page_para(html)
        info_dict = self.get_page_info(html)
        index_list = self.get_page_index(html)
        text_list = self.get_page_text(html)
        for i in range(len(index_list)):
            text_dict[index_list[i]] = text_list[i].strip('\n')
        return {
            'title': title,
            'para': para,
            'info': info_dict,
            'text': text_dict,
        }
