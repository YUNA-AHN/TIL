n = int(input()) # 숫자의 개수
num = list(map(int, input().split()))
p, m , t, d = map(int, input().split()) # + - * /
opers = ['+'] * p + ['-'] * m + ['*'] * t + ['/'] * d

mx = -10 ** 9
mn = 10 ** 9

lst = []
def perm(i, n) : # 시작점
    global lst
    if i == n:
        print(opers)

    else:
        for j in range(i, n):
            opers[i], opers[j] = opers[j], opers[i]
            perm(i+1, n)
            opers[i], opers[j] = opers[j], opers[i] # 원상 복구


perm(0, n-1)