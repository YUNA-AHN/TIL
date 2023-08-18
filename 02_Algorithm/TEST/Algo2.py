# 스택이 비어있다면 True를 반환하는 함수 생성
def isEmpty(stack):
    if len(stack) == 0:
        return True
    return False

T = int(input())
for tc in range(1, T + 1):
    arr = list(input())

    # 빈 스택 생성
    stack = []
    # 조건 충족 여부 확인을 위한 condition 변수 생성
    condition = True

    # 값을 순회
    for item in arr:
        # 닫는 괄호가 아니라면 스택에 push
        if item != ')' and item != '}':
            stack.append(item)
        # 닫는 괄호라면
        else:
            # 스택이 비었다면 조건 미충족
            if isEmpty(stack):
                condition = False
                break

            # 연산 수행을 위한 num_list 생성
            num_list = []
            check = stack.pop(-1)
            # pop한 값에 여는 괄호가 나올 때까지 num_list에 추가
            while check != '(' and check != '{':
                # 문자열이 들어오는 경우 : 숫자라면 정수 출력, 문자라면 -1 출력
                try:
                    num_list.append(int(check))
                    if isEmpty(stack): # 추가하는 중에 리스트가 빈다면 조건 미충족
                        condition = False
                        break
                    else:
                        check = stack.pop(-1)
                except ValueError:
                    condition = False
                    break

            sum_v = 0 # 더하기 연산 수행시
            star_v = 1 # 곱하기 연산 수행시
            if item == ')' and check == '(': # 소괄호인 경우 num_list 모두 더해주기 : item in ['(', '[']
                for i in num_list:
                    sum_v += i
                stack.append(sum_v)
            elif item == '}' and check == '{': # 중괄호인 경우 num_list 모두 곱해주기
                for i in num_list:
                    star_v *= i
                stack.append(star_v)
            else: # 여는 괄호와 닫는 괄호 짝이 맞지 않는 경우 조건 미충족
                condition = False
                break
        
        # 조건 미충족한다면 ans = -1
        if condition == False:
            ans = -1
            break
            
    # 조건을 충족하고, 괄호에 둘러쌓이지 않은 숫자가 존재하지 않는 경우
    # 괄호에 둘러쌓이지 않은 숫자가 존재하지 않는 경우, 최종 결과 값 하나만 스택에 존재함
    if condition == True and len(stack) == 1:
        ans = stack[0]
    else:
        ans = -1

    print(f'#{tc} {ans}')