from config.config import Account

import ssl, time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://dhlottery.co.kr/user.do?method=login&returnUrl="

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

#ID PW 입력
elem_login = driver.find_element(By.XPATH, "/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[1]")
elem_login.send_keys(Account.ID)

elem_login = driver.find_element(By.XPATH, "/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[2]")
elem_login.send_keys(Account.PW)
time.sleep(1)

#로그인
driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a').click()

#구매페이지
time.sleep(1)
driver.get('https://dhlottery.co.kr/myPage.do?method=lottoBuyListView')

#날짜 선택
driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div[2]/div/form/table/tbody/tr[3]/td/span[2]/a[3]').click()
driver.find_element(By.XPATH, '//html/body/div[3]/section/div/div[2]/div/div[1]/a').click()

time.sleep(600)