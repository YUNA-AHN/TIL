# 순열
def f(i, N, k):
    if i == k: # i 이전에 고른 개수, n개에서 k개를 고르는 순열 완성
        print(p)
        return
    else:   # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0: # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, k)
                used[j] = 0

            # f(i+1, N, k)

card = list(map(int, input()))
n = 5 # n개의 숫자에서
k = 3 # k개를 골라 만드는 순열
used = [0] * n # 이미 사용한 카드인지 표시
p = [0] * k
f(0, n, k)
