"""News API Wrapper"""

import requests
import os
from dotenv import load_dotenv
load_dotenv()


class NewsAPIWrapper(object):
	"""News API Wrapper"""

	def __init__(self):
		self.params = {
			'apiKey': os.getenv('NEWS_API_KEY')
		}

		base_url = 'https://newsapi.org/v2'

		self.everything_url = base_url + '/everything'

		self.headline_url = base_url + '/top-headlines'

	@staticmethod
	def _extract_data(data):
		"""Extracts and format data"""
		return {
			'headline': data.get('title'),
			'link': data.get('url'),
			'source': 'newsapi'
		}

	def get_general_headlines(self):
		"""Method for getting top headlines"""

		self.params.update({
			'category': 'general'
		})
		response = requests.get(self.headline_url, params=self.params).json()
		articles = response.get('articles')
		return list(map(self._extract_data, articles))

	def query_everything(self, query):
		"""Method for querying everything"""

		self.params.update({
			'q': query
		})
		response = requests.get(self.everything_url, params=self.params).json()
		articles = response.get('articles')
		return list(map(self._extract_data, articles))
