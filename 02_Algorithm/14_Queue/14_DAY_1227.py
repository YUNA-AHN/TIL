'''
미로 100 * 100
최상단의 칸 (0, 0) 기준
가로 방향 x. 세로 방향 y
미로 시작점에서 도착점까지 도달이 가능할까?!
'''
import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input (1).txt", 'r')

def bfs(maze, visited, sx, sy, ex, ey):
    que = [] # 빈 큐 생성
    que.append([sx, sy]) # 시작점 입력
    visited[sx][sy] = True
    while que:
        i, j = que.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1], [0, -1], [-1, 0], [1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 100 and 0 <= nj < 100 and visited[ni][nj] == False and maze[ni][nj] != 1:
                que.append([ni, nj])
                visited[ni][nj] = True

    if visited[ex][ey] == True:
        return 1
    else:
        return 0




for tc in range(1, 11):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    # 시작점과 도착점 찾기
    sx, sy, ex, ey = 0, 0, 0, 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:  # 시작점 좌표
                sx, sy = i, j
            if maze[i][j] == 3:  # 도착점 좌표
                ex, ey = i, j

    visited = [[False] * 100 for _ in range(100)]

    ans = bfs(maze, visited, sx, sy, ex, ey)

    print(f'#{n} {ans}')
