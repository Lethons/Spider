from bs4 import BeautifulSoup


class ParseHtml():
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'lxml')

    def get_positions_total(self):
        total = self.soup.find('span', class_='search_yx_tj')
        sums = total.find('em').get_text()
        return sums

    def get_positions_text(self):
        message_list = []
        positions = self.soup.find_all('td', class_='zwmc')
        companys = self.soup.find_all('td', class_='gsmc')
        messages = self.soup.find_all('li', class_='newlist_deatil_two')
        details = self.soup.find_all('li', class_='newlist_deatil_last')
        for message in messages:
            span_list = []
            for span in message.find_all('span'):
                span = span.get_text()
                span = span.split('：')
                span_list.append(span)
            message_list.append(span_list)
        for i in range(len(message_list)):
            key_list = ['地点', '公司性质', '公司规模', '经验', '学历', '职位月薪']
            data_dict = {}
            data_dict['职位'] = positions[i].get_text().strip()
            data_dict['公司'] = companys[i].get_text()
            for n in message_list[i]:
                if n[0] in key_list:
                    data_dict[n[0]] = n[1]
                    key_list.remove(n[0])
            for m in key_list:
                data_dict[m] = 'None'
            data_dict['岗位职责'] = details[i].get_text().replace(' ', '')
            data_dict['链接'] = positions[i].find('a')['href']
            yield data_dict