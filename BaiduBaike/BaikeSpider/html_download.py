import requests


header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}


class HtmlDownload():

    def htmlDownload(self, url):
        if not url:
            return None
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code != 200:
            print(response.status_code)
            return None
        response.encoding = 'utf-8'
        return response.text