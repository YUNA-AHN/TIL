'''
전기버스
충전지마다 최대로운행할 수 있는 정류장 수, 최소한의 교체 횟수
'''
t = int(input())
for tc in range(1, t+1):
    n, *arr = map(int, input().strip().split())

    # arr에 0 추가
    arr = [0] + arr
    bus = list(range(0, n))
    # 버스정류장 번호 + 이동 가능 거리
    bus_stop = [x+y for x, y in zip(bus, arr)]

    # 버스정류장 인덱스
    i = 1
    # 충전 횟수
    cnt = 0
    # 도착할 때까지
    while i < n:
        # 이동 가능한 최대 거리
        mx = 0
        # 이동 가능한거리
        charge = arr[i]
        # 이동 가능한 거리 내에 정류장 확인
        for j in range(i + 1, i + charge + 1):
            # 이동 가능한 거리 내에 도착점이 있다면 break
            if bus_stop[j] >= n:
                i = n
                break
            # 이동 가능한 거리 내에 있는 정류장 중 최대로 갈 수 있는 거리
            if mx <= bus_stop[j]:
                mx = bus_stop[j]
                # 해당 정류장에서 충전한 값
                charge = arr[j]
                # 현재 위치 갱신
                i = j
        cnt += 1
    print(f'#{tc} {cnt}')