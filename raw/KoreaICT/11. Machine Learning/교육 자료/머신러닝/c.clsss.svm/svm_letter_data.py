import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

filename= './../dataIn/letterdata.csv'

data = np.loadtxt(filename, skiprows=1, delimiter=',', dtype='str')
table_col = data.shape[1] # csv 파일 열 개수
# print('table_col :', table_col)

y_column = 1 # 정답 컬럼수
x_column = table_col - y_column

x = data[:, 0:x_column]
x = x.astype(float) # 학습을 위하여 숫자화

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

encoder = LabelEncoder()  # 객체 생성
encoder.fit(y)  # 라벨 인코드를 fitting시킵니다.

# transform : 정규화된 인코딩을 라벨로 Transform 시킵니다.
result = encoder.transform(y)
print('after label encoded')
print(result)
print('-'*30)

y = result # 문자열을 숫자 형식으로 변환

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

print('x_train[:10]')
print(x_train[:10])
print('-'*30)

print('y_train[:10]')
print(y_train[:10])
print('-'*30)

# 각 열의 최대값과 최소값 확인
def print_feature(somedata):
    for idx in range(somedata.shape[1]):
        # 각 컬럼별 최소 값과 최대 값 확인
        print(f'컬럼{(idx+1)} 범위 : [{round(min(somedata[:, idx]), 3)}, {round(max(somedata[:, idx]), 3)}]')

print('\n# before normalization')
print_feature(x_train)

scaler = StandardScaler()
scaler.fit(x_train)

x_train_std = scaler.transform(x_train)
x_test_std = scaler.transform(x_test)

print('\n# after normalization')
print_feature(x_train_std)

# model = SVC(kernel='rbf', C=8, gamma=0.1)
model = SVC(kernel='rbf', C=1, gamma=0.1)
# model = SVC(kernel='rbf', C=100, gamma=0.1)

model.fit(x_train_std, y_train)  # svm 분류 모델 훈련

y_pred = model.predict(x_test_std)  # 테스트

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

print("prediction accuracy: {:.2f}".format(np.mean(bool_result)))  # 예측 정확도