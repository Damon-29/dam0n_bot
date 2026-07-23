import requests

url = "https://www.reddit.com/r/WutheringWaves/new.json?limit=5"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(headers=headers, url=url)

print("Status:", response.status_code)
print(response.text[:500])
