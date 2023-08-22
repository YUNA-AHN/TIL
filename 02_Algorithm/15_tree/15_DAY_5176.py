'''
이진탐색
루트 값, n//2번 노드
'''
def inorder(tree, p):
    global cnt
    if p > n: # 노드 개수를 넘어가면 멈추기
        return
    # 중위 순회
    inorder(tree, p*2)
    cnt += 1 # 함수 호출마다 1씩 증가
    tree[p] = cnt
    inorder(tree, p*2+1)


T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 노드 개수
    tree = [0] * (n+1) # 트리 생성

    cnt = 0 # 카운트
    inorder(tree, 1)

    print(f'#{tc} {tree[1]} {tree[n // 2]}')


# # 강사님 코드
# # 중위 순회 코드
# def inorder(tree, p):
#     global cnt
#     if p > n:
#         return
#     inorder(tree, p * 2)
#     # 자기자신에 대한 탐색
#     # 오름차순으로 넣을 요소값을 할당
#     cnt += 1
#     tree[p] = cnt # 중위순회하면서 입력..
#     inorder(tree, p * 2 + 1)
#
# T = int(input())
# for tc in range(1, T+1):
#     # 노드의 개수
#     n = int(input())
#
#     # 로직
#     # 완전이진트리이면서, 이진탐색트리에 해당되는 노드 개수가 N개인 트리를 만들어라
#     tree = [0] * (n+1)
#
#     # 이진탐색트리의 특징 중에 하나인
#     # 중위수회를 하였을 때에 " 오름차순 "이 된다는 특징 사용
#     cnt = 0 # 카운트 변수
#     inorder(tree, 1) # 중위순회를 하면서 오름차순으로 노드값을 채워넣는다
#
#     # 루트노드와 n//2 번째 노드의 값을 출력해라
#     print(f'#{tc} {tree[1]} {tree[n//2]}')