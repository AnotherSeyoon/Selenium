# 필요한 라이브러리 불러오기
from os import name
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# 드라이버 지정
driver = webdriver.Chrome('./chromedriver')

# 옵션 생성
options = webdriver.ChromeOptions()

# 창 숨기는 옵션 추가
options.add_argument("headless")

# 모든 행동에는 time.sleep() 함수를 사용해 딜레이를 주었다.
# 자가진단 사이트 이동
driver.get('https://hcs.eduro.go.kr/#/loginHome')
time.sleep(5)

# 자가진단 참여하기 버튼 클릭
driver.find_element_by_id('btnConfirm2').click()
time.sleep(1)

# 학교 버튼 클릭
driver.find_element_by_id('schul_name_input').click()
time.sleep(1)

# 시/도 선택
select = Select(driver.find_element_by_id('sidolabel'))
select.select_by_visible_text('광주광역시')
time.sleep(1)

# 학교급 선택
select = Select(driver.find_element_by_id('crseScCode'))
select.select_by_visible_text('고등학교')
time.sleep(1)

# 학교명 입력
school = '광주소프트웨어마이스터고등학교'
orgname = driver.find_element_by_id('orgname')
orgname.send_keys(school)
orgname.send_keys(Keys.RETURN)
time.sleep(1)

# 학교 a태그 선택
button = driver.find_element_by_css_selector('a')
button.click()
time.sleep(1)

# 학교 선택 완료
button = driver.find_element_by_class_name('layerFullBtn')
button.click()
time.sleep(1)

# 이름 입력
username = '박세윤'
naemsend = driver.find_element_by_id('user_name_input')
naemsend.send_keys(username)
time.sleep(1)

# 생년월일 입력
birthday = '040626'
birthdaysend = driver.find_element_by_id('birthday_input')
birthdaysend.send_keys(birthday)
time.sleep(1)

# 확인 버튼 클릭
button = driver.find_element_by_id('btnConfirm')
button.click()
time.sleep(1)

# 비밀번호 입력
password = '0626'
passwordsend = driver.find_element_by_class_name('input_text_common')
passwordsend.send_keys(password)
time.sleep(1)

# 확인 버튼 클릭
button = driver.find_element_by_id('btnConfirm')
button.click()
time.sleep(3)

# 이름 선택
item = driver.find_element_by_class_name('btn')
item.click()
time.sleep(2)

# 첫번째 문항 클릭
button = driver.find_element_by_id('survey_q1a1')
button.click()
time.sleep(1)

# 두번째 문항 클릭
button = driver.find_element_by_id('survey_q2a1')
button.click()
time.sleep(1)

# 세번째 문항 클릭
button = driver.find_element_by_id('survey_q3a1')
button.click()
time.sleep(1)

# 제출 버튼 클릭
button = driver.find_element_by_id('btnConfirm')
button.click()
time.sleep(2)

# 자가진단 끝
driver.quit()