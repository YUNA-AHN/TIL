'''
완전 탐색
시작 -> 종료
DFS / BFS
'''

import sys

sys.setrecursionlimit(100000000)
sys.stdin = open("C:/Users/SSAFY/Downloads/input (1).txt", 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 현재 좌표 (x, y) 좌표에서 사방탐색을 진행하며 다음 좌표로 깊게 이동한다...
def dfs(maze, visited, x, y, end_x, end_y):
    # 현재 좌표 x, y 에 대한 방문체크
    visited[x][y] = True
    # 사방탐색을 진행하여 옆의 길로 이동한다
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 해당 좌표가 유효한지...
        # 갈 수 있는 통로인지...
        # 방문한적이 없는지...
        if 0 <= nx < 100 and 0 <= ny < 100 and maze[nx][ny] == 0 and visited[nx][ny] == False:
            dfs(maze, visited, nx, ny, end_x, end_y)

    if visited[end_x][end_y] == True:
        return 1
    else:
        return 0


T = 10


def bfs(maze, visited, start_x, start_y, end_x, end_y):
    q = []
    # 큐를 사용해서 너비 우선 탐색 BFS.
    # 시작점을 큐에 넣고... 방문 체크를 해준다.
    q.append([start_x, start_y])
    visited[start_x][start_y] = True
    maze[start_x][start_y] = 5

    # 큐가 빌 때까지 노드의 값을 뽑아내면서
    while len(q) > 0:
        x, y = q.pop(0)
        # 그 위치와 인첩한 노드를 다시 큐에 넣는다! (방문을 안한 노드)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 해당 되는 nx, ny 좌표가 유효하고,
            # 갈 수 있는 통로이면서
            # 방문을 아직 하지 않았으면 큐에 넣는다...
            if 0 <= nx < 100 and 0 <= ny < 100 and maze[nx][ny] == 0 and visited[nx][ny] == False:
                q.append([nx, ny])
                visited[nx][ny] = True
                maze[nx][ny] = 5
    # 완전탐색 : 갈 수 있는 경로를 모두 진행했으면
    # end_x, end_y 좌표에 visited 방문 체크가 되어있을 것...!
    if visited[end_x][end_y] == True:
        return 1
    else:
        return 0


for _ in range(1, T + 1):
    # 입력
    tc = int(input())
    # 미로 100 x 100
    maze = [list(map(int, input())) for _ in range(100)]

    # 메인로직
    # 출발점과 도착점에 대한 좌표를 확인한다.
    start_x = start_y = end_x = end_y = -1
    # 열 우선 순회를 해서 시작점과 도작점을 확인...
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            elif maze[i][j] == 3:
                end_x, end_y = i, j

    maze[start_x][start_y] = 0
    maze[end_x][end_y] = 0
    # DFS 재귀호출... 시작점 -> 도착점...
    # visited = [[False] * 100 for _ in range(100)]
    # answer = dfs(maze, visited, start_x, start_y, end_x, end_y)
    # BFS
    visited = [[False] * 100 for _ in range(100)]
    answer = bfs(maze, visited, start_x, start_y, end_x, end_y)

    # 출력
    print(f"#{tc} {answer}")