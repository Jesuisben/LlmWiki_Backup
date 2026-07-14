import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

# from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
idg=ImageDataGenerator(rescale=1/255, rotation_range=90, width_shift_range=1.0,
                       height_shift_range=0.5, shear_range=0.8, zoom_range=0.5,
                       horizontal_flip=True, vertical_flip=True)
print('type(idg) :', type(idg) )

target_w, target_h = 512, 512

# iters : 해당 폴더로부터 데이터를 읽어 들이는 반복자(iterator) 객체입니다.
# color_mode는 색상 채널 정보입니다.
# grayscale(1 채널_흑백 TV), rgb(3 채널_컬러 TV), rgba(4 채널)
iters=idg.flow_from_directory(directory='../dataIn/img', target_size=(target_w, target_h), \
                              classes=['cat', 'dog'], color_mode='rgb', \
                              class_mode='binary', batch_size=4, shuffle=False)
'''
Found 20 images belonging to 2 classes.
2개('cat', 'dog')의 분류에 속하는 20개의 이미지가 발견되었습니다.
'''

print('type(iters) :', type(iters)) # DirectoryIterator 객체

print('batch_size 속성과 연관이 있습니다')
print('iters.batch_size :', iters.batch_size)

print('image_shape 속성은 target_size와 color_mode와 연관이 있습니다.')
print('iters.image_shape :', iters.image_shape)

print('클래스 레이블(정답)과 색인 정보를 사전 형식으로 보여 줍니다.')
print('iters.class_indices :', iters.class_indices)

# next 함수는 반복자(iterator) 객체인 iters에서 다음 item을 읽어 들입니다.
x_train, y_train=next(iters)

print('len(x_train) :', len(x_train))

print('x_train.shape은 batch_size, target_w, target_h, col_mode를 의미합니다.')
print('x_train.shape :', x_train.shape)

print('y_train.shape은 batch_size를 tuple 형식으로 반환합니다.')
print('y_train.shape :', y_train.shape)

img_target='../dataOut/'
plt.axis('off')
for idx in range(len(x_train)):
    plt.imshow(x_train[idx])
    filename=img_target + 'image_gen' + str(idx) + '.png'
    plt.savefig(filename)
    print(filename + ' 파일 저장됨')
# end for
