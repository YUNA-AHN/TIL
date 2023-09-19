def n_queen_solve(N):
    # 해당 (row, col) 새로히 퀸을 배치하는 경우
    # 대각선 조건에 위반되는지를 확인하는 함수...
    def check(row, col):
        # 같은 열에 다른 퀸이 대각선이 있는지만 검사
        # 대각선에 있는 경우...
        # 좌표 (i, j) <-> (row, col)
        for i in range(row):
            if abs(i - row) == abs(board[i] - col):
                # 서로 영역이 겹치기 때문에... 놓는데 실패!
                return False
        return True

    def nqueen(row):
        nonlocal cnt
        # 기저조건
        if row == N:  # 모든 퀸을 배치한 경우...
            cnt += 1
            return
        # 해당 row 에 대해서 퀸을 모두 배치해본다...
        for col in range(N):
            if not visited[col] and check(row, col):
                board[row] = col  # (row, col) 위치에 퀸 배치
                visited[col] = True
                # 그 다음 행으로 이동해서 퀸을 마저 배치... (재귀)
                nqueen(row + 1)
                visited[col] = False

    # 카운트 변수
    cnt = 0
    # 퀸의 위치를 저장할 수 있는 리스트 (-1 디버깅을 위한 임의의 값)
    board = [-1] * N
    # 같은 열에 대해서 퀸이 중복 배치되지 않도록 visited 배열
    visited = [False] * N
    nqueen(0)  # 첫번째 행부터 퀸 배치 시작...
    return cnt


# N-퀸에 대해서 넣을 수 있는 경우의 수를 출력...
N = int(input())
cnt = n_queen_solve(N)  # N-퀸 문제를 해결하고 카운트값을 저장
print(cnt)