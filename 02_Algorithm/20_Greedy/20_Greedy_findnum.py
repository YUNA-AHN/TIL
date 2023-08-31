# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i, n, key, arr):    # 1 현재 상태, n 목표, key 찾고자 하는 함수
    if i == n:
        return 0
    elif arr[i] == key:
        return 1
    else:
        return f(i+1, n, key, arr)

n = 5
a = [1,2,3,4,5]
b = [0] * n
key = 10
print(f(0, n, key, a))
