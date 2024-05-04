import requests

url = "https://www.mongard.ir/"

response = requests.get(url)

print(dir(response.request))
print(response.request.headers)

with open('test.html', 'w') as text:
    text.write(response.text)
