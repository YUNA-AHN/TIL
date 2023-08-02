# 연습문제
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    total += abs(arr[ni][nj]- arr[i][j])
    print(f'#{tc} {total}')


# 강사님 코드
# 연습문제
# for tc in range(1, 3):
#     # 입력
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 로직
#     total = 0
#     # 열 우선 순회
#     # 델타값
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     for i in range(N):
#         for j in range(N):
#             # 상하좌우 이웃한 값 순회
#             for k in range(4):
#                 ni = i + di[k]
#                 nj = j + dj[k]
#                 if 0 <= ni < N and 0 <= nj < N:
#                     total += abs(arr[ni][nj] - arr[i][j])
#     print(f'#{tc} {total}')