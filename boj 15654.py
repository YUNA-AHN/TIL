'''
n과 m
n개의 자연수 중에서 m개를 고른 수열
'''
def perm(i, n, m):
    if i == m:
        print(*p)
        return
    else:
        for j in range(n):
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                perm(i+1, n, m)
                used[j] = 0

import sys
input = sys.stdin.readline

# n개의 자연수, m개 선택
n, m = map(int, input().split())

# 자연수
arr = sorted(list(map(int, input().split())))
used = [0] * n
p = [0] * m

perm(0, n, m)