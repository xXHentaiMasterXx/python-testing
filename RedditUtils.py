import urllib.request, json 

from urllib.parse import quote

class RedditFinder:

    settings = dict()

    def __init__(self, settings):
        self.settings = settings

    def getResults(self):
        url = self.getSearchURL()
        print (url)
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        results = []
        for x in data["data"]:
            if x["is_self"] == "true": #Media only
                continue
            if x["domain"] == "reddit.com": #Exclude crossposts
                continue
            results.append(x["url"])
        return results
    
    def getFilteredResults(self, customFilter):
        url = self.getSearchURL()
        print (url)
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        results = []
        for x in data["data"]:
            for filter in customFilter.keys():
                if filter in x:
                    if x[filter] != customFilter[filter]:
                        continue
            results.append(x["url"])
        return results
    
    def getJSONResults(self):
        url = self.getSearchURL()
        print (url)
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        results = []
        for x in data["data"]:
            results.append(x)
        return results

    def getSearchURL(self):
        baseurl = "https://api.pushshift.io/reddit/submission/search?"
        for key in self.settings.keys():
            baseurl = baseurl + "&" + key + "=" + self.settings[key]
        return baseurl

