import openpyxl
import csv
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
    print(f'{i}.{title}')

# 將新聞標題存儲到 Excel 檔案中
filepath = r"C:\\Users\\user\\Desktop\\news_titles.xlsx"

workbook = openpyxl.Workbook()
worksheet = workbook.active

# 在第一列中寫入新聞標題
for i, title in enumerate(titles[:10], 1):
    worksheet.cell(row=i, column=1, value=title)

# 儲存 Excel 檔案
workbook.save(filepath)

print("新聞標題已成功儲存到 Excel 檔案中。")
