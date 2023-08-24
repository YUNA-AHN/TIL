'''
상호의 배틀필드
전차는 사용자의 전차 하나, 적이나 아군으로 만들어진 전차는 등장 X
맵 밖으로 이동이면 이동 X
포탄 발사 - 벽 충돌 혹은 나감
    - 벽돌이면 박살 강철이면 그대로
.	평지
*	벽돌벽
#	강철벽
-	물(전차는 들어갈 수 없다.)

^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

U	Up : 방향을 위쪽으로 변경, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.

S	Shoot : 바라보고 있는 방향으로 포탄을 발사한다.
'''

def game(key):
    global arr, sx, sy
    if key == 'S':
        if arr[sx][sy] == '^':
            di = -1 # 행에 빼주기
            for i in range(1, h+1):
                ni = sx + di * i
                if 0 <= ni < h and arr[ni][sy] == '#':
                    break
                elif 0 <= ni < h and arr[ni][sy] == '*':
                    arr[ni][sy] = '.'
                    break
        elif arr[sx][sy] == 'v':
            di = 1  # 행에 빼주기
            for i in range(1, h+1):
                ni = sx + di * i
                if 0 <= ni < h and arr[ni][sy] == '#':
                    break
                elif 0 <= ni < h and arr[ni][sy] == '*':
                    arr[ni][sy] = '.'
                    break
        elif arr[sx][sy] == '<':
            dj = -1  # 행에 빼주기
            for i in range(1, w+1):
                nj = sy + dj * i
                if 0 <= nj < w and arr[sx][nj] == '#':
                    break
                elif 0 <= nj < w and arr[sx][nj] == '*':
                    arr[sx][nj] = '.'
                    break
        elif arr[sx][sy] == '>':
            dj = 1  # 행에 빼주기
            for i in range(1, w+1):
                nj = sy + dj * i
                if 0 <= nj < w and arr[sx][nj] == '#':
                    break
                elif 0 <= nj < w and arr[sx][nj] == '*':
                    arr[sx][nj] = '.'
                    break
    elif key == 'U':
        arr[sx][sy] = '^'
        if 0 <= sx-1 < h and arr[sx-1][sy] == '.':
            arr[sx][sy] = '.'
            sx -= 1
            arr[sx][sy] = '^'
    elif key == 'D':
        arr[sx][sy] = 'v'
        if 0 <= sx + 1 < h and arr[sx + 1][sy] == '.':
            arr[sx][sy] = '.'
            sx += 1
            arr[sx][sy] = 'v'
    elif key == 'L':
        arr[sx][sy] = '<'
        if 0 <= sy - 1 < w and arr[sx][sy - 1] == '.':
            arr[sx][sy] = '.'
            sy -= 1
            arr[sx][sy] = '<'
    elif key == 'R':
        arr[sx][sy] = '>'
        if 0 <= sy + 1 < w and arr[sx][sy + 1] == '.':
            arr[sx][sy] = '.'
            sy += 1
            arr[sx][sy] = '>'


T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split()) # h x w 격자판
    arr = [list(input()) for _ in range(h)]
    n = int(input()) # 명령 개수
    bomb = list(input()) # 입력

    # 시작 위치 찾기
    sx, sy = 0, 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] in ['^','v','<','>']:
                sx, sy = i, j

    for char in bomb:
        game(char)

    print(f'#{tc}', end =' ')
    for i in arr:
        ans = ''.join(i)
        print(ans)