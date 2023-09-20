'''
두 사람의 친구 네트워크에 몇명이 있는지?
친구 관계만으로 이동할 수 있는 사이!
'''
import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        parents[x] = py

t = int(input().strip())
for _ in range(t):
    parents = dict()
    n = int(input().strip())
    for _ in range(n):
        a, b = input().split()
        # 친구 이름이 존재하지 않는다면, 키를 추가해주고 값으로 친구 이름을 입력
        parents.setdefault(a, a)
        parents.setdefault(b, b)

        union(a, b)

        print(parents)