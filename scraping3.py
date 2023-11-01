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
        url = 'https://hyattregencynaha.jp/guestroom/twin.html'
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




















