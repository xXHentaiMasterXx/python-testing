import urllib.request
from RedditUtils import RedditFinder

def download(url, folder):
    s = url.split("/")
    filename = s[len(s)-1]
    if not filename:
        print("Bad URL / Removed image, skipping %s" % url)
        return
    print("Downloading %s as %s " % (url, filename))
    try:
        urllib.request.urlretrieve(url, folder + filename)    
    except Exception:
        print("Error while downloading %s" % filename)
    print("Done.")

settings = dict()

settings["size"] = input("Insert how many images to download (even): ")
subreddit = input("Insert subreddit: ")
title = input("insert title: ")


if subreddit:
    settings["subreddit"] = subreddit
if title:
    settings["title"] = title

settings["over_18"] = "false"
finder = RedditFinder(settings)

sfw = finder.getResults()

settings["over_18"] = "true"

finder = RedditFinder(settings)

nsfw = finder.getResults()

for url in sfw:
    download(url, "download/sfw/")
for url in nsfw:
    download(url, "download/nsfw/")
