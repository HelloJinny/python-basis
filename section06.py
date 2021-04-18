# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 함수 호출
# function_name()
# 함수 선언 위치 중요


# 예제1 (return 값 X)

def hello(world):
    print("Hello, ", world)


hello("Python!")
hello("0324")

print("--------------------------------------------------")


# 예제2 (return 값 O)


def hello_return(world):
    value = "Hello, " + str(world)
    return value


str = hello_return("Python!!!!!")
print(str)

print("--------------------------------------------------")


# 예제3 (다중 return)


def func_mul1(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul1(3)

print(val1, val2, val3)
print(type(val1), type(val2), type(val3))

print("--------------------------------------------------")


# 튜플 리턴


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)


tup = func_mul2(4)

print(type(tup), tup, list(tup))

print("--------------------------------------------------")

# 리스트 리턴


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lis = func_mul2(6)

print(type(lis), lis, set(lis))

print("--------------------------------------------------")

# 딕셔너리 리턴


def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}


dic = func_mul3(8)

print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())

print("--------------------------------------------------")

# 예제4 ★★★★★
# *args, **kwargs 이해

# *args


def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    # for t in args:
    #     print(t)

    for i, v in enumerate(args):
        print('{}'.format(i), v)


args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print("--------------------------------------------------")


# kwargs


def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])


kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

print("--------------------------------------------------")


# 전체 혼합


def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)

print("--------------------------------------------------")

# 예제5
# 중첩함수 (클로저) ★★★★★


def nested_func(num):
    def func_in_func(num):
        print('>>>', num)

    print("In func")
    func_in_func(num + 100)


nested_func(1)


# 실행불가
# func_in_func(1)

print("--------------------------------------------------")


# 예제6
# Hint

def func_mul6(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print('hint exam1 : ', func_mul6(5))


def tot_length1(word: str, num: int) -> int:
    return len(word) * num


print('hint exam2 : ', tot_length1("i love you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam3 : ', len(word) * num)


tot_length2("niceman", 10)

print("--------------------------------------------------")

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화

# 예제7
# def mul_10(num):
#     return num * 10

# def mul_10_one(num): return num * 10
#
# lambda x: x * 10


# 일반적 함수 -> 변수 할당


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10

print(var_func(5))
print(var_func(6))
print(type(var_func))


# 람다 함수 -> 할당


# lambda_mul_10 = lambda num: num * 10
def lambda_mul_10(num): return num * 10


print('>>>', lambda_mul_10(10))


def func_final(x, y, func):
    print('>>>', x * y * func(10))


func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x * 1000))
