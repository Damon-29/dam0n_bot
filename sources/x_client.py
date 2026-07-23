import json
import requests


class XClient:
    BEARER = (
        "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs="
        "1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    )

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/142.0.0.0 Safari/537.36"
    )

    def __init__(self):
        self.session = requests.Session()
        self.guest_token = None

    def activate_guest(self):
        headers = {
            "Authorization": f"Bearer {self.BEARER}",
            "User-Agent": self.USER_AGENT,
        }

        r = self.session.post(
            "https://api.x.com/1.1/guest/activate.json",
            headers=headers,
            timeout=30,
        )

        r.raise_for_status()

        self.guest_token = r.json()["guest_token"]

        print("Guest token:", self.guest_token)

        return self.guest_token
