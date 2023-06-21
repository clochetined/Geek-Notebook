from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def openRakutenLuckyKuji(pDriver, pURL):
    try:
        pDriver.get(pURL)
        time.sleep(5)
        pDriver.find_element_by_class_name("//*[@id='entry']").click()
        time.sleep(20)
        pDriver.find_element_by_class_name("btn-start")
    except NoSuchElementException:
        print("NoSuchElementException")
        time.sleep(5)

webdriverpath = "C:\Chrome_Driver\chromedriver.exe"
optinons = webdriver.ChromeOptions()
driver = webdriver.Chrome(webdriverpath)
driver.set_window_size(1200, 800)

lstURL = [
    "https://kuji.rakuten.co.jp/7393386d27/already",
    "https://kuji.rakuten.co.jp/ffc1c52299?scid=su_7066",
    "https://kuji.rakuten.co.jp/889373540e",
    "https://kuji.rakuten.co.jp/14d330d3e0",
    "https://kuji.rakuten.co.jp/6573aa9721",
    "https://kuji.rakuten.co.jp/26d37b04b2",
    "https://kuji.rakuten.co.jp/db43b0750c",
    "https://dream.rakuten.co.jp/luckykuji/?scid=wi_grp_gmx_drm_kuji_list",
    "https://kuji.rakuten.co.jp/4351057845/?scid=wi_grp_gmx_too_rjl",
    "https://kuji.rakuten.co.jp/6e7329f994",
    "https://kuji.rakuten.co.jp/18584163d",
    "https://kuji.rakuten.co.jp/c8437c01c5",
    "https://kuji.rakuten.co.jp/46211bf9dd",
    "https://kuji.rakuten.co.jp/38c3861fdc?scid=su_1129",
    "https://kuji.rakuten.co.jp/26e390eccf?scid=wwkuji_rakuma_luckylottery",
    "https://kuji.rakuten.co.jp/5f93b1fd01",
]

url = "https://www.rakuten.co.jp/"
driver.get(url)

url = "https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top"
driver.get(url)
time.sleep(5)

elem_serch_word = driver.find_element_by_id("loginInner_u")
elem_serch_word.send_keys("tagashirataiki@gmail.comm")
elem_serch_word = driver.find_element_by_id("loginInner_p")
elem_serch_word.send_keys("taiki@716")

for itemURL in lstURL:
    openRakutenLuckyKuji(driver, itemURL)

driver.close()

print("end")