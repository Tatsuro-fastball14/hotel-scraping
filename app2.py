# ライブラリ呼び出し
from flask import Flask, render_template
import pandas as pd 
from datetime import datetime
from flask import request



df=pd.read_csv("/Users/tatsuro/projects/hotel-scraping/test.csv")
data = [list(e) for e in zip(df['宿泊人数'],df['眺望'],df["お部屋の設備"],df["バスルームの設備"])]
print(data)

# クラス呼び出し
app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemyでデータベースに接続する
db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

import sqlite3





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





# サーバー起動
app.run(debug=True)


