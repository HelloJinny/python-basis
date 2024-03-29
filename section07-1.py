# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

"""
선언

class 클래스명:
    함수
    함수
    함수
"""

# 예제1


class UserInfo:
    # 속성 (이름, 나이, 성별, 키, 몸무게, 전화번호), 메소드 (걷다, 뛰다)
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")


# 네임스페이스
user1 = UserInfo("Kim")
print(user1.name)
user1.print_info()

user2 = UserInfo("Park")
print(user2.name)
user2.print_info()

print(id(user1))
print(id(user2))

print('user1 : ', user1.__dict__)
print('user2 : ', user2.__dict__)

print("--------------------------------------------------")

# 예제2
# self의 이해


class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
# print(dir(f))
print(id(f))

# f.function1() #예외 발생
f.function2()

print(SelfTest.function1())
# print(SelfTest.function2()) #예외 발생

print("--------------------------------------------------")


# 예제3
# 클래스 변수 , 인스턴스 변수


class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim')
user2 = Warehouse('Park')
user3 = Warehouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)

# Warehouse.stock_num = 50 # 직접 접근 가능

print(user1.name)
print(user2.name)
print(user3.name)

del user1  # 인스턴스 제거

print(user2.stock_num)  # 없으면 클래스 변수 가져옴
print(user3.stock_num)
