# 부분집합의 인덱스
def f(i, N):
    if i == N:
         return
    else:
        B[i] = A[i]
        f(i + 1, N)
        return

N = 3
A = [1, 2, 3]
B = [0] * N

f(0, N)
print(B)

# 부분 집합을 구하는 함수----
def f(i, N):
    if i == N:
        print(bit, end = ' ')
        for j in range(N):
            if bit[j]:
                print(A[j], end = ' ')
        print()
        return
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return

A = [1, 2, 3]
bit = [0] * 3
f(0, 3)

# 부분집합의 합
def f(i, N):
    if i == N:
        print(bit, end = ' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return

A = [1, 2, 3]
bit = [0] * 3
f(0, 3)

# 부분집합의 합을 반환하는 함수
def f(i, N, s): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1      # 부분집합에 A[i] 포함
        f(i + 1, N, s+A[i])
        bit[i] = 0      # 부분집합에 A[i] 빠집
        f(i + 1, N, s)
        return

A = [1, 2, 3]
bit = [0] * 3
f(0, 3, 0)

# 부분집합의 합 가지치기
def f(i, N, s, t): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합). t: 찾으려는 합
    global cnt
    cnt += 1
    if s == t:
        print(bit)
        return
    elif i == N:    # 남은 원소가 없는 경우
        return
    elif s > t:
        return
    else:
        bit[i] = 1      # 부분집합에 A[i] 포함
        f(i + 1, N, s+A[i], t)
        bit[i] = 0      # 부분집합에 A[i] 빠집
        f(i + 1, N, s, t)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print(cnt)
