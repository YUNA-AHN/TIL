'''
파스칼 삼각형
'''
# 행과 열이 순차적으로 증가하는 이차원 배열 생성
memo = [[0] * i for i in range(11)]

memo[1] = [1] # 첫번째 행은 1

for r_idx in range(2, 11):
    for c_idx in range(r_idx):
        if c_idx == 0 or c_idx == r_idx-1: # 첫번째 열과 마지막 열은 1
            memo[r_idx][c_idx] = 1
        else: # 자신의 왼쪽 위와 오른족 위의 숫자의 합
            memo[r_idx][c_idx] = memo[r_idx-1][c_idx - 1] + memo[r_idx-1][c_idx]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N + 1):
        print(*memo[i])