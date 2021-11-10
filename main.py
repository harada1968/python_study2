from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
driver = webdriver.Chrome(
    executable_path='chromedriver.exe',
    options=options)
driver.implicitly_wait(10)

driver.get('https://tenshoku.mynavi.jp/')
sleep(3)

a_tag = driver.find_element_by_css_selector('div._CloseButton__3xX2_ > button')
sleep(3)

a_tag.click()
sleep(5)

b_tag = driver.find_element_by_css_selector('a._karte-temp-btn-close__2u7Y_')
sleep(3)

b_tag.click()
sleep(3)


search_box = driver.find_element_by_css_selector('.topSearch__text')
search_box.send_keys('プログラマー')
sleep(1)
search_box.submit()
sleep(5)

driver.quit()