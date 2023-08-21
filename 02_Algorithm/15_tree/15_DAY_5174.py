'''
subtree
노드 N을 루트로하는 서브트리에 속한 노드의 개수를 알아내는 프로그램
'''
def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T + 1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))

    ch1 = [0] * (e + 2)
    ch2 = [0] * (e + 2)

    for i in range(e):
        p, c = arr[i * 2], arr[i * 2 + 1]

        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

        cnt = 0
        preorder(n)

    print(f'#{tc} {cnt}')