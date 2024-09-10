import requests
from bs4 import BeautifulSoup

url = 'https://www.mongard.ir/articles/51/python-advanced-courses/'
response = requests.get(url)
content = BeautifulSoup(response.text, features='html.parser')
tables = content.select('table.table-bordered')
courses = []

for table in tables:
    headers = [header.text for header in table.find('tr').find_all('th')]

    for row in table.find_all('tr')[1:]:
        values = [value.text for value in row.find_all('td')]

        if values:
            courses_dict = {headers[i]: values[i] for i in range(len(values))}
            courses.append(courses_dict)

for course in courses:
    print(course)
