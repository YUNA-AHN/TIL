'''
N*N 크기의 단어 퍼즐
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수
가로 세로의 경우 모두!
흰색은 1, 검은색은 0 --> 흰색에만 쓸 수 있음

제약사항
N은 5이상 15이하의 정수
K는 2이상 N이하의 정수
'''

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
            if arr[i][j]:  # 해당 칸이 1이면 더해주고
                sum_v += 1
            else: # 0이면은 세어둔 칸 수를 리스트에 추가
                a.append(sum_v)
                sum_v = 0

            # 1로 해당 행이나 열이 끝나는 경우 리스트에 추가되지 않음
            # 인덱스가 마지막 행 / 열이면 리스트에 추가
            if j == N-1 : # 연속된 칸 수 초기화
                a.append(sum_v)

    # 세로 구하기
    for i in range(N):
        sum_v = 0
        for j in range(N):
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