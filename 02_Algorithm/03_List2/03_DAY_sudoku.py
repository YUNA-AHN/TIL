'''
가로 9칸 세로 9칸 1 ~ 9
같은 줄 / 3*3 안에 숫자 겹치지 않도록
겹치지 않는 경우 1, 겹치는 경우 0
'''
T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 가로 세로에 대한 검정
    condition = True
    for r in range(9):
        rows = [0] * 10
        cols = [0] * 10
        for c in range(9): # 카운트 정렬 활용
            rows[arr[r][c]] += 1
            cols[arr[c][r]] += 1
            if rows[arr[r][c]] > 1 or cols[arr[c][r]] > 1:
                condition = False
                break

    # 박스에 대한 검정
    di = [0, -1, 0, 1, 1, 1, 0, -1,-1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1, 0]
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

    print(f'#{tc} {int(condition)}')

# 강사님 코드 ---
T = int(input())

# def id_sudoku(arr):

for tc in range(1, T + 1):
    # 입력
    N = 9
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 로직
    # 가로 순회 (가로에 1~9까지 수가 중복되어 있는가?
    for i in range(N):
        # set 자료형 : 중복되는 요소를 가질 수 없음
        # 중복이 있는 경우 -> 크기가 9 미만
        # 정상인 경우 -> 크기가 9
        check = set()
        for j in range(N):
            check.add(arr[i][j])
        if len(check) != 9:
            # 0이 출력.
            pass

    # 세로 순회 : zip 활용 list(zip(*arr)) -> [list(
    for j in range(N):
        # set 자료형 : 중복되는 요소를 가질 수 없음
        # 중복이 있는 경우 -> 크기가 9 미만
        # 정상인 경우 -> 크기가 9
        check = set()
        for i in range(N):
            check.add(arr[i][j])
        if len(check) != 9:
            # 0이 출력..
            pass

    # 3x3 순회
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = set()
            for x in range(0, 3):
                for y in range(0, 3):
                    # arr[i+x][j+y]
                    check.add(arr[i+x][j+y])
            if len(check) != 9:
                # 0이 출력..
                pass
    # 정상적으로 세로가로 3x3 모두 확인 되었기 대문에
    # 1출 력