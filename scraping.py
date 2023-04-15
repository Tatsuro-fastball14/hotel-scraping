import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary 
import requests
from bs4 import BeautifulSoup
import sqlite3
import MySQLdb
import mysql.connector
import  csv
import pandas as pd
from sqlalchemy import create_engine



cmd = 'pip install --upgrade chromedriver_binary' 
res = subprocess.call(cmd, shell=True)
url = "https://hyattregencynaha.jp/guestroom/club-twin.html"
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'performance': 'ALL' }
def new_func(d):
    return webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=d)
   

driver = new_func(d)
driver.set_window_size('1200','1000')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(driver.page_source)
div=soup.find_all('div', class_="contents_outer next")
img = soup.find('div', class_='inner g3 sg3 ssg6 sspush3') .find('img', class_='fit')
print(img['src'])
r = requests.get('https://hyattregencynaha.jp/guestroom/' + str(img['src']))
with open(f'test.jpg', 'wb') as f:
    f.write(r.content) 
div=soup.find_all('table') [0]
print(div.find("tr"))
print(div.find("th"))
print(div.find("td"))
col_data = []
col_list = []
data = []
import pandas as pd
for tr in div.find_all('tr'):
#     print(tr)
#     print('列名:',tr.find('th').text,'列にいれる値:',tr.find('td').text)
    
    col_list.append(tr.find('th').text)
    data.append(tr.find('td').text.replace("¥n",""))
col_data.append(data)

df = pd.DataFrame(col_data,columns=col_list)
df.to_csv('test.csv',index=False)

df =pd.read_csv('test csv')
with mysql.connect('example.db')as conn:
    df.to_sql('example_table',conn, if_exists='replace',index=False)

print

# 接続する 
conn = MySQLdb.connect(
 unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock',
 user='root',
 passwd='root',
 host='localhost',
 db='mysql')

# カーソルを取得する
cur = conn.cursor()

# SQL（データベースを操作するコマンド）を実行する
# userテーブルから、HostとUser列を取り出す
sql = "select Host, User from user"
cur.execute(sql)

# 実行結果を取得する
rows = cur.fetchall()

# 1行ずつ表示する
for row in rows:
 print(row)

cur.close
conn.close




df = pd.DataFrame(col_data,columns=col_list)
df.to_csv('test.csv',index=False) 
f = open('myfile.txt', 'w')
f.write(str(div))
f.close() 


#Mysqlコネクタの設定
cnx= mysql.connector.connect(user='ユーザー名',password='パスワード')
host='ホスト名'
database='データベース名'

#csvファイルを開いてデータを読み込む
with open('test.csv', newline=''as csvfile:)
    reader  =   csv.reader(csvfile, delimiter=',',  quotechar='')
    next(reader)
    for row in reader:
        add_data('INSERT INTO'テーブル名")

#変更をコミットする
    cnx.commit()

#Mysqlコネクタをクローズする
 cursor.close()
 cnx.close()

 CREATE DATABASE testdb;
> CREATE TABLE testdb.mysql_table(
    col1 int
    ,col2 int
    ,col3 int
  );

df = pd.DataFrame([[1,2,3],[4,5,6]],columns=['col1','col2','col3'])
print(df)

#engine = create_engine('mysql://<user>:<password>@<host>/<database>?charset=utf8')
engine = create_engine('mysql://user:password@localhost/test_db?charset=utf8')
 
#df.to_sql(<table_name>,con=engine, if_exists='append', index=False)
df.to_sql('testdb.mysq_table',con=engine, if_exists='append', index=False)


