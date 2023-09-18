'''
장훈이의 높은 선반
점원의 키 만큼 탑을 쌓기, b 이상 중에서 가장 낮은 값
만들 수 있는 높이 - b
부분집합
'''
# import sys
# sys.stdin = open("C:/Users/SSAFY/Downloads/input (1).txt", "r")

# 부분 집합의 합
# b 이상인 경우 최솟값과 비교하기
def subset(k, s):
    global mn
    if k == n:
        if s >= b and mn > s - b:
            mn = s - b
        return

    # 포함되는 경우
    subset(k+1, s + arr[k])
    subset(k+1, s)

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    mn = 10**7
    subset(0, 0)

    print(f'#{tc} {mn}')