from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# 個別ページのURL一覧
# ここは今はURLを直打ちしているが「https://www.expedia.co.jp/Hotel-Search?destination=%E6%B2%96%E7%B8%84%2C%20%E6%B2%96%E7%B8%84%E7%9C%8C%2C%20%E6%97%A5%E6%9C%AC&endDate=2023-12-17&gad_source=1&gclid=Cj0KCQiAyKurBhD5ARIsALamXaFYmOegRFy5GRyIoPi94MWtbyS6H8vKt1xF3JG3hDPH1EZpwgt_bq8aAkLfEALw_wcB&locale=ja_JP&regionId=6053824&semcid=JP.B.GOOGLE.BD-c-JA.HOTEL&semdtl=a118925758649.b1144349117179.g1aud-2067245471241%3Akwd-336120209959.e1c.m1Cj0KCQiAyKurBhD5ARIsALamXaFYmOegRFy5GRyIoPi94MWtbyS6H8vKt1xF3JG3hDPH1EZpwgt_bq8aAkLfEALw_wcB.r154fc61f005a3b447a19360156769d639189c92ade2591a1c9c667ff5bbfd3f6f.c1VurfUF1sqgoMqYCCzuaDgQ.j11009343.k120670.d1640985421730.h1e.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&siteid=28&sort=RECOMMENDED&startDate=2023-12-16&theme=&useRewards=false&userIntent=」
#をスクレイピングしてURLをリストとして取得する想定
url_list = [
'https://www.expedia.co.jp/Okinawa-Hotels-Naha-Tokyu-REI-Hotel.h8375.Hotel-Information?chkin=2023-11-11&chkout=2023-11-15&x_pwa=1&rfrr=HSR&pwa_ts=1699479560950&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jby5qcC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=10805&destination=%E6%B2%96%E7%B8%84%E6%9C%AC%E5%B3%B6%2C+%E6%B2%96%E7%B8%84%E7%9C%8C%2C+%E6%97%A5%E6%9C%AC&destType=MARKET&neighborhoodId=553248633981723816&latLong=26.212401%2C127.680932&sort=RECOMMENDED&top_dp=9427&top_cur=JPY&userIntent=&selectedRoomType=200166898&selectedRatePlan=389273572&searchId=7229f5c8-c07b-4917-93b3-2da8c42444b0',
]

URL = 'https://www.expedia.co.jp/Okinawa-Hotels-Naha-Tokyu-REI-Hotel.h8375.Hotel-Information?chkin=2023-11-11&chkout=2023-11-15&x_pwa=1&rfrr=HSR&pwa_ts=1699479560950&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jby5qcC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=10805&destination=%E6%B2%96%E7%B8%84%E6%9C%AC%E5%B3%B6%2C+%E6%B2%96%E7%B8%84%E7%9C%8C%2C+%E6%97%A5%E6%9C%AC&destType=MARKET&neighborhoodId=553248633981723816&latLong=26.212401%2C127.680932&sort=RECOMMENDED&top_dp=9427&top_cur=JPY&userIntent=&selectedRoomType=200166898&selectedRatePlan=389273572&searchId=7229f5c8-c07b-4917-93b3-2da8c42444b0'


# ホテルデータを格納するリストを用意する
hotel_data = []


# ブラウザを起動
driver = webdriver.Chrome()


# 指定されたURLにfor文で1件ずつアクセスする
for url in url_list:
    driver.get(url)
    time.sleep(15)
    print("ホテルページにアクセスしました。要素取得処理を開始します")

    # ホテル名を取得
    hotel_name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/h1")
    hotel_name = hotel_name_element.text
    print("ホテル名", hotel_name)

    # 英語ホテル名を取得
    en_hotel_name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/h2")
    en_hotel_name = en_hotel_name_element.text
    print("英ホテル名", en_hotel_name)

    # 住所
    #<ここにコードを書く>
    en_hotel_addres_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]")
    en_hotel_addres = en_hotel_addres_element.text
    print("住所", en_hotel_addres)


    ## ここからスクロール処理が必要になるかもしれない
    # clickable_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[4]/button/span[1]")
    # clickable_element.click()
    # time.sleep(10)
    # # 部屋情報
    # #<ここにコードを書く>
    # en_hotel_room_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section/div[3]/div")
    # en_hotel_room = en_hotel_room_element.text
    # print("部屋情報", en_hotel_room)

   
    # 周辺情報
    #<ここにコードを書く>
    en_hotel_around_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/div[2]")
    en_hotel_around = en_hotel_around_element.text
    print("周辺情報", en_hotel_around)

    driver.get(URL)
    time.sleep(20)


# ここからスクロール処理が必要になるかもしれない
    clickable_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[4]/button/span[1]")
    clickable_element.click()
    time.sleep(10)
    


    # 交通案内
    # <ここにコードを書く>
    en_hotel_traffic_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[8]/div/div/div/div/div[2]/div[2]/div[2]/div")
    en_hotel_traffic = en_hotel_traffic_element.text
    print("交通案内", en_hotel_traffic)

    driver.get(URL)
    time.sleep(20)



    # 施設の設備
    #<ここにコードを書く>
    en_hotel_facility_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[12]/div[1]/div/div/div[1]")
    en_hotel_facility = en_hotel_facility_element.text
    print("施設の設備", en_hotel_facility)

    driver.get(URL)
    time.sleep(20)



    # ポリシー
    #<ここにコードを書く>
    en_hotel_policy_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[15]/div/div/div/section/div/div[1]/div/div/div/div")
    en_hotel_policy = en_hotel_policy_element.text
    print("ポリシー", en_hotel_policy)

    driver.get(URL)
    time.sleep(20)



    # 重要事項
    #<ここにコードを書く>
    en_hotel_important_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[2]/div/div[3]/div[16]/div/div/section/div/div[1]/div/div/div")
    en_hotel_important = en_hotel_important_element.text
    print("重要事項", en_hotel_important)

    driver.get(URL)
    time.sleep(20)




    # これまでに取得した情報をリストとしてリストの中に追加する
    hotel_data.append([
        hotel_name,
        en_hotel_name
        ])


# ブラウザを閉じる
driver.quit()
print("スクレイピング処理終了")

# 取得したリストをデータフレームに変換
print("csv出力処理開始")
df = pd.DataFrame(hotel_data)
# CSV出力
df.to_csv("アウトプット.csv",index=False)
print("csv出力処理終了")


# スクロール処理のサンプルコード
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



