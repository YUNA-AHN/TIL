'''
농작물 수확하기
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    sum_v = 0
    # 행 순회
    for i in range(n//2):
        # 중앙에서 부터 뻗어나가도록 범위 지정
        for j in range(n//2-i, n//2+i+1):
            # 첫행과 마지막 행으로부터 중간 줄로 수렴하도록
            sum_v += arr[i][j]
            sum_v += arr[n-i-1][j]

    # 더해주지 않은 중간줄 추가로 더해주기
    for k in arr[n//2]:
        sum_v += k

    print(sum_v)