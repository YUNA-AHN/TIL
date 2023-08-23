'''
정곤이의 증가하는 단조
규칙은 단조 증가하는 수, 각 숫자의 수가 단순하게 증가하는 수
양의 정수 n개
ai * aj 값이 단조 증가하는 수인 것들을 구하고 그중의 최댓값을 출력
단조 증가하는 수가 없다면 -1
'''
def check(num):
    # 순회하면서 체크해주기 위해 문자열로 변환
    char = str(num)
    
    # 단조증가하는지 체크
    condition = 0
    
    # 다음에 오는 수가 더 크다면 1
    # 아니라면 0, 반환
    for i in range(len(char)-1):
        if int(char[i]) <= int(char[i+1]):
            condition = 1
        else:
            condition = 0
            return condition
    return condition

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    # 최댓값 변수 생성
    mx = 0
    # ai = 1 - n-1 / aj  = i - n
    for i in range(n-1):
        for j in range(i+1, n):
            a = nums[i] * nums[j]
            # 단조 증가한다면 최댓값 갱신
            if check(a):
                mx = max(a, mx)
    # 단조 증가하는 함수가 없다면 -1
    if mx == 0:
        mx = -1

    print(f'#{tc} {mx}')
