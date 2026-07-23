import feedparser
from config import YOUTUBE_RSS


def fetch():
    feed = feedparser.parse(YOUTUBE_RSS)

    if not feed.entries:
        return []

    videos = []

    for entry in feed.entries:

        video = {
            "id": entry.yt_videoid,
            "source": "youtube",
            "type": "video",
            "title": entry.title,
            "url": entry.link,
            "thumbnail": f"https://img.youtube.com/vi/{entry.yt_videoid}/hqdefault.jpg",
            "published": entry.published,
            "author": entry.author,
        }

        videos.append(video)

    return videos
