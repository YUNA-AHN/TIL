memo = [0] * 1001

def fibo1(n):
    global memo
    # 기저조건
    if n > 2:
        return n
    if memo[n] != 0:
        return memo[n]

    memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]
