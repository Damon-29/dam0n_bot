import requests

url = "https://www.reddit.com/r/WutheringWaves/new.json?limit=5"

headers = {
    "User-Agent": "WuWaNewsBot/1.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

data = response.json()

for post in data["data"]["children"]:
    p = post["data"]

    print("---------------------")
    print("Title:", p["title"])
    print("Flair:", p.get("link_flair_text"))
    print("URL:", "https://reddit.com" + p["permalink"])
