'''
퍼펙트 셔플
카드 덱을 절반으로 나누고 교대로 카드를 뽑아 새로운 덱을 만드는 것
N개의 카드가 있는 덱
N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장ㅇ 더
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = input().split()

    a = cards[:n//2 + n % 2 + 1]
    b = cards[n//2 + n % 2:]

    lst = []

    for i in range(n):
        if i % 2 == 0:
            lst.append(a.pop(0))
        else:
            lst.append(b.pop(0))

    print(f'#{tc}', *lst)