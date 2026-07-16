from keras import Sequential
from keras.callbacks import EarlyStopping

targetFolder = r'..\datasets\cats_and_dogs_random'
print(targetFolder)

import os

trainFolder = os.path.join(targetFolder, 'train')
validationFolder = os.path.join(targetFolder, 'validation')

from keras.preprocessing.image import ImageDataGenerator

trainImageGenerator = ImageDataGenerator(rescale=1/.255)
validationImageGenerator = ImageDataGenerator(rescale=1/.255)

IMAGE_WIDTH, IMAGE_HEIGHT = 150, 150
BATCH_SIZE = 20
COLOR_MODE = 3
CLASS_MODE = 'binary'

trainGenerator = trainImageGenerator.flow_from_directory(
    directory=trainFolder,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode=CLASS_MODE
)

validationGenerator = validationImageGenerator.flow_from_directory(
    directory=validationFolder,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode=CLASS_MODE
)

print('1번에 실행할 데이터 모음을 배치라고 합니다.')
for data, label in trainGenerator:
    print('배치 데이터 크기 : ', data.shape)
    print('정답 배치의 크기 : ', label.shape)
    break
# end for

print('케라스 모델을 생성합니다.')
KERNEL_SIZE = (3, 3)
POOLING_SIZE = (2, 2)

model = Sequential()

from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

INPUT_IMAGE_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, COLOR_MODE)

model.add(Conv2D(filters=32, kernel_size=KERNEL_SIZE, activation='relu', input_shape=INPUT_IMAGE_SHAPE))
model.add(MaxPooling2D(pool_size=POOLING_SIZE))

model.add(Conv2D(filters=64, kernel_size=KERNEL_SIZE, activation='relu'))
model.add(MaxPooling2D(pool_size=POOLING_SIZE))

model.add(Conv2D(filters=128, kernel_size=KERNEL_SIZE, activation='relu'))
model.add(MaxPooling2D(pool_size=POOLING_SIZE))

model.add(Conv2D(filters=128, kernel_size=KERNEL_SIZE, activation='relu'))
model.add(MaxPooling2D(pool_size=POOLING_SIZE))

model.add(Flatten())

model.add(Dense(units=512, activation='relu'))

