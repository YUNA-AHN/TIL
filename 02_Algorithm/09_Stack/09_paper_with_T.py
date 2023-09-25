'''
종이 붙이기
점화식
a_x = a_x-10 + 2*  a_x-20
'''

dp = [0] * 301

# 기저조건
dp[10] = 1
dp[20] = 3
# f(X) = f(x=-10) + 2* f(x-20)

for x in range(30, 301, 10):
    dp[x] = dp[x - 10] + 2 * dp[x - 20]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    ans = dp[N]

    print(f'#{tc} {ans}')