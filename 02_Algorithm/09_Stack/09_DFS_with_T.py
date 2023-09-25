
"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# V : 정점의 갯수, E : 간선의 갯수
V, E = map(int, input().split())  # [ 7, 8 ]

# 정점사이의 연결 정보
adj = list(map(int, input().split()))  # [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접행렬 초기화(노드 - 노드 저장할 수 있는 V x V 이차원 배열)
graphs = [[0] * (V + 1) for _ in range(V + 1)]

# 인덱스로 순회...
for idx in range(0, len(adj), 2):
    u = adj[idx]
    v = adj[idx + 1]

    # u 정점 -> v 정점으로 이동...
    graphs[u][v] = 1
    # v 정점 -> u 정점으로 이동...
    graphs[v][u] = 1

# 방문 체크 배열
visited = [False for _ in range(V + 1)]


# 인접행렬을 통해서 DFS 탐색
def dfs1(v):
    global visited
    print(v, end='-')
    visited[v] = True
    # v 노드에서 갈 수 있는 노드를 확인 (인접한 노드)
    for u in range(len(graphs)):
        # 방문 체크
        if visited[u] == True:
            continue
        if graphs[v][u] == 1:  # 내가 갈 수 있는 인접 노드
            # v -> u 이동을 해서 탐색을 진행
            dfs1(u)


dfs1(1)

print()


# 인접리스트 초기화 (해당정점 - 인접한 정점에 대한 리스트 )
graphs = [[] for _ in range(V + 1)]

# 인덱스로 순회...
for idx in range(0, len(adj), 2):
    u = adj[idx]
    v = adj[idx + 1]

    # u 정점 -> v 정점으로 이동...
    graphs[u].append(v)
    # v 정점 -> u 정점으로 이동...
    graphs[v].append(u)

# 방문 체크 배열
visited = [False for _ in range(V + 1)]

# 인접리스트를 통해서 DFS 탐색
def dfs2(v):
    global visited
    print(v, end='-')
    visited[v] = True
    # v 노드에서 갈 수 있는 노드를 확인 (인접한 노드)
    for u in graphs[v]:
        if visited[u] == True:  # 방문을 했다면
            continue
        # 방문을 하지 않았다면 방문을 진행
        dfs2(u)


dfs2(1)

