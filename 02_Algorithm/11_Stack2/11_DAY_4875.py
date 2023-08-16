'''
미로
'''

# 강사님
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


# (i, j) 좌표로부터 상하좌우 순회 (완탐진행)
def dfs(i, j, visited):
    # 방문체크
    visited[i][j] = True

    # 사방탐색 (상하좌우)
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        # 갈 수 있는 경로인지 확인 (+방문체크)
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in [0, 3] and visited[ni][nj] == False:
            dfs(ni, nj, visited)


# -> 도착할 수 있다면 1, 없다면 0 반환
def solution(arr, N):
    # 시작점, 종착점
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 시작점
                sx, sy = i, j
            elif arr[i][j] == 3:  # 종착점
                ex, ey = i, j
    visited = [[False] * N for _ in range(N)]
    # DFS 탐색... 시작점 -> 종착점 여부... (재귀함수)
    dfs(sx, sy, visited)

    # 만약 종착점에 방문했다면 해당 (ex, ey) 좌표에 visited 가 체크가 되어있을 것..
    if visited[ex][ey] == True:
        return 1
    else:
        return 0


# 테스트케이스
T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N 미로의 길이
    N = int(input())
    # arr 미로
    arr = [list(map(int, input())) for _ in range(N)]

    # 메인로직, 완탐 DFS,,, 재귀함수
    result = solution(arr, N)

    # 출력
    print(f"#{tc} {result}")