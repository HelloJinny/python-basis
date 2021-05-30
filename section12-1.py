# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import datetime
import sqlite3

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime', nowDatetime)

"""
now 2021-05-30 23:47:20.095607
nowDatetime 2021-05-30 23:47:20
"""

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

"""
sqlite3.version :  2.6.0
sqlite3.sqlite_version 3.35.4
"""

