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

    # Timestamp (Discord expects ISO 8601, so only include if already formatted)
    if post.get("published"):
        embed["timestamp"] = post["published"]

    # Website thumbnail
    if post.get("thumbnail"):
        embed["image"] = {
            "url": post["thumbnail"]
        }

    # X images (uses the first image if present)
    elif post.get("media"):
        if len(post["media"]) > 0:
            first_media = post["media"][0]

            # Only embed images
            if first_media.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                embed["image"] = {
                    "url": first_media
                }

    payload = {
        "content": post["url"]
    }

    response = requests.post(WEBHOOK_URL, json=payload)

    if not response.ok:
        print("Discord error:", response.status_code)
        print(response.text)

    response.raise_for_status()
