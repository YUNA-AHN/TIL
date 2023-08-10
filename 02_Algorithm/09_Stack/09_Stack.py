# 깊이 우선 탐색하여 깊이 우선 탐색 경로 출력
# 갈 곳이 없으면 pop
'''
V E
v1 w1 v2 w2
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(n, V, adj_m):
    stack = []              # stack 생성
    visited = [0] * (V+1)   # visited 생성
    visited[n] = 1          # 시작점 방문 표시
    print(n)                # do[n]
    while True:
        for w in range(1, V+1):   # 라이브때 V로 잘못 표기. 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w]==0:
                stack.append(n) # push(n), v = w
                n = w
                print(n)        # do(w)
                visited[n] = 1  # w 방문 표시
                break   # for w , n에 인접인 w c찾은경우
        else:
            if stack:# 스택에 지나온 정점이 남아있으면
                n = stack.pop() # pop()해서 다시 다른 w를 찾을 n 준비
            else:       # 스택이 비어있으면
                break       # while True 탐색 끝
    return



V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)


# 재귀 호출 방식
N = 7 # 노드 개수
stacK = []
# 방문 체크
visited = [False for _ in range(N)]
# 갈 수 있는 지점은 숫자로
graphs = [[1, 2],
          [0, 3, 4],
          [0, 4],
          [1, 5],
          [3, 4, 6],
          [5]
]

# 0번 노드에서 갈 수 있는 지점은?
graphs[0] # [1, 2] 1번과 2번 노드로 갈 수 있다!

def dfs(v):
    global visited
    visited[v] = True
    # v 노드에서 갈 수 있는 노드를 확인 (인접한 노드)
    for u in graphs[v]: # 방문을 했다면! 인접한 건 여기서 알 수 있음
        if visited == True:
            continue
        # 방문을 하지 않았다면 방문을 진행
        dfs(u)
