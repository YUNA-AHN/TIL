num = 456789 # 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
# 0~9까지의 값에 대하여 run에서 i+2까지 조사
# 혹시 모를 인덱스 에러를 위해 2개 추가해서 리스트 생성
# if i < 8 이라는 추가 연산을 진행하지 않아도 된다는 이점

for i in range(6):
    c[num % 10] += 1 # 숫자 있는 만큼 더하기
    num //= 10

i = 0
tri = run = 0
while i < 1:
    if c[i] >= 3: # triplete 조사 : 동일한 값 3개 이상인지
        c[i] -= 3 # triplete인 경우 데이터 삭제
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사
        c[i] -= 1       # 데이터 삭제
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2: print('Baby Gin')
else: print("Lose")