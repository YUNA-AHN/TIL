T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 지도의 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # 지도 정보 입력

    # 봉우리의 개수를 받을 cnt 변수 생성
    cnt = 0

    # 상하좌우를 살피기 위한 델타 탐색
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    # 모든 칸을 순회
    for r_idx in range(N):
        for c_idx in range(N):
            condition = True # 봉우리 조건 충족 여부 확인
            for i in range(4):
                moun_v = arr[r_idx][c_idx]

                ni = r_idx + di[i]
                nj = c_idx + dj[i]

                # 해당 칸의 높이가 상하좌우의 높이보다 작으면 봉우리 조건 미충족
                if 0 <= ni < N and 0 <= nj < N:
                    if moun_v <= arr[ni][nj]:
                        condition = False
                        break
            if condition: # 해당 칸이 봉우리 조건을 만족한다면 cnt에 1을 더함
                cnt += 1
    print(f'#{tc} {cnt}')