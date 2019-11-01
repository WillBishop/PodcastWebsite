from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import os
import datetime
wpUrl='yourwebsite/xmlrpc.php' 
#WordPress Username
wpUserName='your_username'
#WordPress Password
wpPassword='your_passowrd'

client = Client(wpUrl, wpUserName, wpPassword)
def get_posts():
	return client.call(posts.GetPosts())

def post(title, content, audioUrl, publishDate, explicit = False):
	post = WordPressPost()
	post.title = title
	post.content = content
	post.id = client.call(posts.NewPost(post))
	date = datetime.datetime.strptime(publishDate, '%a, %d %b %Y %H:%M:%S %Z')
	post.date = date
	post.custom_fields = []
	post.custom_fields.append({
		'key': 'audio_file',
		'value': audioUrl

	})
	post.custom_fields.append({
		'key': 'block',
		'value': ""
	})
	post.custom_fields.append({
		'key': 'date_recorded',
		'value': date.strftime("%d-%m-%Y")
	})
	post.custom_fields.append({
			'key': 'date_published',
			'value': date
	})
	post.custom_fields.append({
		'key': 'episode_type',
		'value': "audio"
	})
	post.custom_fields.append({
		'key': 'explicit',
		'value': ""
	})

	post.post_status = 'publish'
	client.call(posts.EditPost(post.id, post))
