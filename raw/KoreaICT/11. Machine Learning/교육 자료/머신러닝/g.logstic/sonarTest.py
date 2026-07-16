import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

dataIn = './../dataIn/'

filename = dataIn + 'sonarTest.csv'
df = pd.read_csv(filename, header=None)

print('df.info()') # 208행 61열 데이터
print(df.info())

print('정답(label) 클래스별 빈도 수')
print(df[60].value_counts())

# 더 필요하면 판다스 함수들을 이용하여 확인 요망

data = df.values

# 연관 변수들
SEED = 0  # 랜덤 씨드 번호
EPOCHS = 20
TEST_SIZE = 0.3  # 테스트용 데이터 비율
BATCH_SIZE = 5  # 배치 사이즈

# ndarray : n은 숫자, d는 dimension, array는 배열
print(f'데이터 유형 : {type(data)}')

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

print('x.shape = ' + str(x.shape))
print('y.shape = ' + str(y.shape))

print(y[0:10])

# LabelEncoder에서 사용하기 위하여 평탄화 시킵니다.
y = y.ravel()

# 변수 y는 분류 문자열 'M'과 'R' 중에 하나의 값으로 되어 있습니다.
# 따라서, LabelEncoder 클래스를 이용하여 숫자형 데이터로 변환해 주어야 합니다.

encoder = LabelEncoder()
encoder.fit(y)
y = encoder.transform(y)

print('x[0:10] = ')
print(x[0:10])

print('y[0:10] = ')
print(y[0:10])

# 다음 오류를 막기 위하여 실수형 타입으로 변경해야 합니다.
# ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type float).
# 머신 러닝에 숫자 형태로 입력하기 위하여 타입 변환
x = x.astype(float)
y = y.astype(float)

# 데이터 셋 70대 30으로 분리
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=TEST_SIZE, random_state=SEED)

# Keras 모델 생성 후 학습하기
from keras import Sequential
model = Sequential()

from keras.layers import Dense

'''
layer 개수 = add() 함수 개수 + 1

add() 함수 사용 지침
    현재 layer의 출력이 다음 layer의 입력이 됩니다.
    1번째 add() 함수에만 반드시 input_dim 매개 변수가 필요합니다.
    input_dim 매개 변수에는 train 데이터의 열 개수가 입력이 되어야 합니다.
    마지막 layer를 제외한 나머지 layer에는 일반적으로 'relu'라는 활성화 함수를 사용합니다.
    마지막 add() 함수의 units 매개 변수는 반드시 label 열의 개수와 동일해야 합니다.
    마지막 add() 함수에는 activation 매개 변수의 내용이 해당 분석 기법에 맞는 알고리즘을 명시해 주어야 합니다.
    이번 예시에는 로지스틱 회귀 이므로, 'sigmoid'를 명시했습니다.
'''

# 입력 : 60(x_column)개, 출력 : 24개, 활성화 함수 : relu
model.add(Dense(units=24, input_dim=x_column, activation='relu'))

# 입력 : 24개, 출력 : 10개, 활성화 함수 : relu
model.add(Dense(units=10, activation='relu'))

# 입력 : 10개, 출력 : 1(y_column)개, 활성화 함수 : sigmoid
model.add(Dense(units=y_column, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

fit_hist = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1)

from Utility.keras_graph_util import model_information
model_information(model)

from Utility.keras_graph_util import graph_accuracy_loss
graph_accuracy_loss(fit_hist, 'sonaTestGraph', (12, 6))

# '학습'을 하는 데 시간이 많이 소요 되는 모델은 파일 형식으로 저장해 둡니다.
# 차후 학습을 다시 할 필요 없이, 이미 학습된 모델을 가지고 다시 시작할 수 있습니다.
# 이러한 모델을 `사전 학습 모델`(pretrained model)이라고 합니다.
print('모델을 파일로 저장합니다.')
model_name = 'my_model.h5'
model.save(model_name)

del model # 메모리 내에서 해당 model을  삭제합니다.

# print('모델을 다시 로딩합니다.')
# from tensorflow.python.keras.models import load_model
# model = load_model(model_name)
# 
# score = model.evaluate(x_test, y_test)
# print('test loss : %.4f' % (score[0]))
# print('test accuracy : %.4f' % (score[1]))

print('finished')