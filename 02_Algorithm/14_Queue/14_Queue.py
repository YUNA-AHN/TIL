'''
7 8
1 2 1 3 2 4 3 5 4 6 5 6 6 7 3 7
'''
def bfs(s, v): # 시작점 s 마지막 정점 v
    visited = [0] * (v+1) # visited 생성
    que = []       # 큐 생성
    que.append(s)   # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while que:        # 큐에 정점이 남아있으면 front != rear
        t = que.pop(0) # 디큐
        print(t)    # 방문한 정점에서 할 일
        for w in adj_l[t]: # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0: # w 인큐, 인큐 되었음을 표시
                que.append(w)
                visited[w] = visited[t] + 1

v, e = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adj_l =[[] for _ in range(v+1)]
for i in range(e):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

bfs(1, 7)

# # 인접행렬로 해보기
# def bfs(s, v): # 시작점 s 마지막 정점 v
#     visited = [0] * (v+1) # visited 생성
#     que = []       # 큐 생성
#     que.append(s)   # 시작점 인큐
#     visited[s] = 1  # 시작점 방문표시
#     while que:        # 뮤에 정점이 남아있으면 front != rear
#         t = que.pop(0) # 디큐
#         print(t)    # 방문한 정점에서 할 일
#         for w in range(1, v+1): # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
#             if adj_m[t][w] == 1 and visited[w] == 0: # w 인큐, 인큐 되었음을 표시
#                 que.append(w)
#                 visited[w] = visited[t] + 1
#
# v, e = map(int, input().split())
# arr = list(map(int, input().split()))
# # 인접행렬
# adj_m =[[0] * (v+1) for _ in range(v+1)]
# for i in range(e):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1
#
# bfs(1, v)
#
# # -------------------
# def bfs(s, v): # 시작점 s 마지막 정점 v
#     visited = [0] * (v+1) # 방문체크 생성
#     que = [] # 빈 큐 생성
#     que.append(s) # 큐에 시작정점 삽입
#     visited[s] = 1 # 시작 정점 방문 체크
#     while que: # 큐를 다 비울 때까지
#         t = que.pop(0)
#         print(t)
#         for w in adj_l[t]:
#             if visited[w] == 0:
#                 que.append(w)
#                 visited[w] = visited[t] + 1
#
#
# v, e = map(int, input().split())
# arr = list(map(int, input().split()))
#
# # 인접리스트
# adj_l =[[] for _ in range(v+1)]
# for i in range(e):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)
