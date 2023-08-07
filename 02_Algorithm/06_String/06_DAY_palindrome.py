'''
NxN 크기의 글자판에서 길이가 M인 회문 찾아 출력
가로 뿐만 아니라 세로로 찾아질 수도 있다
'''
def is_palin(text):
    text_reverse = ''
    for s in text:
        text_reverse = s + text_reverse

    if text == text_reverse:
         result = text
    else:
        result = 0
    return result

print(is_palin('TLMMHOOOHMMLT'))


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 가로
    for r_idx in range(N):
        text_r = ''
        text_c = ''
        for c_idx in range(N):
            text_r += arr[r_idx][c_idx]
            text_c += arr[c_idx][r_idx]

        r_string = is_palin(text_r)
        c_string = is_palin(text_c)

        if r_string:
            ans = is_palin(text_r)
        if c_string:
            ans = is_palin(text_c)

    print(f'#{tc} {ans}')