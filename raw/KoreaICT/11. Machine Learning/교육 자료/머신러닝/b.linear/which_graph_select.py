import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 실제 데이터
x = np.array([26.0, 28.0, 30.0, 32.0])
y_actual = np.array([148, 164, 168, 183])

# (w, b)
params = [
    (5.45, 7.7),
    (6.00, 0.0),
    (10.0, -100.0)
]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# MSE 결과 저장용
result_list = []

# 모든 예측값 계산
all_y = list(y_actual)

for w, b in params:
    y_pred = w * x + b
    all_y.extend(y_pred)

# 공통 y축 범위 계산
y_min = min(all_y) - 10
y_max = max(all_y) + 10

for idx, (ax, (w, b)) in enumerate(zip(axes, params), start=1):

    y_pred = w * x + b

    # MSE 계산
    mse = np.mean((y_actual - y_pred) ** 2)

    result_list.append({
        'Figure': idx,
        'Weight(w)': w,
        'Bias(b)': b,
        'MSE': round(mse, 2)
    })

    # 실제 데이터
    ax.scatter(
        x,
        y_actual,
        color='red',
        s=50,
        label='Actual Data'
    )

    # 가설 함수
    ax.plot(
        x,
        y_pred,
        color='blue',
        linewidth=2,
        label=f'H(x)={w}x+{b}'
    )

    ax.set_xlim(24, 34)
    ax.set_ylim(y_min, y_max)

    ax.set_title(f'Figure {idx:02d}\nMSE={mse:.2f}')
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.savefig('../dataOut/which_graph_select.png')


summary_rows = []
detail_rows = []

for idx, (w, b) in enumerate(params, start=1):

    y_pred = w * x + b

    errors = y_actual - y_pred
    squared_errors = errors ** 2

    sse = np.sum(squared_errors)
    mse = np.mean(squared_errors)

    # 요약 정보
    summary_rows.append({
        'Figure': idx,
        'Weight(w)': w,
        'Bias(b)': b,
        'SSE': round(sse, 4),
        'MSE': round(mse, 4)
    })

    # 상세 계산 과정
    for xi, actual, pred, err, sq_err in zip(
            x,
            y_actual,
            y_pred,
            errors,
            squared_errors):

        detail_rows.append({
            'Figure': idx,
            'Weight(w)': w,
            'Bias(b)': b,
            'x': xi,
            'Actual(y)': round(actual, 4),
            'Prediction(y_hat)': round(pred, 4),
            'Error(y-y_hat)': round(err, 4),
            'Squared Error': round(sq_err, 4)
        })

# 요약 CSV
summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(
    '../dataOut/mse_summary.csv',
    index=False,
    encoding='utf-8-sig'
)

# 상세 CSV
detail_df = pd.DataFrame(detail_rows)
detail_df.to_csv(
    '../dataOut/mse_detail.csv',
    index=False,
    encoding='utf-8-sig'
)

print(summary_df)
print()
print(detail_df)
