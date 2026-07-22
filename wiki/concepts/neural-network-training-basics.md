---
title: 신경망 학습 기초
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistInfo.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNet.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721121821.png
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv
status: growing
confidence: high
---

# 신경망 학습 기초

## 정의

신경망(neural network)은 입력에 weight와 bias를 적용하고 activation function으로 비선형 변환하는 layer를 쌓아, loss를 줄이는 방향으로 parameter를 학습하는 model이다. 2026-07-10 수업은 MNIST Dense network를 통해 **model 구성 → compile → fit → history → evaluate → artifact 저장 시도**를 처음 연결했다.

## 왜 중요한가

scikit-learn estimator도 `fit`·`predict`를 사용하지만, 신경망에서는 layer 구조, activation, loss, optimizer, epoch, batch와 validation을 함께 설계해야 한다. 이 기초가 07-13 CNN과 이후 사전 학습 model을 이해하는 공통 골격이다.

## MNIST 입력과 label

- image: 28×28 grayscale pixel
- train/test: 노트의 embedded 구조 기준 60,000개/10,000개
- Dense 입력: 각 image를 784열 vector로 reshape하고 255로 나눠 0~1 정규화
- 원래 label: 0~9 정수
- categorical target: 10개 class one-hot vector

`mnist.load_data()`는 code에 있지만 현재 세션에서 download·load를 실행하지 않았다. embedded shape와 sample label은 수업 기록이며 재현 실행 결과와 구분한다.

## layer·activation의 책임

| 요소 | 수업에서의 역할 | 흔한 오해 |
|---|---|---|
| Dense | 이전 layer의 모든 unit과 연결 | layer를 많이 쌓으면 항상 성능이 좋아지는 것은 아님 |
| ReLU | hidden layer에 비선형성 추가 | optimizer나 loss를 대신하지 않음 |
| softmax | 10개 class score를 합 1의 분포로 변환 | 확률이 높다고 calibration·정답이 보장되지는 않음 |
| sigmoid | 주로 binary output을 0~1로 변환 | multiclass softmax와 역할이 다름 |
| one-hot | categorical cross-entropy가 비교할 target 표현 | sparse categorical loss를 쓰면 정수 label도 가능 |

activation이 모두 선형이면 여러 Dense layer도 전체적으로 하나의 선형 변환으로 합쳐질 수 있다. ReLU 같은 비선형 activation이 복잡한 결정 경계를 표현하게 한다.

## loss·gradient descent·optimizer

1. forward pass로 prediction을 계산한다.
2. loss function이 prediction과 target의 차이를 하나의 scalar로 측정한다.
3. backpropagation이 각 parameter에 대한 gradient를 계산한다.
4. optimizer가 gradient를 이용해 weight와 bias를 갱신한다.
5. epoch 동안 batch 단위로 반복한다.

Gradient descent는 loss를 줄이는 방향을 제공하고, Adam·RMSprop 같은 optimizer는 learning rate·momentum·적응적 scale 등의 갱신 규칙을 구현한다. optimizer 변경은 model topology 변경과 다른 축이다.

## compile·fit·evaluate

- `compile`: loss·optimizer·metric 등 학습 설정을 연결한다. 일반적인 의미의 독립 binary artifact 생성 단계가 아니다.
- `fit`: train data를 반복해 parameter를 갱신하고 validation이 있으면 epoch별 metric을 기록한다.
- `History`: train/validation loss·metric의 기록 객체다.
- `evaluate`: 고정된 parameter로 test data의 loss·metric을 계산한다.
- `predict`: 새 입력의 class probability·score를 계산한다.

이 흐름은 [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]의 신경망 확장이다.

## 수업 사례: menu 1~5

