'''
마그네틱
성질에 따라 색이 부여,
푸른 자성체 - N에 끌림 / 붉은 자성체 - S에 끌림
일정 간견을 두고 강한 자기장을 걸었을 때,
자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수
파-빨 만나면 무조건 1개
'''
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 1 다음에 2가 왔을 때!
    # 열 별로 보는게 좋을듯
    cnt = 0
    for j in range(n):
        for i in range(n):
            if arr[i][j] == 1:
            # 다음에 오는 친구가 2여야함
            # 1을 만나면 멈춰 어차피 안더해짐
                for k in range(i+1, n): # 다음부터 열 끝까지
                    if arr[k][j] == 1: # 1을 만나면 멈추기
                        break
                    elif arr[k][j] == 2: # 2를 만나면 더해주고 멈추기
                        cnt += 1
                        break

    print(f'#{tc} {cnt}')
