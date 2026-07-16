import numpy as np
import pandas as pd

dataIn = './../dataIn/'
dataOut = './../dataOut/'

filename = dataIn + 'iris.csv'

data = np.loadtxt(
    filename,
    skiprows=1,
    delimiter=',',
    dtype='str'
)

# =====================================================
# 데이터 분리
# =====================================================

table_col = data.shape[1]  # csv 파일의 열 개수
y_column = 1               # 정답(label) 열 개수
x_column = table_col - y_column  # input data 열 개수

print(f'table_col={table_col}')
print(f'x_column={x_column}')
print(f'y_column={y_column}')

x = data[:, 0:x_column]
x = x.astype(float)  # 머신 러닝 학습을 위하여 숫자로 변경

y = data[:, x_column:]

# ravel() : NumPy 배열을 1차원으로 평탄화
y = y.ravel()

print('\nx[:10]')
print(x[:10])

print('\nbefore label encoded')
print(y[:10])

# =====================================================
# DataFrame 확인
# =====================================================

myframe = pd.DataFrame(x, index=y)

print('\nmyframe')
print(myframe)

print('-' * 30)

print('myframe.index.unique()')
print(myframe.index.unique())

print('-' * 30)

# =====================================================
# Label Encoding
# =====================================================

from sklearn.preprocessing import LabelEncoder

# transform : 문자열 라벨을 숫자로 변환
encoder = LabelEncoder()

encoder.fit(y)

y = encoder.transform(y)

print('\nafter label encoded')
print(y[:10])

print('\n라벨 매핑 정보')

for idx, label in enumerate(encoder.classes_):
    print(f'{label} -> {idx}')

# =====================================================
# 데이터 분리
# =====================================================

from sklearn.model_selection import train_test_split

# 훈련용 데이터와 테스트용 데이터를 70대 30으로 분리
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.3,
    random_state=1234
)

print('\nx_train[:10]')
print(x_train[:10])

print('-' * 30)

print('y_train[:10]')
print(y_train[:10])

print('-' * 30)

# =====================================================
# 정규화 전 데이터 범위 확인
# =====================================================

def print_feature(somedata):
    for idx in range(somedata.shape[1]):
        print(
            f'컬럼{idx+1} 범위 : '
            f'[{round(min(somedata[:, idx]), 3)}, '
            f'{round(max(somedata[:, idx]), 3)}]'
        )

print('\n# before normalization')
print_feature(x_train)

# =====================================================
# 표준화(Standardization)
# =====================================================

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# 학습 데이터 기준으로 평균, 표준편차 계산
scaler.fit(x_train)

# 학습 데이터 변환
x_train = scaler.transform(x_train)

# 테스트 데이터 변환
x_test = scaler.transform(x_test)

print('\n# after normalization')
print_feature(x_train)

# =====================================================
# Gaussian Naive Bayes
# =====================================================

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(x_train, y_train)

# =====================================================
# 예측
# =====================================================

prediction = model.predict(x_test)

print('\n예측된 라벨')
print(prediction)

print('\n실제 라벨')
print(y_test)

# =====================================================
# 결과 확인
# =====================================================

bool_result = prediction == y_test

finalresult = pd.DataFrame({
    '예측값': prediction,
    '실제값': y_test,
    '예측결과': bool_result
})

print('\nfinalresult')
print(finalresult)

print('-' * 30)

hitcount = np.sum(bool_result)

totalcount = len(finalresult)

print(
    "총 {}개 중에서 {}개를 정확히 맞춤".format(
        totalcount,
        hitcount
    )
)

# =====================================================
# 정확도 계산
# =====================================================

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, prediction)

print(
    "prediction accuracy: {:.4f}".format(
        accuracy
    )
)