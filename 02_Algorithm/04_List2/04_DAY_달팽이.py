# 이차원 델타
'''
달팽이 N*N 숫자가 시계방향
정수 N을 입력받아 달팽이 출력하시오

달팽이 크기 N은 1이상 10 이하의 정수
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 오른쪽, 아래, 위, 왼쪽 방향
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    arr = [[0] * N for _ in range(N)]

