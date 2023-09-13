import sys
n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# 회의 종료 시간, 회의 시작 시간을 정렬 key로 설정
# 회의 종료 시간이 동일하디만 시작 시간이 다른 경우가 존재하기 때문
arr.sort(key = lambda x: (x[1], x[0]))

# 0시 부터 체크해주기 위하여 [0,0] 추가
arr = [[0,0]] + arr
# 이전 회의 시간을 체크 하기 위한 인덱스 i
i = 0
cnt = 0
for j in range(1, n + 1):
    # 현재 회의의 시작시간이 이전 회의 종료 시간과 같거나 크다면
    if arr[j][0] >= arr[i][1]:
        cnt += 1
        i = j

print(cnt)