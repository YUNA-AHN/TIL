'''
고대 유적
폭 1m 길이 2m이상인 직선형태로 서로 평행 또는 직각
사진의 해상도 NxM, 구조물이 있는 곳은 1 빈땅은 0으로 표시
평행한 모든 구조물은 서로 1m 이상
가장 긴 구조물의 길이를 찾는 프로그램
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 고대 구조물 지도
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로
    best_v = 0
    ans = []
    for r_idx in range(N):
        cnt = 0
        for c_idx in range(M):
            # 1이면 일단 더하기
            if arr[r_idx][c_idx] == 1:
                cnt += 1
            # 0을 만나면 ans에 추가..
            else:
                ans.append(cnt)
                cnt = 0
        # 인덱스 다 돌았을 때 ans에 추가
        ans.append(cnt)
    # 세로
    for c_idx in range(M):
        cnt = 0
        for r_idx in range(N):
            # 1이면 일단 더하기
            if arr[r_idx][c_idx] == 1:
                cnt += 1
            # 0을 만나면 ans에 추가
            else:
                ans.append(cnt)
                cnt = 0
        # 인덱스 다 돌았을 때 ans에 추가
        ans.append(cnt)

    print(f'#{tc} {max(ans)}')