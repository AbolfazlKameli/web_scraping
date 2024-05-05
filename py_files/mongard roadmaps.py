import requests
from bs4 import BeautifulSoup

url = "https://www.mongard.ir/articles/51/python-advanced-courses/"

response = requests.get(url)
content = BeautifulSoup(response.text, 'html.parser')

tables = content.select('table.table-bordered')
courses = []

for table in tables:
    headers = []
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)

    for row in table.find_all('tr'):
        values = []

        for col in row.find_all('td'):
            values.append(col.text)

        if values:
            courses_dict = {headers[i]: values[i] for i in range(len(values))}
            courses.append(courses_dict)

for i in courses:
    print(i)
