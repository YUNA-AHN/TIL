# # 이진 검색 - 반복문
# arr = [2, 4, 7, 9, 11, 19, 23]
#
# # 문제에서 데이터가 정렬되어 있다라는 조건이 없다면
# # 반드시 정렬을 먼저 수행해야한다.
# arr.sort()
#
# def binarySearch(target):
#     low = 0
#     high = len(arr) - 1
#
#     # low > high 라면 데이터를 못찾은 경우
#     while low <= high:
#         mid = (low + high) // 2
#         # 1. 가운데 값이 정답인 경우
#         if arr[mid] == target:
#             return mid
#
#         # 2. 가운데 값이 정답보다 작은 경우
#         elif arr[mid] < target:
#             low = mid + 1
#         # 3. 가운데 값이 정답보다 크 경우
#         else: high = mid - 1
#
#     return "해당 데이터는 없습니다."
#
# print(f'9 = {binarySearch(9)}')
# print(f'2 = {binarySearch(2)}')
# print(f'10 = {binarySearch(10)}')

# 이진 검색 - 재귀 호출
arr = [2, 4, 7, 9, 11, 19, 23]

# 문제에서 데이터가 정렬되어 있다라는 조건이 없다면
# 반드시 정렬을 먼저 수행해야한다.
arr.sort()

# 함수 한 번 호출때마다 low, hight 변수가 바뀌어서 사용됨
def binarySearch(target, low, high):
    # 기저 조건 : 언제가지 재귀호출을 반복할 것인가?
    mid = (low + high) // 2

    # low > high 라면 데이터를 몾찾음
    if low > high:
        return -1

    if target == arr[mid]:
        return mid
    elif arr[mid] < target:
        return binarySearch(target, mid + 1, high)
    else:
        return binarySearch(target, low, mid-1)

print(f'9 = {binarySearch(9 ,0, len(arr)-1)}')
print(f'2 = {binarySearch(2,0, len(arr)-1)}')
print(f'10 = {binarySearch(10,0, len(arr)-1)}')