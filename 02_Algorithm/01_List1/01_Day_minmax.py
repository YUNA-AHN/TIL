T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for index in range(N):
        if max_v < arr[index]:
            max_v = arr[index]
        if min_v > arr[index]:
            min_v = arr[index]
    ans = max_v - min_v

    print(f'#{test_case} {ans}')

# 강사님 ver ----
# T = int(input())
# for test_case in range(1, T+1):
#     # 입력
#     # N : 양의 정수 갯수
#     N = int(input())
#     # a_i : N개의 양의 정수들
#     arr = list(map(int, input().split()))
#
#     # 로직
#     # 가장 작은 수
#     mn = min(a)
#     # 가장 큰 수
#     mx = max(a)
#     # 차이값을 출력
#     diff = mx - mn
#
#     # 출력
#     print(f'#{test_case} {diff}')
