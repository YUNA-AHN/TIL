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
# import sys
# sys.maxsize

import heapq
# 입력 처리 (그래프: 인접 리스트)
V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
     u, v, w = map(int, input().split())
     # 양방향 그래프 (무향 그래프) # u -> v, v -> u
     graph[u].append((v, w)) # u -> v, 가중치 : w
     graph[v].append((u, w))  # u -> v, 가중치 : w

def dijkstra(graph, start):
    # dust : 시작정점 start --> 각 정점에 대한 최단 거리의 비용을 저장하는 배열 (DP)
    dist = [float('inf') for _ in range(V)]
    dist[start] = 0
    # 우선순위큐.. 가장 최소 비용을 들고 있는 정점을 선택 (최소힙, 비용 낮은 값부터 pop!)
    min_heap = [(0, start)]

    while min_heap:
        cur_cost, node = heapq.heappop(min_heap) # 가장 비용이 작은 정점

        # 현재까지 계산했던 dist 경로의 최소값이 cur_cost보다 작다면, 해당 노드는 skip!
        # 이전에 계산했던 경로가 더 최단거리이므로 스킵
        if cur_cost > dist[node]:
            continue
        # cur_cost : start-node / w = node-nxt
        # 인접한 노드들에 대해서 최소값을 dist에 갱신!
        for nxt, w in graph[node]:
            new_cost = cur_cost + w
            if dist[nxt] > new_cost: # 새로운 최소 비용을 갱신
                dist[nxt] = new_cost
                heapq.heappush(min_heap, (new_cost, nxt))
    return dist

# 다익 스트라 알고리즘 실행
# 시작 정점 0
start = 0
shortest_dist = dijkstra(graph, start)
print(shortest_dist) # 시작 정점 0 -> 해당 정점 i에 대한 최소 경로 바뀜