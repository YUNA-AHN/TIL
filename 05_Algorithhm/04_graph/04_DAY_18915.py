'''
최소신장트리
사이클을 제거하고 모든 노드를 포함하는 트리 - kruskal
'''
t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())

    # 인접 리스트 생성
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    def find(parents, x):
        if x == parents[x]:
            return x
        parents[x] = find(parents, parents[x])
        return parents[x]

    def union(parents, x, y):
        px = find(parents, x)
        py = find(parents, y)

        if px != py:
            parents[px] =py

    def kruskal(graph):
        edges = []
        for u in range(V+1):
            for v, w in graph[u]:
                edges.append((u, v, w))
        # 가중치 값으로 정렬
        edges.sort(key = lambda x: x[2])
        MST = []

        # 각 노드 자시 자신으로 초기화
        parents = [i for i in range(V+1)]

        for u, v, w in edges:
            if find(parents, u) != find(parents, v):
                MST.append((u, v, w))
                union(parents, u, v)
        return MST

    MST = kruskal(graph)
    total = 0
    for u, v, w in MST:
        total += w
    print(f'#{tc} {total}')