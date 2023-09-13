'''
단지번호 붙이기
'''
def dfs(i, j):
    global visited, cnt
    visited[i][j] = 1
    cnt += 1 # dfs 호출시마다 + 1

    for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and visited[ni][nj] == 0:
            dfs(ni, nj)

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]

# 방문 체크 열 생성
visited = [[0] * n for _ in range(n)]

total = []
for i in range(n):
    for j in range(n):
        # 건물이 존재하고, 방문한 적이 없다면
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            # 건물 수 리스트에 추가
            total.append(cnt)

# 단지 수
print(len(total))
# 각 단지 내 건물 수
for k in sorted(total):
    print(k)