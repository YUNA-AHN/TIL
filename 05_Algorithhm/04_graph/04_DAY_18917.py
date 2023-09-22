'''
최소 이동 거리 : 일방 통행 !!
0번에서 n번까지 걸리는 최소한의 거리
'''
import heapq
t = int(input())
for tc in range(1, t+1):
    n, e = map(int, input().split()) # 도착점, 도로의 개수
    # 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w)) # u에서 갈 수 있는 정점 v와 거리 w 저장


    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        # 시작 정점 초기화
        dist[start] = 0
        # 최소 비용을 가지고 있는 정점 출력 : 우선 순위 큐
        min_heap = [(0, start)]

        while min_heap:
            cur_cust, node = heapq.heappop(min_heap)

            if cur_cust > dist[node]:
                continue

            for nxt, weight in graph[node]:
                nxt_cost = cur_cust + weight
                if nxt_cost < dist[nxt]:
                    dist[nxt] = nxt_cost
                    heapq.heappush(min_heap, (nxt_cost, nxt))

        return dist[-1]


    res = dijkstra(0)
    print(f'#{tc} {res}')