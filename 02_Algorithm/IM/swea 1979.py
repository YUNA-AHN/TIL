'''
어디에 단어가 들어갈 수 있을까?
'''
T = int(input())
for tc in range(1, T+1):
    n, k = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    lst = []
    # 가로
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                lst.append(cnt)
                cnt = 0
            if j == n-1:
                lst.append(cnt)
                cnt = 0

    # 세로
    cnt = 0
    for j in range(n):
        for i in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                lst.append(cnt)
                cnt = 0
            if i == n - 1:
                lst.append(cnt)
                cnt = 0

    print(f'#{tc} {lst.count(k)}')
