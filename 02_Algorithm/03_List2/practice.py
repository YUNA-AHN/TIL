T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 단어가 들어갈 수 있는 자리 수
    cnt = 0
    # 연속된 칸 수 리스트
    a = []

    for i in range(N):
        sum_v = 0
        for j in range(N):
            # 가로 구하기 : 행 기준
            if arr[i][j]: # 해당 칸이 1이면 더해주고
                sum_v += 1
            else: # 0이면은 세어둔 칸 수를 리스트에 추가
                a.append(sum_v)
                sum_v = 0  # 연속된 칸 수 초기화

            # 세로 구하기 : 열 기준
            if arr[j][i]:  # 해당 칸이 1이면 더해주고
                sum_v += 1
            else:  # 0이면은 세어둔 칸 수를 리스트에 추가
                a.append(sum_v)
                sum_v = 0

            # 1로 해당 행이나 열이 끝나는 경우 리스트에 추가되지 않음
            # 인덱스가 마지막 행 / 열이면 리스트에 추가
            if j == N - 1:
                a.append(sum_v)
    # 최종적으로 연속된 칸 수 리스트에서 특정 길이 K인 경우를 카운트
    for item in a:
        if item == K:
            cnt += 1

    print(f'#{tc} {cnt}')