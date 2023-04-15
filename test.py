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
from pip._internal.utils.compatibility_tags
import get_supportedprint(get_supported())
import pandas as pd
from sqlalchemy import create_engine
df = pd.DataFrame([[1,'犬'],[2,'猫'],[3,'サル'],[4,'鶏']])

engine = create_engine("mysql:///?User=root&;Password=&Database=create_test2&Port=3306")
df.to_sql(
    name = 'test',
    con = engine,
    if_exists='replace', 
    index = False,
    chunksize = 10000,
    )





    