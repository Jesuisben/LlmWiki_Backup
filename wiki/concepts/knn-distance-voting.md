---
title: KNN의 distance와 voting
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721120235.png
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/likelyhood.csv
status: growing
confidence: high
---

# KNN의 distance와 voting

## 정의

K-Nearest Neighbors(KNN)는 새 데이터와 기존 train sample 사이의 거리를 계산하고, 가장 가까운 K개 이웃의 label을 투표해 class를 정하는 지도 학습 분류 알고리즘이다. 별도의 복잡한 parameter 함수를 미리 학습하기보다 train data 자체를 이웃 검색 기준으로 보존하는 instance-based 또는 lazy learning 방식이다.

## 왜 중요한가

KNN은 feature가 model 판단에 어떻게 직접 참여하는지 눈으로 이해하기 쉽다. 동시에 **거리의 기준, feature scale, K 선택, 데이터 밀도, 평가 분리**가 잘못되면 결과가 쉽게 달라지므로 전처리와 일반화 원칙을 함께 배우기 좋다. 07-09 Titanic에서 처음 적용한 뒤 07-21 preference dataset과 실제 vote 도식으로 반복되어 독립 검색 가치를 얻었다.

## 동작 원리

1. 새 query point를 입력한다.
2. query와 모든 train sample 사이의 distance를 계산한다.
3. distance가 작은 순서로 K개를 고른다.
4. 분류에서는 이웃 class의 다수결 vote를 계산한다.
5. 가장 많은 vote를 받은 class를 prediction으로 반환한다.

회귀형 KNN이라면 이웃 label의 평균·가중평균을 사용할 수 있지만, 수업의 Titanic·preference 사례는 classification이다.

## distance와 scaling

Euclidean distance는 보통 각 feature 차이의 제곱합에 제곱근을 취한다. 한 feature가 0~1, 다른 feature가 0~10,000 범위라면 큰 범위 feature가 거리를 거의 결정할 수 있다.

- StandardScaler: train 평균과 표준편차로 중심·scale을 맞춘다.
- Min-Max scaling: train의 최소·최대 기준으로 보통 0~1 범위에 맞춘다.
- 두 방법 모두 test 통계를 사용해 fit하면 leakage가 생긴다.
- scaling은 값의 단위를 맞추는 전처리이지 이상치 제거가 아니다.

두 방식의 분포·범위·이상치 영향과 선택 기준은 [[comparisons/standardization-vs-minmax-scaling|표준화 vs Min-Max scaling]]에서 비교한다.

07-21 preference code는 일곱 feature를 Min-Max 식으로 바꾸지만 전체 데이터에서 min/max를 계산한 뒤 split한다. 올바른 평가는 split 후 train 기준만 학습해 test에 적용하는 것이다.

## K가 바꾸는 판단 경계

| K | 장점 | 위험 |
|---:|---|---|
| 작음 | 국소적인 패턴에 민감 | noise·outlier에 흔들리고 과적합하기 쉬움 |
| 큼 | vote가 부드러워지고 분산이 줄 수 있음 | 다른 class 영역까지 섞여 과소적합할 수 있음 |

binary classification에서는 tie를 줄이려고 홀수 K를 자주 시도하지만 multiclass에서는 홀수여도 동률이 가능하다. 또한 K는 train sample 수보다 클 수 없다.

KNN의 K와 [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증]]의 K는 이름만 같고 책임이 다르다. 전자는 이웃 수, 후자는 평가용 데이터 분할 수다.

## 수업 사례: preference dataset

`likelyhood.csv`에는 muscle·height·grade·speech·book·travel·skin 일곱 수치 feature와 A/B/C label이 있는 14개 sample이 있다. 날짜 code는 다음 흐름을 작성했다.

1. 각 feature를 Min-Max scaling한다.
2. 80/20 holdout으로 train/test를 나눈다.
3. K=3 model을 학습·평가한다.
4. K=1,3,5,7,9의 test accuracy를 비교한다.
5. 가장 높은 accuracy의 K로 새 model을 만들고 confusion matrix를 계산한다.

작은 test set에서 고른 최고 K는 우연에 민감하다. 같은 test set으로 K를 선택하고 최종 점수도 보고하면 test가 validation 역할까지 겸한다. K 선택은 train 내부 validation 또는 cross-validation에서 하고, 독립 test는 마지막에 한 번 사용하는 편이 안전하다.

## 첨부 도식 읽기

`Pasted image 20260721120235.png`는 파란 구매자, 빨간 비구매자, 새 녹색 point를 그린다. 녹색과 빨간 두 반경 원은 포함되는 이웃 수가 달라지면 vote가 달라질 수 있음을 보여 준다. 이는 Step 1~5의 개념 설명이며 code의 실제 좌표·prediction·confusion matrix를 시각화한 artifact는 아니다.

## KNN과 SVM 구분

| 항목 | KNN | SVM |
|---|---|---|
| 핵심 판단 | query 주변 K개 이웃의 vote | class 사이 margin이 큰 decision boundary |
| 학습 시점 | train sample을 보존하는 비모수적 성격 | support vector와 boundary parameter를 결정 |
| 예측 비용 | train sample과 거리 계산 부담이 큼 | 학습된 boundary로 판단 |
| 공통 주의 | distance·margin이 feature scale에 영향 | distance·margin이 feature scale에 영향 |

둘 다 scaling이 중요할 수 있지만 같은 원리의 알고리즘은 아니다. 07-20 iris SVM과 07-21 preference KNN은 같은 split·preprocessing·평가 lifecycle 안에서 판단 방식만 다르다.

## metric·model·artifact 경계

- `KNeighborsClassifier.fit` code: train sample·label을 사용할 절차를 증명한다.
- `score`·confusion matrix 호출: 평가 의도를 증명한다.
- K별 accuracy list: 실행되었다면 한 split의 metric 모음이지 model artifact가 아니다.
- `savefig` 호출: graph 저장 의도이며 물리 PNG가 없으면 artifact 성공은 미확정이다.
- KNN 도식: 교육 개념도이며 prediction 실행 결과가 아니다.

## 자주 헷갈리는 점

- **가까움은 원래부터 정해지지 않는다.** feature 선택·scale·distance metric이 가까움의 의미를 만든다.
- **K가 크면 무조건 일반화가 좋아지지 않는다.** 너무 크면 국소 class 구조를 잃는다.
- **최고 test accuracy는 최적 K의 확정이 아니다.** 선택과 최종 평가 데이터를 분리해야 한다.
- **KNN은 clustering이 아니다.** train label을 사용해 새 class를 맞히므로 지도 학습 분류다.
- **도식의 원은 실제 decision boundary가 아니다.** 이웃 범위를 설명하는 개념적 반경이다.

## 선행·후속 연결

- 문제 유형: [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- 안전한 순서: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 첫 적용: [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 분류와 성능 평가]]
- 심화 적용: [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]]
- 평가 확장: [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]
- 도구: [[entities/scikit-learn|scikit-learn]]
- SVM 원리: [[concepts/svm-margin-kernel-classification|SVM의 margin과 kernel 분류]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721120235.png`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/likelyhood.csv`
