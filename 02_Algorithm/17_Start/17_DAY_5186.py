'''
이진수2
0보다 크고 1미만인 십진수 N을 이진술 바꾸려고 한다
13자리 이상 필요한 경우 overflow
'''
T = int(input())
for tc in range(1,T+1):
    num = int(input())

    for i in range(13):
