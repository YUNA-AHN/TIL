'''
파리채 !
N*N 파리의 개수
M*M 크기의 파리채

제약조건
N은 5이상 15이하
M은 2이상 N이하
각 영역의 파리 갯수는 30이하
'''

import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input (3).txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    best_v = 0
    for i in range(N):
        for j in range(N):
            sum_v = 0 # 좌표마다 합 새로 만들어주기
            for idx_i in range(M):
                for idx_j in range(M):
                    ni = i + idx_i
                    nj = j + idx_j
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_v += arr[ni][nj]
            if best_v < sum_v:
                best_v = sum_v

    print(f'#{tc} {best_v}')