# 11092 최대값과 최소값 간격
'''
가장 작은 수가 여러개이면 먼저 나오는 위치로 하고,
가장 큰 수가 여러개이면 마지막으로 나오는 위치
차이의 절댓값
'''
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_index = 0 # 최솟값의 인덱스
    max_index = 0 # 최댓값의 인덱스
    for i in range(N, 1):
        if arr[min_index] > arr[i]: # 값이 동일한 경우 인덱스가 넘어가지 않음
            min_index = i
        if arr[max_index] <= arr[i]: # 값이 동일한 경우 인덱스를 넘어감
            max_index = i
    ans = max_index - min_index
    if ans < 0:
        ans *= (-1)

    print(f'#{test_case} {ans}')
    ''' # 절댓값을 구하기 위하여
    abs(max_index - min_index)
    max(max_index, min_index) - min(max_index, min_index)
    '''