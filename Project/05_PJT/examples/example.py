import requests
from bs4 import BeautifulSoup

def crawling_basic():
    # 가져올 웹페이지 url
    url = 'https://quotes.toscrape.com/tag/love/'

    response = requests.get(url)

    # 우리가 얻고자 하는 HTML 내용이 여기에 단긴다
    html_text = response.text

    # HTML을 파싱 가능한 정리된 형태로 변환
    soup = BeautifulSoup(html_text, 'html.parser')

    # 예쁘게 출력하기
    # print(soup.prettify())

    # 1. 태그로 검색하기
    # 1.1 가장 첫 번째 태그에 해당하는 요소
    title = soup.find('a')
    print(f'제목: {title.text}')

    # 1.2 해당 태그 모든 요소
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        print(f'링크: {a_tag}')

    # 2. CSS 선택자로 검색하기
    # 2.1 첫 번째로 CSS 선택자와 일치하는 요소 : class
    word = soup.select_one('.text')
    print(f'첫 번째 글 = {word.text}')

    # 2.2 CSS 선택자와 일치하는 모든 요소
    words = soup.select('.text')
    for w in words:
        print(f'글 : {w.text}')

    # 파일로 저장하기
    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

crawling_basic()