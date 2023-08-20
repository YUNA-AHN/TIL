'''
369 게임
'''
n = int(input())
arr = []

for x in range(1, n+1):
    text = ''
    cnt = 0
    for char in str(x):
        if char in ['3', '6', '9']:
            text += '-'
            cnt += 1

        else:
            text += char

    # 박수가 한번이었으면 - 로 넣어주기
    if cnt == 1:
        arr.append('-')
    else: arr.append(text)

print(*arr)
