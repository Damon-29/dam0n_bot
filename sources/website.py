import requests

URL = "https://hw-media-cdn-mingchao.kurogame.com/akiwebsite/website2.0/json/G152/en/ArticleMenu.json"


def fetch():
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    # Convert the JSON response into a Python list
    articles = response.json()

    # Sort oldest -> newest
    articles.sort(key=lambda x: x["startTime"])

    posts = []

    for article in articles:
        posts.append({
            "id": str(article["articleId"]),
            "title": article["articleTitle"],
            "url": f"https://wutheringwaves.kurogames.com/en/main/news/detail/{article['articleId']}",
            "published": article["startTime"]
        })

    return posts


if __name__ == "__main__":
    posts = fetch()

    print(f"Found {len(posts)} articles\n")

    for post in posts[:5]:
        print(post)
