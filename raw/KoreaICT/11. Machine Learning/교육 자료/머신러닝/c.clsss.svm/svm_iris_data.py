import numpy as np

dataIn = './../dataIn/'
filename = dataIn + 'iris.csv'

data = np.loadtxt(filename, skiprows=1, delimiter=',', dtype='str')

print(f'data.ndim={data.ndim}')
print(f'data.dtype={data.dtype}')
print(f'data.shape={data.shape}')

column_size = data.shape[1] # csv 파일 열 개수
# print('column_size :', column_size)

y_column = 1 # 정답 컬럼수
x_column = column_size - y_column

x = data[:, 0:x_column]
# 문자형을 숫자 형식으로 변환하기
x = x.astype(float)  # 학습을 위하여 숫자화

y = data[:, x_column:]

print('\nx[:10] : \n', x[:10])

print('\ny[:10] : \n', y[:10])

# ravel() : NumPy 배열을 1차원으로 평탄화하는 메소드
y = y.ravel() # 'Unravel'은 '엉킨 것을 풀다'라는 의미입니다.
print('before label encoded')
print('y[:10] : \n', y[:10])

import pandas as pd
myframe = pd.DataFrame(x, index=y)
print('myframe : \n', myframe)

print('myframe.index.unique() : \n', myframe.index.unique())

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 그래프 그리기 시작
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(lbl, color):
    row = myframe.loc[lbl]
    # row[0] : 꽃받침 길이(Sepal.Length)
    # row[0] : 꽃받침 너비(Sepal.Width)
    ax.scatter(row[0], row[1], c=color, label=lbl)
# end def scatter


scatter("setosa", "red")
scatter("versicolor", "blue")
scatter("virginica", "green")
ax.legend()

dataOut = './../dataOut/'

plt.title('꽃받침 길이와 너비 산점도 그래프')
filename = dataOut + 'iris-scatter.png'
plt.savefig(filename)
print(filename + ' 파일로 저장됨')

# 전처리 작업
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()  # 객체 생성
encoder.fit(y)  # 라벨 인코드를 fitting시킵니다.

# transform : 정규화된 인코딩을 라벨로 Transform 시킵니다.
y = encoder.transform(y)

print('\nafter label encoded')
print('y[:10] : \n', y[:10])


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size=0.2, random_state=10) # 80대20

print('\nx_train[:10]')
print(x_train[:10])

print('\ny_train[:10]')
print(y_train[:10])
print()

# min과 max 그리고, round 함수는 파이썬의 내장 함수입니다.
def print_feature(somedata):
    for idx in range(somedata.shape[1]):
        # 각 컬럼별 최소 값과 최대 값 확인
        print(f'컬럼{(idx+1)} 범위 : [{round(min(somedata[:, idx]), 3)}, {round(max(somedata[:, idx]), 3)}]')

print('\n# before normalization')
print_feature(x_train)

# 거리(distance) 기반의 알고리즘인 SVM은 정규화를 진행해 주는 것이 모델 성능 향상을 기대할 수 있습니다.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # 객체 생성
scaler.fit(x_train) # 훈련용 데이터 학습

x_train = scaler.transform(x_train) # 훈련용 데이터 정규화
x_test = scaler.transform(x_test) # 테스트용 데이터 정규화

print('\n# after normalization')
print_feature(x_train)


'''
매개 변수 C
오차 허용 범위를 제어하여 모델이 얼마나 유연하게 결정 경계를 형성하는지에 영향을 미칩니다.
--------------------------------------------------------------------------------------
C 값	마진	오차 허용	일반화 능력	과적합 확률	과소 적합 확률
큼	작아짐	꼼꼼하게 체크	불리	높음	낮음
작음	큼	덜 꼼꼼	유리	낮음	높음
--------------------------------------------------------------------------------------
매개 변수 gamma
비선형 커널에서 결정 경계의 복잡도를 제어합니다.
--------------------------------------------------------------------------------------
gamma 값	데이터의 영향 반경	결정 경계	데이터 민감도	과적합 확률	과소 적합 확률
큼	작게 설정	복잡	민감	높음	낮음
작음	크게 설정	단순	덜 민감	낮음	높음
--------------------------------------------------------------------------------------
'''
from sklearn.svm import SVC
# model = SVC(kernel='rbf', C=8, gamma=0.1)
model = SVC(kernel='rbf', C=1, gamma=0.1)
# model = SVC(kernel='rbf', C=100, gamma=0.1)

model.fit(x_train, y_train)  # svm 분류 모델 훈련

prediction = model.predict(x_test)  # 테스트

print('예측 데이터 :', prediction)
print('실제 정답 :', y_test)

# 보기 좋게 데이터 프레임으로 변환합니다.
bool_result = prediction == y_test

print('\n# 데이터 프레임(예측값, 실제값, 예측 결과)')
result_frame = pd.DataFrame([prediction, y_test, bool_result])
result_frame = result_frame.T # 전치(행렬 바꿈)
result_frame.columns = ['예측값', '실제값', '예측 결과']

print('\n# result_frame')
print(result_frame)

hit_count = np.sum(bool_result)
total_count = len(result_frame.index)

print(f'\n정확도 {hit_count}/{total_count}={(hit_count/total_count):.3f}')
print(f'prediction accurary : {np.mean(bool_result):.3f}')



print('\n# 정확도 계산')
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, prediction)
print(f'accuracy : {accuracy:.3f}')

print('\n# confusion matrix')
from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(y_test, prediction)
print(matrix)

import seaborn as sns

label_list = encoder.classes_

plt.figure(figsize=(10, 7))
sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_list, yticklabels=label_list)
plt.xlabel('prediction')
plt.ylabel('real-label')
plt.title('confusion matrix')
filename = dataOut + 'confusion_matrix.png'
plt.savefig(filename)

print('\n# classification_report')
from sklearn.metrics import classification_report
report = classification_report(y_test, prediction)
print(report)

