# # key가 있으면 1, 없으면 0을 리천하는 함수
# def f(i, n, key, arr):    # 1 현재 상태, n 목표, key 찾고자 하는 함수
#     if i == n:
#         return 0
#     elif arr[i] == key:
#         return 1
#     else:
#         return f(i+1, n, key, arr)
#
# n = 5
# a = [1,2,3,4,5]
# b = [0] * n
# key = 10
# print(f(0, n, key, a))

# # 순열
# def f(i, N, k):
#     if i == k: # i 이전에 고른 개수, n개에서 k개를 고르는 순열 완성
#         print(p)
#         return
#     else:   # p[i]에 들어갈 숫자를 결정
#         for j in range(N):
#             if used[j] == 0: # 아직 사용되기 전이면
#                 p[i] = card[j]
#                 used[j] = 1
#                 f(i+1, N, k)
#                 used[j] = 0
#
#             # f(i+1, N, k)
#
# card = list(map(int, input()))
# n = 5 # n개의 숫자에서
# k = 3 # k개를 골라 만드는 순열
# used = [0] * n # 이미 사용한 카드인지 표시
# p = [0] * k
# f(0, n, k)

# # 부분집합
# a = [3, 6, 7, 1, 5, 4]
# N = 6
# # for i in range(1, (1<<N)-1)
# for i in range(1, (1<<N)//2): # 케이스 빼주면서 원하는 부분집합만 출력
#     subset1 = []
#     subset2 = []
#     total1 = total2 = 0
#     min_v = 0
#     for j in range(N):
#         if i &(1<<j):   # j번 비트가 0이 아니면
#             subset1.append(a[j])
#             total1 += a[j]
#         else:
#             subset2.append(a[j])
#             total2 += a[j]
#     r1 = subset1
#     r2 = subset2
#     if r1 and r2:
#         if min_v > abs(total1 - total2):
#             min_v = abs(total1 - total2)
#     print(subset1, subset2)

# # 단순하게 순열을 생성하는 방법 with 강사님
# nums = [] # 상태 저장 리스트
# def recur(depth):
#     '''
#     :param depth: 재귀호출을 몇번 진행했는지 (카운트값)
#     :return: 없음
#     '''
#     # 기저조건(종료조건)
#     if depth == 3:
#         print(nums)
#         return
#
#     # 유도조건(재귀호출)
#     # i : i -> 3
#     for i in range(1, 4):
#         nums.append(i) # 결정
#         recur(depth + 1)
#         nums.pop() # 복구
#
# recur(0)

# npk with 강사님
def P(arr, n, k, used, picks, depth):
    '''

    :param arr: 뽑고자 하는 배열(요소의 갯수는 n개)
    :param n:  배열의 길이
    :param k: 뽑고자 하는 요소의 갯수
    :return: 없음
    '''

    # 기저조건
    if depth == k: # k만큼 뽑았다면 정치..
        # 내가 지금가지 뽑은 값을 출력
        print(picks)
        return

    # 유도조건(재귀)
    for i in range(n):
        # 사용 여부
        if used[i] == False: # 사용하지 않은 수라면..
            # 결정 : 사용(사용 체크)
            used[i] = True
            picks.append(arr[i]) # 해당 숫자를 픽에 추가
            # 재귀 호출
            P(arr, n, k, used, picks, depth)
            # 복구
            used[i] = False
            picks.pop()

arr = [1, 3, 5, 7, 9, 10]
N = 6 # len(arr)
used = [False] * (N) # 사용한 값을 표기
picks = [] # 내가 뽑을
P(arr, N, 3, used, picks, 0) # 6P3 경우의 수를 모두 출력해봐라