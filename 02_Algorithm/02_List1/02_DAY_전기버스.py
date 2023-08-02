'''
0~N번 정류장
최대한 이동할 수 있는 정류장 수 K
충전기 설치된 M개의 정류장 번호
최소한 몇번의 충전을 해야 하는지?!
    충전기 설치가 잘못되어 도착 X : 0 출력
충전횟수 ans
'''
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 기준 인덱스에서 K안에 충전소 인덱스가 없으면 가장 가까운 충전소에 가도록!
    current = 0  # 현재 위치
    cnt = 0  # 충전 횟수

    # 현재 위치가 목적지에 도척하기 이전까지
    # 3 1 1 / 1
    while current < N:
        station_list = []  # 들릴 수 있는 충전소 리스트 생성
        for idx in range(1, K + 1):  # 현재 위치에서 K 만큼 이동하는 동안
            recent = current + idx
            if recent in arr:
                station_list.append(recent)  # 충전소가 있다면 리스트에 추가
        if station_list:  # 리스트가 요소가 존재한다면
            cnt += 1  # 충전 횟수 + 1
            current = max(station_list)  # 충전 최솟값이므로 가장 먼 충전소에서 충전 및 현재 위치 이동
            if current + M > N:  # 만약 현재 위치에서 충전 없이 종착역 까지 갈 수 있다면 출력해라!
                print(f'#{tc} {cnt}')
                break
        else:
            print(f'#{tc} 0')  # 불가능하면 0 출력
            break

