from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import pandas as pd

app = Flask(__name__)  # Flaskアプリケーションを作成

@app.route('/hyatt', methods=['POST'])  # エンドポイントのパスを修正

def hyatt():
    try:
        # スクレイピングしたいURL
        url = 'https://www.expedia.co.jp/Okinawa-Hotels-Hilton-Okinawa-Sesoko-Resort.h48251410.Hotel-Information?chkin=2023-11-11&chkout=2023-11-15&x_pwa=1&rfrr=HSR&pwa_ts=1698895053628&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jby5qcC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=10805&destination=%E6%B2%96%E7%B8%84%E6%9C%AC%E5%B3%B6%2C+%E6%B2%96%E7%B8%84%E7%9C%8C%2C+%E6%97%A5%E6%9C%AC&destType=MARKET&latLong=26.212401%2C127.680932&trackingData=AAAAAQAAAAEAAAAQmUC26KAl_ZSY003zdeo1G4v2V5PGG821wSdtgDRpf0dhdEZK_1ch6TEA5NA0h4GsFoNmvlIA0g4r977wR3Vr5CVzUjvuEedtJ0wm-iEfBsI0RJvSXpHIjZ-U93LEaC7J6xh387d62H7hVB0sxnKrLaTbolYjAvCO5nWcpiX6umyS4yz7vMmqYdonp4uD555jzYewrd7LrSr0oZqcD_6uZyntKBT03OHmfq4ufFBVNoEK0-MtKk2mFxYrULFiHGCWhmx2Rd4oAvpl9qvCnRvGRk7HPK5h0o2MMAszg59SxMyfJA5Jb5RfpnDo8KbaeNQTMwPSKz_p4ouHXzcI1yvh6328a2-YjygiKJVpSrxQygIzxvxcTRPF3QOJECPvKVbRTynziMtyBS0Mba_vj1RsJmol8uXVfgrAxgYzwQexj6fP8rpfELhicYFhy3rDrsl0gy8rgY5aJywGCL9b7zafJje29rdBj0NghKwMCIo_hMD0KUoXZxrGMe8-J_0nZL5u-AtYrjn6rw4j1j5chi3N2H1zMmTBScirF_-Ub6DcO0V5F_QvhOM4xuxuCIDD1BU38wjg2gfVSOC4ovE54iN-U8IZakPPlcrc8xNRlOQnNfLUTB_M3tpAiScge8wQSutxrWHTNwgfDd_738s4Ixot887Kx-nsZq3A2e1gJBgC2K1nJeBx7N8n1fimPBDTWzMKZI3PRZoWq0wlmOFJaTWeSteWBsv8TKxQ6P4RpJ75_N9IzgYNmjfiqsBLI1LGpUsFzpcleaa9tW7Ubyx2mvf2trVvf2Oha-9r57TwB-Uwkd5gRSU-GXWYI5GaQEVIiVXqpHBJDK4c0ArbDbHjN6_IvDVbdSPANC02yr7Rq4yGXn-v8QqV0DdX9yi5EGmPt4UMZRkS-MpqH08z2oqvK4SOR57_vqkIxBelXbY5FKLhiSFw4lMXiHpUqucihB6aXK2vSTCTULvkUVqKyWFnu_il9myCtgBKimxK5dP800Icpn_XTU2_VSkpE1iegDN4V6k4ZtvRh4_Bd3GkTTmIiPpczND-fthOIjEglaqHmaSSwEoa5-bOa9OuUh4CON5Og_aTSVCwmkclMaTH4vv2OGSSrxDTIuLrd-g5zrTIXyUN90MrlqGlGH2G9gSzmDPaiiLqw4HzX6nlNr9JF8C36TzOmVks0E3XGncqwoAKu7NGeMrG29Wj2LQVPFPqxVB7ly_apgu8WrqHT1F4QeC3P1vISIVhPRphuRpBPxd3oV87mn_7VNPKAMwFKmf3Oj2VvpuI43bz8hMqOpbo-DhdmpTTPvoxq4-PVBqCjyblgUUYfPx3cUlmPS1o1X9xQEW_0N6uJUxsvAoeV2dum4-W-K51AzIvJCNIVkM53TZswW1FHImTYpxWxLgyvzfqorLSX9BEGxalzvO_14zV5EuKg0r3fh-7z68dWSSc7zlq5DJe9hYgqiQAuHW_atdUiyKpX69DBDGYeAsbAxvjG0XbGZBUzWG-UhefrDdU87MxtwonxlyGnqMLRaBZJFDR7rXGdsGIjpP4u0OZPjbSN7M0SDaEqU5QZRebNDowzG3dQx6j1eVr1LHHIdm6z3haFUqrCkDiDEgaSAfU7H9RREa9o5ghIx5RZDWdTPwqT-tbaJUFJMGaieWuOsoYXtHiZFe7umo09TE_f_K_VSHcDdLxqcxraLfC7XahiCipWt37Ool4p8h2JGc9Y8xnHlOKkwOhO5RitKr0p3hcYikGpNqUdXA0DgY8ivvX--VgH2yVuQuCIaNa-iPa_DBtiJKrMnoF2aXbb6IAJnnHloY5h96bO0NwGS3kOrrNA0gec6_DxFiuIzRw0XBi9nYIQ-LlqkwYRN0wLtbeRHfsTKY1JVqlgd-fZ7Z8LI4CMl1nlyjR4IrZMb5qo7dmh0-Rvi8qH3FRFz9upmpNp-msgmJ5EKuneA2Yn2X2Q2WMWmvSp9bhjp7Y1Bzl-eIc61gFzw-MiLD9gIdMuHQa-OhX2Cs7fgrMuuI6F4edvO2Wy_TJvO10X4dlIDAOVVv3qmo8RgCJFoxmGfGiJPmJkRUG0SayefmAcAB4J6xHGBDuHanryGrL2fFSPPs%3D&rank=4&testVersionOverride=Buttercup%2C39483.0.0%2C47230.154757.0%2C49619.150273.0%2C48676.154917.0%2C48304.0.0%2C50206.153476.0%2C50028.155516.0%2C50782.0.0%2C50813.156505.0%2C46969.152461.2%2C47890.143201.1%2C43153.133019.3&slots=&position=9&beaconIssued=&sort=RECOMMENDED&top_dp=22313&top_cur=JPY&userIntent=&selectedRoomType=228009894&selectedRatePlan=260294429&searchId=4a979b28-e28d-4b38-8d58-17008a2fdbf7'
        # POSTリクエストからホテルサイトのURLを取得
        data = request.get_json()
        url = data.get('url')  # URLを取得するためにキー 'url' を使用
        # ホテルサイトからHTMLを取得
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch the website"})  # エラーメッセージをJSONで返す

        # HTMLをBeautiful Soupで解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # 必要な情報を抽出（例：ホテル名）
        hotel_name = soup.find('h1', {'class': 'hotel-name'}).text.strip()

        # 他の情報を抽出するコードをここに追加
        # この部分にサイト固有のHTML解析ロジックを追加して、他の情報を抽出します

        # 抽出した情報をJSON形式で返す
        return jsonify({"hotel_name": hotel_name})  # ホテル名をJSONで返す

    except Exception as e:
        return jsonify({"error": str(e)})  # エラーが発生した場合、エラーメッセージをJSONで返す

