import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

COLORS = {
    "youtube": 0xFF0000,   # Red
    "website": 0x3498DB,   # Blue
    "x": 0x000000          # Black
}


def send_post(source, post):
    embed = {
        "title": post["title"],
        "url": post["url"],
        "color": COLORS.get(source, 0x2F3136),
        "footer": {
            "text": f"Wuthering Waves • {source.title()}"
        }
    }

    # Add timestamp if available
    if post.get("published"):
        embed["timestamp"] = post["published"]

    # Add image if available
    if post.get("thumbnail"):
        embed["image"] = {
            "url": post["thumbnail"]
        }

    payload = {
        "content": post["url"],
        "embeds": [embed]
    }

    response = requests.post(WEBHOOK_URL, json=payload)
    response.raise_for_status()
