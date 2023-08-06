# 이차원 델타
'''
달팽이 N*N 숫자가 시계방향
정수 N을 입력받아 달팽이 출력하시오

달팽이 크기 N은 1이상 10 이하의 정수
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 오른쪽, 아래, 위, 왼쪽 방향
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # N * N 설정
    arr = [[0] * N for _ in range(N)]

    cnt = 1 #카운트
    # 좌표값과 방향값
    r_idx = c_idx = i = 0
    # 초기값 설정
    arr[r_idx][c_idx] = cnt
    while cnt < N * N:
        # 델타값으로 진행
        ni = r_idx + di[i]
        nj = c_idx + dj[i]

        # r_idx 나 c_idx가 끝에 도달했거나, 이미 입력된 값과 마주한다면
        if 0 > ni or ni >= N or 0 > nj or nj >= N or arr[ni][nj] != 0:
            i = (i + 1) % 4
            continue

        # 정상적으로 카운트 값을 넣어햐 하는 경우에는
        r_idx += di[i]
        c_idx += dj[i]
        cnt += 1
        arr[r_idx][c_idx] = cnt

    print(f'#{tc}')

    for item in arr:
        print(*item)
