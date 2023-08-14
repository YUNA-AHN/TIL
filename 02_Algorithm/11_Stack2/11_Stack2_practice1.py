'''
중위 표현식 문자 순회
높은 우선순위 > 낮은 우선순위
피연산자 > 여는괄호 > * / > + - > )
'''
text = input() # 중위식 표현식

stack = []
result = []

# 문자열을 하나하나씩 순회
for ch in text:
    # 1. 피연산자 (숫자)
        if ch.isdigit():
            print(ch, end = '')
    # 2. 여는 괄호 (3/0
    # 가장 우선 순위가 높기 때문에 스택에 바로 삽입
        if ch =='(':
            stack.append(ch)
    # 3. * / 연산   2
        elif ch in ['*', '/']:
            if len(stack) > 0 and stack[-1] in ['*', '/']:
                # 같은 우선순위를 가진 연산자이기에
                # 스택에서 빼주고 출력
                oper = stack.pop()
                print(oper, end='')
            stack.append(ch)
    # 4. + - 연산   1
        elif ch in ['+', '-']:
            while len(stack) > 0 and stack[-1] in ['*', '/','+', '-']:
                # 같은 우선순위를 가진 연산자이기에
                # 스택에서 빼주고 출력
                oper = stack.pop()
                print(oper, end='')
            stack.append(ch)
    # 5. 닫는 괄호 ) -1
    # 여는 괄호가 나올 때까지 스택을 pop을 하면서 진행한다.
        elif ch == ')':
            while len(stack) > 0 and stack[-1] == '(':
                # 여는 괄호가 나올 때까지
                oper = stack.pop()
                print(oper, end='')
            stack.pop() # 여는 괄호 제거
# 스택에 남아있는 연산자
# 남아있는 연산자를 pop하며 출력
while len(stack) > 0:
    oper = stack.pop()
    print(oper, end='')
print() # 후위식 표현식