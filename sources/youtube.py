import feedparser

CHANNEL_ID = "UC0Bi5KMcECRVYis5Gb_ZYZQ"

RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

def fetch():
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        return []

    posts = []

    for entry in feed.entries:
        posts.append({
            "id": entry.yt_videoid,
            "title": entry.title,
            "url": entry.link,
            "published": entry.published,
            "author": entry.author,
            "thumbnail": f"https://i.ytimg.com/vi/{entry.yt_videoid}/maxresdefault.jpg",
            "source": "YouTube"
        })

    return posts
