import requests
from bs4 import BeautifulSoup

# 發送 HTTP GET 請求
url = 'https://www.bbc.com/zhongwen/trad'  # 替換為你要爬取的新聞網站的URL
response = requests.get(url)

# 解析 HTML 內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到新聞標題元素
title_elements = soup.find_all(
    'a', class_='focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0')

# 提取標題文字
titles = [element.text for element in title_elements]

# 輸出前10筆新聞標題
for i, title in enumerate(titles[:10], 1):
    print(f'{i}. {title}')
