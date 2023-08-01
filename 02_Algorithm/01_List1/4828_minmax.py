'''
기본 코드! 잘 외워두기!
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{test_case} {ans})
'''

# 4828 min max
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for index in range(N):
        if max_v < arr[index]:
            max_v = arr[index]
        if min_v > arr[index]:
            min_v = arr[index]
    ans = max_v - min_v
    print(f'#{test_case} {ans}')