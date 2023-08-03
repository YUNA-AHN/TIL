'''
N = 2^a * 3^b * 5^c * 7^d * 11^e
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    num = [2, 3, 5, 7, 11] # 소인수분해 인자
    arr = [0] * 5 # 위치 별 값을 받을 리스트 생성
    while N > 1: # 1이면 모두 나눠진거니까 !
        for idx in range(len(num)):
            if not(N % num[idx]): # 나누어지면
                arr[idx] += 1 # 해당 자리에 1 더해주고
                N //= num[idx] # 몫으로 이어나가기

    print(f'#{tc}', *arr)
