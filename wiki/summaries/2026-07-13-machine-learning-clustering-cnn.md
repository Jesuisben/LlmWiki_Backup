---
title: 2026-07-13 군집과 CNN
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum, study-log]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_example.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/mdsAndDendrogram.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_clustering.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/cnnPreTest.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/Wholesale customers data.csv
status: growing
confidence: high
---

# 2026-07-13 군집과 CNN

## 한 줄 요약

정답 label 없이 거리로 데이터를 묶는 hierarchical clustering·MDS·KMeans를 배운 뒤, image의 공간적 특징을 convolution·pooling으로 추출하고 Dropout으로 과적합을 줄이는 CNN 구조로 확장했다.

## 전체 교시·학습 순서

| 교시 | 학습 흐름 | 역할 |
|---|---|---|
| 1교시 | 군집·비지도 학습 → Euclidean distance·cosine similarity → linkage | label 없이 “비슷함”을 정의하고 계층적으로 묶는 기준을 세웠다. |
| 2교시 | KMeans 중심 이동 → `pdist` → 음식 거리·dendrogram·MDS → 도매 고객 KMeans | 작은 좌표 예시에서 실제 다변량 고객 데이터까지 군집을 적용했다. |
| 3교시 | CNN → convolution/filter/feature map → stride/padding/pooling → CNN 구조 code | Dense network가 버리던 이미지의 2차원 공간 구조를 활용했다. |
| 4교시 | “이어서 작성” | 독립 학습 내용·실행 결과가 기록되지 않았다. |
| 5교시 | Dropout 개념·필요성·train/inference 구분 | CNN/Dense network의 과적합 완화 방법을 추가했다. |
| 6교시 | MNIST CNN과 CNN+Dropout menu 비교 code | 같은 입력·loss·optimizer에서 Dropout 유무를 비교하도록 작성했다. |
| 7교시 | “이어서 작성” | 추가 근거가 없다. |
| 8교시 | 자습 | 별도 output·artifact가 없다. |

## 왜 이 흐름으로 배웠는가

ML-1과 07-10은 정답 label이 있는 지도 학습이었다. 이날 먼저 [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리]]를 통해 label이 없을 때 구조를 찾는 방법을 배웠다. 이후 07-10의 Dense MNIST 분류를 이어받아, pixel을 단순 784열로 펼치지 않고 이웃 pixel의 패턴을 filter로 찾는 [[concepts/cnn-convolution-pooling-dropout|CNN]]으로 확장했다.

## 대표 입력 → 처리 → 결과

### 좌표 10개 → KMeans 2개 cluster

- **입력:** 2차원 점 10개와 초기 중심 2개
- **처리:** `KMeans(n_clusters=2, init=initial_centers, n_init=1)`를 fit해 중심을 갱신하고 각 점에 cluster ID를 붙인다.
- **결과 코드:** 초기/갱신 중심, cluster별 점, 중심 이동 화살표와 graph 저장 호출이 있다.

### 음식 속성 → 거리 → dendrogram·MDS

1. 다섯 음식의 달달함·목넘김·고소함·기름짐·매콤함을 feature matrix로 만든다.
2. `pdist(..., metric='euclidean')`로 쌍별 거리를 계산한다.
3. single linkage로 가까운 cluster를 합쳐 dendrogram을 만든다.
4. 같은 distance matrix를 MDS로 2차원에 배치해 관계를 시각화한다.

### 도매 고객 구매액 → KMeans 5개 cluster

- **입력:** 물리 CSV 440행·8열, 결측 0. `Channel`·`Region`을 제외한 6개 연간 구매액이 feature다.
- **처리:** 전체 feature를 StandardScaler로 표준화하고 KMeans 5개 cluster를 fit한다.
- **결과 코드:** cluster ID를 DataFrame에 붙여 평균·개수·최댓값 cluster를 요약하고 두 쌍의 산점도를 저장하도록 작성했다.
- **정답 구조:** `Cluster`는 원래 CSV에 있는 정답 label이 아니라 algorithm이 만든 group ID다.

### MNIST image → CNN class

- **입력:** 28×28 grayscale image에 channel 차원 1을 붙이고 0~1로 정규화한다. label은 10-class one-hot vector다.
- **처리:** Conv2D→MaxPool을 세 번 반복해 feature map을 줄이고, Flatten→Dense→softmax로 분류한다.
- **비교:** menu 6은 Dense 두 층, menu 7은 각 Dense 뒤 Dropout 0.3을 추가한다.
- **학습·평가 코드:** categorical cross-entropy, Adam, accuracy, validation split, test evaluate, CSV·history graph 저장 호출이 있다.

## code·output·metric·history·model·graph·artifact 경계

