'''
숫자배열회전
NxN 행렬
90도 180도 360도
3 <= N <= 7
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(input().split()) for _ in range(N)]

    arr_90 = list(zip(*arr[::-1]))
    arr_180 = list(zip(*arr_90[::-1]))
    arr_270 = list(zip(*arr_180[::-1]))

    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))