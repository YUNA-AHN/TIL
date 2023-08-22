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

# 강사님 코드
T = int(input())


def preorder(tree, p):
    global cnt

    # 기저조건...
    if p == 0:
        return

    # 카운트를 1 증가
    cnt += 1

    # 자기자신에 대한 탐색
    # 왼쪽 자식 탐색 진행
    preorder(tree, tree[p][0])
    # 오른쪽 자식 탐색 진행
    preorder(tree, tree[p][1])


for tc in range(1, T + 10):
    # 입력
    E, N = map(int, input().split())

    # 노드의 부모와 자식 관계의 입력쌍을 리스트 저장
    nodes = list(map(int, input().split()))

    # 로직
    # 자식 노드를 표기할 수 있는 이차원을 배열 tree.
    tree = [[0] * 2 for _ in range(E + 2)]
    for i in range(0, len(nodes), 2):
        # 부모 노드의 번호
        p = nodes[i]
        # 자식 노드의 번호
        c = nodes[i + 1]
        # 부모 자식 관계를 부여...
        if tree[p][0] == 0:
            tree[p][0] = c  # 왼쪽 자식에 C노드를 할당..
        else:
            tree[p][1] = c  # 오른쪽 //

    # N번 노드로 시작해서 순회를 하며, 서브트리 내에 있는 노드의 갯수를 카운트...
    cnt = 0
    preorder(tree, N)
    # 출력
    print(f"#{tc} {cnt}")