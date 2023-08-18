n = int(input())
arr = []

for x in range(1, n + 1):
    text = ''
    cnt = 0
    for char in str(x):
        if char in ['3', '6', '9']:
            cnt += 1

        else:
            text += char

    if cnt >= 1:
        arr.append('-'*cnt)
    else:
        arr.append(text)

print(*arr)