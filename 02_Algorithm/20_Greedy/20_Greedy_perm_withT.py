# 단순하게 순열을 생성하는 방법 with 강사님
nums = [] # 상태 저장 리스트
def recur(depth):
    '''
    :param depth: 재귀호출을 몇번 진행했는지 (카운트값)
    :return: 없음
    '''
    # 기저조건(종료조건)
    if depth == 3:
        print(nums)
        return

    # 유도조건(재귀호출)
    # i : i -> 3
    for i in range(1, 4):
        nums.append(i) # 결정
        recur(depth + 1)
        nums.pop() # 복구

recur(0)