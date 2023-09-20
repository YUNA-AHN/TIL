import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input (2).txt", "r")

'''
contact
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
u 정점에서 v 정점으로
'''
# for tc in range(1, 11):
#     n, start = map(int, input().strip().split())
#     edges = list(map(int, input().strip().split()))
#
#     # 최대 연락 인원인 100만큼 인접 리스트 생성
#     graph = [[] for _ in range(101)]
#     visited = [0] * 101
#
#     # 인접리스트 생성
#     for idx in range(0, n, 2):
#         u = edges[idx]
#         v = edges[idx+1]
#         # u -> v
#         graph[u].append(v)
#
#     def bfs(current):
#         que = []
#         que.append(current)
#         while que:
#             node = que.pop(0)
#             for nxt in graph[node]:
#                 if visited[nxt] == 0:
#                     que.append(nxt)
#                     visited[nxt] = visited[node] + 1
#
#     bfs(start)
#
#     mx = 0
#     for i in range(101):
#         if visited[i] >= mx:
#             mx = visited[i]
#             res = i
#     print(f'#{tc} {res}')

# 강사님 ver
for tc in range(1, 11):
    n, start = map(int, input().strip().split())
    edges = list(map(int, input().strip().split()))

    # 최대 연락 인원인 100만큼 인접 리스트 생성
    graph = [[] for _ in range(101)]

    # 인접리스트 생성
    for idx in range(0, n, 2):
        u = edges[idx]
        v = edges[idx+1]
        # u -> v
        graph[u].append(v)

    # DFS 순회, 연결되어 있는 그룹들을 확장
    # union-find 알고리즘을 사용
    # 초기화. 자기 자신을 parent를 초기화
    parents = [i for i in range(101)]
    def find(x): # x의 대표자(부모)가 누구인가
        if parents[x] == x:
            return x
        else:
            parents[x] = find(parents[x]) # 경로 압축
            return parents[x]

    def union(x, y): # x와 y가 속한 두개 그룹을 변항
        # 각각의 대표자를 찾아서 병합
        px = find(x)
        py = find(y)

        if px != py:
            parents[px] = py


    def dfs(start):
        # 시작 노드에서 방문 체크
        visited[start] = True
        # 인접한 노드들을 방문
        for nxt in graph[start]:
            if not visited[nxt]:
                union(start, nxt) # 시작점과 인접된 노드들
                dfs(nxt)


    visited = [False] * 101
    dfs(start)

    # 시작 노드와 같은 그룹에 속해 있으면서 노드 번호가 큰 값을 찾는 과정
    mx_node = start
    for i in range(1, 101):
        # 같은 그룹에 속해 있는지 확인
        if find(start) == find(i):
            mx_node = max(mx_node, i) # 가장 큰 번호로 갱신

    print(mx_node)