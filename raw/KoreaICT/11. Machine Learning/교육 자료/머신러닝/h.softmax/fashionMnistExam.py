from keras import Sequential
from keras.datasets import fashion_mnist
from keras.layers import Dense, Flatten

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# 각 클래스의 품목 이름
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

import matplotlib.pyplot as plt

idx = y_train[0]
print(f'y_train[0] : {idx}')
print(f'0번째 클래스 이름 : {class_names[idx]}')

# 이미지 1개를 이용하여 그래프를 그립니다.
plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)
dataOut = './../dataOut/'
filename = dataOut + 'fashion_mnist_01.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

# 데이터를 정규화 합니다.
x_train = x_train / 255.0
x_test = x_test / 255.0

# 그래프를 그릴 행 개수와 열 개수를 정의합니다.
num_rows, num_cols = 4, 4

from Utility.keras_graph_util import plot_gray_image
plot_gray_image(x_train, y_train, num_rows, num_cols, 'fashion_mnist_02.png', class_names)

# 케라스 모델을 생성하고, 학습하도록 합니다.
NB_CLASSES = 10

# 모델을 생성하면서 레이어를 직접 추가합니다.
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(units=128, activation='relu'),
    Dense(units=128, activation='relu'),
    Dense(units=NB_CLASSES, activation='softmax')
])

# sparse_categorical_crossentropy 손실 함수를 사용하면, 원핫 인코딩 작업을 수행하지 않아도 됩니다.
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, verbose=0)

# 모델에 대한 정확도 및 손실을 평가해 봅니다.
score = model.evaluate(x_test, y_test, verbose=0)

print(f'test loss={score[0]}')  # 손실 함수
print(f'test accuracy={score[1]}')  # 정확도

prediction = model.predict(x_test)  # 예측하기

# 잠시 보류
from Utility.keras_graph_util import result_dataframe
result_dataframe(prediction, y_test, 'dataframe.csv')

# 이미지, 예측 문자열, 정답 label, 클래스별 확률(막대 그래프)
from Utility.keras_graph_util import make_graph_probability
make_graph_probability(num_rows, num_cols, prediction, y_test, x_test, class_names, 'fashion_mnist_03.png')

print('finished')