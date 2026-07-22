---
title: CNN과 convolution·pooling·Dropout
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/cnnPreTest.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
status: growing
confidence: high
---

# CNN과 convolution·pooling·Dropout

## 정의

CNN(Convolutional Neural Network)은 작은 filter를 image의 공간 전체에 공유하며 지역 패턴을 찾는 신경망이다. convolution이 feature map을 만들고, pooling이 공간 크기를 줄이며, Flatten·Dense가 추출된 특징으로 class를 결정한다. Dropout은 학습 중 일부 unit을 무작위로 제외해 과적합을 완화하는 regularization 기법이다.

## 왜 중요한가

07-10 Dense MNIST는 28×28 image를 784열로 펼쳐 pixel의 이웃 관계를 명시적으로 보존하지 않았다. CNN은 filter가 가까운 pixel 묶음을 보며 edge·texture 같은 지역 특징을 찾고, 같은 weight를 여러 위치에 공유해 image 구조를 효율적으로 이용한다.

## convolution의 핵심 요소

| 요소 | 책임 | 출력에 미치는 영향 |
|---|---|---|
| filter/kernel | 작은 weight 행렬로 지역 패턴 탐지 | filter 수만큼 feature map channel 생성 |
| stride | filter가 이동하는 간격 | 클수록 공간 크기가 빠르게 감소 |
| padding | 입력 경계에 값을 추가 | `same`은 크기 보존을 돕고 `valid`는 추가 padding 없음 |
| activation | convolution 결과에 비선형성 추가 | 수업에서는 ReLU 사용 |
| feature map | 한 filter를 전체 위치에 적용한 결과 | 특정 패턴이 나타난 위치·강도를 표현 |

kernel은 이동하면서 같은 weight를 공유한다. 이것이 모든 pixel을 독립 weight로 연결하는 Dense layer와의 핵심 차이다.

## pooling

Max pooling은 작은 영역의 최댓값을 남겨 feature map의 폭·높이를 줄인다. 계산량과 parameter 이후 입력 크기를 줄이고 작은 위치 변화에 덜 민감하게 만들 수 있지만, 세부 위치 정보도 잃는다.

**padding과 pooling은 같은 축이 아니다.** padding은 convolution 전에 경계와 출력 크기를 조절하고, pooling은 만들어진 feature map을 요약해 downsampling한다.

## 수업 topology

`cnnPreTest.py`는 150×150 RGB image를 대상으로 다음 구조를 작성한다.

- Conv2D 32 → MaxPooling
- Conv2D 64 → MaxPooling
- Conv2D 128 → MaxPooling
- Conv2D 128 → MaxPooling
- Flatten → Dense 512 → sigmoid output 1

이 source는 model 구조와 정보를 출력하지만 compile·fit·evaluate는 없다. 따라서 “고양이/강아지 binary CNN topology를 작성했다”까지가 증거이고 trained model은 아니다.

날짜 MD의 MNIST 비교 code는 Conv2D·MaxPool을 세 번 거쳐 Flatten·Dense·softmax로 10개 숫자를 분류하도록 작성한다. menu 6은 Dense 두 층, menu 7은 각 Dense 뒤 Dropout 0.3을 추가한다.

## Dropout

- training batch마다 지정 비율의 unit 출력을 무작위로 0으로 만든다.
- 특정 unit 조합에 과도하게 의존하는 것을 줄여 일반화를 돕는다.
- evaluation·inference에서는 framework가 자동으로 비활성화하고 전체 network를 사용한다.
- rate 0.3은 30%를 제외한다는 뜻이다. “유지 비율 30%”와 혼동하지 않는다.

원문 표의 “test 시 반드시 1의 값을 준다”는 설명은 일반적인 Keras 사용법이 아니다. Dropout layer의 training/inference 동작은 framework가 관리하며 test를 위해 rate를 1로 바꾸지 않는다.

## Dense network vs CNN

이 비교는 별도 Comparison 대신 이 Concept에 흡수한다.

| 항목 | Dense | CNN |
|---|---|---|
| 연결 | 모든 입력과 unit 연결 | 작은 지역 filter 연결 |
| 공간 구조 | flatten하면 직접 보존되지 않음 | width·height·channel 구조 활용 |
| weight | 위치마다 별도 연결 weight | filter weight를 위치 간 공유 |
| 주 역할 | 일반 vector·최종 분류 | image feature 추출 |
| 함께 사용 | 단독 가능 | convolution 뒤 Flatten/Dense를 자주 사용 |

CNN도 마지막 분류에서 Dense layer를 사용할 수 있으므로 둘은 완전한 대체 관계가 아니다.

## overfitting·metric·artifact 경계

Dropout을 추가하는 목적은 train data 암기를 줄이는 것이지만 개선 여부는 train/validation curve와 독립 test metric으로 확인해야 한다. ML-2에는 `fit`, `evaluate`, history graph·CSV 저장 호출이 있지만 실제 history 값, score, PNG·CSV, 직렬화 model file은 없다. 따라서 Dropout이 실제 성능을 높였다고 쓰지 않는다.

## 2026-07-16 사전 학습 CNN으로의 연결

07-13에는 CNN topology를 직접 정의했지만 trained weight는 없었다. 07-16에는 ImageNet에서 이미 학습된 VGG16을 load해 image preprocessing과 prediction을 수행하도록 작성했다. 직접 topology 작성·from-scratch training과 pretrained inference는 model lifecycle이 다르며, 자세한 구분은 [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]]이 담당한다.

## 이론 설명과 code 경계

날짜 MD의 CNN 정의·padding·pooling·Dropout 문단과 표는 이론 설명이다. 일부가 `python` fence로 감싸져 있어도 실행 가능한 구문이 아니다. 반대로 `Conv2D`, `MaxPooling2D`, `Flatten`, `Dense`, `Dropout` 호출은 실제 Python source다. 이 페이지는 합성 fence 없이 prose·표·inline code로만 정리했다.

## 자주 헷갈리는 점

- **filter와 feature map:** filter는 학습되는 weight, feature map은 filter를 입력에 적용한 결과다.
- **kernel과 pooling window:** 둘 다 작은 창처럼 보이지만 kernel은 학습 weight로 특징을 계산하고 pooling은 영역을 요약한다.
- **same padding:** stride가 1일 때 공간 크기 보존에 주로 쓰지만 모든 stride에서 무조건 입력과 동일 크기라는 단순화는 피한다.
- **sigmoid와 softmax:** binary output 하나에는 sigmoid, 상호 배타적 다중 class에는 softmax가 일반적이다.
- **one-hot 필수 여부:** categorical loss와는 맞지만 sparse categorical loss는 정수 label을 받을 수 있다.
- **Dropout과 test:** test 때 layer rate를 직접 1로 설정하지 않는다.

## 선행·후속 연결

- 신경망 골격: [[concepts/neural-network-training-basics|신경망 학습 기초]]
- 수업: [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]
- framework: [[entities/keras|Keras]]
- 일반화: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 후속 model: [[entities/vgg16|VGG16]]
- 후속: 07-21 cross-validation 신경망으로 확장된다.

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/cnnPreTest.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
