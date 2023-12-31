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
    n, m = map(int, input().split()) # n개의 화덕자리, m개의 피자
    arr = list(map(int, input().split())) # 치즈 리스트

    # 화덕 개수만큼 que에 !인덱스! 채워 두기
    que = list(range(n))

    # 시작점은 화덕에 마지막으로 들어간 피자 번호
    i = que[-1]
    # 큐가 존재하는 동안에
    while que:
        # 해당 인덱스에 치즈가 다 녹았다면 pop
        if arr[que[0]] == 0:
            que.pop(0)
            # 아직 피자 개수대로 다 안돌았다면 que에 추가해주기
            if i < m-1:
                i += 1
                que.append(i)
                # 넣고도 한 바퀴 돌리니까! 치즈 반으로 녹음
                arr[i] //= 2
        else:
            # 아직 치즈가 덜 녹았다면 맨 뒤로 보낸다
            t = que.pop(0)
            que.append(t)
            # 치즈도 반 녹이기
            arr[t] //= 2
    print(f'#{tc} {t + 1}')
