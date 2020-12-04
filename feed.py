import feedparser

def main():
	feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
	for post in feed.entries:
    	print((
       		f"{post.title}\n"
        	f"{post.summary}\n"
        	#f"{post.link}\n"
    	))

if __name__ == "__main__":
    main()