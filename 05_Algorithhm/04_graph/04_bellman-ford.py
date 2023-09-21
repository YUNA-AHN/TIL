'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# 입력 처리 (그래프: 인접 리스트)
V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
     u, v, w = map(int, input().split())
     # 양방향 그래프 (무향 그래프) # u -> v, v -> u
     graph[u].append((v, w)) # u -> v, 가중치 : w
     graph[v].append((u, w))  # u -> v, 가중치 : w

# 벨만-포드 알고리즘
# 모든 간선(E)에 대해서 정점 갯수 - 1 만큼(V-1) 최소 비용 경로를 계속 갱신한다...!
def bellman_ford(graph, start):
    edges = []  # 모든 간선에 대한 정보
    for u in range(V):
        for v, w in graph[u]:
            edges.append((u, v, w))

    # 경로의 최소 비용을 담는 배열 dist
    dist = [float('inf')] * V
    dist[start] = 0  # 시작점에 대한 비용을 0 초기화

    # 시간복잡도 O(E*V)
    # 정점 갯수 - 1 (V - 1) 만큼 반복해준다
    for _ in range(V - 1):
        # 모든 간선 E 에 대해서 dist (경로의 최소값을 갱신)
        for u, v, w in edges:
            new_cost = dist[v] + w
            if dist[u] > new_cost:
                dist[u] = new_cost

    return dist


# 시작 정점 0
start = 0
shortest_dist = bellman_ford(graph, start)
print(shortest_dist)

# 모든 정점 -> 모든 정점
# 플루이드 워샬 알고리즘...
def floyd_warshall(graph):
    # 최소 비용을 계산하는 dist 배열... 이차원 배열 V x V
    dist = [[float('inf')] * V for _ in range(V)]

    # i -> i (자기자신으로 가는) 정점의 최소비용: 0
    for i in range(V):
        dist[i][i] = 0

    # 인접 리스트에서 모든 간선 정보를 가져와서 최소 비용 갱신
    for u in range(V):
        for v, w in graph[u]:
            dist[u][v] = w

    # i -> k -> j 최소 비용으로 계속 갱신 시도!
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # i ---> j : i ----> k ----> j
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


shortest_dist = floyd_warshall(graph)
for row in shortest_dist:
    print(row)