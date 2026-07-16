from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f'x_train.shape = {x_train.shape}')
print(f'y_train.shape = {y_train.shape}')
print(f'x_test.shape = {x_test.shape}')
print(f'y_test.shape = {y_test.shape}')

# dtype은 data type을 의미합니다.
# uint8 : unsigned int 8
print(f'x_train.dtype = {x_train.dtype}')
print(f'x_train.ndim = {x_train.ndim}')

print(f'x_train[0:5] = {x_train[0:5]}')
print(f'y_train[0:5] = {y_train[0:5]}')

table_row = x_train.shape[0] # 행수
x_column = x_train.shape[1] * x_train.shape[2] # 열수

print(f'이 모델은 {table_row}행 {x_column}열짜리의 이미지 데이터로 학습하는 모델입니다.')
print('숫자 인식을 하므로 class = 10인 다중 분류 모델입니다.')

import matplotlib.pyplot as plt

print('2행 3열로 그려 보기')
nrow, ncol = 2, 3
fig, axes = plt.subplots(nrow, ncol, figsize=(10, 8))

for idx in range(nrow * ncol):
    ax = axes[idx // ncol, idx % ncol]
    ax.imshow(x_train[idx])
    # ax.imshow(x_train[idx], cmap='gray') # 흑백
    ax.set_title(f'label : {y_train[idx]}') # 이미지 레이블 표시
    ax.axis('off')

dataOut = './../dataOut/'
filename = dataOut + 'mnist_subplots.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')