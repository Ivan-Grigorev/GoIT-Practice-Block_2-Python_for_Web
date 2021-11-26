import requests
from bs4 import BeautifulSoup


class HabrPythonNews:

    def __init__(self):
        self.url = 'https://habr.com/ru/hub/python/'
        self.html = self.get_html()

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_python_news(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        news_list = soup.findAll("a", class_="tm-article-snippet__title-link")
        return news_list


if __name__ == "__main__":
    news = HabrPythonNews()
    print(news.get_python_news())


#################################
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com/', 'https://api.github.com/inexistent']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_error:
        print(f'Error:{http_error}')
    except Exception as error:
        print(f'Unknown error: {error}')
    else:
        print("Connected successfully")


####################################
import requests
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("https://httpbin.org/cookies")

print(r.text)


##################################
import sys
import requests


def get_weather():
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    city = "Kiev"
    params = {'key': 'a7ef87032c6843688e6100922212910',
               'q': city,
               'format': 'json',
               'num_of_days': 1,
               'lang': 'ru'}
    r = requests.get(url, params=params)
    the_weather = r.json()
    # данной строкой мы преобразуем полученное содержимое страницы
    # в формат json, который очень похож на тип данных dict() в Python
    # и с которым очень удобно работать
    if 'data' in the_weather:
        if 'current_condition' in the_weather['data']:
            try:
                return the_weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return 'Server Error'
    return 'Server Error'


if __name__ == '__main__':
    weather = get_weather()
    print(f'Weather now is {weather["temp_C"]}, feels like {weather["FeelsLikeC"]}')


######################################
import requests

# Making a GET request
response = requests.get('https://api.github.com/')

# check status code for response received
# success code - 200
print(response)
print(response.url)
# print content of request
print(response.content)
print(response.headers)


# # print(data = response.json())
#
# response = requests.get('https://api.github.com/')
# print(response.headers['content-type'])
