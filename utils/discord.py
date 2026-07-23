import json
import os

import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

COLORS = {
    "youtube": 0xFF0000,
    "website": 0x3498DB,
    "x": 0x000000,
}


def send_post(source, post):
    # Native Discord preview for YouTube
    # and X posts containing videos/GIFs.
    if source == "youtube" or (
        source == "x" and post.get("has_video")
    ):
        payload = {
            "content": post["url"]
        }

        response = requests.post(WEBHOOK_URL, json=payload)

        if not response.ok:
            print("Discord error:", response.status_code)
            print(response.text)

        response.raise_for_status()
        return

    # Build custom embed
    embed = {
        "title": post["title"][:256],
        "url": post["url"],
        "color": COLORS.get(source, 0x2F3136),
        "footer": {
            "text": f"Wuthering Waves • {source.title()}"
        }
    }

    # Discord expects ISO 8601 timestamps
    if post.get("published"):
        embed["timestamp"] = post["published"]

    # Website & X photo thumbnails
    if post.get("thumbnail"):
        embed["image"] = {
            "url": str(post["thumbnail"])
        }

    payload = {
        "content": post["url"],
        "embeds": [embed]
    }

    response = requests.post(WEBHOOK_URL, json=payload)

    if not response.ok:
        print("\n===== DISCORD ERROR =====")
        print("Status:", response.status_code)
        print("Response:", response.text)
        print("Payload:")
        print(json.dumps(payload, indent=2))

    response.raise_for_status()
