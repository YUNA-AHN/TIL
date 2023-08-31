# 부분집합
a = [3, 6, 7, 1, 5, 4]
N = 6
# for i in range(1, (1<<N)-1)
for i in range(1, (1<<N)//2): # 케이스 빼주면서 원하는 부분집합만 출력
    subset1 = []
    subset2 = []
    total1 = total2 = 0
    min_v = 0
    for j in range(N):
        if i &(1<<j):   # j번 비트가 0이 아니면
            subset1.append(a[j])
            total1 += a[j]
        else:
            subset2.append(a[j])
            total2 += a[j]
    r1 = subset1
    r2 = subset2
    if r1 and r2:
        if min_v > abs(total1 - total2):
            min_v = abs(total1 - total2)
    print(subset1, subset2)