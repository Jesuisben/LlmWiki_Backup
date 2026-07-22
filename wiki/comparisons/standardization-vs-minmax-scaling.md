---
title: 표준화 vs Min-Max scaling
created: 2026-07-22
updated: 2026-07-22
type: comparison
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
status: growing
confidence: high
---

# 표준화 vs Min-Max scaling

## 비교 목적

StandardScaler를 이용한 표준화(standardization)와 Min-Max scaling은 feature의 숫자 범위를 조정하지만 기준·결과·이상치 영향이 다르다. 07-09·13·20에는 StandardScaler가, 07-21에는 수동 Min-Max 식이 반복되어 **언제 무엇을 선택하고 어디에 fit해야 하는가**를 독립적으로 비교할 필요가 생겼다.

## 한눈에 보기

| 항목 | StandardScaler 표준화 | Min-Max scaling |
|---|---|---|
| 기준 | train 평균과 표준편차 | train 최솟값과 최댓값 |
| 대표 변환 | `(x - mean) / std` | `(x - min) / (max - min)` |
| 일반적인 결과 | 평균 0·표준편차 1에 가까운 scale | 지정 범위, 보통 0~1 |
| 값의 경계 | 고정된 상·하한 없음 | train 기준은 보통 0~1 |
| 이상치 영향 | 평균·표준편차가 흔들릴 수 있음 | min·max가 늘어나 나머지 값이 압축될 수 있음 |
| 새 test 값 | 0~1 밖으로 나갈 수 있음 | train min/max 밖이면 0 미만·1 초과 가능 |
| 수업 사례 | Titanic SVM/KNN/Tree, 도매 고객 KMeans, iris SVM | preference KNN |

둘 다 이상치를 제거하지 않는다. scaling 전에 이상치의 의미와 처리 정책을 별도로 판단해야 한다.

## 왜 scaling이 필요한가

KNN처럼 거리로 이웃을 찾거나 SVM처럼 feature 좌표에서 margin·kernel을 계산하는 모델은 숫자 범위가 큰 feature의 영향을 과도하게 받을 수 있다. KMeans도 중심과 거리를 사용하므로 feature scale 차이가 cluster를 바꿀 수 있다.

Decision Tree는 값의 순서와 threshold로 분할하므로 일반적으로 scaling이 필수는 아니다. 모든 model에 관성적으로 같은 scaler를 적용하기보다 알고리즘과 데이터 분포를 먼저 본다.

## 언제 무엇을 쓰는가

### StandardScaler가 자연스러운 경우

- feature를 평균 중심으로 맞추고 표준편차 단위로 비교하고 싶을 때
- SVM·logistic regression·신경망 등 중심화된 연속 feature를 사용하는 pipeline
- 값이 반드시 0~1 범위에 있어야 할 요구가 없을 때

분포가 정규분포여야만 사용할 수 있는 것은 아니지만, 심한 skew와 outlier가 있으면 평균·표준편차가 대표성을 잃을 수 있다.

### Min-Max scaling이 자연스러운 경우

- 입력 범위를 0~1처럼 해석하기 쉬운 범위로 맞추고 싶을 때
- KNN처럼 여러 feature의 거리 기여를 같은 범위에서 시작하고 싶을 때
- 원래 하한·상한이 의미 있고 큰 outlier가 적을 때

train 범위를 벗어난 새 값은 0~1 밖으로 나갈 수 있으며, min/max를 강제로 clipping할지는 별도 정책이다.

## 가장 중요한 공통 원칙: split 후 train에만 fit

1. 먼저 train/test 또는 현재 cross-validation fold를 나눈다.
2. train에서만 mean/std 또는 min/max를 계산한다.
3. train과 test를 같은 train 기준으로 transform한다.
4. test 통계를 다시 fit하거나 model 선택에 반복 사용하지 않는다.

07-09 Titanic source는 전체 feature에 StandardScaler를 fit한 뒤 split해 leakage가 있다. 07-20 iris source는 split 뒤 train에만 StandardScaler를 fit해 이 순서를 바로잡았다. 07-21 preference KNN은 전체 14행에서 min/max를 계산한 뒤 split하므로 Min-Max 방식 자체가 아니라 **fit 범위**에 leakage가 있다.

## 수업 사례 연결

### 07-09 StandardScaler

Titanic SVM·KNN과 유방암 Decision Tree source가 전체 `x`를 표준화한 뒤 split한다. SVM·KNN에는 scale 조정 필요성이 있지만 test 통계가 섞였고, Tree에는 scaling이 원리상 필수도 아니다.

### 07-13 KMeans

도매 고객의 서로 다른 구매액 feature를 StandardScaler로 맞춘 뒤 KMeans 5개 cluster를 학습하도록 작성했다. 금액 규모가 큰 열 하나가 거리를 지배하지 않게 하려는 목적이다. 다만 전체 데이터에서 탐색 군집을 수행한 사례와 지도 학습의 독립 test 평가는 목적이 다르다.

### 07-20 train-only StandardScaler

iris SVM은 8:2 split 뒤 train 평균·표준편차를 학습하고 같은 scaler로 test를 변환했다. 이 흐름이 holdout 평가의 기준선이다.

### 07-21 Min-Max KNN

preference feature 7개를 0~1로 맞춰 KNN 거리를 계산했다. 선택 자체는 이해하기 쉽지만 전체 데이터 min/max를 먼저 사용했으므로 올바른 구현은 split 뒤 train 기준으로 바꾸어야 한다.

## 헷갈리기 쉬운 포인트

- 수업 주석의 “정규화”는 StandardScaler와 Min-Max를 넓게 섞어 부르기도 한다. 정확한 transformer와 수식을 확인한다.
- StandardScaler가 이상치 영향을 줄이는 도구라는 설명은 부정확하다. 평균·표준편차를 사용하므로 이상치에 민감하다.
- Min-Max는 원래 분포의 순서를 유지하지만 outlier가 있으면 대부분의 값을 좁은 구간에 압축할 수 있다.
- scaling 성공과 model 성능 향상은 같은 증거가 아니다. validation/test metric으로 확인해야 한다.
- scaler 객체도 train data에서 parameter를 학습하는 fitted transformer이며 model과 함께 재사용되어야 한다.

## 관련 페이지

- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/svm-margin-kernel-classification|SVM의 margin과 kernel 분류]]
- [[concepts/knn-distance-voting|KNN의 distance와 voting]]
- [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리·KMeans]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]
- [[entities/scikit-learn|scikit-learn]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
