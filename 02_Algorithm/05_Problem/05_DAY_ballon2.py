'''
풍선팡
꽃가루 든 풍선 M개씩 N개의 줄
상하 좌우의 풍선 추가로 터지는 게임
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
            sum_v = arr[r_idx][c_idx]
            for j in range(len(di)): # 상하좌우의 꽃가루 개수 더해줌
                ni = r_idx + di[j]
                nj = c_idx + dj[j]
                if 0 <= ni < r and 0 <= nj < c:
                    sum_v += arr[ni][nj]
            best_v = max(best_v, sum_v)

    print(f'#{tc} {best_v}')