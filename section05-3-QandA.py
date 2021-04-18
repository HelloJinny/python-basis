# Section05-3
# 파이썬 흐름제어(제어문)

# 1 ~ 5 문제 if 구문 사용

# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.

q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k in q1.keys():
    if k == '가을':
        print('01-1.\t', q1[k])

for k, v in q1.items():
    if k == '가을':
        print('01-2.\t', v)

print('01-3.\t', ''.join([q1[s] for s in q1 if s == '가을']))


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.

q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "메론"}

for k, v in q2.items():
    if v == '사과':
        print('02-1.\t', k, v)
        break
else:
    print('02-1.\t 사과없음')

hasApple = ['사과다!' for key, val in q2.items() if key == '사과' or val == '사과']

if len(hasApple) > 0:
    print('02-2.\t', '사과있음')
else:
    print('02-2.\t', '사과없음 ㅡㅡ')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

a = 21

if a >= 81:
    print('03-1.\t', 'A학점')
elif a >= 61:
    print('03-1.\t', 'B학점')
elif a >= 41:
    print('03-1.\t', 'C학점')
elif a >= 21:
    print('03-1.\t', 'D학점')
else:
    print('03-1.\t', 'E학점')

score = 100
grade = ''
if 0 < score > 100:
    grade = '나가'
elif score > 80:
    grade = 'A학점'
elif score > 60:
    grade = 'B학점'
elif score > 40:
    grade = 'C학점'
elif score > 20:
    grade = 'D학점'
elif score >= 0:
    grade = 'E학점'

print('03-2.\t', grade)


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18
# a, b, c = 12, 6, 18

best = 0

best = a
if b > a:
    best = b
if c > b:
    best = c

print('04.\t', best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

s = '891022-2473837'

if int(s[7]) % 2 == 0:
    print('05.\t', '여자')
else:
    print('05.\t', '남자')


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.

q6 = ["갑", "을", "병", "정"]

for v in q6:
    if v == "정":
        continue
    else:
        print('06-1.\t', v)

q6 = [x for x in q6 if x != '정']
print('06-2.\t', q6)

print('06-3.\t', ''.join([s for s in q6 if s != '정']))


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

for n in range(1, 101):
    if n % 2 != 0:
        print('07-1.\t', n)

q7 = [x for x in range(1, 101) if x % 2 != 0]
print('07-2.\t', q7)

print('07-3.\t', ' '.join([str(s) for s in range(1, 100) if int(s) % 2 == 1]))


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.

q8 = ["nice", "study", "python", "anaconda", "!"]

for v in q8:
    if len(v) >= 5:
        print('08-1.\t', v)

print('08-2.\t', [s for s in q8 if len(s) >= 5])


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q9 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q9:
    if v.isupper():
        continue
    else:
        print('09-1.\t', v)

for v in q9:
    if v.islower():
        print('09-2.\t', v)

print('09-3.\t', [s for s in q9 if s.islower()])


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q10 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q10:
    if v.upper():
        print('10-1.\t', v.lower())
    else:
        print('10-1.\t', v.upper())

print('10-2.\t', [s.upper() if s.islower() else s.lower() for s in q10])

print("--------------------------------------------------")

# 일반적인 방법
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

# List Comprehension
numbers2 = [x for x in range(1, 101)]
print(numbers2)

"""
x = [x in for x in ragne(1, 100) if 조건문]
- append 시킬 변수 선언 x
- 계속 반복되는 (for 옆 x)
"""
