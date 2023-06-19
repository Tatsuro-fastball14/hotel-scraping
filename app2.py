# ライブラリ呼び出し
from flask import Flask, render_template
import pandas as pd 
df=pd.read_csv("/Users/tatsuro/projects/hotel-scraping/test.csv")
data = [list(e) for e in zip(df['宿泊人数'],df['眺望'],df["お部屋の設備"],df["バスルームの設備"])]
print(data)

# クラス呼び出し
app = Flask(__name__)

# ルーティングを定義
@app.route('/')
def hello_World():
    return 'HelloWorld！'

@app.route('/hello')
def hello():
    return render_template("test.html",username="taro",data=data)

@app.route('/test2')
def hello():
    return render_template("test2.html",username="taro",data=data)


# サーバー起動
app.run(debug=True)


