N = 5
arr = [[0] * N for _ in range(5)]

# 델타 : 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 좌표값
i, j = 0, 0
# 방향값
direction = 0
cnt = 1 # 카운트
arr[0][0] = 1
while cnt < N * N:
    # 델타값 순서대로 쭈우욱 진행을 하다가
    ni = i + di[direction]
    nj = j + dj[direction]
    # 벽을 만나거나, 기존에 값이 있었던 지역을 만나면
    if 0 > ni or ni >= N or 0 > nj or nj >= N or arr[ni][nj] != 0:
        # 다음 델타값으로 변경 (턴 진행)
        direction = (direction + 1) % 4
        continue

    # 정상적으로 카운트 값을 넣어야 하는 경우라면
    i, j = ni, nj
    cnt += 1
    arr[i][j] = cnt


for lst in arr:
    print(*lst)