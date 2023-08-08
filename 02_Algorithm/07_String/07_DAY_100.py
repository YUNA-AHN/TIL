'''
1. 연속된 N일 동안의 물건의 매매가를 예측
2. 하루에 최대 1만큼 구입 가능
3. 판매는 언제든지

남은 날 줄에 내가 제일 비싸지 않으면? 사기
내가 남은 날 중에 가장 비싸면 -> 가진 걸 팔기
산 가격 / 산 개수를 가지고 있어야

'''
# 저격 케이스에 잡힌다.. 정방향은 오답이다...
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    buy_list = []
    j = 0
    ans = 0
    for i in range(N):
        if arr[i] != max(arr[i:]): # 남은 날 들 중에 내가 제일 비싸지 않다면 사기
            buy_list.append(arr[i])

        if buy_list: # 뭐라도 산게 있을때
            # j부터 지금까지 내가 최댓값이고, 내 뒤로도 내가 최댓값일때
            if max(arr[j:i+1]) == arr[i] and max(arr[i:]) == arr[i]:
                for charge in buy_list:
                    ans += arr[i] - charge
                j = i + 1
                buy_list = []
    print(f'#{tc} {ans}')

# 준영 코드 --- 이것이 정배
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 이익 ans 고가 high_v 생성
    ans = 0
    high_v = arr[-1]
    for i in range(N-1, -1, -1): # 역순으로 순회하면서
        if high_v < arr[i]: # 고가인 경우 갱신
            high_v = arr[i]
        ans += high_v - arr[i] # 고가 - 가격
    print(f'#{tc} {ans}')

# enumer
arr = [1,5, 7, 43, 76, 2, 3, 5, 3]
# 최댓값에 해당하는 요소 인덱스를 반환해라
print(*enumerate(arr))

val = max(arr) # N
idx = arr.index(val) # N

idx, val = max(enumerate(arr), key = lambda x: x[1])
print(idx, val)