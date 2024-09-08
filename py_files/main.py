import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Mao_Zedong'

response = requests.get(url)
content = BeautifulSoup(response.text, features='html.parser')
print(content.select('li > a[title="Benjamin Tucker"]'))
