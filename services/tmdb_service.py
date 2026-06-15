import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")


def search_movie(title: str):
    url = "https://api.themoviedb.org/3/search/movie"

    response = requests.get(
        url,
        params={
            "api_key": API_KEY,
            "query": title
        }
    )

    response.raise_for_status()
    return response.json()