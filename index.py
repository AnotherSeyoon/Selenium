# 필요한 라이브러리 불러오기
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# 드라이버 지정
driver = webdriver.Chrome('./chromedriver')

# 모든 행동에는 time.sleep() 함수를 사용해 2초의 딜레이를 주었다.
# 자가진단 사이트 이동
driver.get('https://hcs.eduro.go.kr/#/loginHome');
time.sleep(2)

# 자가진단 참여하기 버튼 클릭
driver.find_element_by_id('btnConfirm2').click()
time.sleep(2)

# 학교 버튼 클릭
driver.find_element_by_id('schul_name_input').click()
time.sleep(2)

# 시/도 선택
select = Select(driver.find_element_by_id('sidolabel'))
select.select_by_visible_text('광주광역시')
time.sleep(2)

# 학교급 선택
select = Select(driver.find_element_by_id('crseScCode'))
select.select_by_visible_text('고등학교')
time.sleep(2)

# 학교명 입력
school = '광주소프트웨어마이스터고등학교'
send = driver.find_element_by_id('orgname')
send.send_keys(school)
send.send_keys(Keys.RETURN)
time.sleep(2)

# 학교 선택
button = driver.find_element_by_id('a')
button.click()
#driver.execute_script('javascript:;')
time.sleep(2)

# 자가진단 끝
driver.quit()