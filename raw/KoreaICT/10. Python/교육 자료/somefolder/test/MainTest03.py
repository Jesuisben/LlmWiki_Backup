import somefolder.character.CharacterModule

name, age = '김가영', 20
result = somefolder.character.CharacterModule.namePrint(name, age)

result = somefolder.character.CharacterModule.sayHello('어서오세요.', 10)

print('from 패키지경로.모듈이름 import 함수')

from somefolder.character.CharacterModule import namePrint

result = namePrint(name='이신영', age=50)

from somefolder.character.CharacterModule import sayHello

result = sayHello('방가워요^^', 5)

print('from 패키지경로 import 모듈이름')

from somefolder.character import CharacterModule

result = CharacterModule.namePrint('이민재', 40)

result = CharacterModule.sayHello('하이루', 3)

print('as 키워드를 사용한 별칭 사용하기')
import somefolder.character.CharacterModule as asdf

result = asdf.namePrint('금채림', 15)

result = asdf.sayHello('안뇽', 7)