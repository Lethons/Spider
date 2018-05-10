import requests


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/65.0.3325.181'}

class GetHtml():
    def __init__(self):
        pass

    def get_html(self, url):
        try:
            response = requests.get(url, headers=header)
            response.encoding = 'utf-8'
        except requests.RequestException as e:
            return e.args
        else:
            return response.text