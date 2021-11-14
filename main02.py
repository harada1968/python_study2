from time import sleep
from selenium import webdriver
# from bs4 import BeautifulSoup

MYNAVI_URL = 'https://tenshoku.mynavi.jp/'

def driver_setting():
    options = webdriver.ChromeOptions()
    # options.add_argument('--incogninto')
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    return driver

def search(driver):
    search_box = driver.find_element_by_css_selector('.topSearch__text')
    search_box.send_keys('プログラマー')
    sleep(1)
    search_box.submit()
    sleep(5)

def fetch_scrape_data(driver):
    companise = driver.find_elements_by_css_selector('div.cassetteRecruit')
    d_list = []
    for company in companise:
        detail_url = company.find_element_by_css_selector(
            '.cassetteRecruit__bottom > .linkArrowS'
        ).get_attribute('href')
        
        driver.get(detail_url)
        sleep(3)
        com_info = driver.find_elements_by_css_selector(
            'nav.tabNaviRecruit > ul.tabNaviRecruit__list > li:tabNaviRecruit__item > a'
        ).get_attribute('href')
        driver.get(com_info)
    
        sleep(2)
        d = {'c_name': company.find_element_by_css_selector('span.companyName').text,
            'title': company.find_element_by_css_selector('span.occName').text,
            'job_description': company.find_element_by_css_selector('div.jobPointArea__head').text,
            'salary': company.find_element_by_css_selector('td.jobOfferTable__body > div.text').text,
            'url': company.get_attribute('href')  
            
        }
        
        d_list.append(d)
    print(d_list)

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
    fetch_scrape_data(driver) 
    driver.quit() 
    
    
if __name__ == '__main__':
    main()   
    