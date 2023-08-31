'''
화물 도크
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 종료시간, 시작시간 순으로 정렬
    arr.sort(key = lambda x : (x[1], x[0]))

    arr = [[0, 0]] + arr
    cnt = i = 0

    for j in range(1, n+1):
        if arr[j][0] >= arr[i][1]:
            cnt += 1
            i = j

    print(f'#{tc} {cnt}')