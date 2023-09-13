import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(r):
    global visited, cnt
    cnt+=1

    for i in sorted(arr[r]):
        if visited[i] == 0:
            visited[i] = cnt + 1
            dfs(i)

# 정점의 수, 간선의 수, 시작 정점
n, m, r = map(int, input().strip().split())

# 인접행렬, 방문 체크열 생성
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().strip().split())
    arr[u].append(v)
    arr[v].append(u)

cnt = 0
# 시작 노드 방문 체크
visited[r] = 1
dfs(r)

for k in visited[1:]:
    print(k)
