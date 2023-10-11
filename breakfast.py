@app.route('/table2')
def index4():
    # データベース接続
    connection = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, db=DATABASE)
    
    # SQLクエリの実行
    df = pd.read_sql('SELECT * FROM my_table', connection)
    
    # 接続のクローズ
    connection.close()

    # HTMLにデータを渡して表示
    return render_template('show3.html', data=df.to_dict(orient='records'))



from flask import Flask, render_template
import pandas as pd 
from datetime import datetime
from flask import request
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import pymysql
import sqlite3


df=pd.read_csv("/Users/tatsuro/projects/hotel-scraping/test2.csv")
df["imgurl"]="https://images.trvl-media.com/lodging/36000000/35740000/35736500/35736430/788d05ca.jpg?impolicy=resizecrop&rw=1200&ra=fit"
data = [list(e) for e in zip(df['hotel_name,breakfast'],df['眺望'],df["お部屋の設備"],df["バスルームの設備"])]
print(data)
