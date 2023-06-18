import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'
html = requests.get(url)

# print(html.text)

# プログラムで扱えるようなデータに変換する処理
# 第二引数に解析に利用するパーサー(parser)を指定する
bsObj = BeautifulSoup(html.text, 'html.parser')
# print(bsObj)

print(bsObj.find_all("HTMLタグ"))
print(bsObj.find(id = "id名"))
print(bsObj.find(class_ = "class名"))
print(bsObj.find_all("HTMLタグ", {"id":"id名"}))

text = bsObj.find_all("HTMLタグ", {"id":"id名"})[0].get_text()
print(text)