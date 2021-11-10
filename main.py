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

search_box = driver.find_element_by_css_selector('topSearch__item')
search_box.send_keys('プログラマー')
sleep(1)
search_box.submit()
sleep(5)

driver.quit()