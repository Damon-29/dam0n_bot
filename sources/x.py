from datetime import datetime

from sources.x_client import XClient


def _best_video_url(media):
    """
    Return the highest bitrate MP4 if this media is a video.
    """
    if media.get("type") != "video":
        return None

    variants = media.get("video_info", {}).get("variants", [])

    mp4s = [
        v
        for v in variants
        if v.get("content_type") == "video/mp4"
    ]

    if not mp4s:
        return None

    mp4s.sort(key=lambda x: x.get("bitrate", 0), reverse=True)

    return mp4s[0]["url"]


def _extract_media(tweet):
    media_urls = []

    media = (
        tweet.get("legacy", {})
        .get("extended_entities", {})
        .get("media", [])
    )

    for item in media:
        media_type = item.get("type")

        if media_type == "photo":
            media_urls.append(item["media_url_https"])

        elif media_type == "video":
            url = _best_video_url(item)
            if url:
                media_urls.append(url)

        elif media_type == "animated_gif":
            url = _best_video_url(item)
            if url:
                media_urls.append(url)

    return media_urls


def _get_thumbnail(tweet):
    """
    Returns the first photo in the tweet (if any).
    Videos return None since Discord previews them automatically.
    """
    media = (
        tweet.get("legacy", {})
        .get("extended_entities", {})
        .get("media", [])
    )

    for item in media:
        if item.get("type") == "photo":
            return item["media_url_https"]

    return None


def _format_timestamp(twitter_time):
    """
    Convert:
    Thu Jul 23 03:00:01 +0000 2026

    to:

    2026-07-23T03:00:01+00:00
    """
    dt = datetime.strptime(
        twitter_time,
        "%a %b %d %H:%M:%S %z %Y"
    )

    return dt.isoformat()


def fetch_x(screen_name="Wuthering_Waves"):
    client = XClient()

    client.activate_guest()

    user_id = client.get_user_id(screen_name)

    timeline = client.get_user_tweets(user_id)

    instructions = (
        timeline["data"]["user"]["result"]["timeline"]["timeline"]["instructions"]
    )

    posts = []

    for instruction in instructions:

        # Skip pinned tweet
        if instruction.get("type") == "TimelinePinEntry":
            continue

        entries = instruction.get("entries", [])

        for entry in entries:

            try:
                tweet = (
                    entry["content"]
                    ["itemContent"]
                    ["tweet_results"]
                    ["result"]
                )

                legacy = tweet["legacy"]

                # Ignore retweets
                if legacy["full_text"].startswith("RT @"):
                    continue

                tweet_id = legacy["id_str"]

                posts.append(
                    {
                        "id": tweet_id,
                        "title": legacy["full_text"],
                        "url": f"https://x.com/{screen_name}/status/{tweet_id}",
                        "published": _format_timestamp(
                            legacy["created_at"]
                        ),
                        "thumbnail": _get_thumbnail(tweet),
                        "media": _extract_media(tweet),
                    }
                )

            except KeyError:
                continue

    return posts
