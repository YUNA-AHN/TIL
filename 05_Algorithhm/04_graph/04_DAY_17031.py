'''
최소비용
기본적으로 1씩 추가, 높이에 따라 더해짐
출발에서 최종 도착지까지
다익 스트라..!
'''
import heapq
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 가중치가 입력된 map...?
    height = [list(map(int, input().split())) for _ in range(n)]

    # 그래프, 시작 인덱스 si, sj
    def dijkstra(graph, si, sj):
        dist = [[float('inf')] * n for _ in range(n)]

        # 시작 인덱스 0으로 초기화
        dist[si][sj] = 0

        # 최소 비용을 들고 있는 우선순위 큐 생성..
        min_heap = [(0, si, sj)] # 가중치, 시작인덱스

        while min_heap:
            cur_cost, i, j = heapq.heappop(min_heap) # 가장 비용이 작은 정점 출력

            # 해당 노드에 입력된 비용보다 크면 skip
            if cur_cost > dist[i][j]:
                continue

            # 상하좌우 탐색
            for di, dj in [[0,1], [0,-1],[1,0],[-1,0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    # 새로운 가격
                    # 높이가 더 높다면 : 현재 가격 + 높이 차이 + 기본값 1
                    # 아니라면 : 현재 가겨 + 높이 차이
                    if graph[i][j] < graph[ni][nj]:
                        stage = graph[ni][nj] - graph[i][j]
                        new_cost = cur_cost + 1 + stage
                    else:
                        new_cost = cur_cost + 1
                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        heapq.heappush(min_heap, (new_cost, ni, nj))

        return dist

    start = 0
    shortest_dist = dijkstra(height, 0, 0)
    print(f'#{tc} {shortest_dist[n-1][n-1]}')