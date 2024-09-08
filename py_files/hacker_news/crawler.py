import requests
from bs4 import BeautifulSoup
import re

# TODO: crawl all.
url = 'https://news.ycombinator.com'
response = requests.get(url)
content = BeautifulSoup(response.text, features='html.parser')
articles = []


def crawl():
    for item in content.find_all('tr', class_='athing'):
        item_a = item.find('span', class_='titleline').find('a')
        item_title = item_a.get_text(strip=True) if item_a else None
        item_link = item_a.get('href') if item_a else None
        next_row = item.find_next_sibling('tr')
        score = next_row.find('span', class_='score')
        score = score.get_text(strip=True) if score else None
        item_comments = next_row.find('a', text=re.compile(r'\d+(&nbsp;|\s)comment(s?)'))
        item_comments = item_comments.get_text(strip=True).replace('\xa0', '') if item_comments else '0 comments'

        articles.append({
            'title': item_title,
            'score': score,
            'comments': item_comments,
            'link': item_link,
        })


crawl()
for article in articles:
    print(article)
