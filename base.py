"""Base Wrapper"""

import requests


class BaseWrapper(object):
	"""Base Wrapper"""

	query_url = None
	general_url = None
	headers = dict()
	query = dict()

	@staticmethod
	def data_extractor(response):
		"""Extracts data from response"""
		return None

	def make_query(self, q=None):
		"""makes Query"""

		if q:
			self.query.update({
				'q': q
			})

		response = requests.get(
			self.query_url,
			params=self.query,
			headers=self.headers
		).json()

		if self.data_extractor(response):
			pass
		return response
