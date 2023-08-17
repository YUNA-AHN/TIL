'''
배열 최소 합
백트래킹
'''


def recur(lst, depth, s):
    global mn, visited, N
    # 가지치기 : s가 mn보다 큰 경우
    if s > mn:
        return  # 종료
    # 기저조건 N == depth
    # 가지치기에 안걸리고 깊이까지 가면 mn 갱신
    if depth == N:
        mn = min(s, mn)
        return  # 종료
    for i in range(N):
        if visited[i] == False:  # 방문한 적 없다면!
            visited[i] = True  # 방문 체크 후
            lst.append(i)  # 해당 값을 리스트에 추가
            recur(lst, depth + 1, s + arr[depth][i])  # 깊이를 더하고, 합을 구해 넘기기
            lst.pop()  # 리스트 복구
            visited[i] = False  # 방문체크 복구


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문체크
    visited = [False] * N
    s = 0
    mn = 100000

    recur([], 0, 0)

    print(f'#{tc} {mn}')

# # 강사님
# temp_sum = 0
# mn_sum = 1000
#
#
# # 첫번째 방법 visited + 재귀형태
# def dfs(arr, N, visited, i):
#     global  mn_sum, temp_sum
#     if i == N:
#         mn_sum = min(mn_sum, temp_sum)
#         return
#     for j in range(N):
#         if visited[j] == True:
#             continue
#         visited[j] = True #결정
#         temp_sum += arr[i][j]
#         dfs(arr, N, visited, i + 1)
#         temp_sum
#         visited = False  #복구
#
# T = int(input())
# for tc in range(1, T+1):
#     # 입력
#     # N
#     N = int(input())
#     mn_sum = 1000
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#
#     # 방문체크
#     visited = [False for _ in range(N)]
#     dfs(arr, N, visited, 0)
#
#     print(f'{tc} {mn_sum}')
#
# # 2. 순열 [0, 1, 2]
# mn_sum = 1000
#
#
# def dfs(arr, N, i, perm):
#     global mn_sum
#
#     # 기저조건
#     if i == N:
#         # print(perm)  # 순열이 완성된 형태...
#         temp = 0
#         for k in range(N):
#             j = perm[k]
#             temp += arr[k][j]
#         mn_sum = min(mn_sum, temp)
#         return
#
#     # 순열을 [0,,,, N-1] 값을 가지고 있는 순열 만들고,, 해당되는 값으로 인덱스 삼아 계산을 하겠다..
#
#     for j in range(i, N):
#         # 리스트 요소를 스왑 (결정)
#         perm[i], perm[j] = perm[j], perm[i]
#         # 재귀호출
#         dfs(arr, N, i + 1, perm)
#
#         # 리스트 요소를 스왑 (복구)
#         perm[i], perm[j] = perm[j], perm[i]
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     # 입력
#     # N
#     N = int(input())
#     mn_sum = 1000
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 순열 만들 배열
#     perm = [i for i in range(N)]
#     dfs(arr, N, 0, perm)
#
#     print(f"#{tc} {mn_sum}")