'''
원재의 메모리 복구하기
1010
'''
T = int(input())
for tc in range(1, T+1):
    memo = input()

    cnt = 0
    # 첫번재 원소가 1이면 +1
    if memo[0] == '1':
        cnt += 1
    # 현재 원소와 다음 원소가 다르면 +1
    for i in range(len(memo)-1):
        if memo[i] != memo[i+1]:
            cnt += 1

    print(f'#{tc} {cnt}')