'''
0~N번 정류장
최대한 이동할 수 있는 정류장 수 K
충전기 설치된 M개의 정류장 번호
최소한 몇번의 충전을 해야 하는지?!
    충전기 설치가 잘못되어 도착 X : 0 출력
'''
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))