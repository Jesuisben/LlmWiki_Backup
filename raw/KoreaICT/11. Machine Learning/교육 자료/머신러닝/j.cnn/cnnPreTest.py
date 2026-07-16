from keras import Sequential  # Keras에서 순차적으로 레이어를 쌓는 모델을 가져옴
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten  # 필요한 레이어들 가져오기 (밀집 레이어, 2D 합성곱, 풀링, 평탄화)

# 입력되는 이미지
# channel : 흑백 이미지는 1, 컬러 이미지는 3
image_size = (150, 150, 3) # width, height, channel

# 머신 러닝 모델 객체 생성: Sequential()은 순차적으로 레이어를 쌓는 방법을 제공
model = Sequential()

# 첫 번째 Conv2D 레이어 (합성곱 레이어):
# 3행 3열짜리 필터 32개를 사용하여 입력 이미지 image_size에 대한 컨블루션 연산을 수행합니다.
# 활성화 함수는 relu 함수를 사용하도록 하겠습니다.
# - filters=32: 32개의 필터(특징 추출기)를 사용하여 입력 이미지를 분석
# - kernel_size=(3, 3): 3x3 크기의 필터(커널)를 사용
# - activation='relu': 활성화 함수로 ReLU(Rectified Linear Unit)를 사용하여 비선형성을 추가
# - input_shape=(150, 150, 3): 입력 이미지의 크기는 150x150 픽셀, 3채널(컬러 이미지)
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=image_size))

# MaxPooling 레이어:
# - pool_size=(2, 2): 2x2 크기의 필터를 사용하여 입력의 크기를 절반으로 줄이는 풀링(최대값 추출) 작업
model.add(MaxPooling2D(pool_size=(2, 2)))

# 두 번째 Conv2D 레이어:
# - filters=64: 64개의 필터를 사용하여 더 복잡한 특징을 추출
# - kernel_size=(3, 3): 3x3 크기의 필터
# - activation='relu': 활성화 함수로 ReLU 사용
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))

# 두 번째 MaxPooling 레이어:
# - pool_size=(2, 2): 2x2 크기의 필터를 사용하여 입력의 크기를 절반으로 줄임
model.add(MaxPooling2D(pool_size=(2, 2)))

# 세 번째 Conv2D 레이어:
# - filters=128: 128개의 필터를 사용하여 더 복잡한 특징을 추출
# - kernel_size=(3, 3): 3x3 크기의 필터
# - activation='relu': 활성화 함수로 ReLU 사용
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))

# 세 번째 MaxPooling 레이어:
# - pool_size=(2, 2): 2x2 크기의 필터로 입력의 크기를 절반으로 줄임
model.add(MaxPooling2D(pool_size=(2, 2)))

# 네 번째 Conv2D 레이어:
# - filters=128: 128개의 필터를 사용하여 더 복잡한 특징을 추출
# - kernel_size=(3, 3): 3x3 크기의 필터
# - activation='relu': 활성화 함수로 ReLU 사용
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))

# 네 번째 MaxPooling 레이어:
# - pool_size=(2, 2): 2x2 크기의 필터로 입력의 크기를 절반으로 줄임
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten 레이어:
# 컨블루션 연산 결과를 1차원 형태의 배열로 만들어, 완전 연결(Dense) 레이어에 전달합니다.
model.add(Flatten())

# 완전 연결(Dense) 레이어:
# - units=512: 512개의 뉴런을 가진 밀집 레이어
# - activation='relu': 활성화 함수로 ReLU 사용
model.add(Dense(units=512, activation='relu'))


# 출력층(Output Layer)
# - units=1: 출력 뉴런의 수는 1 (이항 분류에서 사용할 것임)
# - activation='sigmoid': 활성화 함수로 sigmoid를 사용하여 출력값을 0과 1 사이로 제한 (이항 분류에 적합)
# 우리는 이항 분류(강아지/고양이)를 할 예정이므로, activation 함수는 반드시 sigmoid 함수를 사용해야 합니다.
# 주의) 다항 분류인 경우에는 반드시 one hot encoding을 수행해야 합니다.
y_column = 1
model.add(Dense(units=y_column, activation='sigmoid'))

# 모델의 구조를 출력해주는 함수로, 레이어의 상세 정보를 확인할 수 있음
#model.summary()
from Utility.keras_graph_util import model_information
model_information(model)