# 마지막 layer : 이항 분류이므로 'sigmoid'
y_column = 1
model.add(Dense(units=y_column, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

from Utility.keras_graph_util import model_information, graph_accuracy_validation, graph_loss_validation

model_information(model)

# 검증용 손실 함수 'val_loss'를 모니터링해주세요.
# 3 에포크(patience=3) 동안 나아질 기미가 보이지 않으면 강제로 멈춰 주세요.
earlyStopping = EarlyStopping(patience=3, monitor='val_loss')

# steps_per_epoch : 1번의 epochs내에서 훈련 데이터 셋을 100번 반복하여 사용합니다.
# validation_data : 검증할 데이터 셋 또는 제너레이터
fit_hist = model.fit(x=trainGenerator, steps_per_epoch=100, epochs=30, validation_data=validationGenerator, validation_steps=50, verbose=1, callbacks=[earlyStopping])

print('학습한 데이터를 차후에 사용하려면, 파일 형식으로 저장해 두면 됩니다.')
dataOut = './../dataOut/'
savedFile = dataOut + 'catAndDog.h5'
model.save(savedFile)
print(savedFile + ' 파일이 저장되었습니다.')

print('정확도 그래프')
graph_accuracy_validation(fit_hist, 'catAndDog_accuracy')

print('손실 함수 그래프')
graph_loss_validation(fit_hist, 'catAndDog_loss')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 아래 소스는 이전 소스입니다.

import os

from keras.callbacks import EarlyStopping
from keras.preprocessing.image import ImageDataGenerator
from keras import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

print('실습에 사용할 데이터를 선택해 주세요.')
menu = 1#int(input('순차 복사(0), 랜덤 복사(1) : '))

# 어느 이미지 폴더를 읽어 들일 것인지를 선택합니다.
if menu == 0:
    targetFolder = r'..\datasets\cats_and_dogs_small'
else:
    targetFolder = r'..\datasets\cats_and_dogs_random'
# end if

print(targetFolder)

trainFolder = os.path.join(targetFolder, 'train') # 훈련용 이미지 폴더
validationFolder = os.path.join(targetFolder, 'validation') # 검증용 이미지 폴더

# 훈련용과 검증용에 대한 ImageDataGenerator 객체를 생성합니다.
trainImageGenerator = ImageDataGenerator(rescale=1./255)
validationImageGenerator = ImageDataGenerator(rescale=1./255)

# 읽어 들일 이미지의 너비와 높이와 관련된 변수를 정의합니다.
IMAGE_WIDTH, IMAGE_HEIGHT = 150, 150
BATCH_SIZE = 20  # 한 번에 처리(배치)할 데이터의 개수
COLOR_MODE = 3  # 1(흑백)/3(컬러)
CLASS_MODE = 'binary'

# 케라스 모델에 사용할 제너레이터 객체를 생성합니다.
# trainFolder 폴더에서 이미지 크기는 (IMAGE_WIDTH, IMAGE_HEIGHT)으로,
# 20개(BATCH_SIZE)씩 읽어 들어서 생성해 주세요.
# 이항 분류('binary') 처리입니다.
trainGenerator = trainImageGenerator.flow_from_directory(
    directory=trainFolder,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode=CLASS_MODE
)
'''
    Found 2000 images belonging to 2 classes.
    해당 폴더에 이항 분류(2 classes)를 위한 이미지가 2,000개가 들어 있습니다.
'''

validationGenerator = validationImageGenerator.flow_from_directory(
    directory=validationFolder,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode=CLASS_MODE
)

print('1번에 실행할 데이터 모음을 배치(batch)라고 합니다.')
for data, label in trainGenerator:
    # (20, 150, 150, 3) = (배치사이즈, 이미지너비, 이미지높이, 컬러모드)
    # data는 이미지 크기가 150*150인 컬러 이미지 20개입니다.
    print('배치 데이터 크기 :', data.shape)
    print('정답(label) 배치 크기 :', label.shape)
    break
# end for

print('케라스 모델을 생성합니다.')
# 머신 러닝 모델 객체 생성
model = Sequential()

# input_shape : 해당 이미지에 대한 입력 정보를 정확하게 넣어 주어야 합니다.
INPUT_IMAGE_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, COLOR_MODE)

model.add(Conv2D(filters=32, kernel_size=KERNEL_SIZE, activation='relu', input_shape=INPUT_IMAGE_SHAPE))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 컨블루션/맥스 풀링은 데이터를 2차원적으로 다루는 데, 최종 Dense Layer에서는 1차원으로 변형해 주어야 합니다.
model.add(Flatten())

model.add(Dense(units=512, activation='relu'))

# 우리는 강아지/고양이에 대한 이항 분류를 진행 중입니다.
# last layer에서는 해당 알고리즘에 맞는 활성화 함수(activation)를 사용해야 합니다.
# 그래서, 시그모이드('sigmoid') 함수를 사용하면 됩니다.
y_column = 1
model.add(Dense(units=y_column, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

from Utility.keras_graph_util import model_information
model_information(model)


# 검증용 손실 함수 'val_loss'를 모니터링해주세요.
# 3 에포크(patience=3) 동안 나아질 기미가 보이지 않으면 강제로 멈춰 주세요. 
earlyStopping = EarlyStopping(patience=3, monitor='val_loss')

'''					
x : 훈련용 데이터 셋 또는 ImageGenerator 객체
steps_per_epoch : 
	한 번의 epoch(에포크)에서 모델이 훈련 데이터를 몇 번 사용할지를 결정합니다. 
	1번의 epoch 내에서 훈련 데이터셋을 100번 반복하여 사용합니다.
epochs : 반복할 epoch(에포크) 수
# validation_data : 검증할 데이터 셋 또는 제너레이터
verbose=1 : 1은 진행 막대와 함께 각 epoch마다 정보를 출력합니다.
callbacks : 훈련 중에 적용할 콜백 함수 list
'''
fit_hist = model.fit(x=trainGenerator, steps_per_epoch=100, epochs=30,
                    validation_data=validationGenerator,
                    validation_steps=50,
                    verbose=1,
                    callbacks=[earlyStopping])

print('학습한 데이터를 차후에 사용하려면, 모델을 파일 형식으로 저장해 두면 됩니다.')
savedModelName = targetFolder.split('\\')[-1] + '.h5'
model.save(savedModelName)
print(savedModelName + ' 파일 저장됨')

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
##################################################################
# 학습 결과에 대하여 시각화를 진행합니다.
print('정확도 그래프 그리기')
accuracy = fit_hist.history['accuracy']
val_accuracy = fit_hist.history['val_accuracy']

x_pos = range(len(accuracy)) # x축 눈금
plt.figure() # 새 도화지 준비
plt.plot(x_pos, accuracy, 'bo', label='training accuracy')
plt.plot(x_pos, val_accuracy, 'bo', label='validation accuracy')
plt.title('training and validation accuracy')
fileName = __file__.split('\\')[-1].split('.')[0] + '_01.png'
plt.savefig(fileName)
print(fileName + ' 파일 저장됨')
##################################################################
print('손실 함수 그래프 그리기')
loss = fit_hist.history['loss']
val_loss = fit_hist.history['val_loss']

x_pos = range(len(loss))
plt.figure()
plt.plot(x_pos, loss, 'bo', label='training loss')
plt.plot(x_pos, val_loss, 'bo', label='validation loss')
plt.title('training and validation loss')
fileName = __file__.split('\\')[-1].split('.')[0] + '_02.png'
plt.savefig(fileName)
print(fileName + ' 파일 저장됨')
##################################################################