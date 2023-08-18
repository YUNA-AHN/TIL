'''
연산자 끼워넣기
N-1개의 연산자가 주어진다. + - * //
식의 계산은 연산자 우선 순위를 무시하고, 앞에서부터 진행
음수를 양수로 나눌때에는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼 것
만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램
-10**9 < <10**9
'''
# def perm(i, n, a):
#     global lst
#     # 기저조건
#     if i == n: # 연산
#         # 가지치기까진 못했고...
#         # 중복되는 순열이 있다면 제외
#         if tuple(a) not in lst:
#             lst.append(tuple(a))
#     else:
#         for j in range(i, n):
#             a[i], a[j] = a[j], a[i]
#             perm(i+1, n, a)
#             a[i], a[j] = a[j], a[i]

# lst = []
# a = [1, 1, 2, 3]
# perm(0, 4, a)
# print(lst, len(lst))


def perm(i, n):
    global mx, mn
    # 기저조건
    if i == n: # 연산
        # 가지치기까진 못했고...
        # 중복되는 순열이 있다면 제외
        sum_v = num[0]
        for idx in range(len(opers)):
            if opers[idx] == '+':
                sum_v += num[idx+1]
            elif opers[idx] == '-':
                sum_v -= num[idx+1]
            elif opers[idx] == '*':
                sum_v *= num[idx+1]
            elif opers[idx] == '/': # 음수를 양수로 나누는 경우
                if sum_v < 0:
                    sum_v = (-sum_v // num[idx+1])
                else:
                    sum_v //= num[idx+1]
        mx = max(mx, sum_v)
        mn = min(mn, sum_v)

    else:
        for j in range(i, n):
            opers[i], opers[j] = opers[j], opers[i]
            perm(i+1, n)
            opers[i], opers[j] = opers[j], opers[i]




n = int(input()) # 수의 개수
num = list(map(int, input().split()))
p, m, t, d = map(int, input().split()) # + - * // 의 개수
opers = ['+'] * p + ['-'] * m + ['*'] * t + ['/'] * d # 연산 기호


mx = -10**10
mn = 10**10

# 여러가지 연산 조합 뽑기
perm(0, n-1)
print(mx)
print(mn)