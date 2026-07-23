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

guest_token = r.json()["guest_token"]
headers = {
    "Authorization": f"Bearer {BEARER}",
    "x-guest-token": guest_token,
    "User-Agent": "Mozilla/5.0",
}

r = requests.get(
    "https://api.x.com/graphql",
    headers=headers,
)

print("Status:", r.status_code)
print(r.text[:500])
