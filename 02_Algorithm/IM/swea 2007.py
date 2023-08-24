'''
패턴 마디의 길이
반복되는 부분을 마디, 문자열을 입력받아 마디의 길이를 출력하는 프로그램을 작성
각 문자열의 길이는 30, 마디의 최대 길이는 10
'''
T = int(input())
for tc in range(1, T+1):
    text = input()

    for i in range(1, 11):
        if text[:i] == text[i: i+i] == text[i+i: i+i+i]:
            ans = i
            break

    print(f'#{tc} {ans}')