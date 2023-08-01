# 배열 활용 예제 : Gravity
'''
각 건물의 최대 높이를 체크 !!
낙차를 빼주면 된다..!!
'''
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     # 가장 큰 낙차
#     ans = 0
#     for idx in range(N):
#         cnt = 0
#         for adds in range(idx, N):
#             if arr[idx] <= arr[adds]: # idx 값과 크게나 동일하면 1 추가
#                 cnt += 1
#         local_g = N - idx - cnt
#         if ans < local_g:
#             ans = local_g
#
#     print(f'#{test_case} {ans}')

# 강사님 코드 ---
T = int(input())
for test_case in range(1, T+1):
    # N : 상자가 쌓여있는 개수
    N = int(input())
    # arr : N개의 상자의 높이값
    arr = list(map(int, input().split()))

    # 최댓값
    mx = 0
    # 상자 인덱스를 순환
    for i in range(N):
        # 비교할 상자 인덱스를 순환
        down = 0
        for j in range(i + 1, N):
            # 현재 상자와 카겟 상자의 높이 비교
            if arr[i] > arr[j]:
                # 낙차 + 1
                down += 1
        if mx < down:
            mx = down

    print(f'#{test_case} {mx}')