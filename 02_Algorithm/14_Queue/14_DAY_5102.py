'''
노드의 거리
'''
def bfs(s):
    global visited
    que = []
    que.append(s)
    visited[s] = 1
    while que:
        t = que.pop(0)
        for n in arr[t]:
            if visited[n] == 0:
                que.append(n)
                visited[n] = visited[t] + 1



T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split()) # 노드의 개수, 간선정보
    arr = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    s, g = map(int, input().split())

    # 시작점 s
    bfs(s)
    if visited[g] <= 1: # 1번 방문 이하이면 0으로 처리
        ans = 0
    else: ans = visited[g] - 1
    print(f'#{tc} {ans}')