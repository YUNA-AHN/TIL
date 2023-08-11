'''
쇠막대기
카운트 변수
'''
T = int(input())

for tc in range(1, T + 1):
    iron = input()

    stack = []
    ans = 0

    for idx in range(len(iron)):
        # 여는 괄호면 길이 추가 or 레이저
        if iron[idx] == '(':
            stack.append(idx)
        # 닫는 괄호면 끝점 or 레이저
        else:
            # 일단 닫는 괄호 나오면 pop
            stack.pop()
            # 쇠 막대의 끝점이라면 1 더해주기
            if iron[idx - 1] == ')':
                ans += 1
            # 레어저라면! stack의 길이 만큼 더해주기
            # 길이만큼 쇠막대 층이 생성되어 있기 때문
            else:
                ans += len(stack)

    print(f'#{tc} {ans}')