class UrlManager():
    def __init__(self):
        self.newurls = set()
        self.oldurls = set()

    def has_new_urls(self):
        return len(self.newurls) != 0

    def get_new_url(self):
        new_url = self.newurls.pop()
        self.oldurls.add(new_url)
        return new_url

    def add_new_url(self, url):
        if url:
            if url not in self.newurls and url not in self.oldurls and 'http' in url:
                self.newurls.add(url)
        else:
            return None

    def add_new_urls(self, urls):
        if urls or len(urls) != 0:
            for url in urls:
                self.add_new_url(url)
        else:
            return None
