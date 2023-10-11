import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from bs4 import BeautifulSoup
import pandas as pd


cmd = 'pip install --upgrade chromedriver_binary' 
res = subprocess.call(cmd, shell=True)
url = "https://go-resol-hotel.reservation.jp/ja/hotels/trinity-naha/rooms/10017293?_ga=2.10783924.1442734765.1697063444-1405639140.1697063444&_gl=1*gq2m8k*_ga*MTQwNTYzOTE0MC4xNjk3MDYzNDQ0*_ga_XMWVW0YK44*MTY5NzA2MzQ0My4xLjEuMTY5NzA2MzQ1My41MC4wLjA."
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
r = requests.get('https://go-resol-hotel.reservation.jp/ja/hotels/trinity-naha/rooms/10017293?_ga=2.10783924.1442734765.1697063444-1405639140.1697063444&_gl=1*gq2m8k*_ga*MTQwNTYzOTE0MC4xNjk3MDYzNDQ0*_ga_XMWVW0YK44*MTY5NzA2MzQ0My4xLjEuMTY5NzA2MzQ1My41MC4wLjA.' + str(img['src']))
with open(f'test.jpg', 'wb') as f:
    f.write(r.content) 
div=soup.find_all('table') [0]
print(div.find("tr"))
print(div.find("th"))
print(div.find("td"))
col_data = []
col_list = []
data = []
for tr in div.find_all('tr'):
#     print(tr)
#     print('列名:',tr.find('th').text,'列にいれる値:',tr.find('td').text)
    
    col_list.append(tr.find('th').text)
    data.append(tr.find('td').text.replace("¥n",""))
col_data.append(data)

df = pd.DataFrame(col_data,columns=col_list)
df.to_csv('reservation.csv',index=False)

