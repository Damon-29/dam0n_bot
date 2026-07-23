import requests

BEARER = (
    "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs="
    "1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
)

headers = {
    "Authorization": f"Bearer {BEARER}",
    "User-Agent": "Mozilla/5.0",
}

r = requests.post(
    "https://api.x.com/1.1/guest/activate.json",
    headers=headers,
)

print("Status:", r.status_code)
print(r.text)
