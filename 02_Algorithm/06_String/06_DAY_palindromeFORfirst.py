'''
회문이면 1을 출력, 아니라면 0을ㄹ 출력
'''

T = int(input())
for tc in range(1, T +1):
    word = input().strip() # 공백제거

    # 단어를 거꾸로 해도 동일한지 확인
    if word == word[::-1]:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')

# 슬라이실 없이!
T = int(input())
for tc in range(1, T +1):
    word = input().strip() # 공백제거

    word_reverse = ''
    for s in word:
        word_reverse = s + word_reverse

    if word == word_reverse:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')

