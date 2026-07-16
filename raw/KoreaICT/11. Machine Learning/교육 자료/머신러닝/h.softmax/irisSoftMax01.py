import pandas as pd
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

dataIn = './../dataIn/'
filename = dataIn + 'iris.csv'
df = pd.read_csv(filename)
print('df.head()')
print(df.head())

# 머신 러닝에서는 정답 데이터를 label이라고 합니다.
label = 'Species'
print(df[label].unique())
# 결과를 보면 3가지 품종이 있습니다.
# 따라서, 이 데이터는 SoftMax로 풀어야 됩니다.

# 3가지 데이터의 분포를 보기 위하여 pariplot 그래프를 그려 봅니다.
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

sns.pairplot(df, hue=label)

dataOut = './../dataOut/'
filename = dataOut + 'iris_softmax_01.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

# 머신 러닝에 활용하기 위하여 dataframe을 넘파이 배열로 변환합니다.
data = df.values

# 학습을 위한 기초 변수들을 정의합니다.
table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]
y = y.ravel()  # 1차원으로 flatten

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

encoder.fit(y)
y = encoder.transform(y)

x = x.astype(float)
y = y.astype(float)

# 훈련용 데이터와 테스트용 데이터를 70대 30으로 분리
SEED = 1234
TEST_SIZE = 0.3

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=TEST_SIZE, random_state=SEED)

print('before one hot encoding')
print(y_train)

nb_classes = len(df[label].unique()) # 정답(라벨)의 unique한 개수

# to_categorical 함수는 정수 형태의 벡터를 이전 형태의 행렬으로 변경해주는 함수입니다.
# 다중 분류에서 사용됩니다.
from keras.utils import to_categorical
y_train = to_categorical(y_train, num_classes=nb_classes)

print('\nafter one hot encoding')
print(y_train)

# 모델을 생성하고, 훈련용 데이터를 학습시킵니다.
model = Sequential()

# 입력 : 4개(x_column), 출력 : class 개수(nb_classes), 활성화 함수 : 소프트 맥스
model.add(Dense(units=nb_classes, input_shape=(x_column,), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit_hist : fitting history 정보를 저장하고 있는 객체
# validation_split 매개 변수 :
#     train 데이터 셋에서 일부를 떼어 내어, 학습을 잘 하고 있는 지 검증하기 위한 데이터의 비율

EPOCH = 1000
fit_hist = model.fit(x_train, y_train, epochs=EPOCH, validation_split=0.3)

from Utility.keras_graph_util import graph_loss_validation
graph_loss_validation(fit_hist, 'iris_softmax_validation_loss')

from Utility.keras_graph_util import graph_accuracy_validation
graph_accuracy_validation(fit_hist, 'iris_softmax_validation_accuracy')

import numpy as np

csv_data_list = []  # csv 파일로 저장할 리스트
hit = 0.0  # 데이터를 맞춘 개수

for idx in range(len(x_test)): # 테스트 데이터 각각에 대하여
    # idx 번째 테스트 데이터를 이용하여 예측을 해봅니다.
    H = model.predict(np.array([x_test[idx]]), verbose=0)
    print(H)  # H는 각 class가 가지고 있는 확률 정보를 출력해 줍니다.
    # 예시) [[0.94862247 0.0500623  0.00131516]]

    # argmax : 배열 요소 값(확률)이 가장 큰 요소의 색인 번호를 반환합니다.
    prediction = np.argmax(H, axis=-1)
    print('\n예측 값 : ', prediction, end=' ')
    print(', 정답 : [%d]' % int(y_test[idx]))

    # 엑셀 파일에 저장할 1건의 데이터
    sublist = []  # (예측 값, 정답, 확률01, 확률02, 확률03)

    sublist.append(prediction[0])
    sublist.append(int(y_test[idx]))

    _H = H.flatten()  # 1차원화
    for cnt in range(len(_H)):
        sublist.append(_H[cnt])

    csv_data_list.append(sublist)

    # 정확히 맞추면 1.0이 됩니다.
    hit += float(prediction[0] == int(y_test[idx]))

    # if idx == 2:
    #     break
# end for

hitrate = 100 * hit / len(x_test) # 정확도
print(f'\n정확도 : {hitrate:.4f}')

# csv 파일로 저장합니다.
mycolumns = ['예측 값', '정답', '확률01', '확률02', '확률03']
df = pd.DataFrame(csv_data_list, columns=mycolumns)
csv_filename = dataOut + 'iris_softmax.csv'
df.to_csv(csv_filename, index=False, encoding='UTF-8')
print(csv_filename + ' 파일이 저장되었습니다.')

'''
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=1234)

test_size=0.3에 의하여 다음과 같이 데이터가 분리 됩니다.

전체 데이터  : 100행 5열
train data : 70행 5열
test data : 30행 5열

EPOCH = 1000
fit_hist = model.fit(x_train, y_train, epochs=1000, validation_split=0.3)

validation_split=0.3에 의하여 train data는 다음과 같이 분리 됩니다.

train data : 70*0.7 행 5열 --> 49행 5열
validation data : 70*0.3 행 5열 --> 21행 5열

validation data를 통해 과적합 방지와 모델의 성능 향상을 위하여 사용할 수 있습니다.
'''