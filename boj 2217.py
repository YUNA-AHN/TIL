'''
로프
N(1 ≤ N ≤ 100,000)개의 로프, 들 수 있는 물체의 중량이 서로 다를 수 있음
병렬로 연결하면 각각의 로프에 걸리는 중랼 나눌 수 있음
k개의 로프를 사용하여 w인 물체를 들어올릴 때, 각각의 로프에는 w/k만큼 중랼
최대중량을 구해내는 프로그램!
모든 로프 사용할 필요 없음
'''
# 부분집합 구하기
# def subset(arr, depth):
#     if depth == n:
#         sub = []
#         for i in range(len(arr)):
#             if arr[i] == 1:
#                 sub.append(weight[i])
#         lst.append(sub)
#         return
#
#     for i in range(2):
#         arr[depth] = i
#         subset(arr, depth + 1)
#
# n = int(input())
# weight = [int(input()) for _ in range(n)]
# lst = []
# subset([0]*n, 0)
#
# mx = 0
# for i in lst[1:]:
#     mx = max(min(i) * len(i), mx)
#
# print(mx)
import sys
n = int(sys.stdin.readline())
weight = [int(sys.stdin.readline()) for _ in range(n)]

weight.sort()
len_weight = len(weight)
mx = 0
for i in range(n):
    mx = max(weight[i] * (len_weight - i), mx)

print(mx)