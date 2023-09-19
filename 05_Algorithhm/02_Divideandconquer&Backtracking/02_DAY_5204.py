def merge_sort(arr):
    def divide(left, right):
        nonlocal arr
        # 길이가 1인 경우에 그만 !
        if right - left < 2:
            return
        mid = (left + right) // 2
        divide(left, mid)
        divide(mid, right)
        merge(left, mid, right)
    def merge(left, mid, right):
        nonlocal arr, ans
        if arr[mid-1] > arr[right-1]:
            ans += 1

        merged_arr = []
        i, j = left, mid

        while i < mid and j < right:
            if arr[i] < arr[j]:
                merged_arr.append(arr[i])
                i += 1
            else:
                merged_arr.append(arr[j])
                j += 1
        merged_arr.extend(arr[i:mid])
        merged_arr.extend(arr[j:right])

        arr[left:right] = merged_arr

    ans = 0
    left = 0
    right = len(arr)
    divide(left, right)
    return arr[len(arr)//2], ans

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    val, cnt = merge_sort(arr)
    print(f'#{tc} {val} {cnt}')

