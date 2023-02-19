import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary 
import requests
from bs4 import BeautifulSoup

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
f = open('myfile.txt', 'w')
f.write(str(div))
f.close() 
