import json
from urllib.parse import quote

import requests

from sources.x_constants import (
    USER_BY_SCREEN_NAME_QUERY,
    USER_TWEETS_QUERY,
    DEFAULT_FEATURES,
)


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

    USER_BY_SCREEN_NAME_QUERY = USER_BY_SCREEN_NAME_QUERY
    USER_TWEETS_QUERY = USER_TWEETS_QUERY
    FEATURES = DEFAULT_FEATURES

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

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.BEARER}",
            "User-Agent": self.USER_AGENT,
            "x-guest-token": self.guest_token,
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": "en",
            "Accept": "*/*",
            "Referer": "https://x.com/",
            "Origin": "https://x.com",
        }

    def _graphql_get(self, query_id, operation, variables, field_toggles=None):
        url = (
            f"https://x.com/i/api/graphql/{query_id}/{operation}"
            f"?variables={quote(json.dumps(variables, separators=(',', ':')))}"
            f"&features={quote(self.FEATURES)}"
        )

        if field_toggles:
            url += (
                "&fieldToggles="
                + quote(json.dumps(field_toggles, separators=(",", ":")))
            )

        r = self.session.get(
            url,
            headers=self._headers(),
            timeout=30,
        )

        print(f"\n=== {operation} ===")
        print("Status:", r.status_code)
        print(r.text[:1500])

        r.raise_for_status()

        return r.json()

    def get_user_id(self, screen_name: str):
        variables = {
            "screen_name": screen_name,
            "withSafetyModeUserFields": True,
        }

        field_toggles = {
            "withPayments": False,
            "withAuxiliaryUserLabels": True,
        }

        data = self._graphql_get(
            self.USER_BY_SCREEN_NAME_QUERY,
            "UserByScreenName",
            variables,
            field_toggles,
        )

        return data["data"]["user"]["result"]["rest_id"]

    def get_user_tweets(self, user_id: str):
        variables = {
            "userId": user_id,
            "count": 20,
            "includePromotedContent": False,
            "withQuickPromoteEligibilityTweetFields": False,
            "withVoice": False,
            "withV2Timeline": True,
        }

        field_toggles = {
            "withArticlePlainText": False,
        }

        return self._graphql_get(
            self.USER_TWEETS_QUERY,
            "UserTweets",
            variables,
            field_toggles,
        )
