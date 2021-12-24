import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
authors = soup.find_all('small', class_='author')

for author in authors:
    print(author.text)
