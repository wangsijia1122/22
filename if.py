import requests

data = {'name':'tom','age':'22'}

response = requests.post('http://httpbin.org/post', data=data)
