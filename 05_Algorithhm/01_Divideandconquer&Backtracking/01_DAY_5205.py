'''
퀵정렬
'''
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    i = low
    j = high
    p = arr[i]
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    quicksort(arr, 0, len(arr)-1)
    print(f'#{tc} {arr[n//2]}')