# # MySQLdbのインポート
# import MySQLdb


# # データベースへの接続とカーソルの生成
# connection = MySQLdb.connect(
#     host='localhost',
#     user='root',
#     passwd='',
#     db='create_test2')
# cursor = connection.cursor()

# cursor.execute("INSERT INTO users VALUES (4, '木下');")
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#   print (row)
 
# # 保存を実行
# connection.commit()
 
# # 接続を閉じる
# connection.close()

import pandas as pd
import pymysql.cursors
from sqlalchemy import create_engine
df = pd.DataFrame([[1,'犬'],[2,'猫'],[3,'サル'],[4,'鶏']])
df = pd.read_csv('/Users/tatsuro/projects/hotel-scraping/test.csv')
host = 'localhost' # ローカルホスト
port = 3306 # ポート番号
user = 'root' # ユーザー名
passwd = '' # パスワード
db = 'create_test2' # データベース名


# engine = create_engine("mysql:///?User=root&;Password=&Database=create_test2&Port=3306")
engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}", echo=False)
df.to_sql(
    name = 'test',
    con = engine,
    if_exists='replace', 
    index = False,
    chunksize = 10000,
    )
print('処理完了')




    