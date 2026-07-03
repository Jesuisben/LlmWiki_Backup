# MainTest01.py 방법과 동일한 방식으로 테스트를 해보세요.
import somefolder.sansu.SansuModule

print('# import 구문 사용하기')
su1 = 14
su2 = 5
result = somefolder.sansu.SansuModule.add(su1, su2)
print('더하기 01 :', result)

result = somefolder.sansu.SansuModule.sub(su1, su2)
print('빼기 01 :', result)

print('# from 패키지경로.모듈이름 import 함수')
from somefolder.sansu.SansuModule import add

result = add(su1, su2)
print('더하기 02 :', result)

from somefolder.sansu.SansuModule import sub
result = sub(su1, su2)
print('빼기 02 :', result)

print('# from 패키지경로 import 모듈이름')
from somefolder.sansu import SansuModule
result = SansuModule.add(su1, su2)
print('더하기 03 :', result)

result = SansuModule.sub(su1, su2)
print('빼기 03 :', result)

print('# 별칭 사용하기')
import somefolder.sansu.SansuModule as imsi
result = imsi.add(su1, su2)
print('더하기 04 :', result)
