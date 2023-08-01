'''
0~9 4세트 섞은 후 6개의 카드
연속 3개이상 run
같은 숫자 3개 이사 triplet
플레이어 1, 2 교대로 한 장식 먼저 run / triplet 나오면 승자
모두 가져갈 때가지 없으면 무승부
무승부 0 / 플1 1/ 플2 2
'''
T = int(input())
for tc in range(1, T+1):
    c = [0] * 12 # 플1 12자리의 리스트 생성
    d = [0] * 12  # 플2 12자리의 리스트 생성
    
    arr = list(map(int, input().split()))
    for idx in range(len(arr)): # 플 1 / 2 나누기 위해
        if not(idx % 2): # 홀수인 경우
            c[arr[idx]] += 1
        else: # 짝수인 경우
            d[arr[idx]] += 1

        condition = False
         # run과 triplet 검거
        for i in range(8):
            if (c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1) or (c[i] == 3):
                print(f'#{tc} 1')
                condition = True
                break
            elif (d[i] >= 1 and d[i+1] >= 1 and d[i+2] >= 1) or (d[i] == 3):
                print(f'#{tc} 2')
                condition = True
                break

        if condition:
            break
        # 무승부라면은!
        if idx == len(arr)-1:
            print(f'#{tc} 0')
