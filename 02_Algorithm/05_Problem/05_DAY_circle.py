'''
원점을 중심으로 반지름 N인 원 안에 포함되는 격자점 개수
x^2 + y^2 <= N^2
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    cnt = 0
    for x in range(-N, N+1): # -N과 N사이에 존재하는 모든 좌표에 대하여
        for y in range(-N, N+1):
            if x**2 + y**2 <= N**2:
                cnt += 1

    print(f'#{tc} {cnt}')