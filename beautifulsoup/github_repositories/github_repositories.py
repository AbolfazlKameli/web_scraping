import json
import re

import requests
from bs4 import BeautifulSoup


def crawl(username: str = 'AbolfazlKameli'):
    url = 'https://github.com/{}/'
    response = requests.get(url.format(str(username)), params={'tab': 'repositories'})
    content = BeautifulSoup(response.text, features='html.parser')

    repos_elements = content.find(id='user-repositories-list')
    repos = repos_elements.find_all('li')
    repositories = []

    for repo in repos:
        name = repo.find('h3').find('a').get_text(strip=True)
        language = repo.find('div', class_='f6 color-fg-muted mt-2').find('span',
                                                                          attrs={'itemprop': 'programmingLanguage'})
        language = language.get_text(strip=True) if language else 'unknown'
        stars = repo.find('a', attrs={'href': re.compile(r'\/stargazers')})
        stars = int(stars.get_text(strip=True)) if stars else 0
        description = repo.find(attrs={'itemprop': 'description'})
        description = description.get_text(strip=True) if description else 'no description'

        repositories.append({
            'name': name,
            'description': description,
            'language': language,
            'stars': stars
        })
    with open('repos.json', 'w') as repos_file:
        json.dump(repositories, repos_file, indent=2)


crawl()
