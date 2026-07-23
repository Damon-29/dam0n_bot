import requests
from bs4 import BeautifulSoup


URL = "https://wutheringwaves.kurogames.com/en/main/news"


def fetch():
    response = requests.get(URL)

    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.prettify()[:3000])


if __name__ == "__main__":
    fetch()
