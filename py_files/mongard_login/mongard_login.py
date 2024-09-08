import requests
from bs4 import BeautifulSoup

url = 'https://www.mongard.ir/accounts/{}'
session = requests.Session()
response = session.get(url.format('login'))
data = {}
content = BeautifulSoup(response.text, features='html.parser')

for form in content.find_all('form'):
    for inp in form.select('input[type="hidden"]'):
        data[inp.get('name')] = inp.get('value')

data.update({'email': 'abolfazlkameli0@gmail.com', 'password': 'asdF@123'})

response = session.post(url.format('login'), data=data)
print(response)
