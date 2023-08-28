'''
패턴 마디의 길이
반복되는 부분을 마디, 문자열을 입력받아 마디의 길이를 출력하는 프로그램을 작성
각 문자열의 길이는 30, 마디의 최대 길이는 10
'''
T = int(input())
for tc in range(1, T+1):
    text = input()

    # 10글자까지 패턴이 될 수 있으므로 1~11까지 체크
    for i in range(1, 11):
        # 해당 글자수 단위로 동일하다면 패턴 길이 입력 후 종료
        # cocoa 와 같은 경우 방지하기 위하여 2번 반복해줌
        if text[:i] == text[i: i+i] == text[i+i: i+i+i]:
            ans = i
            break

    print(f'#{tc} {ans}')