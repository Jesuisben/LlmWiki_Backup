import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 정의
x1 = [26, 27, 28, 29, 30]
y1 = [100, 105, 110, 115, 120]

# 회귀직선 계산
m, b = np.polyfit(x1, y1, 1)

# x=31 예측
x_pred = 31
y_pred = m * x_pred + b

# 산점도 (기존 데이터)
plt.figure(figsize=(6, 5))
plt.scatter(
    x1,
    y1,
    color='skyblue',
    edgecolor='black',
    s=100,
    label='학습 데이터'
)

# 예측 데이터 (색상 다르게)
plt.scatter(
    x_pred,
    y_pred,
    color='limegreen',
    edgecolor='black',
    s=150,
    marker='*',
    label=f'예측값 ({x_pred}, {y_pred:.0f})'
)

# 회귀직선
x_line = np.linspace(min(x1), x_pred, 100)
y_line = m * x_line + b

plt.plot(
    x_line,
    y_line,
    color='red',
    linewidth=2,
    label=f'회귀직선: y = {m:.2f}x + {b:.2f}'
)

# 예측점에 좌표 표시
plt.annotate(
    f'({x_pred}, {y_pred:.0f})',
    (x_pred, y_pred),
    xytext=(10, 10),
    textcoords='offset points'
)

# 눈금 설정
plt.xticks(np.arange(26, 32, 1))
plt.yticks(np.arange(100, 126, 5))

# 그래프 꾸미기
plt.title("온도에 따른 에어콘 판매 대수", fontsize=14)
plt.xlabel("온도", fontsize=12)
plt.ylabel("에어콘 판매 대수", fontsize=12)

plt.xlim([26, 31.5])
plt.ylim([100, 126])

plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()