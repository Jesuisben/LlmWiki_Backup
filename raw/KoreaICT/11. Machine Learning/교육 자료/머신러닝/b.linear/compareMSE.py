import numpy as np
import matplotlib.pyplot as plt

# 실제 데이터
x = np.array([26.0, 28.0, 30.0, 32.0])
y_actual = np.array([148, 164, 168, 183])

# 표시할 w 값들
weights = [5.45, 6.0, 10.0]

# b는 고정
b_fixed = 7.7

# w 변화에 따른 MSE
w_values = np.linspace(-1.1, 12, 500)
mse_values = []

for w in w_values:
    y_pred = w * x + b_fixed
    mse = np.mean((y_actual - y_pred) ** 2)
    mse_values.append(mse)

# MSE 곡선
plt.figure(figsize=(10, 6))
plt.plot(
    w_values,
    mse_values,
    color='blue',
    linewidth=2,
    label='MSE Curve'
)

# 빨간 점 (반드시 b=7.7 사용)
for w in weights:

    y_pred = w * x + b_fixed
    mse = np.mean((y_actual - y_pred) ** 2)

    # 콘솔 출력
    print(f'w = {w:5.2f}, MSE = {mse:.4f}')

    plt.scatter(
        w,
        mse,
        color='red',
        s=120,
        zorder=5
    )

    plt.annotate(
        f'w={w}',
        (w, mse),
        xytext=(0, 10),
        textcoords='offset points',
        ha='center'
    )

# 최소 MSE 지점
min_idx = np.argmin(mse_values)
best_w = w_values[min_idx]
best_mse = mse_values[min_idx]

plt.scatter(
    best_w,
    best_mse,
    color='green',
    s=180,
    zorder=6,
    label='Minimum MSE'
)

plt.annotate(
    f'best w={best_w:.2f}',
    (best_w, best_mse),
    xytext=(10, -20),
    textcoords='offset points'
)

plt.xlabel('Weight (w)')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE according to Weight (b = 7.7)')
plt.xlim(-1.1, 12)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('../dataOut/mse_vs_weight.png')
# plt.show()