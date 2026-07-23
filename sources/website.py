import requests
from bs4 import BeautifulSoup


URL = "https://wutheringwaves.kurogames.com/en/main/news"


def fetch():
    response = requests.get(URL)

    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    scripts = soup.find_all("script")

    for script in scripts:
        text = script.string

        if text and "window.__INITIAL__" in text:
            print(text)
            break


if __name__ == "__main__":
    fetch()
