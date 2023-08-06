'''
T : 테스트 케이스 개수
N : 버스 노선수
i번째 버스노선 - 번호 A_i이상 B_i 이하 모든 정류장
P 개의 버스정류장에 대해 각 정류장에 몇개의 버스 노선
P 개의 줄에는 C_j가 주어진다..


'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    res = [0] * 5001  # 5000개 요소를 가진 리스트 생성

    for ns in range(1, N + 1):  # 노선의 개수 만큼
        a, b = map(int, input().split())  # a값과 b값을 받고
        for idx in range(a, b + 1):  # 해당되는 인덱스레 1씩 더해준다.
            res[idx] += 1

    P = int(input())  # 조사할 정류장 개수 받기

    station_list = []
    for _ in range(P):  # 해당되는 정류장에 지나는 버스 대수를 리스트로 받아 출력
        station_idx = int(input())
        station_list.append(res[station_idx])

    print(f'#{tc}', *station_list)