'''
NxN 크기의 글자판에서 길이가 M인 회문 찾아 출력
가로 뿐만 아니라 세로로 찾아질 수도 있다
'''

# 함수 없는 버전
# 회문인지 확인하는 함수 is_palin 생성
def is_palin(text):
    text_reverse = ''
    for s in text:
        text_reverse = s + text_reverse

    if text == text_reverse:
         result = text # 회문이라면 해당 text 반환
    else:
        result = 0 # 회문 아니라면 0 반환
    return result

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for r_idx in range(N):
        for c_idx in range(N - M + 1):  # N-M+1번 순회
            text_r = ''
            text_c = ''
            for n in range(M):  # 길이가 M인 텍스트
                text_r += arr[r_idx][c_idx + n]
                text_c += arr[c_idx + n][r_idx]

            if is_palin(text_r): # text_r이 회문이면 ans에 text_r
                ans = is_palin(text_r)
            if is_palin(text_c):# text_c이 회문이면 ans에 text_c
                ans = is_palin(text_c)
    print(f'{tc} {ans}')

# # 함수 사용 버전 ----------
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = ''
    # 가로
    for r_idx in range(N):
        for c_idx in range(N-M+1): # N-M+1번 순회
            text_r = ''
            for n in range(M): # 길이가 M인 텍스트
                text_r += arr[r_idx][c_idx + n]
        if text_r == text_r[::-1]:
            ans = text_r

    # 세로
    for c_idx in range(N):
        for r_idx in range(N-M+1): # N-M+1번 순회
            text_c = ''
            for n in range(M): # 길이가 M인 텍스트
                text_c += arr[r_idx + n][c_idx]
        if text_c == text_c[::-1]:
            ans = text_c

    print(f'#{tc} {ans}')

