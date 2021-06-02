from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/saaeyun/Downloads/chromedriver')
driver.implicitly_wait(15)

driver.get('https://www.naver.com')

search = driver.find_element_by_css_selector('#query')
search.send_keys('고슴도치')
search.send_keys(Keys.ENTER)
time.sleep(2)

posts = driver.find_element_by_css_selector('a.tit')
posts[0].click()
time.sleep(2)

driver.quit()