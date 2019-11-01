import wordpress
import feedparser

feed = feedparser.parse("yourfeedurl")
existing_episodes = [post.title for post in wordpress.get_posts()]
for episode in feed["entries"]:
		title = episode["title"]		
		if title not in existing_episodes:
		  link = next(x for x in episode["links"] if x["rel"] == "enclosure")["href"]
		  wordpress.post(episode["title"], episode["summary"], link, episode["published"])
