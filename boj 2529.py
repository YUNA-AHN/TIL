'''
부등호
< > 가 k새 나열된 순서열 A
앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부틍호 관계를 먼족
부등호 관계를 만족시키는 정수
최댓값과 최솟값 두 줄에 걸쳐서
숫자 겹치지 않도록록'''
import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()

for i in range(10):
    visited = [0] * 10
    lst = [i] # 첫번째 값은 일단 순차적으로 돌기
    visited[i] = 1
    for es in arr:
        if es == '>':
            for j in range(10):
                if j < lst[-1] and visited[j] == 0:
                    visited[j] = 1
                    lst.append(j)
                    break
                else:
                    continue
        else:
            for k in range(10):
                if k > lst[-1] and visited[k] == 0:
                    visited[k] = 1
                    lst.append(k)
                    break
                else:
                    continue
    print(lst)