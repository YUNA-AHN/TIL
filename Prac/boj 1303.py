'''
전투
우리 병사 W 적군 B
n명이 뭉쳐있으면 n**2 위력
우리 위력의 합과 적군 위력의 합
'''
# dfs 함수 생성
def dfs(color, i, j):
    '''
    :param color: 찾고자 하는 색상
    :param i: 시작 행 인덱스
    :param j: 시작 열 인덱스
    :return: 없음
    '''
    global visited, cnt
    # 시작점 방문 체크
    visited[i][j] = 1
    # 방문할 떼 마다 +1
    cnt += 1

    # 상하좌우 순회하면서 방문하지 않았고, 찾고자 하는 색상인 경우 dfs 진행
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == color:
            dfs(color, ni, nj)


import sys
input = sys.stdin.readline
m, n = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(n)]

# 방문 체크열
visited = [[0] * m for _ in range(n)]

# 흰색의 총 전력, 파란색의 총 전력
w_total = b_total = 0

# 모든 인덱스 순회
for i in range(n):
    for j in range(m):
        # 흰색이고, 방문 이력이 없다면
        if arr[i][j] == 'W' and visited[i][j] == 0:
            cnt = 0
            dfs('W', i, j)
            w_total += cnt ** 2 # cnt의 제곱

        # 파란색이고, 방문 이력이 없다면
        if arr[i][j] == 'B' and visited[i][j] == 0:
            cnt = 0
            dfs('B', i, j)
            b_total += cnt ** 2

print(w_total, b_total)