import numpy as np
import math
from sklearn.model_selection import train_test_split

dataIn = './../dataIn/'
filename = dataIn + 'surgeryTest.csv'

data = np.loadtxt(filename, delimiter=',')
print('type(data) = ' + str(type(data)))
print('data.shape = ' + str(data.shape))

# 연관 변수들
EPOCHS = 30

total_row = data.shape[0] # 전체 행 개수
TEST_SIZE = 0.2 # 테스트용 데이터 비율
train_row = total_row * (1 - TEST_SIZE)
train_row = int(train_row)  # 정수화
BATCH_SIZE = 10  # 배치 사이즈
batchsu_per_epoch = math.ceil(train_row / BATCH_SIZE)
print(f'에포크 당 배치 실행 개수 : {batchsu_per_epoch}')

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

print('x.shape = ' + str(x.shape))
print('y.shape = ' + str(y.shape))

print('클래스별 특정 클래스의 개수 파악')
unique_values, value_counts = np.unique(y, return_counts=True)
print(unique_values, value_counts)

for value, count in zip(unique_values, value_counts):
    print(f'클래스 {int(value)}은(는) {count}개입니다.')

# 데이터 분할
seed = 0
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=TEST_SIZE, random_state=seed)

# 모델 객체 생성
from keras import Sequential
model = Sequential()

from keras.layers import Dense

# 입력 17개, 출력 30개를 갖는 Dense 레이어를 추가합니다.
# 중간 과정의 활성화 함수는 `relu` 함수를 많이 사용합니다.
# activation 매개 변수의 기본 값은 linear 입니다.
model.add(Dense(units=30, input_dim=x_column, activation='relu'))

# 전 단계의 units가 다음 단계의 입력이 됩니다.
# 마지막 레이어에서는 적절한 활성화 함수를 사용하여야 합니다.
# 우리는 이항 분류 모델이므로 반드시 '시그모이드' 함수를 사용해야 합니다.
model.add(Dense(units=y_column, activation='sigmoid'))

# loss는 손실 함수를 정의하는 곳, optimizer는 옵티마이저를 지정하는 곳
# metrics는 `평가 지표`로써, 정확도(accuracy)도 같이 보여 주시길 바랍니다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit_hist : fitting 히스토리 정보를 저장하고 있는 객체
fit_hist = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1)

prediction = model.predict(x_test)
print('예측 확률')
print(prediction)

# 다음 부분을 Utillity 디렉토리 아래에 keras_graph_util.py에 작성하도록 합니다.
# 함수 이름 : model_information
# 매개 변수 : model 객체
from Utility.keras_graph_util import model_information
model_information(model)

# 함수 이름 : graph_accuracy_loss
# 매개 변수 : history 객체, 파일 이름(surgeryTestGraph), figSize(옵션)
from Utility.keras_graph_util import graph_accuracy_loss
graph_accuracy_loss(fit_hist, 'surgeryTestGraph', (12, 6))

print('finished')