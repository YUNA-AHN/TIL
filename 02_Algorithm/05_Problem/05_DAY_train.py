'''
D 두 기차 전면부 사이의 거리
A 기차 A의 속력
B 기차 B의 속력
F 파리 F의 속력

파리는 몇 마일?
'''
T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    print(f'#{tc} {(D / (A + B)) * F}') # 파리가 살아 있는 동안...
