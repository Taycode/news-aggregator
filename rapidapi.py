"""Rapid API Wrapper"""
import requests
import dotenv
import os


dotenv.load_dotenv()


class RapidAPI(object):
	"""Rapid API Wrapper"""

	news_url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"

	headers = {
		'x-rapidapi-key': os.getenv('RAPID_API_KEY'),
		'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
	}

	def make_query(self, q):
		"""makes query to rapid api"""

		response = requests.get(
			self.news_url,
			headers=self.headers,
			params={'q': q}
		)

		return response.json()
