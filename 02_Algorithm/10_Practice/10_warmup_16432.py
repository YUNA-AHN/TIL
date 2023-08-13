'''
산 정상의 높이가 가장 높은 산과 가장 낮은 산의 높이차를 파악
한 구역을 중심으로 8방으로 높으면 산의 정상
가장자리는 산의 정상으로 취급하지 않음
산이 하나 이하인 경우 수행하지 않음
산의 높이 차이, 산이 하나인 경우
'''
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0 # 산 개수
    max_m = 0  # 높이 최솟값
    min_m = 300  # 높이 최댓값

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    for r_idx in range(1, N-1): # 가장 자리 제외
        for c_idx in range(1, N-1):
            condition = True # 산의 조건 충족 여부
            moun_v = arr[r_idx][c_idx]

            for i in range(len(di)): # 델타 검색을 통해 8방 확인
                ni = r_idx + di[i]
                nj = c_idx + dj[i]

                if 0 <= ni < N and 0 <= nj < N:
                    if moun_v <= arr[ni][nj]: # 8방의 산과 높이가 같거나 작다면 조건 미출족
                        condition = False
                        break

            if condition: # 조건 충족했다면 최댓값과 최솟값 갱신
                cnt += 1
                max_m = max(moun_v, max_m)
                min_m = min(moun_v, min_m)

    if cnt <= 1: # 산이 하나밖에 없거나, 없는 경우 -1 반환
        ans = -1
    else: # 산이 2개 이상 존재한다면 높이 차 반환
        ans = max_m - min_m

    print(f'#{tc} {ans}')