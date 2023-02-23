from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import sqlite3
from flask import pandas as pd

app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# SQLAlchemyでデータベースに接続する
db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

# テーブルの中身をクラスとして定義する
class order_table(db.Model):
    orderid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    goods_number = db.Column(db.Integer)
    payment = db.Column(db.Text())

    def __init__(self, pub_date, goods_number, payment):
        self.pub_date = pub_date
        self.goods_number = goods_number
        self.payment = payment


# テーブルに追加するデータ
date = datetime.now()
goods_number = 810
payment = 'cash'

# テーブルにデータを追加する
add_data = order_table(date,goods_number,payment)
db.session.add(add_data)

# テーブルへの変更を保存する
db.session.commit()

#db作成
dbname="hotel.db"

#dbコネクト
conn = sqlite3.connect(dbname)
c = conn.cursor()

#作成したdbを見てみる
select_sql = 'select * from scraping.py'
for row in c.execute(select_sql):
    print(row)

conn.close()

