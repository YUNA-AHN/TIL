# 부분 집합과 비트 연산자
arr = [3, 6, 7]

n = len(arr) # n : 원소의 개수

for i in range(1 << n): # 1 << n: 2^n 부분집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1 << j): # i의 j번 비트가 1인 경우 : 그 자리에 있냐 !!!!!
            c = arr[j]
            print(arr[j], end = ', ') # j번 원소 출력
    print()
print()

'''
i가 한 번의 부분집합 케이스
3, 6이 나오는건
i = 2 : 1 1 일 때
j = 0 : 0 1 / j = 1 : 1 0 에 걸려서 !! 
'''

# 순차 검색 - 정렬되지 않은 경우
def f(a, n, key):
    for i in range(n):
        if key == a[i]:
            return i
    return -1