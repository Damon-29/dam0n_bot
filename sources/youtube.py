import feedparser


def get_latest_video(feed_url):
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        return None

    latest = feed.entries[0]

    return {
        "id": latest.id,
        "title": latest.title,
        "link": latest.link,
        "published": latest.published
    }
