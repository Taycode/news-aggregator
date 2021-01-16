"""Unit Test for main app"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_news():
	list_response = client.get("/news")
	search_response = client.get("/news?q=meddy")
	assert list_response.status_code == 200
	assert search_response.status_code == 200
