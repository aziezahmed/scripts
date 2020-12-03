import feedparser
feed = feedparser.parse("RSS_FEED_URL")
for post in feed.entries:
    print((
        f"{post.title}\n"
        f"{post.summary}\n"
        #f"{post.link}\n"
    ))
