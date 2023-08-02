# 델타 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0 # 모든 원소가 0 이상이라면..
for i in range(N):  # 모든 원소 arr[i][j]에 대해
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s
            
# 델타 다른 형식
max_v = 0 # 모든 원소가 0 이상이라면..
for i in range(N):  # 모든 원소 arr[i][j]에 대해
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s

max_v = 0 # 모든 원소가 0 이상이라면..
for i in range(N):  # 모든 원소 arr[i][j]에 대해
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for p in range(1, m):
            for k in range(4):
                ni, nj = i + di[k]*p, j + dj[k]*p
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s

arr = [3,6,7]

n = len(arr)         # n : 원소의 개수

for i in range(1<<n) :         # 1<<n : 부분 집합의 개수
    for j in range(n):        # 원소의 수만큼 비트를 비교함
        if i & (1<<j):         # i의 j번 비트가 1인경우
            print(arr[j], end=", ")        # j번 원소 출력
    print()
print()