class UrlManager():

    def __init__(self):
        self.newurls = set()
        self.oldurls = set()


    def hasNewUrls(self):
        return  len(self.newurls) != 0


    def getNewUrl(self):
        new_url = self.newurls.pop()
        self.oldurls.add(new_url)
        return new_url


    def addNewUrl(self, url):
        if url:
            if url not in self.newurls and url not in self.oldurls and 'http' in url:
                self.newurls.add(url)
        else:
            return None


    def addNewUrls(self, urls):
        if  urls or len(urls) != 0:
            for url in urls:
                self.addNewUrl(url)
        else:
            return None