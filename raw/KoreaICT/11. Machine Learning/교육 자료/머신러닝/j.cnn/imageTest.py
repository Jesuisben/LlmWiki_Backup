img_source = './../dataIn/image/' # 이미지를 불러 들일 경로
img_target = './../dataOut/'  # 이미지 파일이 저장될 경로

img_dog = img_source + 'mydog.png'
print('원본 이미지 : ' + img_dog)

import matplotlib.pyplot as plt

from keras.utils import load_img, img_to_array, array_to_img

image32 = load_img(img_dog, target_size=(32, 32))
print(type(image32))

plt.axis('off')
plt.figure()
plt.xticks([])
plt.yticks([])
plt.imshow(image32)
filename = img_target + 'dog32.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

image64 = load_img(img_dog, target_size=(64, 64))
plt.figure()
plt.xticks([])
plt.yticks([])
plt.imshow(image64)
filename = img_target + 'dog64.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

image224 = load_img(img_dog, target_size=(224, 224))
plt.figure()
plt.xticks([])
plt.yticks([])
plt.imshow(image224)
filename = img_target + 'dog224.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

arr_dog_224 = img_to_array(image224)
print(type(arr_dog_224))
print(arr_dog_224.shape)
# print(arr_dog_224)

# 저해상도 이미지를 생성해주는 함수
def drop_resolution(x, scale=3.0):
    img = array_to_img(x)

    size = (x.shape[0], x.shape[1])
    print('size : ', size)
    small_size = (int(size[0]/scale), int(size[1]/scale))
    print('small_size : ', small_size)

    small_img = img.resize(small_size, 3)
    print('type(small_img) :', type(small_img))
    plt.imshow(small_img)
    filename = img_target + 'drop_res_image(' + str(scale) + ').png'
    plt.savefig(filename)
    print(filename + ' 파일 저장됨')

drop_resolution(arr_dog_224)
drop_resolution(arr_dog_224, scale=10.0)

import numpy as np
def make_gaussian_noise_data(data_x, scale=0.8):
    gaussian_data_x = data_x + np.random.normal(loc=0, scale=scale, size=data_x.shape)
    gaussian_data_x = np.clip(gaussian_data_x, 0, 1)
    return gaussian_data_x
# end def make_gaussian_noise_data

x_train_gauss = make_gaussian_noise_data(arr_dog_224)
plt.imshow(x_train_gauss.reshape(448, 336), cmap='Greys')
filename = img_target + 'file_gauss.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장됨')

print('finished')