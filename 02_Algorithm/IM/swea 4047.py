'''
영준이 카드 게임
한 덱의 카드 : 무늬별 13장의 카드
스페이드, 다이아몬드, 하트, 클로버 무늬 별로 A, 2~10,J,Q,K
1-13
몇 장의 카드가 더 필요한지?
이미 겹치는 카드를 가지고 있다면 오류 출력

T는 카드의 무늬 : S, D, H, C이며 XY는 카드의 숫자 (01 ~ 13)
무늬 별로(S, D, H, C 순서로) 몇 장의 카드가 부족한지 출력

이미 겹치는 카드가 있다면 문자열 ERROR 출력
'''
T = int(input())
for tc in range(1, T+1):
    cards = input()
    # 카드덱 딕셔너리 생성
    deck = {
        'S': [0] + [1] * 13,
        'D': [0] + [1] * 13,
        'H': [0] + [1] * 13,
        'C': [0] + [1] * 13
    }
    
    # 기본 ans 생성
    ans = ''
    # 카드 인덱스마다 돌기
    for i in range(0, len(cards), 3):
        # 이미 해당 카드 인덱스가 0 이하일 때 에러 & break
        if deck[cards[i]][int(cards[i+1:i+3])] <= 0:
            ans = 'ERROR'
            break
        # 해당 인덱스에 카드 하나 빼주기
        deck[cards[i]][int(cards[i+1:i+3])] -= 1
    
    # ans에 error 값이 추가되지 않았다면, 필요한 남은 카드 수 출력
    if not ans:
        ans = f'{sum(deck["S"])} {sum(deck["D"])} {sum(deck["H"])} {sum(deck["C"])}'

    print(f'#{tc} {ans}')