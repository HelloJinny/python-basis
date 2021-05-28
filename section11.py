# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) # Header Skip

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)

"""
<_csv.reader object at 0x000002939F1B0A60>
<class '_csv.reader'>
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dialect', 'line_num'] 

['번호', '이름', '가입일시', '나이']
['1', '김정수', '2017-01-19 11:30:00', '25']
['2', '박민구', '2017-02-07 10:22:00', '35']
['3', '정순미', '2017-01-22 09:10:00', '33']
['4', '김정현', '2017-02-22 14:09:00', '45']
['5', '홍미진', '2017-04-01 18:00:00', '17']
['6', '김순철', '2017-05-14 22:33:07', '22']
['7', '이동철', '2017-03-01 23:44:45', '27']
['8', '박지숙', '2017-01-11 06:04:18', '30']
['9', '김은미', '2017-02-08 07:44:33', '51']
['10', '장혁철', '2017-12-01 13:01:11', '16']
"""

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 선택
    # next(reader) # Header Skip

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)

"""
<_csv.reader object at 0x000002939F3B4160>
<class '_csv.reader'>
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dialect', 'line_num'] 

['번호', '이름', '가입일시', '나이']
['1', '김정수', '2017-01-19 11:30:00', '25']
['2', '박민구', '2017-02-07 10:22:00', '35']
['3', '정순미', '2017-01-22 09:10:00', '33']
['4', '김정현', '2017-02-22 14:09:00', '45']
['5', '홍미진', '2017-04-01 18:00:00', '17']
['6', '김순철', '2017-05-14 22:33:07', '22']
['7', '이동철', '2017-03-01 23:44:45', '27']
['8', '박지숙', '2017-01-11 06:04:18', '30']
['9', '김은미', '2017-02-08 07:44:33', '51']
['10', '장혁철', '2017-12-01 13:01:11', '16']
"""

# 예제3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-----')

"""
<csv.DictReader object at 0x000002939F1CCF70>
<class 'csv.DictReader'>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_fieldnames', 'dialect', 'fieldnames', 'line_num', 'reader', 'restkey', 'restval']

번호 1
이름 김정수
가입일시 2017-01-19 11:30:00
나이 25
-----
번호 2
이름 박민구
가입일시 2017-02-07 10:22:00
나이 35
-----
번호 3
이름 정순미
가입일시 2017-01-22 09:10:00
나이 33
-----
번호 4
이름 김정현
가입일시 2017-02-22 14:09:00
나이 45
-----
번호 5
이름 홍미진
가입일시 2017-04-01 18:00:00
나이 17
-----
번호 6
이름 김순철
가입일시 2017-05-14 22:33:07
나이 22
-----
번호 7
이름 이동철
가입일시 2017-03-01 23:44:45
나이 27
-----
번호 8
이름 박지숙
가입일시 2017-01-11 06:04:18
나이 30
-----
번호 9
이름 김은미
가입일시 2017-02-08 07:44:33
나이 51
-----
번호 10
이름 장혁철
가입일시 2017-12-01 13:01:11
나이 16
-----
"""

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open('./resource/sample3.csv', 'w', newline='' ) as f:  # newline='' 테스트
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))
    print(type(wt))

    for v in w: # 하나하나 검수해서 쓸 때
        wt.writerow(v) 

# 예제5
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))
    print(type(wt))

    wt.writerows(w) # 데이터를 전부 다 사용하는 경우


# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함

# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요
# pip install pandas 설치 필요

import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx') # sheetname='시트명' 또는 숫자, header=3, skiprow=1

# 상위 데이터 확인
print(xlsx.head())

"""
  Sap Co.      대리점 영업사원       전월       금월  TEAM  총 판매수량
0  KI1316  경기수원대리점  이기정  1720000  2952000     1     123
1  KI1451  충청홍성대리점  정미진  4080000  2706000     2     220
2  KI1534  경기화성대리점  경인선   600000  2214000     1     320
3  KI1636  강원속초대리점  이동권  3720000  2870000     3     110
4  KI1735  경기안양대리점  강준석  4800000  2296000     1     134
"""
print()

# 데이터 확인
print(xlsx.tail())
print()

"""
   Sap Co.       대리점 영업사원       전월       금월  TEAM  총 판매수량
15  KI2870  경기구리시대리점  박진형  6000000  3400000     2     143
16  KI2910   강원춘천대리점  김은향  4800000  4896000     1     176
17  KI3030   강원영동대리점  전수창  4560000  3128000     2      98
18  KI3131   경기하남대리점  김민정  2750000  7268000     3     293
19  KI3252   강원포천대리점  서가은  2420000  4740000     4     240
"""

# 데이터 구조
print(xlsx.shape) # 행, 열

"""
(20, 7)
"""

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)