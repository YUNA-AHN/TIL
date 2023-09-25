def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False # 검색 실패

def binarySearch2(a, low, high, key):
    if high < low:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle - 1, key)
        elif a[middle] > key:
            return binarySearch2(a, middle + 1, high, key)



# 2일차 이진 탐색-------
'''
짝은 이룬 A, B 찾을 쪽 번호 이진 탐색
중간 페이지 int((l+r)/2)
'''
def binarybook(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        middle = int((start + end)/2)
        if middle == key:
            return cnt
        elif middle < key:
            start = middle
            cnt += 1
        elif middle > key:
            end = middle
            cnt += 1
        else:
            cnt = 0

    return cnt



T = int(input())

for tc in range(1, T + 1):
    N, a, b = map(int, input().split())

    res_a = binarybook(N, a)
    res_b = binarybook(N, b)

    if res_a > res_b:
        print(f'#{tc} B')
    elif res_a < res_b:
        print(f'#{tc} A')
    else:
        print(f'{tc} 0')