'''
미로
'''
def dfs(x, y):
    global visited

    # 방문체크
    visited[x][y] = True
    
    # 사방탐색
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    for i in range(4):
        ni = x + di[i]
        nj = y + dj[i]
        
        # 범위내에 존재하고 아직 방문하지 않았나요?
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == False:
            # 아직 방문하지 않았다면, 도세요 !
            if arr[ni][nj] == 0:
                dfs(ni, nj)
            # 도착지라면, 방문체크 후 종료
            elif arr[ni][nj] == 3:
                visited[ni][nj] = True
                return


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    
    # 방문 체크용
    visited = [[False] * n for _ in range(n)]

    # 시작점과 끝점 : 둘이 안주어지는 경우가 있는가?
    sx, sy, ex, ey = 0, 0, 0, 0
    # 인덱스 순회하면서 시작점과 끝점 탐색
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                sx, sy = i, j
            elif arr[i][j] == 3:
                ex, ey = i, j

    dfs(sx, sy)
    
    # 탐색 후에 간 적 있는지 체크
    if visited[ex][ey] == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')




# # 강사님
# di = [0, 0, -1, 1]
# dj = [-1, 1, 0, 0]
#
#
# # (i, j) 좌표로부터 상하좌우 순회 (완탐진행)
# def dfs(i, j, visited):
#     # 방문체크
#     visited[i][j] = True
#
#     # 사방탐색 (상하좌우)
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         # 갈 수 있는 경로인지 확인 (+방문체크)
#         if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in [0, 3] and visited[ni][nj] == False:
#             dfs(ni, nj, visited)
#
#
# # -> 도착할 수 있다면 1, 없다면 0 반환
# def solution(arr, N):
#     # 시작점, 종착점
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:  # 시작점
#                 sx, sy = i, j
#             elif arr[i][j] == 3:  # 종착점
#                 ex, ey = i, j
#     visited = [[False] * N for _ in range(N)]
#     # DFS 탐색... 시작점 -> 종착점 여부... (재귀함수)
#     dfs(sx, sy, visited)
#
#     # 만약 종착점에 방문했다면 해당 (ex, ey) 좌표에 visited 가 체크가 되어있을 것..
#     if visited[ex][ey] == True:
#         return 1
#     else:
#         return 0
#
#
# # 테스트케이스
# T = int(input())
#
# for tc in range(1, T + 1):
#     # 입력
#     # N 미로의 길이
#     N = int(input())
#     # arr 미로
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     # 메인로직, 완탐 DFS,,, 재귀함수
#     result = solution(arr, N)
#
#     # 출력
#     print(f"#{tc} {result}")