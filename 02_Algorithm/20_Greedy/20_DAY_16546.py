'''
baby gin
'''
def perm(depth, k, arr):
    # cards도 받아서 같은게 있다면 True, 없다면 False
    if depth == k:
        lst.append(tuple(arr))
        return
    for i in range(len(arr)-1):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        perm(depth + 1, k, arr)
        arr[i], arr[i+1] = arr[i+1], arr[i]


T = int(input().strip())
for tc in range(1, T+1):
    arr = list(map(int, input().strip()))
    cards = [0] * 6

    lst = []
    perm(0, len(arr), arr)

    ans = False
    # triplet - triplet
    for i in range(10):
        cards[0] = cards[1] = cards[2] = i
        for j in range(10):
            cards[3] = cards[4] = cards[5] = j
            if tuple(cards) in lst:
                ans = True
                break
        if ans:
            break

    if ans == False:
        # run - triplet
        for i in range(0, 8):
            cards[0] = i
            cards[1] = i + 1
            cards[2] = i + 2
            for j in range(10):
                cards[3] = cards[4] = cards[5] = j
                if tuple(cards) in lst:
                    ans = True
                    break
            if ans:
                break

    if ans == False:
        # triplet - run
        for j in range(10):
            cards[0] = cards[1] = cards[2] = j
            for i in range(0, 8):
                cards[3] = i
                cards[4] = i + 1
                cards[5] = i + 2
                if tuple(cards) in lst:
                    ans = True
                    break
            if ans:
                break

    if ans == False:
        # run - run
        for j in range(0, 8):
            cards[0] = j
            cards[1] = j + 1
            cards[2] = j + 2
            for i in range(0, 8):
                cards[3] = i
                cards[4] = i + 1
                cards[5] = i + 2
                if tuple(cards) in lst:
                    ans = True
                    break
            if ans:
                break

    if ans:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')

