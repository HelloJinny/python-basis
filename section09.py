# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
print(dir(f)) # f 안에 있는 모든 속성 값을 볼 수 있다.
# 반드시 close 리소스 반환
f.close()

"""
The film, projected in the form of animation,
imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,      
which eventually paves the path for gaining a fresh perspective on an age-old problem.      
The story also happens to centre around two parallel characters, Shundi King and Hundi King,
who are twins, but they constantly fight over unresolved issues planted in their minds      
by external forces from within their very own units.
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 
'writelines']
"""

print("-------------------------------")
print("-------------------------------")

# 예제2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(list(c))
    print(iter(c))
    print(c)

"""
['T', 'h', 'e', ' ', 'f', 'i', 'l', 'm', ',', ' ', 'p', 'r', 'o', 'j', 'e', 'c', 't', 'e', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'm', ' ', 'o', 'f', ' ', 'a', 'n', 'i', 'm', 'a', 't', 'i', 'o', 'n', ',', '\n', 'i', 'm', 'p', 'a', 'r', 't', 's', ' ', 't', 'h', 'e', ' ', 'l', 'e', 's', 's', 'o', 'n', ' ', 'o', 'f', ' ', 'h', 'o', 'w', ' ', 'w', 'a', 'r', 's', ' 
', 'c', 'a', 'n', ' ', 'b', 'e', ' ', 'e', 'l', 'u', 'd', 'e', 'd', ' ', 't', 'h', 'r', 'o', 'u', 'g', 'h', ' ', 'r', 'e', 'a', 
's', 'o', 'n', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'p', 'e', 'a', 'c', 'e', 'f', 'u', 'l', ' ', 'd', 'i', 'a', 'l', 'o', 'g', 'u', 'e', 's', ',', '\n', 'w', 'h', 'i', 'c', 'h', ' ', 'e', 'v', 'e', 'n', 't', 'u', 'a', 'l', 'l', 'y', ' ', 'p', 'a', 'v', 
'e', 's', ' ', 't', 'h', 'e', ' ', 'p', 'a', 't', 'h', ' ', 'f', 'o', 'r', ' ', 'g', 'a', 'i', 'n', 'i', 'n', 'g', ' ', 'a', ' ', 'f', 'r', 'e', 's', 'h', ' ', 'p', 'e', 'r', 's', 'p', 'e', 'c', 't', 'i', 'v', 'e', ' ', 'o', 'n', ' ', 'a', 'n', ' ', 'a', 'g', 'e', '-', 'o', 'l', 'd', ' ', 'p', 'r', 'o', 'b', 'l', 'e', 'm', '.', '\n', 'T', 'h', 'e', ' ', 's', 't', 'o', 'r', 'y', ' ', 'a', 'l', 's', 'o', ' ', 'h', 'a', 'p', 'p', 'e', 'n', 's', ' ', 't', 'o', ' ', 'c', 'e', 'n', 't', 'r', 'e', ' ', 'a', 'r', 'o', 'u', 'n', 'd', ' ', 't', 'w', 'o', ' ', 'p', 'a', 'r', 'a', 'l', 'l', 'e', 'l', ' ', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's', ',', ' ', 'S', 'h', 'u', 'n', 'd', 'i', ' ', 'K', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'H', 'u', 'n', 'd', 'i', ' 
', 'K', 'i', 'n', 'g', ',', '\n', 'w', 'h', 'o', ' ', 'a', 'r', 'e', ' ', 't', 'w', 'i', 'n', 's', ',', ' ', 'b', 'u', 't', ' ', 't', 'h', 'e', 'y', ' ', 'c', 'o', 'n', 's', 't', 'a', 'n', 't', 'l', 'y', ' ', 'f', 'i', 'g', 'h', 't', ' ', 'o', 'v', 'e', 'r', ' ', 'u', 'n', 'r', 'e', 's', 'o', 'l', 'v', 'e', 'd', ' ', 'i', 's', 's', 'u', 'e', 's', ' ', 'p', 'l', 'a', 'n', 't', 'e', 
'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', 'i', 'r', ' ', 'm', 'i', 'n', 'd', 's', '\n', 'b', 'y', ' ', 'e', 'x', 't', 'e', 'r', 'n', 'a', 'l', ' ', 'f', 'o', 'r', 'c', 'e', 's', ' ', 'f', 'r', 'o', 'm', ' ', 'w', 'i', 't', 'h', 'i', 'n', ' ', 't', 'h', 'e', 
'i', 'r', ' ', 'v', 'e', 'r', 'y', ' ', 'o', 'w', 'n', ' ', 'u', 'n', 'i', 't', 's', '.']
<str_iterator object at 0x00000289A6810FA0>
The film, projected in the form of animation,
imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
which eventually paves the path for gaining a fresh perspective on an age-old problem.
The story also happens to centre around two parallel characters, Shundi King and Hundi King,
who are twins, but they constantly fight over unresolved issues planted in their minds
by external forces from within their very own units.
"""

