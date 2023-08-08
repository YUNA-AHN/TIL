'''
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
작은 수 부터 정렬하여 출력하는 프로그램
'''
import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/GNS_test_input.txt", "r")

num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)
    arr = input().split()

    res_list = []
    result = []
    for num in num_list:
        for i in range(10):
            if num == num_list[i]:
                res_list.append(i)

    res_list.sort()

    for i in res_list:
        result.append(num_list[i])

    print(tc)
    print(*result)


# 강사님 코드 ---
# 딕셔너리 활용하기
stoi = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
itos = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)
    arr = input.split()
    # 요소값을 문자열에서 정수로 바꿔서
    # 정렬을 진행한 다음(오름차순)
    # 정수 -> 문자열 표현
    arr = list(map(lambda x: stoi[x], arr))
    arr.sort()
    # 정수 -> 문자열 표현
    itos = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    arr = list(map(lambda x: itos[x], arr))


# 준영 코드 --------
T = int(input())
for test_case in range(1, T + 1):
    trash, can = input().split()
    arr = input().split() # 문자열 리스트
    txt = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    print(f'#{test_case} ')

    for i in txt: # 숫자 리스트
        for j in range(arr.count(i)): # i가 존재하는 만큼 출력하기
            print(i, end = ' ')