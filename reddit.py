"""Reddit API Wrapper"""

import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
load_dotenv()


class RedditAPIWrapper(object):
	"""Reddit API Wrapper"""

	def __init__(self):
		self.client_id = os.getenv('REDDIT_CLIENT_ID')
		self.client_secret = os.getenv('REDDIT_CLIENT_SECRET')
		self.username = os.getenv('REDDIT_USERNAME')
		self.password = os.getenv('REDDIT_PASSWORD')
		self.base_url = "https://oauth.reddit.com/r/news"
		self.user_agent = os.getenv('USER_AGENT')

	def _get_access_token(self):
		"""Gets Reddit Access token"""

		auth = HTTPBasicAuth(self.client_id, self.client_secret)

		auth_data = {
			'grant_type': 'password',
			'username': self.username,
			'password': self.password
		}

		headers = {'User-Agent': self.user_agent}

		response = requests.post(
			"https://www.reddit.com/api/v1/access_token",
			auth=auth,
			data=auth_data,
			headers=headers
		).json()

		access_token = response.get('access_token')

		return access_token

	@staticmethod
	def _extract_data(data):
		data = data.get('data')

		return {
			'headline': data.get('title'),
			'link': data.get('url'),
			'source': 'reddit'
		}

	def get_news(self, query=None):
		"""Get news from reddit"""

		access_token = self._get_access_token()

		endpoint = self.base_url + '/new' if query is None else self.base_url + f'/search?q={query}'

		headers = {
			'Authorization': f'bearer {access_token}',
			'User-Agent': self.user_agent
		}

		response = requests.get(endpoint, headers=headers).json()
		articles = response.get('data').get('children')

		return list(map(self._extract_data, articles))
