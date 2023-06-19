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

# 子要素を取得する
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

# 兄弟要素を取得する
for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)

# 親要素を取得する
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())