import requests
from bs4 import BeautifulSoup

MENU_URL = (
    "https://hw-media-cdn-mingchao.kurogame.com/"
    "akiwebsite/website2.0/json/G152/en/ArticleMenu.json"
)

DETAIL_URL = (
    "https://hw-media-cdn-mingchao.kurogame.com/"
    "akiwebsite/website2.0/json/G152/en/article/{}.json"
)


def get_thumbnail(article_id):
    """Fetch the first image from an article."""

    response = requests.get(DETAIL_URL.format(article_id), timeout=15)
    response.raise_for_status()

    article = response.json()

    html = article.get("articleContent", "")

    soup = BeautifulSoup(html, "html.parser")

    img = soup.find("img")

    return img["src"] if img else None


def fetch():
    response = requests.get(MENU_URL, timeout=15)
    response.raise_for_status()

    articles = response.json()

    articles.sort(key=lambda x: x["startTime"])

    posts = []

    for article in articles:
        posts.append({
            "id": str(article["articleId"]),
            "article_id": article["articleId"],   # Needed later
            "title": article["articleTitle"],
            "url": f"https://wutheringwaves.kurogames.com/en/main/news/detail/{article['articleId']}",
            "published": article["startTime"],
            "thumbnail": None
        })

    return posts


if __name__ == "__main__":
    posts = fetch()

    print(f"Found {len(posts)} articles\n")

    # Demo: fetch thumbnail for the newest article only
    newest = posts[-1]

    thumb = get_thumbnail(newest["article_id"])

    print(newest["title"])
    print(thumb)
