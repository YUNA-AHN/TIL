'''
두 사람의 친구 네트워크에 몇명이 있는지?
친구 관계만으로 이동할 수 있는 사이!

시간초과..
'''
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
        cnt[px] += cnt[py]
        parents[py] = px

    return cnt[px]


t = int(input().strip())
for _ in range(t):
    parents = dict()
    cnt = dict()
    n = int(input().strip())
    for _ in range(n):
        a, b = input().split()
        # 친구 이름이 존재하지 않는다면, 키를 추가해주고 값으로 친구 이름을 입력
        parents.setdefault(a, a)
        parents.setdefault(b, b)
        # 카운트 딕셔너리. 존재하지 않는다면 키를 추가해주고 1 입력
        cnt.setdefault(a, 1)
        cnt.setdefault(b, 1)

        res = union(a, b)
        print(res)

        # print(parents)
        # # parents.values()).count(parents[a]
        # # find 활용해서 체크 리스트 만들어서
        # # find(a)와 find(b)는 동일할 것 union 했으니까..! find(a)와 동일하면 더해주자
        # cnt = 0
        # for key in parents.keys():
        #     if find(key) == find(a):
        #         cnt += 1
        #
        # print(cnt)
        # print(parents)
