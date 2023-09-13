'''
체스판 다시 칠하기
mxn 크기의 보드
검은색과 흰색이 번갈아서 칠해져 있어야 한다
맨 왼쪽 위 칸이 흰생인 경우 / 검은색인 경우
8x8 크기의 체스판으로 잘라낸 후 다시 칠해야 하는 정사각형의 최소 개수 구하는 프로그램
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(n)]

case_a = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
case_b = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

for i in range(n-8+1):
    for j in range(m-8+1):
        for k in range(8):
            if k % 2:
                pass
            else:
                pass