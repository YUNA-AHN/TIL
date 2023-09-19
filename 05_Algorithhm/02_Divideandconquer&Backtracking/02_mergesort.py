# # 최대한 리스트를 덜 생성하는 방식으로..!
# def merge_sort(arr):
#     # 병합 처리할대에만 리스트를 생성하겟다
#     def merge(left_arr, right_arr):
#         """정렬이 되어있는 left_arr 과 right_arr 배열을
#         하나의 정렬되어 있는 배열로 만드는 함수
#
#         Args:
#             left_arr (list[int]): 정렬이 되어 있는 리스트1
#             right_arr (list[int]): 정렬이 되어 있는 리스트1
#         Return: left_arr + right_arr 을 병합하여 정렬한 리스트
#         """
#         merged_arr = []
#         i = j = 0  # 인덱스 변수 초기화
#
#         # i 인덱스 또는 j 인덱스가 배열 범위를 넘은 경우 루프 종료...
#         while i < len(left_arr) and j < len(right_arr):
#             # i 인덱스가 가리키는 값 <-> j 인덱스가 가리키는 값을 비교
#             if left_arr[i] < right_arr[j]:
#                 merged_arr.append(left_arr[i])
#                 i += 1
#             else:
#                 merged_arr.append(right_arr[j])
#                 j += 1
#
#         merged_arr += left_arr[i:]
#         merged_arr += right_arr[j:]
#
#         return merged_arr
#         # 남아있는 리스트 요소들을 merged_arr 에 넣어주는 과정...
#         # 남아있는 리스트가 left_arr 이다..
#         # if i < len(left_arr):
#             # merged_arr.extend(left_arr[i:])
#
#         # 남아있는 리스트가 right_arr 이다..
#         # if j < len(right_arr):
#             # merged_arr.extend(right_arr[j:])
#
#     if len(arr) == 1:
#         return arr
#     # 왼쪽 리스트와 오른쪽 리스트로 나눈다..
#     mid = len(arr) // 2
#     left_arr = merge_sort(arr[:mid])
#     right_arr = merge_sort(arr[mid:])
#     return merge(left_arr, right_arr)
#
#
# arr = [34, 1, 543, 536, 24, 45, 11, 24, 83, 64, 12, 3, 0, 2]
# print(merge_sort(arr))

# 최대한 리스트를 덜 생성하는 방식으로 진행하겠다...!
# 최대한 제자리 정렬 형태로 진행(like in-place sort...?)
def merge_sort(arr):
    # divide : 분할 처리하는 부분
    def divide(left, right):
        nonlocal arr
        if right - left < 2:
            return
        mid = (left + right) // 2
        divide(left, mid)
        divide(mid, right)
        merge(left, mid, right)

    # merge : 병합 처리하는 부분
    def merge(left, mid, right):
        nonlocal arr
        merged_arr = []
        i, j = left, mid

        while i < mid and j < right:
            if arr[i] < arr[j]:
                merged_arr.append(arr[i])
                i += 1
            else:
                merged_arr.append(arr[j])
                j += 1
        # 나머지 있는 요소들을 merged_arr에 추가...!
        merged_arr += arr[i:mid]
        merged_arr += arr[j:right]

        # 원본 배열 arr에 부여...!
        # for k in range(left, right):
        #     arr[k] = merged_arr[k - left]
        arr[left:right] = merged_arr
        # return arr

    # 리스트를 슬라이싱 방식으로 직접 새로운 리스트를 생성x
    # 인덱스(시작점, 끝점)를 전달하는 방식으로 진행하겠다
    right = 0
    left = len(arr) - 1
    return divide(right, left)


arr = [34, 1, 543, 536, 24, 45, 11, 24, 83, 64, 12, 3, 0, 2]
sorted_arr = merge_sort(arr)
print(arr)