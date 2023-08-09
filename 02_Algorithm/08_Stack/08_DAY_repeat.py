'''
문자열 s  반복된 문자 삭제
지워진 부분은 다시 앞뒤를 연결, 연결에 의한 반복문자 생성시 다시 삭제
'''

T = int(input())

for tc in range(1, T + 1):
    text = input()

    stack = [] # 빈 스택 설정
    for s in text:
        if len(stack) == 0: # 스택이 비어 있다면 push
            stack.append(s)
        elif stack[-1] == s: # peek가 현재 문자와 동일하다면 pop
            stack.pop(-1)
        else: # 아무것도 해당되지 않으면 push
            stack.append(s)

    res = len(stack)

    print(f'#{tc} {res}')