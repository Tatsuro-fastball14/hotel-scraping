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







    















