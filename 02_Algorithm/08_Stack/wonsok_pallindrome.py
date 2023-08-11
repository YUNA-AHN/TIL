for tc in range(1, 11):
    N = int(input())
    arr = [list(input())for i in range(8)]
    s_r = []
    s_c = []
    ans = 0
    for i in range(8):
        for j in range(8-N+1):
            s_r.clear()
            s_c.clear()
            for k in range(0, N//2):
                s_r.append(arr[i][j+k])
                s_c.append(arr[j+k][i])
            for k in range(N // 2 + N % 2, N):
                if s_r[len(s_r)-1] == arr[i][j+k]:
                    s_r.pop()
                if s_c[len(s_c)-1] == arr[j+k][i]:
                    s_c.pop()
            ans += (1 ^ int(bool(len(s_r))))+(1 ^ int(bool(len(s_c))))
    print(f'#{tc} {ans}')