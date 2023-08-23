'''
농작물 수확하기
n*n  농장
농장의 크기는 항상 홀수
수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    sum_v = 0
    for i in range(n//2 + 1): # n//2번행까지
        for j in range(n//2 - i, n//2 + i + 1): # 중심에서 i만큼 떨어져있는 곳까지
            sum_v += arr[i][j]  # 더해주기!
            sum_v += arr[n - i - 1][j] # 역순도 더해주기!

    for k in range(n): # 두번 더해진 중간줄 빼주기
        sum_v -= arr[n//2][k]

    print(f'#{tc} {sum_v}')
