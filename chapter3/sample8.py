import requests
from fake_useragent import UserAgent

url = 'https://www.google.co.jp/search'
params = {'p':'python'}
response = requests.get(url,params=params)

print(response.text)
# print(response.text[:500])
# print(response.status_code)
# for key,value in response.headers.items():
#     print(key,' ',value)

# ua = UserAgent()
# print(ua.chrome)
# print(ua.ie)

