'''
행렬 곱셈
'''
def conquer(times_a, times_b):
    global res
    for k in range(n):
        for l in range(k):
            res[k][l] += times_a[k][l] * times_b[k][l]


def divide(a, b):
    # a 행렬의 행
    times_a = a
    # b 행렬의 열
    times_b = list(map(list, zip(*b)))

    print(times_a)
    print(times_b)
    # return conquer(times_a, times_b)


import sys
input = sys.stdin.readline

# 행렬 a의 크기 n행 m열 / b 행렬 크기 m행 n열
n, m = map(int, input().strip().split())
a = [list(map(int, input().strip().split())) for _ in range(n)]

m, k = map(int, input().strip().split())
b = [list(map(int, input().strip().split())) for _ in range(m)]

res = [[0] * n for _ in range(n)]

divide(a, b)

print(res)