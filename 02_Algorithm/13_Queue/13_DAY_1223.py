'''
계산기 2
'''
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/input.txt','r')

for tc in range(1,11):
    n = int(input())
    text = input()

    stack = []
    susik = ''
    for x in text:
        if x not in '+*':
            susik += x
        else:
            if x == '+':
                if stack: # 스택에 값이 있으면
                    while stack: # 빼야한다 : 우선순위가 같거나 높을테니까
                        susik += stack.pop()
                    stack.append(x) # 다 빼고난 후에 연산자 스택에 삽입
                else: # 스택이 비어있으면 넣기
                    stack.append(x)

            else:
                if len(stack) == 0: # 빈 스택이면 스택에 삽입
                    stack.append(x)
                elif stack[-1] == '+': # peek 가 +여도 스택에 삽입
                    stack.append(x)
                else: # *이면 + 나올때까지 pop
                    susik += stack.pop()
                    stack.append(x)
    if stack:
        for i in stack[::-1]:
            susik += i


    # 후위 표기식 계산
    stack = []
    for x in susik:
        if x not in '+*':
            stack.append(x)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if x == '+':
                stack.append(int(op1)+int(op2))
            else:
                stack.append(int(op1)*int(op2))

    print(f'#{tc} {stack[0]}')