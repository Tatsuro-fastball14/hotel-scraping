import requests
from bs4 import BeautifulSoup

# スクレイピングしたいURL
url = 'https://www.expedia.co.jp/'

# URLからHTMLを取得
response = requests.get(url)
response.raise_for_status()  # エラーがあれば例外を発生させる

# HTMLをBeautifulSoupで解析
soup = BeautifulSoup(response.content, 'html.parser')

# 例: タイトルを取得
title = soup.title.string
print(title)

# その他の情報もこのようにして取得可能





