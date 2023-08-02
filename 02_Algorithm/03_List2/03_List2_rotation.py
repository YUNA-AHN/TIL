N = 2 # 헹의 크기
M = 4 # 열의 크기
arr = [[0,1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        # 행 우선 순횐
        print(arr[i][j])

for i in range(N):
    for j in range(M):
        # 지그재그 순회
        print(arr[i][j + (M - 1 - 2 * j) * (i % 2)])

for j in range(M):
    for i in range(N):
        # 열 우선 순회
        print(arr[i][j])
