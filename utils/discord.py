import os
import requests


WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")


def send_post(post):
    if not WEBHOOK_URL:
        raise ValueError("DISCORD_WEBHOOK environment variable is not set.")

    payload = {
        "content": f"**{post['title']}**\n{post['url']}"
    }

    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code not in (200, 204):
        raise Exception(
            f"Discord webhook failed ({response.status_code}): {response.text}"
        )
