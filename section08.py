# Section08
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(100)

print("ex1 : ", Fibonacci.fib2(200))
print("ex1 : ", Fibonacci().title)

"""
0 1 1 2 3 5 8 13 21 34 55 89
ex1 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
ex1 :  fibonacci
"""

# 사용2(클래스) - 메모리 많이 차지 하기 때문에 권장 X
from pkg.fibonacci import *

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

"""
0 1 1 2 3 5 8 13 21 34 55 89 144 233
ex2 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
ex2 :  fibonacci
"""

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(500)

print("ex3 : ", fb.fib2(600))
print("ex3 : ", fb().title)

"""
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
ex3 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
ex3 :  fibonacci
"""

# 사용4(함수) : 파일 Alias
import pkg.calculations as c

print("ex4 : ", c.add(10,10))
print("ex4 : ", c.mul(10,4))


"""
ex4 :  20
ex4 :  40
"""

# 사용5(함수)
from pkg.calculations import div as d

print("ex5 : ", int(d(100,10)))

"""
ex5 :  10
"""

# 사용6
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(p))
print(dir(builtins))

"""
I'm HelloJinny!
I'm Goodjob!
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'prt1', 'prt2']
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 
'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 
'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
"""