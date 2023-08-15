'''
Forth
숫자는 스택에
연산자를 만나면 숫자 두개를 꺼내 더하고 다시 스택에
. 스택에서 숫자를 꺼내 출력
연산이 불가능한 경우 error 출력
'''
T = int(input())
for tc in range(1, T+1):
    susik = input().split()
    stack = [0] * 50
    top = -1

    for x in susik:
        if x not in '+-*/.': # 피연산자라면 더하기
            top += 1
            stack[top] = int(x)
        else:
            if top == 0 and x == '.':  # 계산이 정상적으로 완료되었다면 top = 0
                ans = stack[top]

            elif top >= 1: # 2개의 피연산자를 뽑아야 하니 top이 1 이상인 경우
                op2 = stack[top]
                top -= 1
                op1 = stack[top]
                top -= 1

                if x == '+':
                    top += 1
                    stack[top] = op1 + op2
                elif x == '-':
                    top += 1
                    stack[top] = op1 - op2
                elif x == '*':
                    top += 1
                    stack[top] = op1 * op2
                elif x == '/':
                    top += 1
                    stack[top] = op1 // op2
                else: # 연산자에 비해 피연산자가 많은 경우를 고려
                    ans = 'error'
            else:
                ans = 'error'
                break
    print(f'#{tc} {ans}')