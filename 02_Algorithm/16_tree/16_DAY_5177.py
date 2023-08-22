'''
이진 힙
부모가 있고, 부모 > 자식 : 교환
마지막 노드의 조상노드에 저장된 정수의 합
'''
from heapq import heappush #heapq 이용

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    hq = []
    for i in arr:
        heappush(hq, i)

    sum_v = 0
    p = n // 2
    while p > 0:
        sum_v += hq[p-1]
        p = p // 2


    # hq = [0] + hq # 이거 하면 인덱스 - 1 안해도 된다.
    print(f'#{tc} {sum_v}')
