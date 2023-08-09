'''
붙어있는 쌍을 소거하고 납은 번호로 비밀번호
'''

for tc in range(1, 11):
    N, arr = input().split()

    stack = [] # 빈 스택
    for i in range(int(N)):
        if len(stack) == 0: # 스택이 비어있다면 push
            stack.append(arr[i])
        elif stack[-1] == arr[i]: # peek와 현재 값디 동일하다면 pop
            stack.pop(-1)
        else: # 모두 아니라면 push
            stack.append(arr[i])
    res = ''.join(stack)

    print(f'#{tc} {res}')