T = int(input())
for tc in range(1, T+1):
    # N : 돌아가야 할 학생들의 수
    N = int(input())
    count = [0] * 101
    for _ in range(N):
        # 현재의 방, 돌아갈 방
        a, b = map(int, input().split())

        # 복도의 시작점, 끝점
        a = (a - 1) // 2
        b = (b - 1) // 2
        if a > b:
            a,b = b, a

        # 해당복도의 시작점에서 끝점까지 카운트를 1씩
        for i  in range(a, b+1):
            count[i] += 1

    # 가장 많이 겹치는 영역의 카운트 수를 가져오기
    answer = max(count)

    # 출력
    print(f'#{tc} {answer}')