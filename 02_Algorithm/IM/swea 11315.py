'''
오목 판정
n*n 크기의 판
판의 각 칸에는 돌이 있거나 없을 수 있다.
가로 세로 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분 있는지 판정
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    ans = 'NO'
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                cnt_r = cnt_c = cnt_cr = cnt_cc = 1
                for k in range(1,5):
                    # 가로
                    ri, rj = i, j+(1*k)
                    if 0 <= ri < n and 0 <= rj < n and arr[ri][rj] == 'o':
                        cnt_r += 1
                    # 세로
                    ci, cj = i-(1*k), j
                    if 0 <= ci < n and 0 <= cj < n and arr[ci][cj] == 'o':
                        cnt_c += 1
                    # 대각선오른쪽
                    cri, crj = i+(1*k), j+(1*k)
                    if 0 <= cri < n and 0 <= crj < n and arr[cri][crj] == 'o':
                        cnt_cr += 1
                    # 대각선 왼쪽
                    cci, ccj = i+(1*k), j-(1*k)
                    if 0 <= cci < n and 0 <= ccj < n and arr[cci][ccj] == 'o':
                        cnt_cc += 1
                if cnt_r == 5 or cnt_c == 5 or cnt_cr == 5 or cnt_cc == 5:
                    ans = 'YES'
                    break
            if ans == 'YES':
                break
        if ans == 'YES':
            break
    print(f'#{tc} {ans}')