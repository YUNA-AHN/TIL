## 괄호 검사
stack = []
def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    return stack.pop()

def isEmpty():
    if len(stack) == 0 :
        res = True
    else:
        res = False
    return res

def isEmpty():
    if len(stack) == 0:
        return
    return stack[-1]



test1 = "( )( )((( )))"
test2 = "((( )((((( )( )((( )( ))((( ))))))"

for ch in test2:
    # '(' 괄호를 만났을 때는 '(' 삽입
    if ch == '(':
        push('(')
        # ')' 괄호 만났을 때에는 삭제
    elif ch == ')':
        if isEmpty(): # 도중에 비어있는 스택에서 삭제(pop)를 진행
            failed = True
            break
        pop()
if failed == False and isEmpty():
    print('성공')
else:
    print('실패')
# 괄호 검사 성공한 경우는 괄호 검사를 수행 완료한 후에 스택이 비어있는 경우
#   // 실패한 경우는 검사를 수해하는 도중에 비어있는 스택에서 삭제를 진행하려하거나
#           괄호 검사를 수행 완료한 후에 스택이 차 있는 경우 검사 실패

def check(text):
    for ch in test2:
        # '(' 괄호를 만났을 때는 '(' 삽입
        if ch == '(':
            push('(')
            # ')' 괄호 만났을 때에는 삭제
        elif ch == ')':
            if isEmpty():  # 도중에 비어있는 스택에서 삭제(pop)를 진행
                return False
            pop()
    if isEmpty():
        return True
    else:
        return False