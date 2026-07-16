from keras.preprocessing.image import ImageDataGenerator
from keras.utils import load_img, img_to_array, array_to_img

img_source='../dataIn/image/'
sample_image=img_source + 'cat.jpg'

# 150*150 형태로 이미지를 읽어 옵니다.
target_w, target_h=150, 150
myimage=load_img(sample_image, target_size=(target_w, target_h))

# 이미지를 배열로 변경시킵니다.

x=img_to_array(myimage)
print('before x.shape : ', x.shape)

print('flow 메소드는 4차원의 이미지 정보를 필요로 하기 때문에')
print('차원 변경(reshape)을 수행해 주어야 합니다.')
x=x.reshape((1,) + x.shape)
print('after x.shape : ', x.shape)


idg=ImageDataGenerator(rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, \
                         shear_range=0.2, zoom_range=0.2, \
                         horizontal_flip=True, vertical_flip=True, \
                         fill_mode='nearest')

import matplotlib.pyplot as plt


# flow() 메소드는 랜덤하게 변형된 이미지의 배치 목록들을 무제한으로 생성합니다.
idx=0 # 카운터 변수
image_gen_su=20 # 생성할 이미지 갯수
for batch in idg.flow(x, batch_size=1):
    # print('type(batch) :', type(batch))
    # print(batch)
    idx += 1

    plt.figure(num=idx)
    plt.axis('off')
    newimg=array_to_img(batch[0])
    plt.imshow(newimg)

    filename='../dataOut/' + str(idx).zfill(3) + '.png'
    plt.savefig(filename)
    print(filename + ' 파일 저장됨')

    if idx%image_gen_su == 0:
        break

print('finished')