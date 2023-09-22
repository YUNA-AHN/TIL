'''
격자판의 숫자 이어 붙이기
임의의 위치에서 시작하여 동서남북 네방향으로 인접한 격자로 총 여섯 번 이동
서로 다른 일곱 자리 수들의 개수를 구하는 프로그램..
'''
def make_code(i, j, number):
    # 길이가 7이 되면 result에 추가하고 return
    if len(number) == 7:
        result.add(number)
        return

    # 상하좌우 탐색, 이미 방문했던 격자판 재방문 가능 -> 방문 체크 X
    for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
        ni, nj = i + di, j + dj
        # 격자판 내에 존재한다면
        if 0 <= ni < 4 and 0 <= nj < 4:
            make_code(ni, nj, number + arr[ni][nj])

t = int(input())
for tc in range(1, t+1):
    arr = [input().strip().split() for _ in range(4)]

    # 중복 제거
    result = set()

    # 모든 인덱스 순회
    for i in range(4):
        for j in range(4):
            make_code(i, j, arr[i][j])

    # result 요소 개수 출력
    print(f'#{tc} {len(result)}')