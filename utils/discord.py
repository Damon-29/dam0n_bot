import os
import requests


WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")


def send_post(post):
    data = {
        "content": (
            f"**{post['title']}**\n"
            f"{post['url']}"
        )
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code not in (200, 204):
        raise Exception(
            f"Discord webhook failed: {response.status_code}\n{response.text}"
        )
