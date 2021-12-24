import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# tags = set(soup.find_all('a', class_='tag'))
set_tags = set()
tags = soup.find_all('a', class_='tag')

for tag in tags:
    set_tags.add(tag.text)

print(set_tags)
print(len(tags))
print(len(set_tags))
