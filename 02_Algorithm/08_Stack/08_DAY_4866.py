'''
괄호가 짝을 제대로 이뤘는지?
왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 !
여는 괄호에 push, 닫는 괄호에 pop
1) 괄호 짝이 안맞는 경우
1-1) 수식 끝, 괄호 남음: isEmpty()
1-2) 다든 괄호, 스택이 비어 있음
2) pop과 다른 경우
'''
def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    return stack.pop()

def isEmpty():
    if len(stack) == 0:
        return True
    return False

T = int(input())

for tc in range(1, T + 1):
    text = input()

    # stack 설정
    stack = []
    res = True
    for s in text:
        # 여는 괄호이면 push
        if s == '(' or s == '{':
            push(s)
        # 닫는 괄호이면 pop : 틀리면 걍 False니까 break 걸고 나오기
        elif s == ')' or s == '}':
            if isEmpty(): # 스택이 비었는데 닫는 괄호가 들어오면 ?!
                res = False
                break
            item = pop() # 스택에서 하나 뽑아 왔을 때 !
            if s == ')' and item != '(': # 괄호 짝이 안맞으면 기각
                res = False
                break
            elif s == '}' and item != '{':
                res = False
                break
    # 괄호 검사에서 문제가 없고, 스택도 깔끔하게 비워져있다면 ?!
    if res == True and isEmpty():
        res = True
    else: # 스택에 여는 괄호가 남아있다면...
        res = False

    print(f'#{tc} {int(res)}')

# ( 인데 peek가 )가 아니라면
# { 인데 peek가 }가 아니라면