
# 부분 집합의 합 만드는 코드
A = [1, 2, 3, 4]

# 무식하게 작성...
# 중첩된 포문으로 작성이 가능
bits = [0, 0, 0, 0]


# 포문으로 해당 인덱스의 비트를 0 또는 1로 바꿔주는 과정을 진행한다...
# for i in [0, 1]:
#     bits[0] = i
#     for j in [0, 1]:
#         bits[1] = j
#         for k in [0, 1]:
#             bits[2] = k
#             for l in [0, 1]:
#                 bits[3] = l
#                 # print(bits)
#                 subset = []
#                 for m in range(len(bits)):
#                     # 해당되는 비트가 1일 때에는
#                     if bits[m] == 1:
#                         # 부분집합에 해당 요소를 추가
#                         subset.append(A[m])
#                 print(subset)


# 재귀함수로 부분집합 코드
# i : 해당 인덱스에 대해서 값을 변경할 수 있도록 매개변수...
# def recur(i):
#     # 기저조건
#     if i == len(bits):
#         # print(bits)
#         subset = []
#         for j in range(len(bits)):
#             # bits 값이 1이라면 해당 요소를 추가하고
#             if bits[j] == 1:
#                 subset.append(A[j])
#         print(subset)
#         return
#     bits[i] = 0
#     recur(i + 1)
#     bits[i] = 1
#     recur(i + 1)
#
#
# recur(0)

# 재귀로 작성을 했을 때...
# 완전탐색... 깊이 우선 탐색 DFS
# 부분집합에 대한 합이 3일 때의 부분집합을 출력해보아라...
# def recur(i):
#     # 기저조건
#     if i == len(bits):
#         # print(bits)
#         subset = []
#         for j in range(len(bits)):
#             # bits 값이 1이라면 해당 요소를 추가하고
#             if bits[j] == 1:
#                 subset.append(A[j])
#         if sum(subset) == 3:
#             print(subset)
#         return
#     bits[i] = 0
#     recur(i + 1)
#     bits[i] = 1
#     recur(i + 1)
#
#
# recur(0)


# 재귀로 작성을 했을 때...
# 백트래킹 : DFS + 가지치기
# 부분집합에 대한 합이 3일 때의 부분집합을 출력해보아라...
def recur(i, s):
    # 기저조건
    # 현재까지 부분집합의 합이 3을 넘어가는 겨웅에는 가지치기
    if s > 3:
        return
    if i == len(bits):
        # print(bits)
        subset = []
        for j in range(len(bits)):
            # bits 값이 1이라면 해당 요소를 추가하고
            if bits[j] == 1:
                subset.append(A[j])
        if sum(subset) == 3:
            print(subset)
        return
    bits[i] = 0
    recur(i + 1, s)
    bits[i] = 1
    recur(i + 1, s + A[i])


recur(0, 0)