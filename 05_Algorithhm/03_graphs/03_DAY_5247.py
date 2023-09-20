'''
연산
자연수 n에 몇번의 연산 -> 자연수 m
최소 몇번의 연산?
+1 -1 *2 - 10
'''
from collections import deque
t = int(input())
for tc in range(1, t+1):
    num, m = map(int, input().split())
    visited = [0] * (10**6+1)

    que = deque()
    que.append((num, 0))
    while num != m:
        num, cnt = que.popleft()
        visited[num] = 1
        oper = num + 1
        if oper <= 10 ** 6 and visited[oper] == 0:
            que.append((oper, cnt + 1))
            visited[oper] = 1
        oper = num * 2
        if oper <= 10 ** 6 and visited[oper] == 0:
            que.append((oper, cnt + 1))
            visited[oper] = 1
        oper = num - 1
        if oper >= 0 and visited[oper] == 0:
            que.append((oper, cnt + 1))
            visited[oper] = 1

        oper = num - 10
        if oper >= 0 and visited[oper] == 0:
            que.append((oper, cnt + 1))
            visited[oper] = 1

    num, cnt = que.popleft()
    print(f'#{tc} {cnt}')