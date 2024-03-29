from app2 import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# SQLAlchemyでデータベースに接続する ※test.dbがない場合は自動的に作成されます
db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


# データベースの仕様をクラスで定義する
class order_table(db.Model):
    orderid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    goods_number = db.Column(db.Integer)
    payment = db.Column(db.Text())

    # ※order_idはプライマリキー(自動で値が挿入される)ので、要らない
    def __init__(self, pub_date, goods_number, payment):
        self.pub_date = pub_date
        self.goods_number = goods_number
        self.payment = payment

# テーブルを作成する
db.create_all()
print('ok')