| 증거 | 확인된 범위 | 확인되지 않은 범위 |
|---|---|---|
| 날짜 MD·독립 `.py` 4개·embedded `abcd.py` code | 군집·MDS·KMeans·CNN layer 구성과 save 호출이 작성되고 독립 source는 AST parse 가능 | dependency·dataset read·fit·evaluate 전체 runtime 성공 |
| 도매 고객 CSV | 440행·8열, 행 폭 일정, 결측 0 | 수업 code가 모든 행을 끝까지 처리했는지 |
| embedded 표·이론 block | 교육용 입력·설명·도식이 보존됨 | Python stdout 또는 model 결과라는 단정 |
| `kmeans.labels_`·cluster center 접근 | fitted KMeans 결과를 읽을 code가 존재 | 실제 출력 cluster 번호·중심 좌표 |
| `fit_hist.history`·`evaluate` | history와 test metric을 계산할 code가 존재 | 실제 loss·accuracy와 Dropout 개선 효과 |
| `savefig`·`to_csv` | graph·CSV 저장 의도가 존재 | 교육자료 `dataOut`이 비어 있어 물리 artifact 부재 |
| CNN model construction | layer topology가 작성됨 | 직렬화된 model file·재현 가능한 trained weight |

## 실제 오류·불일치·미확정 실행

- 원문이 “Euclidean distance”라고 제시한 음식 거리 표의 3·4·12·28 등은 실제 Euclidean distance가 아니라 **거리 제곱값**과 대응한다. 독립 source도 원래 distance matrix를 출력한 뒤 `distance ** 2`를 별도로 계산한다.
- 계층 군집 source는 `linkage(distance, method='single')`을 사용한다. 이때 입력이 관측 행렬인지 condensed distance vector인지 구분해야 하며, 이 source는 `pdist`의 condensed vector를 전달한다.
- KMeans cluster 번호 0~4는 class 의미가 고정된 정답이 아니다. 평균 구매액 등으로 사후 해석해야 한다.
- `kmeans_clustering.py`의 초기 출력 경로는 `dataout`, 후반 저장 경로는 `dataOut`으로 표기가 다르다. 물리 graph가 없으므로 저장 성공은 미확정이다.
- CNN 이론 중 Max Pooling 설명 일부가 원문에서 `python` fence로 감싸져 있지만 실행 가능한 Python code가 아니라 설명문이다. 이 위키에서는 prose로만 정리했다.
- `cnnPreTest.py`는 layer를 구성하고 model 정보를 출력하지만 compile·fit·evaluate·save를 하지 않는다. 이를 trained CNN으로 부르면 안 된다.
- 날짜의 Dropout 표가 “test 시 반드시 1의 값을 준다”고 설명하지만, 일반적인 Keras Dropout은 inference/evaluation에서 framework가 자동으로 비활성화한다. rate를 1로 바꿔 test하는 절차가 아니다.
- 6교시의 `abcd.py` code는 날짜 MD에 embedded되어 있으나 같은 이름의 독립 교육 source와 저장 artifact는 확인되지 않았다.

## 헷갈린 점과 정확한 구분 기준

- **classification vs clustering:** classification은 정답 class를 배우고, clustering은 feature만으로 group을 만든다.
- **distance vs similarity:** Euclidean은 가까울수록 작은 거리, cosine similarity는 방향이 같을수록 1에 가깝다. scale과 목적에 따라 선택한다.
- **hierarchical vs KMeans:** hierarchical은 합쳐지는 tree를 만들고, KMeans는 미리 정한 K개의 중심을 반복 갱신한다.
- **MDS vs clustering:** MDS는 거리 관계를 저차원에 표현하는 embedding이며 그 자체가 cluster 정답을 만드는 절차는 아니다.
- **padding vs pooling:** padding은 convolution 전 경계에 값을 덧붙여 출력 크기·경계 정보를 조절하고, pooling은 feature map을 요약해 공간 크기를 줄인다.
- **Dropout과 성능:** 과적합 완화를 기대하는 기법이지, 한 번 넣으면 test accuracy가 반드시 높아진다는 보장은 없다.
- **Dense vs CNN:** Dense는 모든 입력과 연결되고, CNN은 작은 filter의 weight를 공간 전체에 공유해 지역 패턴을 찾는다.

## 이전·다음 학습 연결

- 이전: [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]에서 logistic regression·Dense network의 지도 분류와 학습 lifecycle을 다뤘다.
- 다음: [[summaries/2026-07-14-machine-learning-nlp-vectorization|07-14 NLP 표현]]에서 [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|07-16 Bayesian filter·사전 학습 model]]까지 text 표현과 image 추론으로 이어진다.

## 관련 페이지

- [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리·hierarchical clustering·KMeans]]
- [[concepts/cnn-convolution-pooling-dropout|CNN과 convolution·pooling·Dropout]]
- [[concepts/neural-network-training-basics|신경망 학습 기초]]
- [[entities/scikit-learn|scikit-learn]]
- [[entities/keras|Keras]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_example.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/mdsAndDendrogram.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_clustering.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/cnnPreTest.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/Wholesale customers data.csv`
