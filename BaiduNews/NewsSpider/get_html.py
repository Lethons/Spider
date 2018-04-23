import requests


header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}


class GetHtml():
    def __init__(self):
        pass

    def download_html(self, url, params=None):
        html = requests.get(url, params, headers=header)
        if html.status_code == 200:
            return html.text
        else:
            print(html.status_code)