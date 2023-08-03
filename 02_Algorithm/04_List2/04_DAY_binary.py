'''
A, B : 각각 찾을 쪽 번호
몇 번째 탐색에서 쪽수를 찾았나?!
이진 탐색 이긴 사람 A / B / 0 (비긴 경우)
'''
def binarySearch(N, key): # 탐색횟수 구하는 함수
    start = 1 # 책 시작 페이지
    end = N # 책 끝 페이지
    cnt = 0 # 탐색 횟수
    while True:
        cnt += 1
        middle = (start + end) // 2
        if middle == key: # middle과 key가 같아지면 출력
            break
        elif middle > key: # middle이 key보다 작으면 end 값 갱신
            end = middle
        else: # middle이 key보다 크면 start 값 갱신
            start = middle
    return cnt


T = int(input())


for tc in range(1, T + 1):
    p, a, b = map(int, input().split())

    res_a = binarySearch(p, a) # a의 횟수
    res_b = binarySearch(p, b) # b의 횟수
    if res_a < res_b:
        ans = f'#{tc} A'
    elif res_a > res_b:
        ans = f'#{tc} B'
    else:
        ans = f'#{tc} 0'
    print(ans)

# # 원석 코드
# def n_binary_search(P, key):
#     first = 1
#     last = P
#     res = 0
#     while True:
#         res += 1
#         mid = (first + last) // 2
#         if mid == key:
#             break
#         elif mid < key:
#             first = mid
#         else:
#             last = mid
#     return res
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     P, Pa, Pb = map(int, input().split())
#     n_a = n_binary_search(P, Pa)
#     n_b = n_binary_search(P, Pb)
#     if n_a > n_b:
#         ans = f'#{tc} B'
#     elif n_a < n_b:
#         ans = f'#{tc} A'
#     else:
#         ans = f'#{tc} 0'
#     print(ans)
