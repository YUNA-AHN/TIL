'''
종이 붙이기
a_x = a_x-10 + 2* a_x-20
'''

# N은 300까지 가능
memo = [0] * 301

# 기저조건
memo[10] = 1
memo[20] = 3

# 30부터 300까지 10단위로 메모 생성
for idx in range(30, 301, 10):
    memo[idx] = memo[idx-10] + 2*memo[idx-20]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = memo[N]

    print(f'#{tc} {ans}')