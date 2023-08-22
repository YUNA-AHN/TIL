'''
삭제
'''
def deq():
    global last
    tmp = heap[1]           # 루트백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1       # 루트에 옮긴 값을 자식과 비교
    c = p * 2   # 왼쪽 자식 (비교할 자식노드 번호)
    while c <= last: # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1      # 비교 대상이 오른쪽 자식 노드
        if heap[p] < heap[c]: # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c # 자식을 새로운 부모로
            c = p * 2 # 왼족 자식 번호를 계산
        else:   # 부모가 더 크면
            break # 비교 중단
    return tmp

heap = [0] * 100
last = 0


# 최소힙 구현(라이브러리 heapq 사용)
from heapq import heappop, heappush, heapify

# 우선순위 큐 값이 가장 작은 값을 꺼내고 넣는 과정
heap = [] # 비어있는 리스트(완전 이진 트리 형태를 저장)

heappush(heap, 80)
heappush(heap, 40)
heappush(heap, 30)
heappush(heap, 90)
heappush(heap, 100)

print(heap) # [30, 80, 40, 90, 100]

item = heappop(heap)
print(item)
print(heap) # [40, 80, 100, 90] : 마지막 값인 100을 맨위로올린 후 더 작은 자식 노드와 교환

# 최대힙은 음수로 변경해서 사용!