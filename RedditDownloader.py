import urllib.request
from RedditUtils import RedditFinder

def download(url):
    s = url.split("/")
    filename = s[len(s)-1]
    print("Downloading %s as %s " % (url, filename))
    urllib.request.urlretrieve(url, "download/" + filename)    
    print("Done.")

settings = dict()

subreddit = input("Insert subreddit: ")
title = input("insert title: ")

if subreddit:
    settings["subreddit"] = subreddit
if title:
    settings["title"] = title

finder = RedditFinder(settings)

for url in finder.getResults():
    download(url)

