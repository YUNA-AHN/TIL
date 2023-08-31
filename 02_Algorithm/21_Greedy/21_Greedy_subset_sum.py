# # 부분집합 만들기1
# # N 배열의 길이
# # i 현재 재귀 호출한 깊이
# def subset(N, i):
#     # 기저조건
#     if i == N:
#         total = 0
#         # bits 1은 유, 0은 무.
#         for j in range(N):
#             if bits[i] == 1:  # 해당 원소를 사용o.
#                 # 요소값을 더해서
#                 total += arr[i]
#         # 최종적인 합이 0이라면.
#         if total == 0:
#             # 요소들을 출력...
#             for j in range(N):
#                 if bits[i] == 1:
#                     print(arr[i], end=' ')
#             print()
#         return
#
#     # i 번째에 있는 요소를 사용o
#     bits[i] = 1
#     subset(N, i + 1)
#
#     # i 번째에 있는 요소를 사용x
#     bits[i] = 0
#     subset(N, i + 1)
#
#
# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# N = len(arr)
# bits = [0] * N  # 해당 원소를 사용o 1, 해당 원소를 사용x 0
# subset(N, 0)


# 부분집합 만들기2
# N 배열의 길이
# i 현재 재귀 호출한 깊이
# s 지금까지의 원소 합을 계산한 값
def subset(N, i, s):
    # 기저조건
    if i == N:
        if s == 0:
            print(*result)
        return

    # i 번째에 있는 요소를 사용o
    result.append(arr[i])
    subset(N, i + 1, s + arr[i])

    # i 번째에 있는 요소를 사용x
    result.pop()
    subset(N, i + 1, s)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
result = []  # 부분집합을 저장할 리스트
subset(N, 0, 0)