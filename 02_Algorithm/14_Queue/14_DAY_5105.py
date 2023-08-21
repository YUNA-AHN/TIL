'''
미로의 거리
출발지에서 도착지 : 최소 몇 개의 칸?1
경로가 있는 경우 최소한의 칸 수, 경로가 없는 경우는 0 출력
'''
def bfs(maze, visited, sx, sy):
    que = []
    que.append([sx, sy])
    visited[sx][sy] = 1
    while que:
        i, j = que.pop(0)
        for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                que.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    sx = sy = ex = ey = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sx, sy = i, j
            elif maze[i][j] == 3:
                ex, ey = i, j

    # 방문 체크열
    visited = [[0] * n for _ in range(n)]

    bfs(maze, visited, sx, sy)

    if visited[ex][ey]: # 방문을 했다면
        # 시작점과 도착점 제외
        ans = visited[ex][ey] - 2
    else:
        ans = 0

    print(f'#{tc} {ans}')
