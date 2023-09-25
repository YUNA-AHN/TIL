# # 거짓말
# # 거짓말쟁이로 알려지지 않으면서 과장된 이야기 가능한 파티의 개수
# import sys
# input = sys.stdin.readline
#
# def find(x):
#     if x == parents[x]:
#         return x
#     parents[x] = find(parents[x])
#     return parents[x]
#
#
# def union(x, y):
#     px = find(x)
#     py = find(y)
#
#     if px != py:
#         parents[py] = px
#
# # 사람의 수, 파티의 수
# n, m = map(int, input().strip().split())
#
# # 자기 자신으로 초기화 !
# parents = [i for i in range(n + 1)]
#
# # 진실을 나는 사람의 수, 번호
# truth, *arr_t = map(int, input().strip().split())
#
# # 파티의 수 만큼 순회
# # 진실을 아는 사람이 있거나 같이 파티에 참석한 적이 있다면(조상노드가 같다면...) 그 파티는 못감
# for _ in range(m):
#     people, *arr_p = map(int, input().strip().split())
#
#     # 사람 숫자만큼 순회
#     for person in arr_p:
#         if parents[person] in arr_t:
#             pass

'''
도시분할계획
MST - 간선이 많으면 kruskal
'''
import sys
input = sys.stdin.readline

def find(parents, x):
    if x == parents[x]:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    px = find(parents, x)
    py = find(parents, y)
    if px == py:
        return
    if px < py:
        parents[py] = px
    else:
        parents[px] = py

def kruskal(graph):
    edges = [] # 모든 간선 정보가 잇는 리스트
    for u in range(n+1):
        for v, w in graph[u]:
            edges.append((u, v, w))

    # 간선 가중치를 기준으로 오름차순 ㅊ정렬
    edges.sort(key = lambda x:x[2])
    MST = []

    parents = [i for i in range(n+1)]

    for u, v, w in edges:
        if find(parents, u) != find(parents, v):
            MST.append((u, v, w))
            union(parents, u, v)
    return MST

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    # 길이니까 왔다갔다 가능한~
    graph[u].append((v, w))
    graph[v].append((u, w))

MST = kruskal(graph)
total = 0
mx = 0
for u, v, cost in MST:
    total += cost
    mx = max(mx, cost)

print(total - mx)