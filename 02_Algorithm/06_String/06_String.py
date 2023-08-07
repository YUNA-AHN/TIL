# python에서 문자열 뒤집기
# 1안
s = 'Reverse thid strings'
s  = s[::-1]

# 2안
s = 'abcd'
s = list(s)
s.reverse()
s = ''.join(s)

# 3안
s = 'REVERSE'
# str -> list
s_lst = list(s)
N = len(s)
for i in range(N//2):
    s_lst[i], s_lst[N-1-i] = s_lst[N-1-i], s_lst[i]
s = ''.join(s_lst)


# 문자열 비교
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

if s1 == s5:
    print('s1==s5')
else:
    print('s1!=s5')

if s1 is s5:
    print('s1 is s5')
else:
    print('s1 is not s5')


# 아스키 코드를 기준으로 나누어짐
# abc < abd
# abc < ABC
# abc > abcd
# abcd > abcD
s1 = 'abcd'
s2 = 'abc'
print(s1 < s2)
print(s2 < s1)
print(s1 == s2)

# int()와 같은 atoi()함수 만들기
def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord('0')
        # 아스키 코드 번호를 활용하여 값을 만든다.
    return i

s = '123'
a = atoi(s)
print(a + 1)

# 연습문제 str() 함수를 사용하지 않고, itoa()를 구현
# 양의 정수를 입력받아 문자열로 변환하는 함수
# 입력 값: 변환할 정수 값, 변환된 문자열을 저장할 문자배열 - 반환 값 없음

def itoa(a):
    s = ''
    while a > 0:
        s += chr(ord('0') + a % 10) # 1의 자리 숫자의 ASCII 값 + s
        a //= 10
    return s[::-1]

a = 123
print(type(itoa(a))) # str로 변환



# itoa() 구현 : 양의 정수를 문자열로
'''
ord() : 문자열을 ascii 코드값으로 ex) ord('A') -> 65
chr() : ascii 코드값을 문자열로 ex) chr(65) -> "A"
'''
def itoa(num):
    result=[]
    while num != 0:
        result.append(chr(ord('0') + num % 10))
        result.reverse()
    return ''.join(result)

def itoa(i):
    res = ''
    if i < 0: # 음수라면 음수 기호 생성
        s = '-'
        tmp = -i
    else: # 양수면 공백
        s = ''
        tmp = i

    while tmp != 0:
        res = chr(tmp % 10 + ord('0')) + res
        tmp //= 10

    return s + res


print(itoa(-1579) + '0') # -15790
print(itoa(1234) + '0') # 12340

# atoi() 구현 : 문자열을 정수로
