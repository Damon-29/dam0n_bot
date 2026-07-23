\import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

COLORS = {
    "youtube": 0xFF0000,
    "website": 0x3498DB,
    "x": 0x000000,
}


def send_post(source, post):
    # Let Discord generate the native preview for
    # YouTube and X video posts.
    if source == "youtube" or (
        source == "x" and not post.get("thumbnail")
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

    embed = {
        "title": post["title"],
        "url": post["url"],
        "color": COLORS.get(source, 0x2F3136),
        "footer": {
            "text": f"Wuthering Waves • {source.title()}"
        }
    }

    if post.get("published"):
        embed["timestamp"] = post["published"]

    if post.get("thumbnail"):
        embed["image"] = {
            "url": post["thumbnail"]
        }

    payload = {
        "content": post["url"],
        "embeds": [embed]
    }

    response = requests.post(WEBHOOK_URL, json=payload)

    if not response.ok:
        print("Discord error:", response.status_code)
        print(response.text)

    response.raise_for_status()
