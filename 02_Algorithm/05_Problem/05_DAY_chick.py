'''
병아리
max min sum abs slice 사용할 수 없음!
왼쪽 위 / 오른쪽 아래 칸
평균값 (영역에 병아리 개수) // (영역의 칸 수) : 소수점 아래는 버린다.

한 번의 작업으로 병아리를 1라미 더 놓거나 뺄 수 있다.
'''

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