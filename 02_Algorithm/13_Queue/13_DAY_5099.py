'''
피자굽기
N새의 피자 동시에 구울 수 있는 화덕
치즈가 모두 녹으면 화덕에서 꺼낸다. 치즈의 양은 피자마다 다르다.
꺼내지는 순서는 바뀔 수 있음
마지막에 남는 피자 번호를 구해라
- 피자 1번 위치에서 넣거나 뺄 수 있음
- 잠시 꺼내 확인가능
- M개의 피자에 처음 뿌려진 치즈의 양, 한반퀴 돌때 녹지않은 치즈의 양 반으로 줄어듬 c//2
- 0이면 화덕에서 꺼내고 그자리에 남은 피자를 순서대로 넣는다.
'''

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split) # n개의 화덕자리, m개의 피자
    arr = list(map(int, input().split())) # 치즈 리스트

    # 화덕
    que = []
    for i in range(n):
        que.append(i)

    while i < m:
        if arr[que[0]] == 0:
            que.pop(0)
            que.append(arr[i + 1])
        else:
            arr[que[0]] //= 2
            que.append(que.pop(0))