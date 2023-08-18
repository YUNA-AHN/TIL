'''
풍선팡
N*N 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터짐
해당 풍선의 꽃가루 갯수 만큼 상하좌우의 방향에 있는 풍선들이 터짐
최댓값과 최솟값의 차
'''
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 최댓값과 최솟값 생성
    mx = 0
    mn = 10000000

    # 모든 칸을 순회
    for r_idx in range(n):
        for c_idx in range(n):
            flower = arr[r_idx][c_idx] # 해당 칸의 꽃가루 수
            sum_v = flower # 해당 칸의 풍선을 터트렸을 때 총 꽃가루 수
            for i in range(1, flower + 1): # 풍선의 꽃가루 수 만큼
                for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]: # 상하좌우 순회
                    ni = r_idx + di * i
                    nj = c_idx + dj * i
                    if 0 <= ni < n and 0 <= nj < n:
                        sum_v += arr[ni][nj]
            mx = max(mx, sum_v) # 최댓값
            mn = min(mn, sum_v) # 최솟값

    ans = mx - mn
    print(f'#{tc} {ans}')