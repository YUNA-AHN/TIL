'''
가로 길이 항상 100
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
'''
for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    # 가장 높은 곳에서 가장 낮은 곳으로 N번 상자 옮기기
    for i in range(N):
        max_idx = 0
        min_idx = 0
        for idx in range(len(arr)):
            if arr[min_idx] > arr[idx]:
                min_idx = idx
            if arr[max_idx] < arr[idx]:
                max_idx = idx
        arr[max_idx] -= 1
        arr[min_idx] += 1
    
    # N번의 덤프 후 가장 높은 층과 가장 낮은 층의 층수 구하기
    max_idx = 0
    min_idx = 0
    for idx in range(len(arr)):
        if arr[min_idx] > arr[idx]:
            min_idx = idx
        if arr[max_idx] < arr[idx]:
            max_idx = idx

    ans = arr[max_idx] - arr[min_idx]
    print(f'#{test_case} {ans}')

# 강사님 코드 ---
for tc in range(1, 11):
    # 입력
    # n : 덤프를 진행할 수 있는 개스
    n = int(input())
    # arr : 상자 높이 갯수 100개
    arr = list(map(int, input().split()))

    # 메인로직
    # 평탄화 진행하는 메인로직
    # 총 n번 반복
    for i in range(n):
        # 평탄화 최고점 최저점
        mn = mx = arr[0]
        # // 인덱스
        mn_idx = mx_idx = 0
        for idx in range(100):
            # 최고점 찾기
            if arr[idx] > mx:
                mx = arr[idx]
                mx_idx = idx
            # 최저점 찾기
            if arr[idx] < mn:
                mn = arr[idx]
                mn_idx = idx
        # 최고점 1 감소, 최저점 1 증가 로직을 진행
        arr[mx_idx] -= 1
        arr[mn_idx] += 1
    # 출력
    # 최댓값과 최솟값을 찾아내서 이 차를 반환
    diff = max(arr) - min(arr)
    print(f'#{test_case} {diff}')
    
# 정렬을 활용한 방법 ---
for tc in range(1, 11):
    # 입력
    # n : 덤프를 진행할 수 있는 개스
    n = int(input())
    # arr : 상자 높이 갯수 100개
    arr = list(map(int, input().split()))

    # 메인로직
    # 평탄화 진행하는 메인로직
    # 총 n번 반복
    for i in range(n):
        # 정렬을 사용한 평탄화
        arr.sort()
        if arr[0] == arr[-1]:
            break

        arr[0] += 1 # 최솟값
        arr[-1] -= 1 # 최댓값
        arr.sort()

'''
문제를 잘 읽어보면,,,
최솟값과 최대값이 동일한 경우 종료..!
'''