arr = [1,2, 3, 4, 5, 6, 7, 8]

# 재귀 호출
# 순열, 4개의 값을 뽑아내는 경우를 모두 출력해봐라
# [1, 2, 3, 4] # 순서가 달라도
# [1, 2, 4, 3] # 똑같다!
# [1, 2, 3, 5]
result = []
# 체크리스트 : true는 만나면 그 자리는 이미 사용한 것
checked = [False for _ in range(len(arr))]
cnt = 0
def generate_permutations(arr, depth):
    global cnt
    # 기저 조건
    if depth == 4:
        cnt += 1 # 4개의 값을 뽑아내는 경우의 수
        # result 값을 출력
        print(result)
        return

    # arr를 순회하면서 하나의 값을 뽑아낸다.
    for idx in range(len(arr)):
        # 해당 번호를 뽑게 되면, 다음에 뽑지 못하도록 체크
        if checked[idx]:
            continue
        # 사용 표시
        checked[idx] = True
        result.append(arr[idx])
        generate_permutations(arr, depth + 1) # 재귀호출
        # 사용 복구
        checked[idx] = False
        result.pop()

generate_permutations(arr, 0)


# 조합, 4개의 값을 뽑아내는 경우를 모두 출력했바롸
# [1, 2, 3, 4]
# [1, 2, 3, 5]
# [1, 2, 3, 6]

def generate_combination(arr, depth, current):
    global cnt
    # 기저 조건
    if depth == 4:
        cnt += 1  # 4개의 값을 뽑아내는 경우의 수
        # result 값을 출력
        print(result)
        return

    # arr를 순회하면서 하나의 값을 뽑아낸다.
    for idx in range(current, len(arr)):
        # 해당 번호를 뽑게 되면, 다음에 뽑지 못하도록 체크
        if checked[idx]:
            continue
        # 사용 표시
        checked[idx] = True
        result.append(arr[idx])
        generate_combination(arr, depth + 1, idx + 1)  # 재귀호출
        # 사용 복구
        checked[idx] = False
        result.pop()

generate_combination(arr, 0, 0)