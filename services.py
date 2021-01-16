"""Services or Utilities for News Aggregator API"""

from news import NewsAPIWrapper
from reddit import RedditAPIWrapper


def aggregate_news(q=None):
	"""This aggregates news from both APIs"""

	news_api = NewsAPIWrapper()
	reddit_api = RedditAPIWrapper()

	news_from_news_api = news_api.query_everything(q) if q else news_api.get_general_headlines()
	news_from_reddit_api = reddit_api.get_news(q)

	return [*news_from_news_api, *news_from_reddit_api]
