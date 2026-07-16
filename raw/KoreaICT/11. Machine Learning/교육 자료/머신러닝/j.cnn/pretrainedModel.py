import pandas as pd
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.utils import load_img, img_to_array
from pandas import Series

from Utility.keras_graph_util import model_information

model = VGG16()
print('type(model)')
print(type(model))

model_information(model)

IMAGE_WIDTH, IMAGE_HEIGHT = 224, 224
image_source = './../dataIn/image/'  # 이미지 출처
image_target = './../dataOut/'  # 파일을 저장할 이미지 경로

import os

file_list = os.listdir(image_source)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# total_data는 예측을 수행하고자 하는 전처리된 이미지 관련 배열들을 저장하고 있는 리스트입니다.
total_data = []

for filename in file_list:
    # 현재 작업 중인 이미지
    curr_image = load_img(image_source + filename, target_size=(IMAGE_WIDTH, IMAGE_HEIGHT))
    plt.imshow(curr_image)

    # 읽어 들인 이미지 정보를 다시 파일로 저장해 봅니다.
    saved_file = image_target + 'pretrained_model_' + filename
    plt.savefig(saved_file)
    print(filename + ' 파일 저장 완료')

    # 이미지를 numpy 배열로 만듭니다.
    ndarray = img_to_array(curr_image)
    # print(ndarray)

    # 해당 이미지를 VGG16 모델의 학습 환경과 동일하게 형상을 변경해 줍니다.
    pre_input = preprocess_input(ndarray)
    # print(pre_input)
    print(f'pre_input.shape = {pre_input.shape}')

    total_data.append(pre_input)
    print('*' * 30)
# end for

import numpy as np
x_test = np.stack(total_data)

# 입력 데이터의 형상 = (4, 224, 224, 3)
# 224*224 컬러 이미지 4개입니다.
print(f'입력 데이터의 형상 = {x_test.shape}')
# print(x_test)

prediction = model.predict(x_test)
print(f'prediction.shape = {prediction.shape}')
print(f'입력 데이터 개수 = {prediction.shape[0]}')
print(f'VGG16 모델의 class 개수 = {prediction.shape[1]}')
print(prediction)

print('예측 값 표시 : ')
probability_topn = decode_predictions(prediction, top=10)
print(probability_topn)

# csv 파일에 저장될 데이터 리스트
csv_list = []

for idx in range(len(file_list)):
    print(f'이미지 : `{file_list[idx]}`의 확률 값')

    for prob in range(len(probability_topn[idx])):
        # sublist에 들어 가는 순서 : (이미지이름, 결과문자열, 확률값)
        sublist = [file_list[idx],
                   probability_topn[idx][prob][1],
                   probability_topn[idx][prob][2]]
        csv_list.append(sublist)
    print('-' * 30)
    # end inner for
# end outer for

print(csv_list)

mycolumns = ['image', 'description', 'probability']
df = pd.DataFrame(csv_list, columns=mycolumns)

dataOut = './../dataOut/'
filename = dataOut + 'prediction_result.csv'
df.to_csv(filename, encoding='UTF-8')

# 이미지별 상위 top 10을 막대 그래프로 시각화.
mycolor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'Beige', '#FF1493', '#FF00CC']

for idx, prob_list in enumerate(probability_topn):
    plt.figure(figsize=(10, 8))

    # 리스트 컴프리헨션으로 data와 captions을 생성합니다.
    captions = [item[1] for item in prob_list]
    data = [100 * item[2] for item in prob_list] # 확률값에 100곱하기

    # 시리즈로 데이터 생성 후 차트 그리기
    chartdata = Series(data, index=captions)
    chartdata.plot(kind='bar', rot=12, color=mycolor[:len(captions)])

    # 제목 및 기타 설정
    plt.title(f'이미지 {file_list[idx]} 분류 결과', size=15)
    plt.ylim([-10, 100])
    plt.grid(True)

    filename = f'{image_target}probability_{file_list[idx]}'
    plt.savefig(filename)
    print(f'{filename} 파일이 저장되었습니다.')

# end for

print('finished')