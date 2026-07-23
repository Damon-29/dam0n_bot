import requests
from bs4 import BeautifulSoup

URL = "https://wutheringwaves.kurogames.com/en/main/news"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

print("JavaScript files:\n")

for script in soup.find_all("script", src=True):
    print(script["src"])
