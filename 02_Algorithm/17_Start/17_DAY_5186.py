'''
이진수2
0보다 크고 1미만인 십진수 N을 이진술 바꾸려고 한다
13자리 이상 필요한 경우 overflow
2 ** (-1)로 나눈 나머지로 계속 나눔
'''
T = int(input())
for tc in range(1,T+1):
    num = float(input())

    binary = ''
    for i in range(13):
        binary += str(int(num // 2 ** (-i)))
        num = num % 2 ** (-i)
        if num == 0:
            break
    if num:
        ans = 'overflow'
    else:
        ans = binary[1:]

    print(f'#{tc} {ans}')
