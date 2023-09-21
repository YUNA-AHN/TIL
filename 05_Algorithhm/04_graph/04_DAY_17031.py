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
    # 가중치가 입력된 인접 행렬 생성
    height = [list(map(int, input().split())) for _ in range(n)]

    def dijkstra(graph, start):
        pass