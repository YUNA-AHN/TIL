'''
연속된 1의 개수
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N개의 수열
    arr = list(map(int,input()))

    best_v = cnt = 0
    for i in range(N):
        if arr[i]:
            cnt += 1
            if best_v < cnt:
                best_v = cnt
        else:
            cnt = 0

    print(f'#{tc} {best_v}')