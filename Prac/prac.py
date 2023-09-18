'''
A와 B
문자열 S를 T로 바꾸는 게임
문자열 뒤에 A 추가하기
문자열 뒤집고 B 추가하기
'''
import sys
input = sys.stdin.readline

s = input().strip()
t = list(input().strip())

n = len(s)
ans = 0

for i in t[::-1]:
    if len(t) == n:
        if ''.join(t) == s:
            ans = 1
        break
    if i == 'B':
        t.pop()
        t.reverse()
    else:
        t.pop()

print(ans)