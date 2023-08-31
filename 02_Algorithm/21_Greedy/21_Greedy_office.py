N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meet = []
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
meet.sort(key = lambda x: x[1])

meet = [[0, 0]] + meet
print(meet)
S = []
i = 0
for j in range(1, N+1):
    if meet[j][0] > meet[i][1]:
        S.append(j)
        i = j
print(S)