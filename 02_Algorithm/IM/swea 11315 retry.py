'''
오목 판정
가로 / 세로 / 대각선 오른쪽 / 대각선 왼쪽
[1,0] [0,1] [1,1] [1,-1]
'''
def check(i, j, di, dj, n):
    cnt = 1
    # 5칸까지 연속으로 돌이 있는 지 확인
    for k in range(1,5):
        ni = i + di * k
        nj = j + dj * k
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
            cnt += 1
    if cnt == 5:
        return True
    else:
        return False

def Search():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for di, dj in [[1, 0], [0, 1], [1, 1], [1, -1]]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                       if check(i, j, di, dj, n):
                           return True



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    if Search():
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

