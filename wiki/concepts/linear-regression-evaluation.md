---
title: 선형회귀와 R²·MSE
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/auto-mpg.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/multiple_linear_regression_dataset.csv
status: growing
confidence: high
---

# 선형회귀와 R²·MSE

## 정의

선형회귀(Linear Regression)는 feature와 연속형 label 사이의 관계를 직선 또는 hyperplane으로 근사하는 지도 학습 회귀 모델이다.

- 단순 선형회귀: $\hat{y}=w x+b$
- 다중 선형회귀: $\hat{y}=w_1x_1+w_2x_2+\cdots+w_px_p+b$

$w$는 feature 변화가 예측값에 미치는 방향과 크기, $b$는 모든 feature가 0일 때의 절편이다. 다만 관측 범위 밖의 절편 해석은 현실적 의미가 없을 수 있다.

## 왜 중요한가

복잡한 모델을 배우기 전에 feature·label, parameter, fit, predict, residual, train/test 평가를 가장 단순한 형태로 익힐 수 있다. 2026-07-08에는 자동차 무게와 연비 관계에서 이 구조를 처음 연결했다.

## 수업 사례: `auto-mpg`

물리 dataset은 header 없는 398행·9열이다. `horsepower`의 `?`를 결측값으로 처리하고 평균으로 채운 뒤 분석용 열을 골랐다.

### 단순 회귀

- feature: `weight`
- label: `mpg`
- 처리: 7:3 split → `LinearRegression.fit` → 계수·절편 → test predict
- 평가: test $R^2$와 실제값-예측값의 squared error 평균

수업 설명은 무게가 커질수록 연비가 낮아지는 음의 계수를 다룬다. 이것은 데이터에서 관찰한 선형 관계이지, 무게 하나가 연비를 전부 결정한다는 인과 결론은 아니다.

### 다중 회귀

- feature: `cylinders`, `horsepower`, `weight`
- label: `mpg`
- 처리: 같은 split·fit·predict 흐름
- 해석: 각 계수는 다른 feature를 고정했을 때 해당 feature 1단위 변화와 예측값 변화의 관계다.

feature 사이 상관이 높거나 단위가 크게 다르면 계수 크기만으로 중요도를 단순 비교하기 어렵다.

## 2026-07-20 재방문: 나이·경력 → 소득

`multiple_linear_regression_dataset.csv`의 20개 data row에서 `age`와 `experience`를 feature, `income`을 label로 두었다. pairplot·상관 heatmap·feature별 산점도로 관계를 탐색하고 7:3 split→`LinearRegression.fit`→test $R^2$·prediction→행별 squared error와 평균 MSE 순서로 반복했다.

이 사례는 feature가 두 개인 다중 선형회귀다. 독립 source의 주석은 “단순 회귀”라고 부르지만 실제 `x`가 두 열이므로 model 책임은 다중회귀로 판정한다. 20개 표본과 한 holdout split의 metric은 분할 우연에 민감하므로 [[concepts/k-fold-cross-validation-generalization|교차 검증]]이나 별도 데이터로 안정성을 확인해야 한다. 날짜·source에는 저장 호출만 있고 실제 $R^2$·MSE stdout, CSV·PNG, 직렬화 model은 남아 있지 않다.

## residual과 MSE

residual은 실제값과 예측값의 차이 $y-\hat{y}$다. MSE는 이를 제곱해 평균낸다.

$$
\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

- 낮을수록 예측이 실제값에 가깝다.
- 큰 오류를 제곱하므로 더 크게 벌준다.
- 단위는 label 단위의 제곱이다. 따라서 서로 다른 target·scale의 MSE를 그대로 비교하면 안 된다.
- 0이 최솟값이지만 train MSE가 작다고 test 일반화가 보장되지는 않는다.

## R² 결정계수

$R^2$는 모델의 residual 제곱합을 label 평균만 예측하는 기준과 비교한다.

$$
R^2=1-\frac{SS_{res}}{SS_{tot}}
$$

- 1: 평가 데이터에서 완벽하게 일치
- 0: 평가 데이터의 평균만 예측하는 기준과 같은 수준
- 음수: 평균 기준보다도 못한 예측이 가능함

수업 원문은 0~1 중심으로 설명하지만, 특히 test set의 $R^2$는 음수가 될 수 있다. 또한 높은 $R^2$가 인과관계·편향 없음·운영 적합성을 자동으로 뜻하지 않는다.

## R²와 MSE를 함께 보는 이유

| 지표 | 묻는 질문 | 방향 | 주의점 |
|---|---|---|---|
| $R^2$ | 평균 기준보다 변동을 얼마나 더 설명하는가? | 높을수록 좋음 | test에서 음수 가능, 인과관계 아님 |
| MSE | 실제값과 예측값의 제곱 오차가 평균 얼마인가? | 낮을수록 좋음 | target scale·이상치에 민감 |

하나는 상대적 설명력, 다른 하나는 오류 크기를 보여 주므로 함께 보면 모델을 더 입체적으로 판단할 수 있다.

## 자주 헷갈리는 점

- **상관계수와 회귀계수:** 상관계수는 두 변수의 선형 동행 정도, 회귀계수는 model에서 feature 변화와 예측 변화의 관계다.
- **계수와 feature importance:** 선형회귀 계수는 단위·scale·다중공선성 영향을 받으므로 절댓값 순위를 곧 중요도 순위로 보면 안 된다.
- **학습 metric과 저장 artifact:** `model.score()`와 MSE 값은 평가이고, model·CSV·PNG 저장 여부는 별도로 확인해야 한다.
- **단순 vs 다중:** feature 수가 늘면 항상 좋아지는 것이 아니다. 불필요한 feature·과적합·누수를 점검해야 한다.
- **설명력과 신뢰도:** $R^2$ 하나를 모델 전체의 “신뢰도”라고 부르면 calibration·robustness·업무 비용을 놓칠 수 있다.

## 선행·후속 연결

- 문제 유형: [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- 실행 순서: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 수업: [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]]
- 재방문: [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- 도구: [[entities/scikit-learn|scikit-learn]], [[entities/pandas|Pandas]], [[entities/matplotlib|matplotlib]]
- 후속: 분류 문제는 [[concepts/classification-evaluation-metrics|분류 성능 평가]]처럼 다른 metric을 사용한다.

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/auto-mpg.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf` — 선형회귀·MSE·$R^2$ 정의 보조
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/multiple_linear_regression_dataset.csv`
