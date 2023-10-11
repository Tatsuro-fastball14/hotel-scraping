from flask import Flask, render_template
import pandas as pd 
df=pd.read_csv("/Users/tatsuro/projects/hotel-scraping/test.csv")
df=df[["アクセス",""]]
row_list = df.iloc[0, :].tolist()
print(row_list)

# クラス呼び出し
app = Flask(__name__)

# ルーティングを定義
@app.route('/reservation')
def hello():
    return render_template("reservation.html",username="taro",data=row_list)

# サーバー起動
app.run(debug=True)



@app.route('/access')
def index3():
    # データベース接続
    connection = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, db=DATABASE)
    
    # SQLクエリの実行
    df = pd.read_sql('SELECT * FROM my_table', connection)
    
    # 接続のクローズ
    connection.close()

    # HTMLにデータを渡して表示
    return render_template('show3.html', data=df.to_dict(orient='records'))

