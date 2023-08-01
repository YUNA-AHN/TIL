# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     max_v = arr[0]
#     min_v = 0
#     for idx in range(M):
#         min_v += arr[idx]
#
#     for index in range(N - M + 1):
#         sum_v = 0
#         for adds in range(M):
#             sum_v += arr[index + adds]
#         if max_v < sum_v:
#             max_v = sum_v
#         if min_v > sum_v:
#             min_v = sum_v
#     ans = max_v - min_v
#     print(f'#{test_case} {ans}')

# 강사님 코드 ---
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 메인로직
    mn = 10000 * 99 # 주어진 조건 활용한 최댓값 M은 최댓값 99, 정수 a_i의 최댓값 10000
    mx = 0 # 최댓값
    for i in range(N - M + 1):
        total = 0
        for j in range(M): # i, i + M
            # i + j 가 합삽을 요하는 요소 인덱스
            total += arr[i + j]
        # 슬라이스 total = sum(arr[i:i+m])
        # 최댓값과 최솟값 갱신
        if mx < total:
            mx = total
        if mn > total:
            mn = total
        # 차를 계산
        result = mx - mn

    # 출력
    print(f'#{test_case} {result}')