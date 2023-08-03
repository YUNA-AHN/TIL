'''
1부터 12까지의 숫자를 원소로 가진 집합 A
N개의 원소, 원소의 합이 K인 부분집합의 개수를 출력

부분집합 없는 경우 0
모든 부분 집합을 만들어 답을 찾아도 된다.
'''
T = int(input())

arr = list(range(1, 13)) # 집합 A

for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0 # 원소의 합이 K인 부분집합의 개수
    for i in range(1 << len(arr)):
        res = [] # 부분집합을 받을 리스트 생성
        for j in range(len(arr)):
            if i & (1 << j):
                res.append(arr[j])

        if len(res) == N and sum(res) == K: # 부분집합의 길이가 N이고 합이 K일 때!
            cnt += 1

    print(f'#{tc} {cnt}')


# 강사님 코드 ---

T = int(input())

for tc in range(1, T+1):
    # 입력
    N, K = map(int, input().split())
    # N개의 요소를 가지고 있는 부분집합을 만들고
    # 그 합이 K인 요소를 카운트 해라
    cnt = 0
    # 부분집합을 만드는 코드
    # 1 ~12까지의 숫자를가지는 집합
    arr = [i for i in range(1, 13)]

    # 부분집합을 생성하는 코드(비트 연산)
    for i in range( 1 << 12):
        total = 0 # 부분집합 요소들의 합
        length = 0 # 부분집합의 요소 갯수
        # i의 j번재 비트가 1인 경우
        for j in range(12):
            if i & (1 << j):
                total += arr[j]
                length += 1
        if length == N and total == K:
            cnt += 1
    print(f'#{tc} {cnt}')