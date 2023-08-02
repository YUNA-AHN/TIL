'''
100*100 : 2차원 배열
각 행의 합, 열의 합, 대각선의 합 중 최댓값을 구하는 프로그램
'''

import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input (2).txt", "r")
#
# for tc in range(1, 11):
#     K = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     # 행별 합
#     best_v = sum(arr[0])
#     for i in range(100):
#         r_sum = sum(arr[i])
#         if best_v < r_sum:
#             best_v = r_sum
#
#     # 열별 합
#     for j in range(100):
#         c_sum = 0
#         for i in range(100):
#             c_sum += arr[i][j]
#         if best_v < c_sum:
#             best_v = c_sum
#
#     # 왼-오 대각선 합
#     d_sum = 0
#     for i in range(100):
#         d_sum += arr[i][i]
#         if best_v < d_sum:
#             best_v = d_sum
#     # 오-왼 대각선 합
#     u_sum = 0
#     for i in range(100):
#         u_sum += arr[i][j + (100 - 1 - 2*j)]
#         if best_v < u_sum:
#             best_v = u_sum
#     print(f'#{tc} {best_v}')

for tc in range(1, 11):
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행별 합
    best_v = sum(arr[0])

    for i in range(100):
        r_sum = sum(arr[i]) # 헹별 합# 왼-오 대각선 합
        d_sum = 0
        c_sum = 0
        u_sum = 0
        for j in range(100):
            d_sum += arr[j][j] # 왼-오 대각선
            u_sum += arr[i][j + (100 - 1 - 2 * j)] #오-왼 대각선
            c_sum += arr[j][i] # 열별 합

        if best_v < max(r_sum, c_sum, u_sum, d_sum): # 그중 가장 큰 값과 비교
            best_v = max(r_sum, c_sum, u_sum, d_sum)

    print(f'#{tc} {best_v}')