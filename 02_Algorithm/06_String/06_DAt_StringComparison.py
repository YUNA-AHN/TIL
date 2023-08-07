'''
str2안에서 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
존재하면 1 아니면 0
'''
T = int(input())
for tc in range(1, T +1):
    keyword = input()
    text = input()

    if keyword in text:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')

# 순차적으로..?
