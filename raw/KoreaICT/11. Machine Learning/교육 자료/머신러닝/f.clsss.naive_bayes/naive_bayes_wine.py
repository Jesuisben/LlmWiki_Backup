import numpy as np
import pandas as pd

dataIn = './../dataIn/'
dataOut = './../dataOut/'

filename= dataIn + 'wine.csv'

data = np.loadtxt(filename, skiprows=1, delimiter=',', dtype='str')
table_col = data.shape[1] # csv 파일 열 개수
# print('table_col :', table_col)

y_column = 1 # 정답 컬럼수
x_column = table_col - y_column

x = data[:, 0:x_column]
# x = x.astype(float) # 학습을 위하여 숫자화

y = data[:, x_column:]

print('x[:10] : \n', x[:10])
print('-'*30)

# ravel() : NumPy 배열을 1차원으로 평탄화하는 메소드
y = y.ravel()
print('before label encoded')
print('y[:10] : \n', y[:10])
print('-'*30)

myframe = pd.DataFrame(x, index=y)
print('myframe : \n', myframe)
print('-'*30)

print('myframe.index.unique() : \n', myframe.index.unique())
print('-'*30)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

print('x_train[:10]')
print(x_train[:10])
print('-'*30)

print('y_train[:10]')
print(y_train[:10])
print('-'*30)

# 각 열의 최대값과 최소값 확인
for idx in range(12):
    print("특성 " + str(idx) + "의 범위: ", "[", min(x_train[:, idx]), ",", max(x_train[:, idx]), "]")


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(x_train)

x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

for idx in range(12):
    print("표준화된 특성 " + str(idx) + "의 범위: ", "[", min(x_train_std[:, idx]), ",", max(x_train_std[:, idx]), "]")

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

nb.fit(x_train_std, y_train)

y_pred = nb.predict(x_test_std)  # 테스트

print("예측된 라벨:", y_pred)
print("ground-truth 라벨:", y_test)

# finalresult = pd.DataFrame([y_pred, y_test, y_pred==y_test], columns=)
bool_result = y_pred == y_test
finalresult = pd.DataFrame([y_pred, y_test, bool_result])
finalresult = finalresult.T
finalresult.columns = ['예측값', '실제값', '예측 결과']
print('finalresult : \n', finalresult)
print('-'*30)

hitcount = np.sum(bool_result)
totalcount = len(finalresult.index)

print("총 {}개 중에서 {}개를 정확히 맟춤".format(totalcount,hitcount ))

print("prediction accuracy: {:.4f}".format(np.mean(bool_result)))  # 예측 정확도
