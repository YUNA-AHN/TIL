# 나의 풀이
N = int(input())
arr = [list(map(int, input())) for _ in range(N)] # 집 위치 지도
visited = [[False] * N for _ in range(N)] # 방문 체크 리스트

# 상하좌우 델타
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


cnt = 0 # 단지내 집 수 카운트

def dfs(x, y):
    global cnt
    cnt += 1
    # 현재 좌표에 방문 체크하고, 카운트를 1 더한다 : 총 단지 수 구해야하니까
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상하좌우를 돌면서 인덱스가 넘어가는지 테크
        # 해당 좌표에 집이 있는지? 방문한 적은 없는지 확인
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)

# 단지의 집수를 저장하는 리스트
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt = 0 # cnt 초기화
            dfs(i, j) # dfs 진행
            ans.append(cnt)

# 오름차순 정렬
ans.sort()

# 그 값을 각 줄에 출력
print(len(ans))
for i in ans:
    print(i)