'''
11, 45, 23, 81, 28, 34
11, 45, 22, 81, 23, 34, 99, 22, 17, 8
1, 1, 1, 1, 1, 0, 0, 0, 0, 0
'''

# def quickSort(A, left, right):
#     if left < right:
#         s = partition(A, left, right)
#         quickSort(A, left, s - 1)
#         quickSort(A, s + 1, right)
#
# def partition(A, left, right):
#     i = left
#     j = right
#     p = A[i]
#
#     while i <= j:
#         while i <= j and A[i] <= p:
#             i += 1
#         while i <= j and A[i] >= p:
#             j -= 1
#         if i < j:
#              A[i], A[j] = A[j], A[i]
#         A[left], A[j] = A[j], A[left]
#     return j

# 퀵소트 with T
def quickSort(A, left, right):
    # 왼쪽 오른쪽 범위 나누어서 정렬
    if left < right:
        pivot_index = partition(A, left, right)
        quickSort(A, left, pivot_index - 1)
        quickSort(A, pivot_index + 1, right)
def partition(A, left, right):
    i = left
    j = right
    pivot = A[i]
    # 인덱스 i ->, <- j 서로 교차할 때까지
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        # 인덱스를 이동하고 스왑하는 과정을 진행
        if i < j:
            # swap i <-> j
            A[i], A[j] = A[j], A[i]
    # 반복이 끝난 후에 최종적으로 피봇 인덱스를 중앙에 입력
    A[left], A[j] = A[j], A[left]

    return j

arr1 = [11, 45, 23, 81, 28, 34]
arr2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
arr3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]


quickSort(arr1, 0, len(arr1)-1)
quickSort(arr2, 0, len(arr2)-1)
quickSort(arr3, 0, len(arr3)-1)

print(arr1)
print(arr2)
print(arr3)