for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    total = 0
    for i in range(2, N - 2):
        max_v = arr[i - 2]
        for j in range(i - 2, i + 3):
            if max_v < arr[j]:
                max_v = arr[j]
        if max_v == arr[i]:
            sec_v = 0
            for k in [i - 2, i - 1, i + 1, i + 2]:
                if sec_v < arr[k]:
                    sec_v = arr[k]
            total += (arr[i] - sec_v)

    print(f'#{test_case} {total}')

# 강사님 풀이 ---
for tc in range(1, 11):
    # 입력
    # N : 건물의 갯수
    # builds : N개의 건물의 높이들
    N = int(input())
    buildings = list(map(int, input().split()))
    # 로직
    # 건물들을 순횐하면서 양쪽 2개 거리에 있는
    # 건물의 최고 높이와 중앙에 있는 건물의 높이 차를
    # 계산하고 조망권을 확인한다
    # 인덱스를 가져와서 양쪽의 건물을 가져올 수 있게끔 순환
    cnt = 0
    for idx in range(2, N-2):
        b1 = buildings[idx - 2]
        b2 = buildings[idx - 1]
        center = buildings[idx]
        b3 = buildings[idx + 1]
        b4 = buildings[idx + 2]
        mx_b = max(b1, b2, b3, b4)

        # mx_b = max(buildings[idx - 2],
        #            buildings[idx - 1],
        #            buildings[idx + 1],
        #            buildings[idx + 2])

        # 차이 값을고 구하기
        # center = buildings[idx]
        # diff1 = center - buildings[idx - 2]
        # diff2 = center - buildings[idx - 1]
        # diff3 = center - buildings[idx + 1]
        # diff4 = center - buildings[idx + 2]
         
        # diff = min(diff1, diff2, diff3, diff4)
        # mn_diff = min(diff)
        # if mn_diff > 0:
        #     cnt += mn_diff


        # 만약 중앙에 있는 건물이 양옆에 가장 높은 높이보다 ㅋ,다면
        # 조망권이 확보된 세대 (양수, 조망권 세대 수)
        diff = center - mx_b
        if diff > 0:
            cnt += diff

    # 출력
    print(f'#{test_case} {cnt}')