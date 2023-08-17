'''
회전
'''

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n개의 숫자, m번의 작업
    arr = list(map(int, input().split()))

    for idx in range(n):
        if (idx - m) % n == 0:
            print(f'#{tc} {arr[idx]}')


    # for i in range(m):
    #     arr.append(arr.pop(0))
    # print(f'#{tc} {arr[0]}')


