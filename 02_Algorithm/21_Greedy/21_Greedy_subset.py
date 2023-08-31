def subset(i, N):
    if i == N:
        s = 0
        if s == 0:
            for j in range(N):
                if bit[j]:
                    print(arr[j], end= ' ')
            print()
    else:
        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N
subset(0, N)

# def subset(i, N, s, c):
#     if s == 0 and c != 0:
#         return 1
#     if i == N:
#         return 0
#     else:
#         if subset(i+1, N, s + arr[i], c+1):
#             return 1
#         if subset(i + 1, N, s, c + 1):
#             return 1
#         return 0
#
# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# N = len(arr)
# bit = [0] * N
# subset(0, N)