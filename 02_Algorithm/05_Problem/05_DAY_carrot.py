'''
연속으로 커지는 당근
최대 갯수는 얼마일까요?!
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = best_v = 1
    for i in range(N-1):
        if arr[i] + 1 == arr[i + 1]:
            cnt += 1
            best_v = max(cnt, best_v)
        else:
            cnt = 1
    print(f'#{tc} {best_v}')