import os
import requests

webhook = os.environ["DISCORD_WEBHOOK"]

data = {
    "content": "✅ Hello! Your GitHub Action is working."
}

response = requests.post(webhook, json=data)

print(response.status_code)
print(response.text)
