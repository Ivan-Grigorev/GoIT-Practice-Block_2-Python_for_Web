import urllib.request

response = urllib.request.urlopen('https://api.github.com')
headers = response.getheaders()
content_type = response.getheader('Content-Type')

print(headers)
# [('Content-Type', 'text/html; charset=utf-8'), ('Transfer-Encoding', 'chunked'), ...]

print(content_type)
# "text/html; charset=utf-8"
