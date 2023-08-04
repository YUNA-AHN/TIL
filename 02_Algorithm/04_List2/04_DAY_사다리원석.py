while True:
    tc = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    now_r = 99
    now_c = arr[99].index(2)
    while now_r >= 0:
        is_moved_left = False
        while now_c - 1 >= 0 and arr[now_r][now_c - 1]:
            now_c -= 1
            is_moved_left = True
        if not is_moved_left:
            while now_c + 1 < 100 and arr[now_r][now_c + 1]:
                now_c += 1
        now_r -= 1
    print(f'#{tc} {now_c}')

    if tc == 10:
        break