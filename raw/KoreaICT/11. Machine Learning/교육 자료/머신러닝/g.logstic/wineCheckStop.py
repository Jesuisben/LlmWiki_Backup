import pandas as pd

dataIn, dataOut = './../dataIn/', './../dataOut/'
filename = dataIn + 'wine.csv'

df_wine = pd.read_csv( filename, header= None )

print('df_wine.shape :', df_wine.shape)
print('-' * 40)

df = df_wine.sample(frac=0.15) # 15%만 샘플링
print('df.shape :', df.shape)
print('-'*30)

data = df.values

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

model = Sequential()

model.add(Dense(units=30, activation='relu', input_dim=x_column))
model.add(Dense(units=12, activation='relu'))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=y_column, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 사용할 콜백 함수에 대한 객체를 생성합니다.
# ModelCheckpoint : 주어진 조건을 만족하면 해당 모델을 파일 형식으로 저장합니다.
# EarlyStopping : 학습에 대한 개선의 기미가 보이지 않으면, 강제로 종료를 수행합니다.
from tensorflow.python.keras.callbacks import ModelCheckpoint, EarlyStopping

model_dir = dataOut + 'model/' # 파일이 저장될 폴더

# 폴더가 없는 경우를 대비하여 폴더 생성
import os # 운영 체제와 관련된 파이썬 모듈
if not os.path.exists(model_dir):
    os.mkdir(model_dir)

model_name = model_dir + '{epoch:02d}-{val_loss:.4f}.hdf5' # 저장될 파일 형식

# save_best_only=True : 학습을 진행하는 동안 이전보다 개선이 된 경우에만 저장할께요.
mcp = ModelCheckpoint(filepath=model_name, monitor='val_loss', verbose=1, save_best_only=True)

# 학습 자동 중단 설정
# patience=100 : 테스트 오차가 좋아지지 않더라도 epoch 100번 정도는 기다려 줍니다.
es = EarlyStopping(monitor='val_loss', patience=100)

history = model.fit(x, y, validation_split=0.2, epochs=3500, batch_size=500, verbose=0, callbacks=[es, mcp])

# history = model.fit(x, y, validation_split=0.2, epochs=3500, batch_size=500, verbose=1)

# y_vloss에 테스트셋으로 실험 결과의 오차 값을 저장
val_loss=history.history['val_loss']

print(model.metrics_names)

# 학습 셋으로 측정한 정확도의 값을 저장합니다.
accuracy=history.history['accuracy']

# 데이터 시각화
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

print('정확도는 파란 색, 오차는 빨간 색으로 시각화')
x_len = np.arange(len(accuracy)) # x 축에 그려지는 눈금 단위
# plt.legend(['val_loss','accuracy'])

plt.figure()
plt.plot(x_len, val_loss, 'o', c='red', markersize=1)
plt.title('손실 함수 그래프')
savefilename = dataOut + 'wineCheckStop01.png'
plt.savefig(savefilename)
print(savefilename + ' 파일 저장됨')

plt.figure()
plt.plot(x_len, accuracy, 'o', c='blue', markersize=1)
plt.title('정확도 그래프')
savefilename = dataOut + 'wineCheckStop02.png'
plt.savefig(savefilename)
print(savefilename + ' 파일 저장됨')

print('finished')