| menu | 구조 변화 | optimizer |
|---|---|---|
| 1 | output softmax만 사용 | RMSprop |
| 2 | menu 1과 같은 topology | Adam |
| 3 | ReLU Dense 512 한 층 추가 | RMSprop |
| 4 | ReLU Dense 512 두 층 | RMSprop |
| 5 | menu 4와 같은 topology | Adam |

이 비교는 layer 깊이와 optimizer를 분리해 보려는 설계다. 그러나 실제 CSV·history graph·test metric이 없으므로 어느 구성이 더 좋았다고 결론 내릴 수 없다.

## metric·history·artifact 증거 사다리

1. **model code:** topology와 학습 의도
2. **fit 호출:** 학습 시도 절차
3. **History/stdout:** 특정 실행의 epoch별 관찰
4. **evaluate score:** 특정 test 입력의 loss·metric
5. **CSV/PNG:** 저장된 평가·graph artifact
6. **직렬화 model/weights:** 재사용 가능한 parameter artifact
7. **재현·독립 평가:** 같은 pipeline의 반복 가능성과 일반화 확인

ML-2에는 1~2단계 code와 embedded 설명은 있지만, 교육자료 `dataOut`이 비어 있어 3~6단계의 물리 결과는 확인되지 않는다. `fit_hist.history`를 읽는 code만으로 history 값이 보존됐다고 쓰지 않는다.

## 2026-07-21 sonar 10-fold 평가

sonar 수업은 60개 수치 feature와 R/M binary label을 Dense 24 ReLU→Dense 10 ReLU→Dense 1 sigmoid topology에 넣었다. `StratifiedKFold(n_splits=10)`의 각 반복에서 model을 새로 만들고 200 epochs·batch 5로 fit한 뒤 test fold의 loss와 accuracy를 얻도록 작성했다.

첨부 topology는 입력 `i1`, `i2`, 두 hidden layer의 `h11 … h1n`, output `o1`과 ReLU·sigmoid를 그린 축약도다. 실제 source의 60-24-10-1 unit 수를 그대로 그린 것이 아니므로 node 수 불일치를 model 오류로 읽지 않는다.

- fold별 `evaluate` loss·accuracy: 서로 다른 train/test subset에서 학습한 서로 다른 model의 평가
- 평균 loss·accuracy: 10개 평가의 중심 요약
- History: `fit` 반환값을 변수에 저장하지 않아 epoch별 기록이 보존되지 않음
- model artifact: 매 fold 메모리 model code는 있으나 직렬화 file과 전체-data 최종 model은 없음
- graph artifact: 저장 code는 있으나 물리 PNG는 없음

독립 `sonarTestKFold.py`는 filename과 달리 470×18 `surgeryTest.csv`를 읽고 평균 출력에서 끝난다. 날짜 code의 208×61 sonar 입력·public Keras import·graph code와 같은 version의 실행 근거로 사용하지 않는다. fold 내부 preprocessing과 일반화 판단은 [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]가 소유한다.

## 실제 불일치와 주의점

- MNIST source 주석의 `744 = 28 * 28`은 오기이며 실제 입력 열 수는 784다.
- 학습 source의 결과 이름 `mnist_result_01.csv`와 graph source가 읽는 `mnistResult01.csv`가 일치하지 않는다. graph source가 앞 단계 artifact를 그대로 소비한다고 단정할 수 없다.
- train metric은 학습 데이터 적합도, validation metric은 학습 중 선택 신호, test metric은 마지막 일반화 평가다. 가장 높은 train accuracy를 최고의 model 근거로 삼으면 과적합을 놓친다.
- 고정 epoch 5는 수업 설정일 뿐 충분한 학습 또는 최적 epoch를 보장하지 않는다.

## 선행·후속 연결

- 선행: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]], [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- 첫 수업: [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- framework: [[entities/keras|Keras]]
- 후속: [[concepts/cnn-convolution-pooling-dropout|CNN과 convolution·pooling·Dropout]], [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]
- 교차 검증 확장: [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistInfo.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNet.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721121821.png`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv`
