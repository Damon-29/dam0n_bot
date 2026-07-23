import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")


def send_post(source, post):
    payload = {
        "content": (
            f"## 📰 New {source.title()} Update\n\n"
            f"**{post['title']}**\n"
            f"{post['url']}"
        )
    }

    response = requests.post(WEBHOOK_URL, json=payload)

    response.raise_for_status()
