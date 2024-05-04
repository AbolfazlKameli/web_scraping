import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Shadmehr_Aghili"

response = requests.get(url)

content = BeautifulSoup(response.text, "html.parser")
result = content.select('h1 > span[class=mw-page-title-main]')

print(result)
