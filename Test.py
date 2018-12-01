from RedditUtils import RedditFinder
settings = dict()
settings["subreddit"] = "animemes"
#settings["over_18"] = "true"
settings["size"] = "1000"
search = RedditFinder(settings)
print("Searching")
res = search.getResults()
print("Results: ")
for x in res:
    print(x)
print("Done")