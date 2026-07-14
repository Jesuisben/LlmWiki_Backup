import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

cm = np.array([
    [2, 1],
    [3, 94]
])

labels = np.array([
    ['TP\n2', 'FP\n1'],
    ['FN\n3', 'TN\n94']
])

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=labels,
    fmt='',
    cmap='Blues',
    xticklabels=['정답 양성', '정답 음성'],
    yticklabels=['예측 양성', '예측 음성']
)

plt.title('Confusion Matrix')
plt.xlabel('Actual')
plt.ylabel('Predicted')

plt.tight_layout()
# plt.show()

dataOut = './../dataOut/'
filename = dataOut + 'make_heatmap.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')