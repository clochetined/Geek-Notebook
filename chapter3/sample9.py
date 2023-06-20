import requests
from bs4 import BeautifulSoup
import urllib
import pathlib
import time 


target_url = "https://scraping-for-beginner.herokuapp.com/image"
response = requests.get(target_url)
soup = BeautifulSoup(response.content, "html.parser")
filename = "ranking.csv"

path = pathlib.Path("img_folder")
path.mkdir(exist_ok=True)

for i in soup.find_all("img"):
    src = i.get("src")
    img_url = urllib.parse.urljoin(target_url, src)
    abs_url = requests.get(img_url)
    img_name = img_url.split("/")[-1]
    img_path = path.joinpath(img_name)

    with open(img_path, mode="wb") as f:
        f.write(abs_url.content)
    time.sleep(2)