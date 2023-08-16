'''
계산기 1
'''
import sys
sys.stdin = open("C:/Users/sgvin/Downloads/input (2).txt", "r")

for tc in range(1, 11):
    N = int(input())
    text = input()

    # 후위표기식으로 변경
    stack = []
    susik = ''
    for x in text:
        if x != '+': # 숫자면 바로 수식으로
            susik += x
        else:
            if stack: # 스택에 연산자가 존재하면 무조건 pop (순위가 동등한 +뿐이기 때문)
                susik += x
            else:
                stack.append(x)
    susik += stack[0] # 마지막에 다 돌고 마지막

    # 후위표기식 계산
    stack = []
    for x in susik:
        if x != '+':
            stack.append(x)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(int(op1) + int(op2))

    print(f'#{tc} {stack[0]}')