'''
풍선팡
꽃가루 든 풍선 M개씩 N개의 줄
꽃가루 개수만큼 상하 좌우의 풍선 추가로 터지는 게임

꽃가루가 1개씩일 때 - 가운데 터뜨리면 상하좌우 추가로 1개씩 터지면 5개의 꽃가루
한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력
'''

T = int(input())

for tc in range(1, T+1):
    r, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(r)]

    # 델타 검색
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    best_v = 0 # 꽃가루의 최대 개수
    for r_idx in range(r):
        for c_idx in range(c):
            N = arr[r_idx][c_idx] # 꽃가루의 개수
            sum_v = N
            for i in range(1, N+1): # 꽃가루의 개수만큼 상하좌우 칸을 늘려서 더해줌
                for j in range(len(di)):
                    ni = r_idx + di[j] * i
                    nj = c_idx + dj[j] * i
                    if 0 <= ni < r and 0 <= nj < c:
                        sum_v += arr[ni][nj]
            best_v = max(best_v, sum_v)

    print(f'#{tc} {best_v}')