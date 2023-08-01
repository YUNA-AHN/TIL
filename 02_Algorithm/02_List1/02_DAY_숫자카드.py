'''
N: 카드 장수
가장 많은 카드에 적힌 숫자와 카드가 몇장인지?
카드 장수가 같을 때는 적힌 숫자가 큰 쪽 출력
'''

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, list(input())))

    # 숫자카드 범위 길이의 리스트 생성
    c = [0] * 10
    for num in arr:
        c[num % 10] += 1  # 숫자 있는 만큼 더하기
        num //= 10

    # 최댓값일 때 출력, 모두 동일한 경우 가장 큰 값 출력
    max_idx = 0
    for idx in range(len(c)):
        if c[max_idx] <= c[idx]:
            max_idx = idx
    print(f'#{test_case} {max_idx} {c[max_idx]}')