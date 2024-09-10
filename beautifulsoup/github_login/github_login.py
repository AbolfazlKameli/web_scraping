import requests
from bs4 import BeautifulSoup

url = 'https://github.com/{}'
username = 'AbolfazlKameli'

session = requests.Session()
response = session.get(url.format('login'))
content = BeautifulSoup(response.text, features='html.parser')
data = {}

for form in content.find_all('form'):
    for inp in form.select('input[type="hidden"]'):
        data[inp.get('name')] = inp.get('value')

data.update({'login': '', 'password': ''})

response = session.post(url.format('session'), data=data)
print(response)

response = session.get(url.format(username))
content = BeautifulSoup(response.text, features='html.parser')
user_info = content.find(class_='vcard-detail')
print(user_info.text)
