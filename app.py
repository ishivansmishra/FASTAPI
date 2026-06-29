from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news(page: int = 1, limit: int = 5):
    url = "https://news.ycombinator.com/"
    response = requests.get(url)  # ✅ pass the variable, not a hardcoded string
    soup = BeautifulSoup(response.text, "html.parser")
    titles = []

    for item in soup.find_all("span", class_="titleline"):  # ✅ correct HN class
        a_tag = item.find("a")
        if a_tag:
            titles.append(a_tag.text)

    # Pagination Logic
    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(titles),
        "data": titles[start:end]
    }