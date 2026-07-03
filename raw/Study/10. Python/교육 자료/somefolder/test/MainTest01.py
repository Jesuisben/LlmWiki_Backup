# 방법01: import 전체경로명시
# 전체 경로를 매번 작성해야 하므로 잘 활용되지 않습니다.

print('import 구문 사용하기')
import somefolder.mymath.MathModule

su = 5
result = somefolder.mymath.MathModule.square_root(su)
print('루트 %.2f = %.4f' % (su, result))

su01, su02 = 2, 3
result = somefolder.mymath.MathModule.jegob(su01, su02)
print('%d^2 + %d^2 = %d' % (su01, su02, result))


print('from 패키지경로.모듈이름 import 함수')

# 실제 호출시에는 함수 이름만 명시하면 됩니다.
from somefolder.mymath.MathModule import square_root

su = 3
result = square_root(su)
print('루트 %.2f = %.4f' % (su, result))

from somefolder.mymath.MathModule import jegob
su01, su02 = 4, 5
result = jegob(su01, su02)
print('%d^2 + %d^2 = %d' % (su01, su02, result))

print('from 패키지경로 import 모듈이름')

# 실제 호출시에는 모듈이름.함수이름()의 형식으로 사용 됩니다.
from somefolder.mymath import MathModule

su = 10
result = MathModule.square_root(su)
print('루트 %.2f = %.4f' % (su, result))

su01, su02 = 5, 12
result = MathModule.jegob(su01, su02)
print('%d^2 + %d^2 = %d' % (su01, su02, result))


print('as 키워드를 사용한 별칭 사용하기')
import somefolder.mymath.MathModule as asdf

su = 15
result = asdf.square_root(su)
print('루트 %.2f = %.4f' % (su, result))

su01, su02 = 7, 8
result = asdf.jegob(su01, su02)
print('%d^2 + %d^2 = %d' % (su01, su02, result))