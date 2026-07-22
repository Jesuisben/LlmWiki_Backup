---
title: Machine Learning 학습 방식과 문제 유형
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf
status: growing
confidence: high
---

# Machine Learning 학습 방식과 문제 유형

## 정의

Machine Learning 문제를 고를 때는 두 축을 구분해야 한다.

1. **학습 방식:** 정답 label을 주는가, 주지 않는가, 환경의 reward로 배우는가
2. **출력 문제:** 연속 숫자를 예측하는가, 범주를 예측하는가, 비슷한 데이터끼리 묶는가

이 두 축을 섞지 않으면 “회귀·분류·군집이 모두 같은 수준의 학습 방식인가?”라는 혼동을 피할 수 있다.

## 왜 중요한가

알고리즘 이름부터 외우면 데이터와 목표가 바뀔 때 무엇을 선택해야 하는지 판단하기 어렵다. 먼저 label 유무와 원하는 출력 형태를 확인하면 적절한 model과 metric을 좁힐 수 있다. 2026-07-08 수업은 이 기준을 세운 뒤 `mpg` 숫자 예측을 선형회귀로 연결했다.

## AI·ML·DL의 포함 관계

- **Artificial Intelligence:** 추론·계획·문제 해결 등 인간 지능을 모방하는 가장 넓은 범위
- **Machine Learning:** 명시적 규칙만 작성하는 대신 데이터에서 패턴을 학습하는 AI의 하위 범위
- **Deep Learning:** 여러 층의 neural network로 표현을 학습하는 ML의 하위 범위

즉, Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence다. 사용하는 library나 데이터 양이 포함 관계를 결정하는 것이 아니라 학습 방법의 책임이 기준이다.

## 학습 방식

| 방식 | 학습 데이터 | 목표 | 07-08 수업 예 |
|---|---|---|---|
| 지도 학습 | feature와 정답 label | 새 feature의 label 예측 | 선형회귀, 분류 알고리즘 |
| 비지도 학습 | feature만 있음 | 숨은 구조·그룹·저차원 표현 발견 | K-Means, hierarchical clustering |
| 강화 학습 | state·action·reward의 상호작용 | 장기 누적 reward를 높이는 policy 학습 | 환경에서 보상을 받는 agent |

지도/비지도는 label 제공 여부, 강화 학습은 정적인 label 표보다 환경과 reward feedback이 핵심이다.

## 회귀·분류·군집 비교

| 문제 | 원하는 출력 | 일반 학습 방식 | 질문 예 | 대표 평가 관점 |
|---|---|---|---|---|
| 회귀(Regression) | 연속 숫자 | 지도 학습 | 자동차 연비는 얼마인가? | $R^2$, MSE, MAE |
| 분류(Classification) | 정해진 class | 지도 학습 | 승객이 생존했는가? | confusion matrix, F1, ROC/AUC |
| 군집(Clustering) | 유사도 기반 group | 비지도 학습 | 고객을 어떤 그룹으로 묶을까? | cluster 응집도·분리도와 업무 해석 |

회귀 vs 분류 vs 군집은 이 페이지의 핵심 비교 책임으로 흡수했다. 별도 Comparison을 만들지 않아도 문제 선택 기준과 수업 사례를 한곳에서 찾을 수 있기 때문이다.

## 수업 사례

### 2026-07-08 `auto-mpg`

- feature: 자동차 `weight`, 또는 `cylinders`·`horsepower`·`weight`
- label: 연속 숫자인 `mpg`
- 판단: label이 있고 숫자를 예측하므로 지도 학습의 회귀 문제

### 2026-07-09로 이어지는 분류

- Titanic feature: 선실 등급·나이·가족 수·성별·승선항 등
- label: 생존 0/1
- 판단: label이 있고 범주를 예측하므로 지도 학습의 분류 문제

### 2026-07-13 도매 고객 군집

- feature: 판매 channel·region을 제외한 6개 상품군의 연간 구매액
- label: 입력에는 정답 label이 없음
- 출력: KMeans가 만든 cluster ID와 cluster별 평균
- 판단: 미리 정한 고객 유형을 맞히는 분류가 아니라 feature 거리로 group을 찾는 비지도 군집 문제

cluster ID 0~4는 정답 class 이름이 아니다. 번호는 algorithm 실행 결과의 식별자이므로 [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리]]에서 feature·scale·K·linkage에 따른 해석 책임을 별도로 다룬다.

## 자주 헷갈리는 점

- **class와 범주형 feature는 다르다.** class는 모델이 맞힐 target 범주이고, 성별·승선항처럼 입력으로 쓰는 범주형 feature도 있다.
- **분류와 군집은 다르다.** 분류는 미리 정의된 label을 배우지만 군집은 label 없이 데이터 구조를 찾는다.
- **로지스틱 회귀는 이름과 달리 주로 분류에 쓴다.** 알고리즘 이름보다 출력과 loss의 책임을 확인한다.
- **추천·이상치 탐지는 한 알고리즘으로 고정되지 않는다.** label 유무와 설계에 따라 지도·비지도 접근이 모두 가능하다.
- **ML이 항상 DL인 것은 아니다.** 선형회귀·SVM·KNN·Decision Tree는 neural network 없이도 동작한다.

## 선행·후속 연결

- 선행: [[entities/python|Python]]과 [[entities/pandas|Pandas]]로 데이터를 읽고 가공하는 능력
- 실행 골격: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 회귀 세부: [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]
- 분류 세부: [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- 군집 세부: [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리·hierarchical clustering·KMeans]]
- 수업: [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf` — AI/ML/DL·학습 방식·문제 유형 보조
