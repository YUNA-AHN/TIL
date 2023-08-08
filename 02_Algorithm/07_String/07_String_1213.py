# 1213.string
'''
주어진 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램
'''
for _ in range(10):
    tc = int(input())
    keyword = input()
    text = input()

    ans = 0
    for i in range(len(text) - len(keyword) + 1):
        s = ''
        for j in range(i, len(keyword) + i):
            s += text[j]
        if s == keyword:
            ans += 1

    print(f'#{tc} {ans}')


# 강사님 코드 --
for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    t_len = len(text)
    p_len = len(keyword)

    # bruteforce 알고리즘
    answer = 0
    for t_idx in range(t_len - p_len + 1):
        cnt = 0
        for p_idx in range(p_len):
             # 해당 문자가 target pattern이 맞는다면
            if pattern[p_idx] == target[t_idx]:
                cnt += 1
        # 패턴 매팅 성공
        if cnt == p_len:
            answer += 1
    # 2안 for else
    for t_idx in range(t_len - p_len + 1):
        cnt = 0
        for p_idx in range(p_len):
             # 해당 문자가 target pattern이 맞는다면
            if pattern[p_idx] == target[t_idx]:
                cnt += 1
        # 패턴 매팅 성공
        if cnt == p_len:
            answer += 1

    # 3안
    # 문자열에서 특정 문자가 몇번 반복되었는지
    # 그 횟수를 반환하는 메소드
    # count()
    answer = target.count(pattern)