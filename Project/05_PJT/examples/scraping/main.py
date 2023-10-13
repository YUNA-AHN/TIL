import requests
import bs4

# 현재 제출 현황을 스크래핑...!

cookies = {}
headers = {
    # 크롬 브라우저랑 안내를 해줄 수 있는 메시지
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://www.acmicpc.net/status',
                        cookies=cookies, headers=headers)


# HTML 파싱을 위해 beautifulsoup 사용
soup =  bs4.BeautifulSoup(response.text, 'html.parser')

# 테이블을 파싱
table = soup.select_one('#status-table')

# 테이블의 헤더들 출력
headers = table.find_all("th")
for header in headers:
    print(header.text, end=', ')

# 테이블의 데이터 출력
rows = table.find_all("tr")
for row in rows:
    tds = row.find_all("td")
    for td in tds:
        print(td.text, end = ", ")


# print(table.prettify())

