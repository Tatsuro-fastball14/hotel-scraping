# ライブラリ呼び出し
from flask import Flask, render_template
import pandas as pd 
from datetime import datetime
from flask import request
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import pymysql
import sqlite3




df=pd.read_csv("/Users/tatsuro/projects/hotel-scraping/test.csv")
df["imgurl"]="https://images.trvl-media.com/lodging/36000000/35740000/35736500/35736430/788d05ca.jpg?impolicy=resizecrop&rw=1200&ra=fit"
data = [list(e) for e in zip(df['宿泊人数'],df['眺望'],df["お部屋の設備"],df["バスルームの設備"])]
print(data)


df=pd.read_csv("/Users/tatsuro/projects/hotel-scraping/test.csv")
df["imgurl"]="https://www.expedia.co.jp/Okinawa-Hotels-Hilton-Okinawa-Sesoko-Resort.h48251410.Hotel-Information?chkin=2024-01-15&chkout=2024-01-19&x_pwa=1&rfrr=HSR&pwa_ts=1705281209888&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jby5qcC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=10805&destination=%E6%B2%96%E7%B8%84%E6%9C%AC%E5%B3%B6%2C+%E6%B2%96%E7%B8%84%E7%9C%8C%2C+%E6%97%A5%E6%9C%AC&destType=MARKET&latLong=26.212401%2C127.680932&trackingData=AAAAAQAAAAEAAAAQF-jNBRpbnMSedbDOpiHNm8iY8awjIKdSa4pytvHwga_ZZ48f9eIKRd7oaK9yS_gumNexUJrDyH8TJvXye6OxBcbEfAMkzke57NQ_C9wVBjle1omNTMI0wQsNbzFbi6EIkOKHGiT_7h4_Hiy8wc91r__1vLhgs58Jr3ccJJPNEBBuVq2fEMsR_sq53xzwg8Zn1KqGNsXH9AHiVFxvkbRRcscIIYnJ3oMeMgKZG7fAXkdd-78gmvEcBZeyNE4y1yO8p0Wn37vk811LRvGaxbHTRWjqgQbSa3U1Kk4E5iTl7XcJdYccSStdQD3CILDQGeCS58FaUBKmaqmFhAxOde3sF1AvtUUY06mhHD_KU2fBtwWvyscTU7gA2D1ItDZ3NU9pB_PrDeq7SbpBsSzyyWRAb5dKg0gQlqhVq7cN8dZLgZ9TmV2rYP7z371DwwdW20qugS7zOlkhtss5aw8wdcRXGSR-0MNB0kT0t5k4x-kFIRQSDHvITSYa5HEkgntuvhj5Zc4eo8L7_DpTW2QCfyEEzRlcpXrq6zv90ATuw04amEGz58Z1WP1EtXfUgkKmE_12qenzqqbPgHln27bSf2G5Sh2zOVgr6XErsTat_IdgI8kpEEYFWtcJlrRETQsizZvIYI0zqeTh_EIFQl1gLpdEyy3wt_2UI7t0P1GQGRsapasTRV2RsYyQhrtjXGf6u0JwVpa4K8SenCuQFZo_LMtv9pWKqaU45cgK_gT5pE2KNzxzSeIE_piVcWdw5xUtnLdyU76fin5wddgsKoRvApqC6-NTi5Sg4egEtb2I-AZXxX2j4P40OU0TWDi5-FJw-uXgTSqsQjrqLDC41mXBdyFyJebosqTjIRJOzusdwtsa4S18dmOf22j_J8_LHIlB7bDOZBm1iiMVM3prKWAO11J7E3y7Q8Vd7Oh1yzNpvQHDBZiyZNfUts_-zw4hJ2iejCPwDxp_qt_dEXCE025FLAbE1j0lhfwU3aHsQkjOCN61j1r7ZkBl0yQWP7TMJF0n6glMQkoTcAXk4Y3VrSdsz5E_ePuETbZih2cpPc6COoDNPP3ftCjyo-hvSDM-2jd-wRtdyBg-5vIG77SYv9oMu2QODRAlobRxbbfl5fXMGaXkzABxvtQmWQwkz8AHCHRc-nV-0lm4nuJnQjdXfuJEof1sWbbzqYtyElKeX123jq0--Yb4uuYgeYdOQnIoAWnWjXEEeoVap30Qm2dz2vwEdUkG80xX-kWJZS44_Rh0VoKG9mhs-nUzAIC7Yj_5TWorEhz5CfEYL4YAKjrXHZmd22XnKxrPYqm4XayEbvwGce7_gbTBbHJ4wegjuTUdnaqrOjCOPwXqhcNLJTL_o9KmxV0m6AGLwKSYH-mvhufMOlAyPTcwDHqsm2Eel95-MVLfnzL0NSA6Jz5NznSl8cXLBs_mYoAcJ6GrKmjvfHphnFOzmJfaSDI4g2HN4S0T9cnpKtWhN37n7l6aqteQoHNxm5rHM3e2-Ju0TqA-J42vWWiUFSOZe8ojBxtDVZ2HluQrOJgVxwitRiSlI0xJ_eZ_Uet0EOAf8AjqKqHHannbzHWxByKtrWCsnOpSLBqTBy37OT3fc9SxKwZMhFCUA4So85IC5wKEju08CJKdGDmKAtuafXRFgojvX5Ivqt2xfOiNHzqcrqLX8yEKqZwowp__j-JezNg98W7eC5Cd9nwk5rzYehelp0sBs1sj9xj2yH8QuHW686zX3TVVG8jbkhGYzIxYrHF5_s5HoneDeGCFeffP4IaDX6sAvbpxD_mw45SSWh9b7s3cFIEdAL7lJQ7rgY2LKFKQKpbiNY8p357AmlKIDpPaludmkTJO14bq-k4CHUYzprkohRDlDN_e-oCkXCAuqb_iMTXxOemguXn9sXPgbT6QKAw9BG1m4XBjqTrNCQP4jYoWiPAtytJmGARSHMNPvO82x4xnqHsQxLuNwAo5cImFQVONg5L-gZxV_mcJJrrY93XA-Hsyq55VirVFUyYVslSC2JPf9xh_f-nbLpszmyFx9jyLzR6AmMyHdldjzbg6vs-hCQa_FnadgCG9B0GWDxq5Q7lKIx6-y9JRrvQOqgE%3D&rank=1&testVersionOverride=Buttercup%2C39483.0.0%2C47230.158373.1%2C49619.150273.0%2C48676.160236.2%2C48304.159182.1%2C50206.163597.1%2C50028.155516.0%2C50782.0.0%2C50813.156505.0%2C49817.162635.0%2C50988.158353.0%2C47890.143201.1&slots=&position=1&beaconIssued=&sort=RECOMMENDED&top_dp=23000&top_cur=JPY&userIntent=&selectedRoomType=228009885&selectedRatePlan=260294295&searchId=536c4b7a-cd57-4a7e-80a0-d67d695141d8"
data = [list(e) for e in zip(df['宿泊人数'],df['眺望'],df["お部屋の設備"],df["バスルームの設備"])]
print(data)

