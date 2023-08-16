def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N): # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]

A = [0, 1, 2]
f(0, 3)

# # 강사님 코드
# P = [1, 2, 3]
#
# # 재귀적으로 요소값을 교환을 하면서 만들 수 있는 순서를 만들어본다.
# # i : 깊이 (재귀를 얼마나 호출했는가)
# # N ; 순열을 만들 리스트의 크기
# def f(i, N):
#     # 기저조건
#     if i == N: # 순열 완성
#         print(P)
#
#     for j in range(i, N):
#         # 교환 (결정)
#         P[i], P[j] = P[j], P[i]
#         f(i + 1, N)
#         # 복구
#         P[i], P[j] = P[j], P[i]
# f(0, 3)