import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sympy import symbols, diff

plt.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False

# 주어진 함수 정의
def quadratic_function(x):
    return 2 * (x - 5) ** 2 + 20

# x 값 범위 설정
xlim, ylim = -10, 20
x_values = np.linspace(xlim, ylim, 400)

# 함수 값 계산
y_values = quadratic_function(x_values)

# 그래프 그리기
plt.plot(x_values, y_values, label='곡선 그래프')
# plt.xlabel('x')
# plt.ylabel('y')
plt.title('이차 함수와 미분 계수')
plt.scatter(5, 20, color='red', label='극소 값 = (5, 20)')
plt.grid(True)
plt.legend()

# 접선 그리기
x = symbols('x')
f = 2 * (x - 5) ** 2 + 20
f_prime = diff(f, x)  # 함수 f의 미분
for x_val in [0, 15]:  # x 값이 10과 15일 때
    tangent_slope = f_prime.subs(x, x_val)  # 접선의 기울기 계산
    tangent_intercept = quadratic_function(x_val) - tangent_slope * x_val  # 접선의 y 절편 계산
    tangent_values = tangent_slope * x_values + tangent_intercept  # 접선의 y 값 계산
    mylabel = f'x={x_val}에서 기울기 = {tangent_slope}'
    plt.plot(x_values, tangent_values, label=mylabel, linestyle='--')
    plt.ylim([-100, 500])

plt.legend()

dataOut = './../dataOut/'
filename = dataOut + 'quadraticFunction.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')