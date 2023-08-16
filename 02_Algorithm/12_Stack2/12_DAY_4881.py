'''
배열 최소 합
백트래킹
'''
# def dfs(i):
#     if visited[i]:
#         return
#     else:
#         visited[i] = True
#         dfs(i + 1)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))]
#
#     visited = [False] * N


# 강사님
temp_sum = 0
mn_sum = 1000


# 첫번째 방법 visited + 재귀형태
def dfs(arr, N, visited, i):
    global  mn_sum, temp_sum
    if i == N:
        mn_sum = min(mn_sum, temp_sum)
        return
    for j in range(N):
        if visited[j] == True:
            continue
        visited[j] = True #결정
        temp_sum += arr[i][j]
        dfs(arr, N, visited, i + 1)
        temp_sum
        visited = False  #복구

T = int(input())
for tc in range(1, T+1):
    # 입력
    # N
    N = int(input())
    mn_sum = 1000
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 방문체크
    visited = [False for _ in range(N)]
    dfs(arr, N, visited, 0)

    print(f'{tc} {mn_sum}')

# 2. 순열 [0, 1, 2]
mn_sum = 1000


def dfs(arr, N, i, perm):
    global mn_sum

    # 기저조건
    if i == N:
        # print(perm)  # 순열이 완성된 형태...
        temp = 0
        for k in range(N):
            j = perm[k]
            temp += arr[k][j]
        mn_sum = min(mn_sum, temp)
        return

    # 순열을 [0,,,, N-1] 값을 가지고 있는 순열 만들고,, 해당되는 값으로 인덱스 삼아 계산을 하겠다..

    for j in range(i, N):
        # 리스트 요소를 스왑 (결정)
        perm[i], perm[j] = perm[j], perm[i]
        # 재귀호출
        dfs(arr, N, i + 1, perm)

        # 리스트 요소를 스왑 (복구)
        perm[i], perm[j] = perm[j], perm[i]


T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N
    N = int(input())
    mn_sum = 1000
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 순열 만들 배열
    perm = [i for i in range(N)]
    dfs(arr, N, 0, perm)

    print(f"#{tc} {mn_sum}")