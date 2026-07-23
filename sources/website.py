import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

MENU_URL = (
    "https://hw-media-cdn-mingchao.kurogame.com/"
    "akiwebsite/website2.0/json/G152/en/ArticleMenu.json"
)

DETAIL_URL = (
    "https://hw-media-cdn-mingchao.kurogame.com/"
    "akiwebsite/website2.0/json/G152/en/article/{}.json"
)

CDN_BASE = "https://hw-media-cdn-mingchao.kurogame.com/"


def get_thumbnail(article_id):
    """Fetch the first image from an article."""

    response = requests.get(DETAIL_URL.format(article_id), timeout=15)
    response.raise_for_status()

    article = response.json()

    html = article.get("articleContent", "")

    soup = BeautifulSoup(html, "html.parser")

    img = soup.find("img")

    if not img:
        return None

    src = img.get("src", "").strip()

    # Handle URLs like //cdn...
    if src.startswith("//"):
        src = "https:" + src

    # Handle relative URLs like /images/...
    elif src.startswith("/"):
        src = urljoin(CDN_BASE, src)

    # Debug (remove later if you want)
    print("Website thumbnail:", src)

    return src


def fetch():
    response = requests.get(MENU_URL, timeout=15)
    response.raise_for_status()

    articles = response.json()

    articles.sort(key=lambda x: x["startTime"])

    posts = []

    for article in articles:
        posts.append(
            {
                "id": str(article["articleId"]),
                "article_id": article["articleId"],
                "title": article["articleTitle"],
                "url": (
                    "https://wutheringwaves.kurogames.com/"
                    f"en/main/news/detail/{article['articleId']}"
                ),
                "published": article["startTime"],
                "thumbnail": None,
            }
        )

    return posts


if __name__ == "__main__":
    posts = fetch()

    print(f"Found {len(posts)} articles\n")

    newest = posts[-1]

    thumb = get_thumbnail(newest["article_id"])

    print(newest["title"])
    print(thumb)
