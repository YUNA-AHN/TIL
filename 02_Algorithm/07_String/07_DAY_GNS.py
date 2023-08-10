'''
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
작은 수 부터 정렬하여 출력하는 프로그램
'''
import sys
sys.stdin = open("C:/Users/sgvin/Downloads/GNS_test_input.txt", "r")

stoi = {
    "ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4,
    "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9
}

itos = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    arr = input().split()

    # stoi 키값으로 접근! -> lambda 함수 사용해서 한번에 진행
    arr = list(map(lambda x: stoi[x], arr))

    arr.sort() # 정렬

    # itos 인덱스 값으로 접근  -> lambda 함수 사용해서 한번에 진행
    arr = list(map(lambda x: itos[x], arr))

    print(tc)
    print(*arr)