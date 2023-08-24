'''
사칙연산
'''
def postorder(tree, x):
    global lst
    if x:
        postorder(tree, ch1[x])
        postorder(tree, ch2[x])
        if tree[x].isdigit(): # 숫자라면
            lst.append(float(tree[x]))
        else: # 연산 기호라면
            if len(lst) > 1:
                op2 = lst.pop()
                op1 = lst.pop()
                if tree[x] == '+':
                    lst.append(op1 + op2)
                elif tree[x] == '-':
                    lst.append(op1 - op2)
                elif tree[x] == '*':
                    lst.append(op1 * op2)
                elif tree[x] == '/':
                    lst.append(op1 / op2)
for tc in range(1,11):
    n = int(input())
    tree = [0] * (n + 1)
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    for _ in range(n):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
        if len(arr) > 2 : # 자식 노드가 있다면 ~
            ch1[int(arr[0])] = int(arr[2])
        if len(arr) == 4: # 오른쪽 자식 노드가 있다면 ~
            ch2[int(arr[0])] = int(arr[3])

    lst = []
    postorder(tree, 1)
    ans = int(lst[0])
    print(f'#{tc} {ans}')

