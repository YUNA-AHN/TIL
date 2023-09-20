'''
동철이의 일 분배
직원들의 번호 1부터 N까지, i번 직원이 j번 일을 하면 성공할 확률이 pij
주어진 일이 모두 성공할 확률
순열이네 !!
'''

import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input (3).txt", "r")

def perm(i, n, s):
    global mx
    if i == n:
        mx = max(mx, s)
        return
    else:
        for j in range(n):
            # 소수이기 때문에 곱할수록 작아짐
            # 이미 mx보다 작다면 쉽지 않다...!
            if used[j] == 0 and s * (arr[i][j]/100) > mx:
                used[j] = 1
                perm(i + 1, n, s * (arr[i][j]/100))
                used[j] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    used = [0] * n
    mx = 0
    perm(0, n, 1)

    print(f'#{tc}', format(mx*100, '.6f'))