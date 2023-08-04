'''
10X10  빨간색과 파란색
N개의 영역에 대한 왼쪽위, 오른쪽 아래 인덱스, 칠할 색상

보라섹인 칸 수

T = 테스트 케이스
N = 칠할 영역의 개수
r1, c1 = 왼쪽 위 모서리 인덱스
r2, c2 = 오른쪽 아래 모서리
color = 1 (빨강) color = 2 (파랑)
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr1 = [[0] * 10 for _ in range(10)] # 빨강
    arr2 = [[0] * 10 for _ in range(10)] # 파랑

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1:
            for r_idx in range(r1, r2 + 1):
                for c_idx in range(c1, c2 + 1):
                    arr1[r_idx][c_idx] = 1
        else:
            for r_idx in range(r1, r2 + 1):
                for c_idx in range(c1, c2 + 1):
                    arr2[r_idx][c_idx] = 1
    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr1[r][c] and arr2[r][c]:
                cnt += 1

    print(f'#{tc} {cnt}')
