# 테스트01~테스트05까지의 손실 함수 결과와 정확도를 사용하여 그래프를 비교해 봅니다.
import matplotlib.pyplot as plt
import pandas as pd


totalFrame = pd.DataFrame()

for idx in range(1, 6):  # 테스트01~테스트05
    fileName = 'mnistResult' + str(idx).zfill(2) + '.csv'
    df = pd.read_csv(fileName)
    totalFrame = pd.concat([totalFrame, df], axis=0)
# end for

print(totalFrame)

plt.rc('font', family='Malgun Gothic')

# 손실 함수와 정확도를 이용하여 서브 플로팅하기
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

caption = ['테스트0' + str(idx) for idx in range(1, 6)]

# 1번째 영역
axes[0].bar(caption, totalFrame['loss'])
axes[0].set_title('손실 함수')
axes[0].grid(True)

# 2번째 영역
axes[1].bar(caption, totalFrame['accuracy'])
axes[1].set_title('정확도')
# axes[1].set_yticks(range(0, 11), [0.1*idx for idx in range(0, 11)])
axes[1].grid(True)

fileName = 'mnistNeuralNetGraph.png'
plt.savefig(fileName)
print(fileName + ' 파일 저장됨')