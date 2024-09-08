import requests

url = 'https://www.wikipedia.org'

response = requests.get(url)
print(response.text)
