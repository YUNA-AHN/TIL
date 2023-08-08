'''
한 글자씩 타이핑 - A의 길이만큼 키를 눌러야 한다
문자열 b 전체 타이핑 가능
키 눌러야하는 횟수의 최솟값
'''

T = int(input())

for tc in range(1, T+1):
    text, pattern = input().split()

    t_len = len(text)
    p_len = len(pattern)

    ans = 0
    for t_idx in range(t_len - p_len + 1):
        cnt = 0
        for p_idx in range(p_len):
            if text[p_idx + t_idx] == pattern[p_idx]:
                cnt += 1

        if cnt == p_len:
            ans += 1

    res = t_len - (p_len * ans) + ans
    print(f'#{tc} {res}')


# # 강사님 코드
#
# def BruteForce(p,t):
#     N = len(p)
#     M = len(t)
#
#     # 카운드 변수
#     cnt = 0
#     for i in range(N - M + 1):
#         for j in range(M):
#             # 패턴 매칭 실패
#             if t[i + j] != p[j]:
#                 break
#         else: # for else : break에 걸리지 않은 경우
#             # 검색 성공
#             return cnt += 1
#     return cnt
#
# T = int(input())
#
# for tc in range(1, T+1):
#     A, B = input().split()
#
#     cnt = BruteForce(A, B) # A.count(B) 로 변경 가능
#     answer = len(A) - (len(B) * cnt) + cnt
#
#     # 방안 2
#     # A = A.replace(B,'X')
#     # answer = len(A)
#
#     print(f'#{tc} {answer}')
