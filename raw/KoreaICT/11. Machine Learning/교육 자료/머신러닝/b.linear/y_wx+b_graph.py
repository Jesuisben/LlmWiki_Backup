import numpy as np
import matplotlib.pyplot as plt

# x 데이터
x = np.arange(26.0, 32.1, 2.0)

# 실제 데이터
y_answer = [148, 164, 168, 183]

# 절편
b = 7.7

# 기울기 목록
weights = [5.45, 6, 10]

# 색상 목록
colors = ['red', 'green', 'orange']

# 실제 데이터 (파란색 선)
plt.plot(
    x,
    y_answer,
    linestyle='None',  # 선 제거
    marker='o',
    color='blue',
    label='Actual Data'
)

# 예측 결과들 (점만 표시)
for w, color in zip(weights, colors):
    y = w * x + b

    plt.plot(
        x,
        y,
        marker='o',
        color=color,
        markersize=8,
        linewidth=2,
        linestyle='solid',
        label=f'w = {w}'
    )

plt.xlim(x.min() - 2, x.max() + 2)
plt.ylim(100, 400)

plt.grid(True)
plt.legend(loc='upper left')

plt.xlabel('Temperature')
plt.ylabel('Sales')
plt.title('Effect of Different Weights')

plt.show()