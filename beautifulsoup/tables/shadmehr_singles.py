import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Shadmehr_Aghili'
response = requests.get(url)
content = BeautifulSoup(response.text, features='html.parser')


def crawl():
    table = content.find('table', class_='tracklist')

    singles = []
    headers = [header.text for header in table.find('tr').find_all('th')]

    for row in table.find_all('tr')[1:]:
        values = [value.text for value in row.find_all(['th', 'td'])]

        if values:
            singles_dict = {headers[i]: values[i] for i in range(len(values))}
            singles.append(singles_dict)

    for single in singles:
        print(single)


crawl()
