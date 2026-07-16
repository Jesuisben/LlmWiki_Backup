import matplotlib.pyplot as plt
from keras.datasets import fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
print('x_train.shape :', x_train.shape)
print('-' * 40)

print('x_train.dtype :', x_train.dtype)
print('-' * 40)

print('x_train.ndim :', x_train.ndim)
print('-' * 40)

print('len(y_train) :', len(y_train))
print('-' * 40)

print('y_train :', y_train)
print('-' * 40)

print('x_test.shape :', x_test.shape)
print('-' * 40)

print('len(y_test) :', len(y_test))
print('-' * 40)

print('y_test :', y_test)
print('-' * 40)

dataOut = '../dataOut/'

# import random
# rand = random.randint(0, len(x_train))
# print(rand)
# digit = x_train[rand]
for idx in range(5):
    digit = x_train[idx]
    plt.imshow(digit)
    filename = dataOut + 'index' + str(idx) + '(' + str(y_train[idx]) + ').png'
    plt.savefig(filename)

print('이미지 파일로 저장됨')
# plt.show()

print('finished')

# x_train.shape : (60000, 28, 28)
# ----------------------------------------
# x_train.dtype : uint8
# ----------------------------------------
# x_train.ndim : 3
# ----------------------------------------
# len(y_train) : 60000
# ----------------------------------------
# y_train : [9 0 0 ... 3 0 5]
# ----------------------------------------
# x_test.shape : (10000, 28, 28)
# ----------------------------------------
# len(y_test) : 10000
# ----------------------------------------
# y_test : [9 2 1 ... 8 1 5]
# ----------------------------------------
# 43743
# fashionMnistImage.png 파일로 저장됨
