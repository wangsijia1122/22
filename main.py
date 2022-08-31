

import requests

response = requests.get('http://httpbin.org/get')
print(response.text)

data = {'name':'tom','age':'22'}

response = requests.post('http://httpbin.org/post', data=data)
print(response.text)
11111111

