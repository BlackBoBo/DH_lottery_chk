from config.config import Account
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "https://dhlottery.co.kr/user.do?method=login&returnUrl="
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

#ID PW 입력
elem_login = driver.find_element(By.NAME, "userId")
elem_login.send_keys(Account.ID)

elem_login = driver.find_element(By.NAME, "password")
elem_login.send_keys(Account.PW)

#로그인
driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a').click()

#구매 페이지
time.sleep(1)
driver.get('https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40')


#나의 번호 고르기
driver.switch_to.frame('ifrm_tab')
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[4]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/li/input").click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/input[1]').click()


#자동 번호 고르기
driver.find_element(By.XPATH, '//*[@id="num2"]').click()

#구매 개수 선택
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/select/option[4]').click()

#자동구매 확인
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input').click()

#최종 결제
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/input[1]').click()
time.sleep(600)
