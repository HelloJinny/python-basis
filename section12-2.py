# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/workspaces/Git/python-basis/resource/database.db') # DB 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())

"""
One -> 
 (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53')
Three ->
 [(2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', '2021-05-30 23:54:53'), (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', '2021-05-30 23:54:53'), (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', '2021-05-30 23:54:53')]
All ->
 [(5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', '2021-05-30 23:54:53')]
"""

print()

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1  >', row)

"""
retrieve1  > (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53')   
retrieve1  > (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', '2021-05-30 23:54:53')
retrieve1  > (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', '2021-05-30 23:54:53')   
retrieve1  > (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', '2021-05-30 23:54:53')   
retrieve1  > (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', '2021-05-30 23:54:53')   
"""

# 순회2
# for row in c.fetchall():
#     print('retrieve2 >', row)

"""
retrieve2 > (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53')   
retrieve2 > (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', '2021-05-30 23:54:53')
retrieve2 > (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', '2021-05-30 23:54:53')   
retrieve2 > (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', '2021-05-30 23:54:53')   
retrieve2 > (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', '2021-05-30 23:54:53')  
"""

# # 순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

"""
retrieve3 >  (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', '2021-05-30 23:54:53')   
retrieve3 >  (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', '2021-05-30 23:54:53')   
retrieve3 >  (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', '2021-05-30 23:54:53')   
retrieve3 >  (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', '2021-05-30 23:54:53')
retrieve3 >  (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53')  
"""

print()

# WHERE Retrieve1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

"""
param1 (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53')
param1 []
"""

# WHERE Retrieve2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())

"""
param2 (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53')
param2 []
"""

# WHERE Retrieve3
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())

"""
param3 (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53')
param3 []
"""

# WHERE Retrieve4
param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4', c.fetchall())

"""
param4 [(1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53'), (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', '2021-05-30 23:54:53')]
"""

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())

"""
param5 [(1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53'), (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', '2021-05-30 23:54:53')]
"""

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())

"""
param6 [(1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-05-30 23:54:53'), (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', '2021-05-30 23:54:53')]
"""

# Dump 출력(데이터베이스 백업 시 중요)
with conn:
    with open('C:/workspaces/Git/python-basis/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')


