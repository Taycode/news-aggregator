"""Fast API APP"""

from fastapi import FastAPI
from services import aggregate_news

app = FastAPI()


@app.get('/news')
async def get_news(q: str = None):
	"""Endpoint for getting news"""
	return aggregate_news(q)
