# pip install lxml
# pip install requests
# pip install beautifulsoup4

# <div>  <i> </i> </div>
# <p>  jjkjl </p>

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
