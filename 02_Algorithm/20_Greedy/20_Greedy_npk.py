# npk with 강사님
def P(arr, n, k, used, picks, depth):
    '''

    :param arr: 뽑고자 하는 배열(요소의 갯수는 n개)
    :param n:  배열의 길이
    :param k: 뽑고자 하는 요소의 갯수
    :return: 없음
    '''

    # 기저조건
    if depth == k: # k만큼 뽑았다면 정치..
        # 내가 지금가지 뽑은 값을 출력
        print(picks)
        return

    # 유도조건(재귀)
    for i in range(n):
        # 사용 여부
        if used[i] == False: # 사용하지 않은 수라면..
            # 결정 : 사용(사용 체크)
            used[i] = True
            picks.append(arr[i]) # 해당 숫자를 픽에 추가
            # 재귀 호출
            P(arr, n, k, used, picks, depth)
            # 복구
            used[i] = False
            picks.pop()

arr = [1, 3, 5, 7, 9, 10]
N = 6 # len(arr)
used = [False] * (N) # 사용한 값을 표기
picks = [] # 내가 뽑을
P(arr, N, 3, used, picks, 0) # 6P3 경우의 수를 모두 출력해봐라