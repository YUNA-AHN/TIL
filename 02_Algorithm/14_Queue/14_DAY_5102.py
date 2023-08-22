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
    v,e = map(int, input().split()) # 노드의 개수, 간선정보
    arr = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    s, g = map(int, input().split())

    bfs(s)
    print(visited[v])