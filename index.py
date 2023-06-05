from flask import Flask, render_template
import pandas as pd 
df=pd.read_csv("/Users/tatsuro/projects/hotel-scraping/test.csv")
df=df[["宿泊人数","眺望"]]
row_list = df.iloc[0, :].tolist()
print(row_list)

# クラス呼び出し
app = Flask(__name__)

# ルーティングを定義
@app.route('/index')
def hello():
    return render_template("index.html",username="taro",data=row_list)

# サーバー起動
app.run(debug=True)