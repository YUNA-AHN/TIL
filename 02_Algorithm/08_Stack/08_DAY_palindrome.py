'''
제시된 길이를 가진 회문의 개수
'''
# for tc in range(1,11):
#     N = int(input())
#     arr = [list(input()) for _ in range(8)]
#
#     #  가로
#     cnt = 0
#     for r_idx in range(8):
#         for c_idx in range(8 - N + 1):
#             text_r = ''
#             for i in range(N):
#                 text_r += arr[r_idx][c_idx + i]
#             if text_r == text_r[::-1]:
#                 cnt += 1
#
#     # 세로
#     for c_idx in range(8):
#         for r_idx in range(8 - N + 1):
#             text_c = ''
#             for i in range(N):
#                 text_c += arr[r_idx+i][c_idx]
#             if text_c == text_c[::-1]:
#                 cnt += 1
#
#
#     print(f'#{tc} {cnt}')

# stack으로 풀어보기
for tc in range(1,11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    #  가로
    cnt = 0