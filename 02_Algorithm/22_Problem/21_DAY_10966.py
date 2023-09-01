'''
물놀이를 가자
NxM 물이면 W 땅이면 L
상하좌우에 있는 칸 반복
물에서 출발...?

자리별로 걸리는 시간을 리스트로 받고 최솟값으로 다 더하기
'''
from collections import deque

t = int(input())
for tc in range(1, t+1):
    # NxM 데이터 입력
    n, m = map(int, input().split())
    visited = [[-1] * m for _ in range(n)]

    que = deque()
    for i in range(n):
        arr = input()
        for j in range(m):
            if arr[j] == 'W':
                visited[i][j] = 0
                que.append((i,j))

    sv = 0
    while que:
        i, j = que.popleft()
        for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                que.append((ni, nj))
                sv += visited[ni][nj]


    print(f'#{tc} {sv}')