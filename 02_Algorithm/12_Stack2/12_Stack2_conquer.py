# 거듭제곱
def f1(b, e):
    global cnt1
    if e == 0:
        return 1
    r = 1
    for i in range(e):
        r *= b
        cnt1 += 1
    return r

# 분할정복
def f2(b, e):
    global cnt2
    if b == 0 or e == 0:
        return 1
    r = 1
    if e % 2: # 홀수면
        r = f2(b, (e-1) // 2)
        cnt2 += 1
        return r*r*b
    else: # 짝수면
        r = f2(b, e//2)
        cnt2 += 1
        return r*r

cnt1 = 0
cnt2 = 0

print(f1(2, 10), cnt1)
print(f2(2, 10), cnt2)

# 반복문을 사용해서
# x값을 n번 곱하는 연산
# 반복문을 사용해서 시간복잡도는 O(n)
def power1(x, n):
    tmp = 1
    for _ in range(n):
        tmp *= x
    return tmp
print(power1(2, 10))

# 재귀함수 (분할정복)
def power2(x, n):
    # 기저조건
    if x == 0 or n == 0:
        return 1
    # 지수가 짝수라면
    if n % 2 == 0:
        tmp  = power2(x, n//2)
        return tmp * tmp
    # 지수가 홀수라면
    else:
        tmp = power2(x, n // 2)
        return tmp * tmp * x