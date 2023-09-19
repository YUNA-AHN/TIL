# 함수 안의 함수 (nested function : 중첩 함수)
# 내부 함수 (inner function)
# 퀵소트 함수 작성
def quick_sort(A):
    # 호어 partition 로직...
    # 함수 내부에서만 사용할 수 있는 보조격 함수... (바깥에서는 해당 함수를 사용x)
    # 변수 스코프 제어 용이 (DFS... 재귀함수... visited 배열 초기화 -> 인자)
    def partition(A, left, right):
        i = left
        j = right
        pivot = A[i]
        # 인덱스 i -> ...  <- j 서로 교차할 때까지
        while i <= j:
            while i <= j and A[i] <= pivot:
                i += 1
            while i <= j and A[j] >= pivot:
                j -= 1
            # 인덱스를 이동하고 스왑하는 과정을 진행...
            if i < j:
                # swap i <-> j
                A[i], A[j] = A[j], A[i]

        # 반복이 끝난 후에 ... 최종적으로 피봇을 중앙에 넣는다.
        # swap left <-> j
        A[left], A[j] = A[j], A[left]

        # 피봇 인덱스를 반환한다...
        return j

    def sort(A, left, right):
        # 왼쪽 오른쪽 범위 나누어서 정렬... (pivot 중간값으로 해서 범위를 정복)
        if left < right:
            pivot_index = partition(A, left, right)
            quick_sort(A, left, pivot_index - 1)
            quick_sort(A, pivot_index + 1, right)

    left = 0
    right = len(A) - 1
    return sort(A, left, right)


arr1 = [11, 45, 23, 81, 28, 34]
arr2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
arr3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

quick_sort(arr1)
quick_sort(arr2)
quick_sort(arr3)

print(arr1)
print(arr2)
print(arr3)