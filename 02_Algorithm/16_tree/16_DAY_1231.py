'''
중위순회
순서가 뒤바껴 있을 수도!
'''
def inorder(p,n):
    if p <= n: # 완전 이진트리의 마지막 정점
        inorder(p*2, n) # 왼쪽으로 : 왼쪽 자식 노드 인덱스 : 부모노드 * 2
        print(tree[p], end='')
        inorder(p*2+1, n) # 오른쪽으로 : 오른쪽 자식 노드 인덱스 : 부모노드 * 2 + 1

for tc in range(1, 11):
    n = int(input()) # 정점의 총 수
    tree = [0] * (n+1)

    for _ in range(n):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위 순회
    print(f'#{tc}', end = ' ')
    inorder(1, n) # root = 1, 루트가 1이라고 지정 및 완전 이진트리
    print()