from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://www.expedia.co.jp/Okinawa-Hotels-Naha-Tokyu-REI-Hotel.h8375.Hotel-Information?chkin=2023-11-11&chkout=2023-11-15&x_pwa=1&rfrr=HSR&pwa_ts=1699479560950&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jby5qcC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=10805&destination=%E6%B2%96%E7%B8%84%E6%9C%AC%E5%B3%B6%2C+%E6%B2%96%E7%B8%84%E7%9C%8C%2C+%E6%97%A5%E6%9C%AC&destType=MARKET&neighborhoodId=553248633981723816&latLong=26.212401%2C127.680932&sort=RECOMMENDED&top_dp=9427&top_cur=JPY&userIntent=&selectedRoomType=200166898&selectedRatePlan=389273572&searchId=7229f5c8-c07b-4917-93b3-2da8c42444b0'


# ブラウザを起動
driver = webdriver.Chrome()

# 指定されたURLにアクセス
driver.get(URL)
time.sleep(5)


# 例: CSSクラスを使う場合
clickable_element = driver.find_element(By.CLASS_NAME, 'uitk-text')
clickable_element.click()
wait = WebDriverWait(driver, 10)
clickable_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'uitk-text')))
clickable_element.click()






# JavaScriptを使用してページの最下部までスクロール
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 100ピクセルだけ下にスクロール
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)

# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)

# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)

# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)

# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)

# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,300 );")
# time.sleep(10)



# ページのタイトルを取得
title = driver.title
print(title)

html = driver.page_source

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(html, 'html.parser')

h2_tag = soup.find_all('h2')

print(h2_tag)

# サービスのリストを抽出
services_list = soup.find_all('div', class_="uitk-text")
for service in services_list:
    print(service.span.text)


#     header = soup.find('h4', class_='uitk-heading').text

# # 周辺情報のリストを取得
# info_list = [item.text for item in soup.find_all('div', class_='uitk-text')]

# print(header)
# for info in info_list:
#     print(info)
# # 例：ページのタイトルを取得
# title = soup.title.string
# print("ページのタイトル:", title)

# # ブラウザを閉じる
# driver.quit()
