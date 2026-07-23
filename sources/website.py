import requests

URL = "https://hw-media-cdn-mingchao.kurogame.com/akiwebsite/website2.0/json/G152/en/ArticleMenu.json"


def fetch():
    response = requests.get(URL)
    response.raise_for_status()

    data = response.json()

    posts = []

    # Find the list of articles in the JSON
    # (We'll verify the exact key if needed.)
    articles = data.get("data", data)

    for article in articles:
        posts.append({
            "id": str(article["articleId"]),
            "title": article["articleTitle"],
            "url": f"https://wutheringwaves.kurogames.com/en/main/news/detail/{article['articleId']}",
            "published": article["createTime"]
        })

    return posts


if __name__ == "__main__":
    posts = fetch()

    print(f"Found {len(posts)} articles\n")

    for post in posts[:5]:
        print(post)
