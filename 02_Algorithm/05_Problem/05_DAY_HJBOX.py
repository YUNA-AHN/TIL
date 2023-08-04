'''
현주의 상자 바꾸기
1-N 까지 N개의 상자 / 모두 숫자 0
Q회 동안 일정 범위의 연속한 상자 동일한 숫자로 변견
i번째 작업에 대해 L번 상자부터 R번 상자까지
'''

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split()) # 상자 개수 N, 작업 회수 Q

    cnt = [0] * (N + 1)

    for i in range(1, Q+1):
        l, r = map(int, input().split())

        for idx in range(l, r + 1):
            cnt[idx] = i # i번째 작업일 때 i값 입력

    print(f'#{tc}', *cnt[1:])