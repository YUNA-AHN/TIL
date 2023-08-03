'''
N개의 정수 : 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2 번재 작은 수
결과를 10개까지!! 출력하씨오
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    res_list = []

    # 선택정렬
    for i in range(N-1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    for k in range(10):
        if k % 2: # 홀수자리에는 최솟값
            num = arr.pop(0)
        else: # 짝수자리에는 최댓값
            num = arr.pop(-1)
        res_list.append(num)

    print(f'#{tc}', *res_list)