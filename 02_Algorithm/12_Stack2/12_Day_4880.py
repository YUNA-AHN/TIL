'''
토너먼트 카드게임
'''
# 정복
# 입력값으로는 두 플레이어의 인덱스 값을 각각 입력
# 두 플레이어가 싸웠을 때에 승자의 인덱스를 반환
def conquer(p1, p2):
    # 가위 바위 보
    v1 = cards[p1]
    v2 = cards[p2]
    if v1 - v2 == 1 or v1 - v2 == -2 or v1 == v2:
        return p1
    else:
        return p2


# 분할
# 입력값으로 시작점과 끝점을 입력받아서
# 반환하는 값 : 승자의 인덱스를 반환
def divide(start, end):
    # 기저 조건
    if start == end:
        return start
    # 절반씩 분할을 해서 진행
    mid = (start + end) // 2
    w1 = divide(start, mid)
    w2 = divide(mid + 1, end)
    return conquer(w1, w2)


T = int(input())
for tc in range(1, T+1):
    # 입력
    N = int(input())
    cards = list(map(int, input().split()))

    # 메인로직 (분할-정복 알고리즘)
    winner = divide(0, N-1) + 1
    # 출력
    print(f'#{tc} {winner}')