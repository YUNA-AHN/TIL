# BruteForce
p = "is"  # 찾을 패턴
t = "This i a book~!"  # 전체 텍스트
M = len(p)  # 찾을 패턴의 길이
N = len(t)  # 전체 텍스트의 길이


def BruteForce(p, t):  # i와 j 동시에 증가
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j  # 실패하면 자연스럽게 첫 시작보다 한칸 이동
            j = - 1  # 처음으로 돌아가기
        i = i + 1
        j = j + 1
    if j == M:
        return i - M  # 검색성공 : 검색 길이 만큼 빼주기
    else:
        return -1  # 검색 실패

# BruteForce : 강사님 코드
p = 'is'
t = 'This is a book~!'
M = len(p)
N = len(t)

def BruteForce(p,t):
    for i in range(N - M + 1):
        for j in range(M):
            # 패턴 매칭 실패
            if t[i + j] != p[j]:
                break
        else: # for else : break에 걸리지 않은 경우
            # 검색 성공
            return i # t 인덱스
    # 검색 실패
    return - 1

# 슬라이싱 사용 / while과 find도 활용해서 작성해보자!


# KMP
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)
    # preprocessing
    j = 0 # 일치한 개수 == 비교할 패턴 이치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print(lps)


# KMP 강사님 코드
def kmp(t, p ):
    N = len(t)
    M = len(p)

    # next 배열을 만드는 전처리(preprocessing)
    j = 0 # 일치한 갯수 == 비교할 패턴 인덱스
    lps = [0] * (M + 1) # 해당 되는 길이보다 ! 크게
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
              j += 1
        else:
            j = 0 
    lps[M] = j
    
    # 검색
    i = 0 # 비교할 텍스트(t) 인덱스
    j = 0 # 비교할 패턴(p) 인덱스
    while i < N and j <= M: # 일치 했을 때
        if p[j] == -1 or t[i] == p[j]: # 첫글자가 시작될 때!
            i += 1
            j += 1
        else: # 일치 하지 않았을 때
            j = lps[j]
            
        if j == M: # 패턴을 찾은 경우
            return i - M # 시작 위치점
            # 여러개를 찾아야 하는 경우
            # print(i-M, end=" ") # 패턴이 매칭
            # j = lps[j]

t = 'abcdabcdabcefzzzzzzzzz'
p = 'abcdabcef'
kmp(t,p)