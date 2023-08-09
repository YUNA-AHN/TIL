# push
def push(item, size):
    global top
    top += 1 # top을 증가
    if top == size:
        print('overflow!') # 디버깅 목적
    else:
        stack[top] = item # top이 가리키는 곳에 저장


size = 10
stack = [0] * size
top = -1

push(10, size)
# push(20)
top += 1
stack[top] = 20

print(stack)

# pop
def pop():
    global top
    if top == -1 :
        print('underflow') # 디버깅용 출력
        return 0
    else:
        top -= 1 # 먼저 top을 내려주고!
        return stack[top+1] # 아까 내 있던 자리 가져가라!

print(pop())

#  pop()
if top > -1:
    top -= 1
    print(stack[top+1])

# 스택 구현하기
stack = [0] * 10
top = -1

# push(1)
top += 1
stack[top] = 1
# push(2)
top += 1
stack[top] = 2
# push(3)
top += 1
stack[top] = 3
# pop(3)
print(stack[top])
top -= 1
# pop(2)
top -= 1
print(stack[top])


# stack with 강사님
#  빈 리스트
stack = []

# push : 마지막에 요소를 삽입
def push(item):
    stack.append(item)

# pop : 마지막에 요소를 꺼내는 연산
# pop을 시행했을 때 요고사 없다면 ?? 에러!
def pop():
    if len(stack) == 0:
        return
    return stack.pop()

# 삽입(push) 3개
push(10)
push(20)
push(30)

# 삭제(pop) 3개
item = pop()
print(item)
item = pop()
print(item)
item = pop()
print(item)
item = pop()
print(item)

# peek : 가장 마지막에 넣었던 요소의 값 반환 함수
def peek():
    if len(stack) == 0:
        return
    return stack[-1]

# isEmpty : 현재 스택이 비어있는지 여부를 반환해주는 함수
def isEmpty():
    if len(stack) == 0 :
        res = True
    else:
        res = False
    return res

# peek를 후에 선언한다면
def isEmpty():
    if len(stack) == 0:
        return
    return stack[-1]


