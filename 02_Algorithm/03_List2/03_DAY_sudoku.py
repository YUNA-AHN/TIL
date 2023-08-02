'''
가로 9칸 세로 9칸 1 ~ 9
같은 줄 / 3*3 안에 숫자 겹치지 않도록
겹치지 않는 경우 1, 겹치는 경우 0
'''
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    condition = True
    for r in range(9):
        rows = [0] * 10
        cols = [0] * 10
        for c in range(9):
            rows[arr[r][c]] += 1
            cols[arr[c][r]] += 1
            if rows[arr[r][c]] > 1 or cols[arr[c][r]] > 1:
                condition = False
                break


    di = [0, -1, 0, 1, 1, 1, 0, -1,-1]
    dj = [0, 1, 1, 1, 0 -1, -1, -1, 0]
    for idx_i in range(1, 9, 3):
        for idx_j in range(1, 9, 3):
            b = [0] * 10
            for i in range(9):
                ni = idx_i + di[i]
                nj = idx_j + dj[i]
                b[arr[ni][nj]] += 1

                if b[arr[ni][nj]] > 1:
                    condition = False
                    break
    if condition:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
