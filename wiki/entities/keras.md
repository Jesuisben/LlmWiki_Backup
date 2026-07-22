---
title: Keras
created: 2026-07-22
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistInfo.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNet.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/cnnPreTest.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/pretrainedModel.py
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721121821.png
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv
status: growing
confidence: high
---

# Keras

## 무엇인가

Keras는 neural network의 layer·model·loss·optimizer·metric·dataset utility를 고수준 API로 조립하는 deep learning framework API다. 이 위키에서는 `Sequential`에 Dense·Conv2D·Pooling·Dropout layer를 순서대로 추가하고 MNIST 분류 구조를 만드는 도구로 처음 등장했다.

## 이 위키에서의 맥락

scikit-learn이 split·전처리·전통 ML estimator·metric의 공통 API를 제공했다면, Keras는 layer topology와 gradient 기반 학습 설정을 직접 구성하는 역할로 2026-07-10부터 사용됐다. 원문은 Keras와 TensorFlow의 내부 관계를 독립 학습 주제로 충분히 구분하지 않으므로 TensorFlow Entity를 별도로 만들지 않는다.

## 첫 등장과 날짜별 학습 이력

### 2026-07-10 — MNIST Dense network

- `keras.datasets.mnist.load_data()`로 image·label 입력 code 작성
- `to_categorical()`로 10-class one-hot target 구성
- `Sequential`과 `Dense`로 0~2개 hidden layer 비교
- ReLU·softmax, categorical cross-entropy, RMSprop·Adam 사용
- `fit` history, `evaluate` test score, CSV·history graph 저장 시도

### 2026-07-13 — CNN과 Dropout

- `Conv2D`, `MaxPooling2D`/`MaxPool2D`, `Flatten`으로 image feature extractor 구성
- Dense sigmoid binary output topology와 MNIST softmax multiclass topology 작성
- Dense 사이에 `Dropout(0.3)`을 넣는 비교 code 작성
- training에서만 Dropout을 활성화하고 inference에는 비활성화하는 책임 학습

### 2026-07-16 — VGG16 pretrained inference

- application의 VGG16 사전 학습 model load
- image 224×224 resize·batch array·전용 preprocessing
- `predict`와 `decode_predictions`로 ImageNet class 해석
- probability graph·prediction CSV 저장 code

이날은 현재 image로 VGG16을 `fit`한 것이 아니라 기존 weight를 이용한 inference다. graph 4개는 남았지만 weight file과 prediction CSV는 없다.

### 2026-07-21 — sonar 10-fold neural evaluation

- 60-feature sonar 입력에 Dense 24·10 hidden unit과 sigmoid output을 구성했다.
- 각 stratified fold 안에서 `Sequential`을 새로 만들고 compile→fit→evaluate를 반복했다.
- fold별 binary cross-entropy loss·accuracy와 평균을 계산하고 graph 4개를 저장하도록 작성했다.
- 첨부 topology의 입력 2개와 생략 node는 실제 60-24-10-1 구조를 설명하는 축약도다.

날짜 code는 public `tensorflow.keras` import를 사용하지만 TensorFlow 자체 runtime·device·low-level API를 독립 주제로 학습한 근거는 없다. 따라서 TensorFlow Entity를 별도로 만들지 않고 Keras의 cross-validation 적용 이력으로 누적한다. 독립 `sonarTestKFold.py`는 다른 surgery dataset과 internal import를 사용하므로 같은 실행 version으로 간주하지 않는다.

## 핵심 기능 / 특징

| API | 책임 | 수업 사례 |
|---|---|---|
| `Sequential` | 단일 입력·출력의 순차 layer stack | Dense MNIST, CNN topology |
| `Dense` | 완전 연결 layer | ReLU hidden, softmax/sigmoid output |
| `Conv2D` | 2D convolution feature map 생성 | image filter 32·64·128개 |
| `MaxPooling2D` | feature map downsampling | 2×2 max pooling |
| `Flatten` | 공간 feature map을 1D로 변환 | Dense classifier 연결 |
| `Dropout` | training 중 unit 무작위 제외 | rate 0.3 과적합 완화 |
| `compile` | loss·optimizer·metric 설정 | categorical cross-entropy·Adam/RMSprop |
| `fit` | batch·epoch 단위 parameter 학습 | validation split 0.3 |
| `evaluate` | test loss·metric 계산 | score의 loss·accuracy 접근 |

## framework 책임과 실행 환경 구분

- Keras는 model과 layer·학습 API를 제공한다.
- [[entities/python|Python]]은 이를 조립하는 언어다.
- [[entities/pandas|Pandas]]는 score CSV와 표 데이터를 다룬다.
- [[entities/matplotlib|matplotlib]]은 history·metric graph를 그린다.
- [[entities/jupyter-notebook|Jupyter Notebook]]이나 IDE는 code 실행·기록 환경이며 Keras layer 기능이 아니다.
- import가 있다는 사실만으로 Keras/TensorFlow dependency 설치나 hardware 가속, MNIST download 성공을 증명하지 않는다.

## model lifecycle과 artifact 경계

1. `Sequential`·`add`: topology 정의
2. `compile`: 학습 설정 연결
3. `fit`: parameter 학습 시도와 History 반환
4. `evaluate`·`predict`: 고정 parameter로 평가·예측
5. `to_csv`·`savefig`: metric·graph 저장 시도
6. model/weight save: 재사용 가능한 model artifact

07-10~13 source에는 1~5단계 code가 있지만 실제 history 값·test score·CSV·PNG·model file은 보존되지 않았다. 특히 `cnnPreTest.py`는 1단계 topology와 model 정보 출력만 있고 compile·fit이 없다. 07-16의 VGG16 probability graph 4개는 별도 inference artifact이며, 이를 Dense/CNN 학습 history나 저장 model로 해석하지 않는다.

## 정확히 구분할 점

- `compile()`은 일반적인 의미의 standalone binary file을 만드는 단계가 아니다.
- one-hot은 categorical cross-entropy 조합에서 사용하지만 multiclass 문제의 유일한 label 표현은 아니다.
- Dropout은 inference 시 framework가 자동으로 비활성화한다. test를 위해 rate를 1로 변경하지 않는다.
- Keras code가 TensorFlow backend 위에서 실행될 수 있다는 일반 사실과, 이번 날짜 원문이 TensorFlow 자체 API·runtime을 독립적으로 학습했다는 주장은 다르다.

## 관련 개념

- [[concepts/neural-network-training-basics|신경망 학습 기초]]
- [[concepts/cnn-convolution-pooling-dropout|CNN과 convolution·pooling·Dropout]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]
- [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]]
- [[entities/vgg16|VGG16]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]
- [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]]

## 프로젝트/면접에서 설명할 관점

“Keras는 layer topology와 loss·optimizer·metric을 고수준 API로 구성하고 fit/evaluate/predict를 제공한다. 하지만 API 호출과 실제 history·metric·saved model artifact는 서로 다른 증거다. 수업에서는 Dense MNIST→CNN·Dropout→VGG16 inference→fold별 신경망 평가로 확장했다”고 설명할 수 있다.

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistInfo.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNet.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/cnnPreTest.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/pretrainedModel.py`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721121821.png`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv`
