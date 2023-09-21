'''
일단 둘다 그리디다 !
프림
- 시작 점점
- 우선순위큐(최소흽)
정점 수보다 간선이 더 많은 밀집그래프에서 더 좋은 성능! (간선이 짱 많은 경우)

크루스칼
- 모든 간선 정렬
정점 수보다 간선이 적은 희소 그래프에서 더 좋은 성능 ! (간선이 적은 경우)
'''

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
# 입력 처리 (그래프: 인접리스트)
# 정점 개수(v), 간선 개수(e)
V, E = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(V)]

# 간선 갯수 만큼 v -< u, 가중치 w를 입력받는다 (u, v, w)
for _ in range(E):
    u, v, w = map(int, input().split())
    # 양방향 그래프(무향 그래프)
    graph[u].append((v, w)) # u -> v 가중치 w
    graph[v].append((u, w))  # v -> u 가중치 w

# 프림(prim) 알고리즘 (그리디)
# 한 정점에 대해서 최소 가중치를 가진 정점을 선택해가며
# 범위를 계속 확대하는 방식으로 진행된다.
# -> 모든 노드(V)를 방문했을 때 중단 ! (v-1)개의 간선
import heapq
def prim(graph, start):
    # 방문 체크를 진행할 visited
    visited = [False] * V
    # 우선순위 큐 : 최소힙(간선의 가중치가 낮은 값 먼저 뽑아낼 수 있느)
    min_heap = [(0, start)] # 첫 시작점의 정점 가중치는 0
    MST = [] # 최소 신장 트리를 저장해서 반환 리스트

    while min_heap:
        cost, node = heapq.heappop(min_heap) # 간선의 가중치 중에서 가장 작은 가중치를 가지고 있는 간선 추출
        # 이미 방문한 정점이면 무시
        if visited[node]:
            continue
        # 아직 방문하지 않은 정점이라면 방문하는 현태로 진행
        visited[node] = True
        MST.append((node, cost))

        for nxt, cost in graph[node]:
            if not visited[nxt]:
                # 연결된 정점을 최소 힙에 추가
                heapq.heappush(min_heap, (cost, nxt))
    return MST # 최소 신장트리 반환

start = 0
MST = prim(graph, start) # 0번 정점을 시작으로 MST 생성

# 출력 : MST의 비용의 합 출력
total_cost = 0
for node, cost in MST:
    total_cost += cost

print("프림 알고리즘으로 진행한 최소 비용:", total_cost)

# 크루스칼 알고리즘 (그리디)
# 간선의 가중치를 기준으로 해서 모든 간선 오름차순 정렬하고
# 해당되는 가중치가 낮은 간선을 선택하는 것으로 진행하되,
# (단, 사이클이 발생하지 않는 간선만 선택한다!) -> union-find
# -> V-1개의 간선을 선택하면 종료
# 부모 노드를 찾는 함수
def find(parents, x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents, parents[x]) # 경로 압축
        return parents[x]

# 두 집합을 합치는 함수
def union(parents, x, y):
    # x, y에 대한 부모 찾기
    px = find(parents, x)
    py = find(parents, y)

    if px != py:
        parents[px] = py

def kruskal(graph):
    edges = [] # 모든 간선 정보가 있는 리스트
    for u in range(V):
        for v, w in graph[u]:
            edges.append((u, v, w)) # u-> v, 가중치 w

    # 간선 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    MST = [] # 최소 신장 트리를 반환할 리스트

    parents = [i for i in range(V)] # 각 정점의 부모를 초기화

    for u, v, w in edges:
        if find(parents, u) != find(parents, v): # 이 간선을 추가한다면 사이클이 없는지 확인
            MST.append((u, v, w))
            union(parents, u, v)
    return MST

MST = kruskal(graph)

# 출력 : MST의 비용의 합 출력
total_cost = 0
for u, v, w in MST:
    total_cost += w

print("크루스칼 알고리즘으로 진행한 최소 비용:", total_cost)