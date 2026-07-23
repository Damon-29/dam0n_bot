import json

from sources.x_client import XClient

client = XClient()

client.activate_guest()

user_id = client.get_user_id("Wuthering_Waves")
print("User ID:", user_id)

timeline = client.get_user_tweets(user_id)

with open("timeline.json", "w", encoding="utf-8") as f:
    json.dump(timeline, f, indent=2, ensure_ascii=False)

print("Saved timeline.json")
