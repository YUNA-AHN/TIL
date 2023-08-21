'''
subtree
노드 N을 루트로하는 서브트리에 속한 노드의 개수를 알아내는 프로그램
'''
def postorder(root):
    global cnt, n
    cnt += 1
    if root == n:
        return
    if root:
        postorder(ch1[root])
        postorder(ch2[root])


T = int(input())

for tc in range(1, T+1):
    # 간선의 개수 e, 루트 n
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    # 자식 1, 2
    ch1 = [0] * (e + 2)
    ch2 = [0] * (e + 2)
    par = [0] * (e + 2)

    for i in range(e):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0: # 왼쪽 노드가 비어 있으면 입력
            ch1[p] = c
        else:           # 아니면 오른쪽 노드
            ch2[p] = c
        par[c] = p

    root = 1
    while par[root] != 0:
        root += 1

    postorder(root)

    print(cnt)