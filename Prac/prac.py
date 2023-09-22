'''
RGB거리
아래의 조건을 모두 만족하면서 모든 집을 칠하는 비용의 최솟값
1번집의 색은 2번집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 <= i <= N-1) i-1번, i+1번 집의 색과 같지 않아야 한다.

3
26 40 83
49 60 57
13 89 99
- 96

3
1 100 100
100 1 100
100 100 1
- 3

3
1 100 100
100 100 100
1 100 100
- 102
'''

# 거짓말
# 거짓말쟁이로 알려지지 않으면서 과장된 이야기 가능한 파티의 개수
import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        parents[py] = px

# 사람의 수, 파티의 수
n, m = map(int, input().strip().split())

# 자기 자신으로 초기화 !
parents = [i for i in range(n + 1)]

# 진실을 나는 사람의 수, 번호
truth, *arr_t = map(int, input().strip().split())

# 파티의 수 만큼 순회
# 진실을 아는 사람이 있거나 같이 파티에 참석한 적이 있다면(조상노드가 같다면...) 그 파티는 못감
for _ in range(m):
    people, *arr_p = map(int, input().strip().split())

    # 사람 숫자만큼 순회
    for person in arr_p:
        if parents[person] in arr_t:
            pass