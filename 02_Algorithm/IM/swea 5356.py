'''
의석이의 세로로 말해요
'''
T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    # 가장 긴 문자열 길이 구하기
    max_len = 0
    for i in range(5):
        max_len = max(len(arr[i]), max_len)

    # 열 우선 순회, 5개의 열 가장 긴 문자열 개수 만큼 순ㄴ회
    print(f'#{tc}', end = ' ')
    for j in range(max_len):
        for i in range(5):
            # 해당 인덱스에 값이 존재하지 않으면 pass
            try:
                print(arr[i][j], end = '')
            except:
                pass
    print()
