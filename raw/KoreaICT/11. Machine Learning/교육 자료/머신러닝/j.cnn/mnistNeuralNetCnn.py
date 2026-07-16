import pandas as pd
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout

menu = int(input('CNN은 숫자 6을, DropOut은 7을 입력해주세요.) : '))
print(f'menu={menu}')

import sys

if menu < 6 or menu > 7 :
    print('프로그램을 종료합니다.')
    sys.exit(0)

from keras import Sequential
from keras.datasets import mnist
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# CNN 실습 추가 01 변수 추가
TARGET_WIDTH = x_train.shape[1]  # 이미지 너비
TARGET_HEIGHT = x_train.shape[2]  # 이미지 높이
COLOR_MODE = 1  # 손글씨 데이터 셋은 흑백 이미지 입니다.

# CNN 실습 추가 02 형상 변경
# CNN은 이미지를 4차원 형식으로 넣어 주어야 합니다.
x_train.shape = x_train.shape + (1,) # 3차원 + 1차원
x_train = x_train.astype(float) / 255

# 테스트용 데이터도 동일하게 적용합니다.
x_test.shape = x_test.shape + (1,) # 3차원 + 1차원
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

# CNN 실습 추가 03 : 컨블루션 연산 + 맥스 풀링
# 3행 3열짜리 커널 32개를 흑백 이미지와 컨블루션 연산합니다.
KERNEL_SIZE = (3, 3)
POOL_SIZE = (2, 2)

# 1번째 Convolution 연산
model.add(Conv2D(filters=32, kernel_size=KERNEL_SIZE, activation='relu', input_shape=(TARGET_WIDTH, TARGET_HEIGHT, COLOR_MODE)))
model.add(MaxPool2D(pool_size=POOL_SIZE))

# 2번째 Convolution 연산
model.add(Conv2D(filters=64, kernel_size=KERNEL_SIZE, activation='relu'))
model.add(MaxPool2D(pool_size=POOL_SIZE))

# 3번째 Convolution 연산
model.add(Conv2D(filters=64, kernel_size=KERNEL_SIZE, activation='relu'))
model.add(MaxPool2D(pool_size=POOL_SIZE))

model.add(Flatten())

# CNN 실습 추가 04 : 기존의 다중 if 구문 삭제
# 참조 옵티 마이저 : https://journeysnote.tistory.com/66

# CNN 실습 추가 05 : 다음 구문은 DropOut를 위하여 분기 처리합니다.

if menu == 6: # Dropout는 과적합 방지를 위하여 수치 값을 0으로 바꿔주는 역할 입니다.
    model.add(Dense(units=512, activation='relu'))
    model.add(Dense(units=512, activation='relu'))

elif menu == 7:
    DROPOUT_RATE = 0.3
    model.add(Dense(units=512, activation='relu'))
    model.add(Dropout(DROPOUT_RATE))  # 지정 비율 만큼 노드(Node)를 비활성화 시킵니다.

    model.add(Dense(units=512, activation='relu'))
    model.add(Dropout(DROPOUT_RATE))
# end if

model.add(Dense(units=NB_CLASSES, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


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