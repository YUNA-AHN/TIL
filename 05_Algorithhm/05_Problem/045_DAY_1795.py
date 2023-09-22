'''
인수의 생일파티
N개의 정점, 단반향 간선, 도로는 모든 집들 간에 이동이 가능하도록 구성
모든 집들 간에 이동이 가능하도록

가장 오래 걸리는 집!
'''
t = int(input())
for tc in range(1, t+1):
    # n : 정점의 개수  m : 간선의 개수  x : 인수의 집
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
