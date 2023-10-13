import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워지낟.
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # div  태그 중 g 클래스를 가진 모든 요소 선택
    g_list = soup.select('div.g')
    # 해당 요소를 반복하며
    for g in g_list:
        # 요소 안에 LC201b DKV0Md 클래스를 가진 특정 요소 선택
        title = g.select_one('.LC20lb.MBeuO.DKV0Md')
        # 요소가 존재한다면
        if title is not None:
            title_text = title.text
            print(f'제목 = {title_text}')

get_google_data('파이썬')