# クラス呼び出し
app = Flask(__name__)
from sqlalchemy import create_engine

# データベースの接続設定
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'test2'

# SQLAlchemyを使用してMySQLに接続
engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}")


@app.route('/table')
def index2():
    # データベース接続
    connection = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, db=DATABASE)
    
    # SQLクエリの実行
    df = pd.read_sql('SELECT * FROM my_table', connection)
    
    # 接続のクローズ
    connection.close()

    # HTMLにデータを渡して表示
    return render_template('show3.html', data=df.to_dict(orient='records'))


# ルーティングを定義
@app.route('/')
def hello_World():
    return 'HelloWorld！'

@app.route('/hello')
def hello():
    return render_template("test.html",username="taro",data=data)

@app.route('/index')
def test2():
    return render_template("index.html",username="taro",data=data)

@app.route('/index')
def custom():
    return render_template("custom.html",username="taro",data=data)
@app.route('/aaa')
def custom2():
    return render_template("aaa.html",username="taro",data=data)
@app.route('/show2')
def custom3():
    return render_template("show2.html",username="taro",data=data)

@app.route('/show3')
def custom4():
    return render_template("show3.html",username="taro",data=data)

@app.route("/receive_get", methods=["GET"])
def receive_get():
        name = request.args["my_name"]
        print(name)
        # データベースの作成・接続とカーソル生成
        c = sqlite3.connect("test.db")
        cur = c.cursor()
        # データテーブルを作成する
        try:
            cur.execute("create table sample_table2(id integer primarykey auto_increment , date, text)")
        except:
            pass
        cur.execute(f"insert into sample_table2(id,text) values(1,'{name}');")
        c.commit()
        cur.execute('SELECT * FROM sample_table2')
        for row in cur:
            print(row)
        
        c.close()
        return render_template("custom.html")

@app.route('/show4')
def custom5():
    return render_template("for.html")



@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    name = data["name"]
    age = data["age"]

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO mytable(name, age) VALUES (%s, %s)", (name, age))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Data added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)







    















