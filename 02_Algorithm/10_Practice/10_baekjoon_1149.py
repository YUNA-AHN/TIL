# 집에 칠하는 비용 입력

"""
3
26 40 83
49 60 57
13 89 99
"""
R = 0  # 빨간색 상수
G = 1  # 초록색 상수
B = 2  # 파란색 상수

# 집의 갯수 N
N = int(input())

# 집마다 색을 칠하게 되는 비용
houses = [list(map(int, input().split())) for _ in range(N)]

# 완전탐색 : 모든 경우의 수를 다 따져보는 방법
# DFS (깊이 우선 순위) 탐색 진행...
# 시간복잡도 : 3 * 2^(N-1) -> 3 * 2^1000 -> 3 * 10^300


# 모든 집을 칠했을 때의 최소 비용을 계산하자...!

# 최소비용
mn_cost = 10000000000000


# 집번호 / 색상 / 현재까지의 비용
def dfs(house, color, cost):
    global mn_cost

    # 기저조건
    # 모든 집을 칠했을 때 최소비용을 갱신을 진행...
    if house == N:
        mn_cost = min(mn_cost, cost)
        return

    # 현재 집에 칠할 색상을 고른다.
    # 이전 집과 같은 색상은 칠할 수 없다.
    for i in [R, G, B]:
        if i != color:
            # 다음에 해당하는 집을 칠하도록 탐색을 진행한다...
            # 현재 집에 해당 색상을 칠한 비용을 더해주고 넘긴다.
            dfs(house + 1, i, cost + houses[house][i])


# 첫번째 집을 빨간색을 칠할 때
dfs(0, R, houses[0][R])
# 첫번째 집을 초록색을 칠할 때
dfs(0, G, houses[0][G])
# 첫번째 집을 초록색을 칠할 때
dfs(0, B, houses[0][B])

# 최소비용 출력
print(mn_cost)

# 메모이제이션으로 시간복잡도 해소
# 메모이제이션 : 이미 구한 값은 다시 구하지 않는다...

# 집의 갯수 N
N = int(input())

# 집마다 색을 칠하게 되는 비용
houses = [list(map(int, input().split())) for _ in range(N)]

# 모든 집을 칠했을 때의 최소 비용을 계산하자...!

# memo[집번호][색상] = 해당 집을 해당 색상으로 칠했을 때까지의 지금까지의 최소 비용...
memo = [[0] * 3 for _ in range(N)]  # N x 3

# 최소비용
mn_cost = 10000000000000


# 집번호 / 색상 / 현재까지의 비용
def dfs(house, color, cost):
    global mn_cost

    # 기저조건
    # 모든 집을 칠했을 때 최소비용을 갱신을 진행...
    if house == N:
        mn_cost = min(mn_cost, cost)
        return

    if memo[house][color] != 0:
        dfs(house + 1, color, cost + memo[house][color])
        return

    # 현재 집에 칠할 색상을 고른다.
    # 이전 집과 같은 색상은 칠할 수 없다.
    for i in [R, G, B]:
        if i != color:
            # 다음에 해당하는 집을 칠한 경우의 비용에서 최소비용을 계산한다.
            # 현재 집에 해당 색상을 칠한 비용을 더해주고 넘긴다.
            dfs(house + 1, i, memo[house][i])
            # 메모가 안되어 있다면
            if memo[house][i] == 0:
                memo[house][i] = cost + houses[house][i] # 오류 나면 memo
            else:  # 최소비용으로 갱신
                memo[house][i] = min(memo[house][i], cost + houses[house][i])


# 첫번째 집을 빨간색을 칠할 때
memo = [[0] * 3 for _ in range(N)]  # N x 3
dfs(0, R, houses[0][R])
# 첫번째 집을 초록색을 칠할 때
memo = [[0] * 3 for _ in range(N)]  # N x 3
dfs(0, G, houses[0][G])
# 첫번째 집을 초록색을 칠할 때
memo = [[0] * 3 for _ in range(N)]  # N x 3
dfs(0, B, houses[0][B])

# 최소비용 출력
print(mn_cost)

# DP 로 풀이
# 메모이제이션 코드에서 재귀함수 형태를 제거한다...
N = int(input())

# 집마다 색을 칠하게 되는 비용
houses = [list(map(int, input().split())) for _ in range(N)]

# 모든 집을 칠했을 때의 최소 비용을 계산하자...!
# dp[집번호][색상] = 지금까지의 최소비용을 계산값
dp = [[0] * 3 for _ in range(N)]

# 기저조건 : 첫 시작 집을 칠하는 비용...
dp[0][R] = houses[0][R]
dp[0][G] = houses[0][G]
dp[0][B] = houses[0][B]

# RGB 거리 문제에 점화식...
for x in range(1, N):
    dp[x][R] = min(dp[x - 1][G], dp[x - 1][B]) + houses[x][R]
    dp[x][G] = min(dp[x - 1][R], dp[x - 1][B]) + houses[x][G]
    dp[x][B] = min(dp[x - 1][R], dp[x - 1][G]) + houses[x][B]

# 최소 비용
print(min(dp[N - 1][R], dp[N - 1][G], dp[N - 1][B]))