'''
비상연락망과 연락을 시작하는 당번에 대한 정보
가장 나중에 연락을 받게되는 사람 중 번호가 가장 큰 사람
최대 100명 부여될 수 있는 번호 1이상, 100이하
# visited에서 가장 큰 사람의 인덱스, 그중에서 가장 큰 값
'''
import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input (3).txt", 'r')

def bfs(s): # 시작 정점
    global visited
    que = []        # 빈 큐를 생성
    que.append(s)   # 시작점 삽입
    visited[s] = 1  # 방문 체크
    while que:      # 큐가 빌 때까지
        t = que.pop(0)  # 큐를 pop
        for w in adj_l[t]:  # 해당 정점에서 이동할 수 있는 정점을 순회
            if visited[w] == 0: # 방문한 적이 없다면
                que.append(w) # 큐에 삽입
                visited[w] = visited[t] + 1 # 지나온 정점 개수


for tc in range(1, 11):
    n, s = map(int, input().split()) # 길이, 시작점
    arr = list(map(int, input().split()))

    # 인접리스트 생성
    adj_l = [[] for _ in range(101)]
    # 방향이 존재하기 때문에 v1에 인접한 정점 추가
    for i in range(n//2):
        v1, v2 = arr[i * 2], arr[i * 2 +1]
        adj_l[v1].append(v2)

    # 방문 체크 리스트 생성
    visited = [0] * 101

    # bfs
    bfs(s)

    # 최댓값 mx
    mx = 0

    # 방문체크열을 순회
    # 최댓값인 경우 갱신 및 인덱스 저장
    for j in range(101):
        if mx <= visited[j]:
            mx = visited[j]
            ans = j
    print(f'#{tc} {ans}')

