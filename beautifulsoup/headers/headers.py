import requests
from bs4 import BeautifulSoup

url = 'https://bama.ir'
headers = {'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0'}
response = requests.get(url, headers=headers)
print(response.status_code)
