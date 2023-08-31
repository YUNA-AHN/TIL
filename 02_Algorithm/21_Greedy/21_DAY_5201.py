'''
컨테이너 운반
n개의 컨테이너, m대의 트럭
트럭당 한 개의 컨테이너 운반 가능, 적재용량 초과시 운반 x
편도로 한번만 운행
총 중량이 최대가 되도록, 전체 무게가 얼마인지?
모든 트럭이 확물 옮기지 안하도 된다
'''
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 컨테이너, 트럭 중량
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 정렬
    container.sort(reverse=True)
    truck.sort(reverse=True)

    # 트럭을 모두 순회
    i = j = 0
    sv = 0
    while i < n:
        # 트럭 중량이 컨테이너 중량보다 크거나 같다면
        # 최종 중량에 더해주고
        # 트럭, 컨테이너 인덱스 + 1
        # 아니라면 컨테이너 인덱스 + 1
        try:
            if truck[i] >= container[j]:
                sv += container[j]
                i += 1
                j += 1
            else:
                 j +=1
        # 컨테이너가 더이사 없다면 break
        except:
            break

    print(f'#{tc} {sv}')