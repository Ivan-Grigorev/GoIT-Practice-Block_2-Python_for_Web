import time

import requests
from bs4 import BeautifulSoup
import redis

r = redis.StrictRedis(host='localhost', port=6380, db=0)

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

i = 0
for quote in quotes:
    r.set(i, quote.text, 2)
    i += 1

print(r.get(2).decode('utf-8'))
time.sleep(3)
print(r.get(5).decode('utf-8'))