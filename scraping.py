import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary 
import requests
from bs4 import BeautifulSoup
import sqlite3
import mysql
import mysql.connector

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

df = pd.DataFrame(col_data,columns=col_list)
df.to_csv('test.csv',index=False) 
f = open('myfile.txt', 'w')
f.write(str(div))
f.close() 
