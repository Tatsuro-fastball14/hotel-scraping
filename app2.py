# ライブラリ呼び出し
from flask import Flask, render_template
import pandas as pd 
from datetime import datetime



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

# SQLAlchemyでデータベースに接続する
db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri


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





# サーバー起動
app.run(debug=True)


