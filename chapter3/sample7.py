import requests
from bs4 import BeautifulSoup 

target_url = "https://scraping-for-beginner.herokuapp.com/ranking/"
response = requests.get(target_url)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup)
print(soup.find("div",class_="row"))