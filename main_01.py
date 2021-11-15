# ライブラリ

from time import sleep
from selenium import webdriver
import pandas as pd


MYNAVI_URL = 'https://tenshoku.mynavi.jp/'

# ドライバー

def driver_setting():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path='chromedriver.exe',
                              options=options)
    return driver

# 検索関連

def search(driver):
    search_box = driver.find_element_by_css_selector('.topSearch__text')
    search_box.send_keys('プログラマー')
    sleep(1)
    search_box.submit()
    sleep(3)
    
# 情報取得 

def fetch_scrape_deta(driver):
    companise = driver.find_elements_by_css_selector('.cassetteRecruit') 
    d_list = []
    
    for company in companise:
        d = {'会社名': company.find_element_by_css_selector('.cassetteRecruit__name').text,
             'タイトル': company.find_element_by_css_selector('.cassetteRecruit__copy > a').text,
             '仕事の内容': company.find_element_by_css_selector('.tableCondition__body').text,
             '給与': company.find_element_by_css_selector('.tableCondition__body').text,
             '詳細URL': company.get_attribute("href")
            
        }
        d_list.append(d)
    df = pd.DataFrame(d_list) 
    print(df)
    
def main():
    driver = driver_setting()
    driver.get(MYNAVI_URL)  
    driver.implicitly_wait(10) 
    sleep(3)
    try:
        driver.execute_script('document.querySelector(".karte-close").click()') 
        sleep(1)
        driver.execute_script('document.querySelector(".karte-close").click()')
        
    except Exception:
        pass    
    search(driver)
    fetch_scrape_deta(driver)
    
    driver.quit()
    
if __name__ == '__main__':
    main()   
        
          
    

