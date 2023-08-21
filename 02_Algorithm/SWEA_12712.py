'''
파리퇴치3
'''
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n 크기, m 세기
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 최댓값 변수
    mx = 0
    # 모든 인덱스 순회
    for i in range(n):
        for j in range(n):
            sum_1 = sum_2 = arr[i][j] # 합 초기값 설정
            for k in range(1, m): # 스프레이 세기만큼 순회
                for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]: # +
                    ni = i + di * k
                    nj = j + dj * k
                    if 0 <= ni < n and 0 <= nj < n:
                        sum_1 += arr[ni][nj]

                for ki, kj in [[1,1], [1,-1],[-1,-1],[-1,1]]: # x
                    ei = i + ki * k
                    ej = j + kj * k
                    if 0 <= ei < n and 0 <= ej < n:
                        sum_2 += arr[ei][ej]
            # sum_1, sum_2, mx 중 최댓값으로 갱신
            mx = max(sum_1, sum_2, mx)
    print(f'#{tc} {mx}')