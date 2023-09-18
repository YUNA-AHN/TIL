'''
이진 탐색
n 개의 정수가 리스트 b에 저장된 m개의 정수에 대해 a에 들어있는 수인지 이진 탐색을 통해 확인
'''
import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input.txt", "r")

def binary(target):
    low = 0
    high = len(a) - 1
    cond = ''
    while low <= high:
        mid = (low + high) // 2
        # 타겟 값을 찾았다면 return 1
        if a[mid] == target:
            return 1
        # 왼쪽을 탐색해서
        elif a[mid] < target:  # 중앙값이 target보다 작으면 right 탐색
            low = mid + 1
            if cond == 'right':
                return 0
            else:
                cond = 'right'

        elif a[mid] > target:  # 중앙값이 target보다 크면 left 탐색
            high = mid - 1
            if cond == 'left':
                return 0
            else:
                cond = 'left'
        else:
            return 0
    return 0


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    total = 0

    # a에 속한 정수
    for i in b:
        if binary(i):
            total += 1
    print(f'#{tc} {total}')