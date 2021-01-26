"""Unit Test for main app"""

from fastapi.testclient import TestClient
from main import app
from reddit import RedditAPIWrapper

client = TestClient(app)


def test_reddit_news():
	reddit_wrapper = RedditAPIWrapper()
	assert reddit_wrapper.get_news('meddy')
	assert reddit_wrapper.get_news()


def test_get_news():

	list_response = client.get("/news")
	search_response = client.get("/news?q=meddy")

	assert list_response.status_code == 200
	assert search_response.status_code == 200

