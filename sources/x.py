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

                tweet_id = legacy["id_str"]

                # Ignore retweets
                if legacy["full_text"].startswith("RT @"):
                    continue

                posts.append(
                    {
                        "id": tweet_id,
                        "title": legacy["full_text"],
                        "url": f"https://x.com/{screen_name}/status/{tweet_id}",
                        "published": legacy["created_at"],
                        "media": _extract_media(tweet),
                    }
                )

            except KeyError:
                continue

    return posts
