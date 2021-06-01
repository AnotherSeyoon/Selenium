import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.miraeassetdaewoo.com/hki/hki3028/r01.do'

driver = webdriver.Chrome(executable_path='Selenium/Selenium/chromedriver')
driver.get(url=URL)

print(driver.current_url)