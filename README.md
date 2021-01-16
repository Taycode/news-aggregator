# News API Aggregator

This is a news api built upon News API and Reddit API

To run the application, you need to install the dependencies first. 

Taking a Linux environment as our point of reference, first you need to clone this repo.

```git clone https://github.com/Taycode/news-aggregator.git```

then you navigate to the folder 

```bash
cd news-aggregator
```

then you have to set up a python virtual environment

```bash
python3 -m venv env

source env/bin/activate
```

Now we should have our python virtual environment set up, 
we need to install all the dependencies needed to run the app

```bash
pip install -r requirements.txt
```

now we have all the requirements installed. The Reddit and News API were accessed
using several credentials, an example is in `sample.env`

Now you are to create a new file `.env` and duplicate what we have in `sample.env` but this time
fill in the correct credentials

After setting the right credentials in `.env`

you can now run the FastAPI APP

```bash
uvicorn main:app --reload
```

Now we are going to have the server running on `localhost:8000`

to get the `list` of news you make a `GET` request to `/news` 

to `search` for news based on a query, make a `GET` request to `/news` by filling your 
query into a parameter `q`

```
/news?q=eminem
```

I hope you enjoyed this

Thank you 

Tairu
