edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접 행렬 : 이차원 배열에 저장
# u -> v : graph[u][v] = 1
#
# # 정점의 개수
# v = 7
# graph = [[0] * (v+1) for _ in range(v+1)]
#
# for idx in range(0, len(edges), 2):
#     u = edges[idx]
#     v = edges[idx+1]
#     # 정점의 연결 정보를 인접 행렬에 저장
#     graph[u][v] = 1
#     graph[v][u] = 1



# 정점의 개수
v = 7

# 인접 리스트 : 해당 정점 -> 인접한 정점들
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for idx in range(0, len(edges), 2):
    u = edges[idx]
    v = edges[idx+1]

    # 정점의 연결 정보를 인접 리스트에 저장
    graph[u].append(v) # u -> v
    graph[v].append(u) # v -> u

def dfs(current, visited):
    visited[current] = True
    print(current, end = '->')
    for nxt in graph[current]:
        if visited[nxt]:
            continue
        dfs(nxt, visited)

dfs(1, visited)
print()

# bfs 순회 (큐 자료형)
def bfs(current):
    visited = [False] * (v + 1)
    que = []
    que.append(current)
    visited[current] = True
    while que:
        node = que.pop(0)
        print(node, end="->")
        for nxt in graph[node]:
            if not visited[nxt]:
                que.append(nxt)
                visited[nxt] = True

bfs(1)