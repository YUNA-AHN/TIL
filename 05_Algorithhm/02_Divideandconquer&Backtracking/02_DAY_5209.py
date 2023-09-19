'''
최소 생산 비용
순열...?
'''
# n개 중에서 n개를 순서 있게 뽑아야함..!
def perm(i, n, s):
    global mn
    if i == n:
        mn = min(mn, s)
        return
    if s > mn:
        return
    else:
        for j in range(n):
            if used[j] == 0:
                used[j] = 1
                perm(i + 1, n, s + arr[i][j])
                used[j] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    used = [0] * n
    total = 0
    mn = 10 ** 7
    perm(0, n, 0)
    print(f'#{tc} {mn}')
