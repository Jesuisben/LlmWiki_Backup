import pandas as pd
from keras.layers import Dense

menu = int(input('1부터 5사이의 숫자를 입력 : '))
print(f'menu={menu}')

import sys

if menu < 1 or menu > 5 :
    print('프로그램을 종료합니다.')
    sys.exit(0)

from keras import Sequential
from keras.datasets import mnist
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_column = x_train.shape[1] * x_train.shape[2]
print(f'입력 데이터 열수 : `{x_column}`개')

# 3차원 데이터를 2차원 데이터로 형상 변경하고, 정규화를 수행합니다.
x_train = x_train.reshape(x_train.shape[0], x_column)
x_train = x_train.astype(float) / 255

# 테스트용 데이터도 동일하게 적용합니다.
x_test = x_test.reshape(x_test.shape[0], x_column)
x_test = x_test.astype(float) / 255

print(f'train data shape : `{x_train.shape}`')
print(f'x_test data shape : `{x_test.shape}`')

print('before y_train[0]')
print(y_train[0])

print('정답(숫자 10개)에 대한 one hot encoding을 적용합니다.')
NB_CLASSES = 10  # 숫자가 0~9이므로 ...
y_train = to_categorical(y_train, num_classes=NB_CLASSES)
y_test = to_categorical(y_test, num_classes=NB_CLASSES)

print('after y_train[0]')
print(y_train[0])

# 관련 변수
EPOCH_SU = 5
BATCH_SIZE = 64
VALIDATION_SPLIT = 0.3  # 검증용 분리 비율

# 모델 생성하기
model = Sequential()

# 참조 옵티 마이저 : https://journeysnote.tistory.com/66
if menu == 1: # test01
    model.add(Dense(units=NB_CLASSES, input_shape=(x_column,), activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

elif menu == 2:  # 1번에서 optimizer만 변경됨
    model.add(Dense(units=NB_CLASSES, input_shape=(x_column,), activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

elif menu == 3:  # 1번에서 hidden layer이 하나 더 추가됨
    model.add(Dense(units=512, input_shape=(x_column,), activation='relu'))

    model.add(Dense(units=NB_CLASSES, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

elif menu == 4:  # 3번에서 hidden layer가 또 하나 추가됨
    # hidden layer 01
    model.add(Dense(units=512, input_shape=(x_column,), activation='relu'))

    # hidden layer 02
    model.add(Dense(units=512, activation='relu'))

    model.add(Dense(units=NB_CLASSES, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

elif menu == 5:  # 4번에서 optimizer의 종류를 `adam`으로 변경함
    model.add(Dense(units=512, input_shape=(x_column,), activation='relu'))

    model.add(Dense(units=512, activation='relu'))

    model.add(Dense(units=NB_CLASSES, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# end if

# fit_hist : 모델을 학습시킨 이후, 해당 이력을 저장하고 있는 개체입니다.
fit_hist = model.fit(x_train, y_train, epochs=EPOCH_SU, batch_size=BATCH_SIZE, validation_split=VALIDATION_SPLIT, verbose=1)

print('history 객체가 소유하고 있는 키 목록 보기')
print(fit_hist.history.keys())

from Utility.keras_graph_util import model_information, graph_accuracy_validation, graph_loss_validation, \
    graph_accuracy_loss

model_information(model)

print('모델의 성능 평가')
score = model.evaluate(x_test, y_test, verbose=0)
print(type(score))

# `손실 함수`와 `정확도`를 출력해 봅니다.
print(f'test loss : {score[0]}, test accuracy : {score[1]}')

# 차후를 위하여 별도의 파일로 기록해 둡니다.
dataOut = './../dataOut/'

filename_suffix = str(menu).zfill(2)

filename = dataOut + 'mnist_result_' + filename_suffix + '.csv'

df = pd.DataFrame(score).T
df.columns = ['loss', 'accuracy']
df.to_csv(filename, index=False)
print(filename + ' 파일이 저장되었습니다.')

# 유틸리티 모듈을 이용하여 그래프를 그립니다.
graph_accuracy_validation(fit_hist, 'mnist_accuracy_validation_' + filename_suffix)

graph_loss_validation(fit_hist, 'mnist_loss_validation_' + filename_suffix)

graph_accuracy_loss(fit_hist, 'mnist_accuracy_loss_' + filename_suffix)

print('finished')