print("-------------------------------")
print("-------------------------------")

# read : 전체 내용 읽기, read(10) : 10글자 읽기

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c)
        print(c.strip())

"""
The film, projected in the form of animation,
imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
which eventually paves the path for gaining a fresh perspective on an age-old problem.
The story also happens to centre around two parallel characters, Shundi King and Hundi King,
who are twins, but they constantly fight over unresolved issues planted in their minds
by external forces from within their very own units.
"""

print("-------------------------------")
print("-------------------------------")

# 예제4
with open('./resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)  # 내용 없음
    f.seek(0, 0)
    contents = f.read()
    print('>', contents)

"""
> The film, projected in the form of animation,
imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
which eventually paves the path for gaining a fresh perspective on an age-old problem.
The story also happens to centre around two parallel characters, Shundi King and Hundi King,
who are twins, but they constantly fight over unresolved issues planted in their minds
by external forces from within their very own units.
>
> The film, projected in the form of animation,
imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
which eventually paves the path for gaining a fresh perspective on an age-old problem.
The story also happens to centre around two parallel characters, Shundi King and Hundi King,
who are twins, but they constantly fight over unresolved issues planted in their minds
by external forces from within their very own units.
"""

print("-------------------------------")
print("-------------------------------")

# 예제5
# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='######')
        line = f.readline()

"""
The film, projected in the form of animation,
######imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
######which eventually paves the path for gaining a fresh perspective on an age-old problem.
######The story also happens to centre around two parallel characters, Shundi King and Hundi King,
######who are twins, but they constantly fight over unresolved issues planted in their minds
######by external forces from within their very own units.######
"""

print("-------------------------------")
print("-------------------------------")

# 예제6
# readlines : 전체 읽은 후 라인 단위 리스트 저장
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end='******')

"""
['The film, projected in the form of animation,\n', 'imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,\n', 'which eventually paves the path for gaining a fresh perspective on an age-old problem.\n', 'The story also happens to centre around two parallel characters, Shundi King and Hundi King,\n', 'who are twins, but they constantly fight over unresolved issues planted in their minds\n', 'by external forces from within their very own units.']

The film, projected in the form of animation,
******imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
******which eventually paves the path for gaining a fresh perspective on an age-old problem.
******The story also happens to centre around two parallel characters, Shundi King and Hundi King,
******who are twins, but they constantly fight over unresolved issues planted in their minds
******by external forces from within their very own units.******
"""

print("-------------------------------")
print("-------------------------------")

# 예제7
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)
print('Average : {:6.3}'.format(sum(score) / len(score)))

"""
[95, 78, 92, 89, 100, 66]
Average :   86.7
"""

# 파일 쓰기

# 예제1
with open('./resource/test.txt', 'w') as f:
    f.write('HelloJinny\n')

# 예제2
with open('./resource/test.txt', 'a') as f:
    f.write('Python-Study\n')

# 예제3
from random import randint

with open('./resource/score2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(50, 100)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('./resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)
