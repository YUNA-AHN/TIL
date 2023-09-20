def make_set(n): # 각 요소를 부모로 자기 자신을 초기화
    # 초기화를 진행한다. (각 요소를 자기 자신으로 초기화 진행)
    parent = [i for i in range(n+1)]
    return parent
def find_set(x): # 요소 x에 대해서 대표자(부모)를 찾아서 반환
    # 자기 자신을 가리키는 노드라면 자신을 반환 (대표자를 찾을 때까지)
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x]) # 최적화: 경로 압축
        return parent[x]

def union(x, y) : #요소 x, y 속해있는 두개의 그룹을 하나로 통합
    parent_x = find_set(x)
    parent_y = find_set(y)

    if parent_x != parent_y:
        parent[parent_x] = parent_y

# 노드 갯수
n = 10
parent = make_set(n)

union(1, 2)
union(3, 4)
union(2, 4)
print(parent)