'''
삼성시 버스
i번째 노선은 ai이상 bi이하인 모든 정류장만을 다니는 버스
p개의 버스 정류장
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input()) # n개의 버스 노선
    arr = [0] * 5001 # 5000개의 버스 정류장 생성

    # 노선만큼 순회
    for _ in range(n):
        a, b = map(int, input().split())
        # a 이상 b 이상에 더하기
        for i in range(a, b+1):
            arr[i] += 1

    # p개의 정류장에 들리는 버스 수 출력
    p = int(input())
    print(f'#{tc}', end = ' ')
    for _ in range(p):
        c = int(input())
        print(arr[c], end = ' ')
    print()