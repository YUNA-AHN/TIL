# 색칠하기 ---
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 빈 배열 생성 : 곱해주기 위해서 1로 채움
    arr = [[1] * 10 for _ in range(10)]

    # 색칠 횟수 만큼 반복
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r_idx in range(r1, r2 + 1):
            for c_idx in range(c1, c2 + 1):
                # 동시에 칠해져있을 때 라는 조건때문인걸까?
                arr[r_idx][c_idx] *= color + 1

        ans = 0
        for i in range(10):
            for j in range(10):
                if arr[i][j] != 0 and arr[i][j] % 6 == 0:
                    ans += 1

    print(f'{tc} {ans}')

# 파리퇴치  ---
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for r_idx in range(N):
        for c_idx in range(N):
            sum_v = 0
            for i in range(M):
                for j in range(M):
                    ni = r_idx + i
                    nj = c_idx + j

                    if 0 <= ni < N and 0 <= nj < N:
                        sum_v += arr[ni][nj]

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')


# 병아리 분배
# 영역에 포함된 병아리 수 평균 구하는 함수
def my_average(arr, l_r, l_c, r_r, r_c):
    total = cnt = 0
    for r_idx in range(l_r, r_r + 1):
        for c_idx in range(l_c, r_c + 1):
            total += arr[r_idx][c_idx]
            cnt += 1

    aver = total // cnt
    return aver


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    l_r, l_c, r_r, r_c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    aver = my_average(arr, l_r, l_c, r_r, r_c)

    cnt = 0
    # 인덱스를 돌아가면서 cnt 더해주기
    # 평균과 값의 차를 cnt
    for r_idx in range(l_r, r_r + 1):
        for c_idx in range(l_c, r_c + 1):
            if arr[r_idx][c_idx] > aver:
                cnt += (arr[r_idx][c_idx] - aver)
            elif arr[r_idx][c_idx] < aver:
                cnt += (aver - arr[r_idx][c_idx])

    print(f'#{tc} {cnt}')
