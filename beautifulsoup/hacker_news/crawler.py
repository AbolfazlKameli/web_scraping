import json
import re

import requests
from bs4 import BeautifulSoup


def crawl(pages: int = 1):
    url = 'https://news.ycombinator.com'
    articles = []
    with requests.Session() as session:
        for page in range(1, pages + 1):
            print(f'page:{page}')
            response = session.get(url, params={'p': page}, verify=False)

            if response.status_code != 200:
                print(f"Failed to retrieve page {page}")
                continue

            content = BeautifulSoup(response.text, features='html.parser')

            for item in content.find_all('tr', class_='athing'):
                item_rank = item.find('span', class_='rank')
                item_rank = item_rank.get_text(strip=True)
                item_a = item.find('span', class_='titleline').find('a')
                item_title = item_a.get_text(strip=True) if item_a else None
                item_link = item_a.get('href') if item_a else None
                next_row = item.find_next_sibling('tr')
                score = next_row.find('span', class_='score')
                score = score.get_text(strip=True) if score else None
                item_comments = next_row.find('a', text=re.compile(r'\d+(&nbsp;|\s)comment(s?)'))
                item_comments = item_comments.get_text(strip=True).replace('\xa0',
                                                                           '') if item_comments else '0 comments'

                articles.append({
                    'rank': item_rank,
                    'title': item_title,
                    'score': score,
                    'comments': item_comments,
                    'link': item_link,
                })

    if articles:
        with open('articles.json', 'w') as articles_file:
            json.dump(articles, articles_file, indent=2)


crawl()