if __name__ == '__main__':
    app.run(debug=True)  # Flaskアプリケーションを実行


    cmd = 'pip install --upgrade chromedriver_binary' 
res = subprocess.call(cmd, shell=True)
url = "https://www.expedia.co.jp"
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'performance': 'ALL' }
def new_func(d):
    return webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=d)


driver = new_func(d)
driver.set_window_size('1200','1000')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(driver.page_source)
div=soup.find_all('div', class_="contents_outer next")
img = soup.find('div', class_='inner g3 sg3 ssg6 sspush3') .find('img', class_='fit')
print(img['src'])
r = requests.get('https://go-resol-hotel.reservation.jp/ja/hotels/trinity-naha/rooms/10017293?_ga=2.10783924.1442734765.1697063444-1405639140.1697063444&_gl=1*gq2m8k*_ga*MTQwNTYzOTE0MC4xNjk3MDYzNDQ0*_ga_XMWVW0YK44*MTY5NzA2MzQ0My4xLjEuMTY5NzA2MzQ1My41MC4wLjA.' + str(img['src']))
with open(f'test.jpg', 'wb') as f:
    f.write(r.content) 
div=soup.find_all('table') [0]
print(div.find("tr"))
print(div.find("th"))
print(div.find("td"))
col_data = []
col_list = []
data = []
for tr in div.find_all('tr'):
#     print(tr)
#     print('列名:',tr.find('th').text,'列にいれる値:',tr.find('td').text)
    
    col_list.append(tr.find('th').text)
    data.append(tr.find('td').text.replace("¥n",""))
col_data.append(data)

df = pd.DataFrame(col_data,columns=col_list)
df.to_csv('reservation.csv',index=False)




















