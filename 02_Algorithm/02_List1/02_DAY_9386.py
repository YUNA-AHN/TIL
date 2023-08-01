# 9386 연속한 1의 개수
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split())) # split('0')으로 작성도 가능 !

    for idx in range(N):
        if arr[idx] == 1:
            pass