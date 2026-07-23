import json

...

timeline = client.get_user_tweets(user_id)

with open("timeline.json", "w", encoding="utf-8") as f:
    json.dump(timeline, f, indent=2, ensure_ascii=False)

print("Saved timeline.json")
