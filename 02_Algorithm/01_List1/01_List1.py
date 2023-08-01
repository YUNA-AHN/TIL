# 배열 활용 예제 : Gravity
'''
9
7 4 2 0 0 6 0 7 0
'''
N = int(input())
arr = list(map(int, input().split()))

print(N)
print(arr)

# 배열을 활용한 버블 정렬 (오름차순)
def BubbleSort(a, N): # 정렬한 List, N 원소 수
    for i in range(N - 1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]