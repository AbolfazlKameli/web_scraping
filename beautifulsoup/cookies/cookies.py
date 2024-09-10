import requests
from bs4 import BeautifulSoup

url = 'https://mongard.ir/accounts/{}'
response = requests.get(url.format('dashboard'), cookies={'sessionid': 'm52hpop6f78wylxccys0b184sr6704k0'})
content = BeautifulSoup(response.text, features='html.parser')
print(content.find('h3', class_='profile-title').text)
