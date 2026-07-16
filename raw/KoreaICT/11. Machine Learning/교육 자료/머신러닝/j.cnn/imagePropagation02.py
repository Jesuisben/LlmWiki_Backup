from keras.preprocessing.image import ImageDataGenerator
from keras.utils import load_img, img_to_array, array_to_img

idg = ImageDataGenerator(rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, \
                         shear_range=0.2, zoom_range=0.2, \
                         horizontal_flip=True, vertical_flip=True, \
                         fill_mode='nearest')



import matplotlib.pyplot as plt

# 150*150 형태로 이미지를 읽어 옵니다.
target_w, target_h = 150, 150
image_gen_su = 10  # 생성할 이미지 갯수

# 파일들의 이름이 목록으로 출력됨
import os
img_source='../dataIN/image/'
filelist=os.listdir(img_source)

for onefile in filelist:
    sample_image = img_source + onefile
    # print(sample_image)
    myimage = load_img(sample_image, target_size=(target_w, target_h))

    # 이미지를 배열로 변경시킵니다.
    x = img_to_array(myimage)
    print('before x.shape : ', x.shape)

    x = x.reshape((1,) + x.shape)
    print('after x.shape : ', x.shape)

    idx = 0  # 카운터 변수
    # flow() 메소드는 랜덤하게 변형된 이미지의 배치 목록들을 무제한으로 생성합니다.
    for batch in idg.flow(x, batch_size=1):
        idx += 1

        plt.figure(num=idx)
        plt.axis('off')
        newimg = array_to_img(batch[0])
        plt.imshow(newimg)
        currfile = onefile.split('.')[0] # 파일의 이름
        filename = '../dataOut/' + currfile + str(idx).zfill(3) + '.png'
        plt.savefig(filename)
        print(filename + ' 파일 저장됨')

        if idx % image_gen_su == 0:
            break
    # inner for
# outer for

print('finished')