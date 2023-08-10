'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램

경로가 있으면 1, 없으면 0
'''
import sys
sys.stdin = open("C:/Users/sgvin/Downloads/sample_input (1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)] # E줄 동안 입력받기
    S, G = map(int, input().split())

    # 인접 리스트 초기화
    graphs = [[] for _ in range(V + 1)]

    for uv in arr:
        u = uv[0]
        v = uv[1]

        # u 정점에서 v 정점으로 이동
        graphs[u].append(v)

    # 방문 체크 행렬
    visited = [False for _ in range(V + 1)]

    def dfs(v):
        visited[v] = True # 일단 들어왔으니까 True

        for u in graphs[v]:
            if visited[u] == True: # 방문한 적 있다면 패스
                continue
            # 방문 안했으면 진행
            dfs(u)

    dfs(S)

    # visited에 True가 찍혀있다면 다녀온 것이기 때문에
    if visited[G]:
        ans = f'#{tc} 1'
    else:
        ans = f'#{tc} 0'

    print(ans)
