graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

def bfs(start):
    visited = [0] * 5

    # 먼저 방문 했던 것을 먼저 처리해야 한다 = queue
    que = [start]
    visited[start] = 1

    while que:
        # que의 맨 앞 요소를 꺼냄
        now = que.pop(0)
        print(now, end=' ')

        # 인접한 노드들을 que에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next]:
                continue

            que.append(next)
            # bfs니까 여기서 방문 체크해도 된다
            visited[next] = 1
bfs(0)