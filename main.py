from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

MYNAVI_URL = 'https://tenshoku.mynavi.jp/'

options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
driver = webdriver.Chrome(
        executable_path='chromedriver.exe',
        options=options)

def main():   
    driver.implicitly_wait(10)
    driver.get(MYNAVI_URL)
    sleep(3)
    try:
        driver.execute_script('document.querySelector(".karte_close").click()')
        sleep(1)
        driver.execute_script('document.querySelector(".karte_close").click()')
    except Exception:
        pass 
    
if __name__ == "__main__":
    main()   
        
    

search_box = driver.find_element_by_css_selector('.topSearch__text')
search_box.send_keys('プログラマー')
sleep(1)
search_box.submit()
sleep(5)

soup = BeautifulSoup(driver.page_source, 'lxml')
a_tag = soup.select('div.cassetteRecruit')
print(len(a_tag))

driver.quit()