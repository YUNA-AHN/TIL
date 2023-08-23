'''
암호생성기
n개의 수 처리하면 8자리의 암호 생성
- 8개 숫자 입력
- 첫번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
- 다음 첫번재 수는 2 감소한 뒤 맨뒬 ..
- 숫자가 0보다 작아지는 경우 0으로 유지, 프로그램은 종료
'''
from collections import deque

for _ in range(10):
    tc = int(input())
    arr = deque(map(int, input().split()))

