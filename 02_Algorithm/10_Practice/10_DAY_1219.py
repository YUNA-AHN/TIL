'''
길찾기
A -> B로 가는길 존재히는지 조사
일방통행
출발점 0 도착점 99
분기점은 98개를 넘어가지 않으며, 한개읮 ㅓㅇ점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않음
정점의 개수가 100개 이기 때문에 size[100] 배열 2개 선언, 정점의 번호를 주소로 사용
저장되는 데이터는 각 정점에서 도착하는 정점의 번호를 저장
'''

import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input (2).txt", "r")

for _ in range(10):
    tc, N = map(int, input().split())

    # v(시작) u(갈 수 있는 곳) 이루어진 리스트 받기
    arr = list(map(int, input().split()))
    # 방문 체크
    visited = [False for _ in range(100)]

    # 그래프 생성
    graphs = [[] for _ in range(100)]

    # 인접 리스트 생성
    for i in range(0, len(arr), 2):
        v = arr[i]
        u = arr[i + 1]
        graphs[v].append(u) # v에서 u로 갈 수 있어요 !

    # dfs 함수 생성
    def dfs(v):
        global visited
        visited[v] = True # 일단 들어갔으니까 방문 체크

        for u in graphs[v]: # v에서 다 들렸으면 이제 못가셔유...
            if visited[u] == True:
                continue
            dfs(u) # 아직 갈 수 있는 곳이 있다면 가봅시다 !

    dfs(0)

    # 시작점에서 돌았을 때 도착지점에 방문을 했다면
    # 갈 수 있다는 이야기겠지용~?
    if visited[99]:
        ans = f'#{tc} 1'
    else:
        ans = f'#{tc} 0'

    print(ans)