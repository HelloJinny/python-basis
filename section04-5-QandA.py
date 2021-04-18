# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈

import re

# 1. 아래 문자열의 길이를 구해보세요.

q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print('01. q1길이:\t', len(q1))


# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print('02. print:\t', """apple;orange;banana;lemon""")
print('02. print:\t', '''apple;orange;banana;lemon''')


# 3. 화면에 * 기호 100개를 표시하세요.

print('03. *100개:\t', '*' * 100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

print('04. 정수형:\t', int("30"))
print('    실수형:\t', float("30"))
print('    복소수형:\t', complex("30"))
print('    문자형:\t', str(30))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

q5 = "Niceman"
print('05. 문자추출:\t', q5[4:7])

str = "Niceman"
manIdx = str.index("man")
print('05. 문자추출:\t', str[manIdx: manIdx + 3])


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

sb = "Strawberry"
print('06. reverse:\t', list(reversed(sb)))
print('06. reverse:\t', sb[::-1])


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

phoneNumber = "010-7777-9999"
print('07. - 제거:\t', phoneNumber[0:3] + phoneNumber[4:8] + phoneNumber[9:13])

# 7. 정규 표현식
#    import re

print('07. - 제거:\t', re.sub('[^0-9]', '', phoneNumber))


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

url = "http://daum.net"
urlIdx = url.index('''http://''')

print('08. http제거:\t', url[7:])
print('08. http제거:\t', url[urlIdx + 7:])


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

str = "NiceMan"
print('09. 대문자:\t', str.upper())
print('09. 소문자:\t', str.lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

str = "abcdefghijklmn"
print('10. 슬라이싱:\t', str[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

list = ["Banana", "Apple", "Orange"]
list.remove("Apple")
print('11. 삭제:\t', list)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

tup = (1, 2, 3, 4)
print('12. 변환:\t', [s for s in tup])


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

q13_dict = {
    '성인': 100000,
    '청소년': 70000,
    '아동': 30000
}
print('13. 딕셔너리:\t', q13_dict)

dict = {}
dict['성인'] = 100000
dict['청소년'] = 70000
dict['아동'] = 30000
print('13. 딕셔너리:\t', dict)


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

dict['소아'] = 0
print('14. 추가:\t', dict)


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print('15. Key항목:\t', dict.keys())


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.

print('16. value항목:\t', dict.values())
