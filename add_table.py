import pandas as pd
import pymysql
from sqlalchemy import create_engine

# データベースの接続設定
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'test'

# SQLAlchemyを使用してMySQLに接続
engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}")

# CSVファイルを読み込む
df = pd.read_csv('/Users/tatsuro/projects/hotel-scraping/test2.csv')

# データフレームをMySQLテーブルにインポート
df.to_sql('my_table', engine, index=False, if_exists='replace')

print("CSV has been imported into MySQL!")
