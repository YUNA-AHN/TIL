# 비트 연산 예제 1 : 이진수로 표현하기
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)

for i in range(-5, 6):
    print("%d = " % i, end='')
    Bbit_print(i)


# 비트 연산 예제 2
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output, end = ' ')

a = 0x10 # 16
x = 0x01020304
print("%d = " % a, end = '')
Bbit_print(a)
print()

output = ''
for j in range(31, -1, -1):
    output += '1' if x & (1 << j) else '0'
print(output)

print("0%X = " % x, end = '')
for i in range(0, 4):
    Bbit_print((x >> i * 8) & 0xff)

# 비트 연산 예제 3
def ce(n): # change endian
    p = []
    for i in range(0,4):
        p.append((n >> (24 - i * 8)) & 0xff)
    return p

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i * 8)) & 0xff)


print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
p = ce(x)
print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))

# 비트 연산 예제 4
def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n << 8 & 0xff00) | (n << 24 & 0xff)
print(hex(ce1(x)))

# 비트 연산 예제 5
# 비트 연산자 ^를 두 번 연산하면 처음 값을 반환한다.
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)

a = 0x86
key = 0xAA

print("a        ==> ", end='')
Bbit_print(a)

print("a^=key   ==> ", end='')
a ^= key
Bbit_print(a)

print("a^=key   ==> ", end='')
a ^= key
Bbit_print(a)

# 진수 만들기
bit = [0] * 8
a = 149
i = 7
while a > 0:
    bit[i] = a % 2
    a //= 2
    i -= 1
print(''.join(map(str, bit)))


# 연습문제 1
# a = '0000000111100000011000000111100110000110000111100111100111111001100111'
# # 문자열을 7개씩 잘라서 (슬라이싱_
# for i in range(0, len(a), 7):
#     num = int(a[i: i+7], 2)
#     print(num, ":", oct(num)[2:],":", hex(num)[2:])
#
#     # bin : 2진수의 표현법 문자열
#     # oct : 8진수의 표현법 문자열
#     # hex : 16진수의 표현법 문자열
#
# # 연습문제2 : 0269FAC9A0
# text = input()
# # 딕셔너리 한자리 16진수 -> 네자리 2진수
# HEX_TO_BIN = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     '3': '0011',
#     '4': '0100',
#     '5': '0101',
#     '6': '0110',
#     '7': '0111',
#     '8': '1000',
#     '9': '1001',
#     'A': '1010',
#     'B': '1011',
#     'C': '1100',
#     'D': '1101',
#     'E': '1110',
#     'F': '1111'
#
# }
# binary = ""
# for h in text:
#     binary += HEX_TO_BIN[h]
#
# # 2진수 -> 7자리씩 끊어서 10진수로 변환
# for i in range(0, len(binary), 7):
#     num = int(binary[i:i+7],2)
#     print(num)

# 연습문제 3 : 0269FAC9A0
text = '0269FAC9A0' # input()
# 딕셔너리 한자리 16진수 -> 네자리 2진수
HEX_TO_BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'

}
binary = ''
for h in text:
    binary += HEX_TO_BIN[h]


# 2진수 값에서 암호화 비트가 끝점을 탐색(순회)
e = -1
for i in range(len(binary)-1, -1, -1):
    if binary[i] == '1':
        e = i
        break

PASSWORD = {
    "001101" : '0',
    "010011" : '1',
    "111011" : '2',
    "110001" : '3',
    "100011" : '4',
    "110111" : '5',
    "001011" : '6',
    "111101" : '7',
    "011001" : '8',
    "101111" : '9'
}

code = ''
for i in range(e - 5, -1, -6):
    print(binary[i:i+6])

# 만든 암호 요소를 거꾸로 변경
print(code[::-1])

