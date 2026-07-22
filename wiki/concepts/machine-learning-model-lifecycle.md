---
title: Machine Learning 모델 생명주기
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py
  - raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py
status: growing
confidence: high
---

# Machine Learning 모델 생명주기

## 정의

Machine Learning 모델 생명주기는 문제와 데이터를 정한 뒤 **feature/label 분리 → train/test split → 전처리 학습·적용 → model fit → predict → evaluate → 필요 시 artifact 저장·검증**으로 이어지는 반복 가능한 작업 흐름이다.

## 왜 중요한가

모델 class만 바꿔도 선형회귀·SVM·KNN·Decision Tree가 비슷해 보이는 이유는 이 공통 골격을 공유하기 때문이다. 반대로 순서를 잘못 지키면 test 정보가 학습에 새어 들어가 metric이 실제보다 좋아지는 leakage가 생긴다.

## 단계별 책임

| 단계 | 핵심 질문 | 산출물 |
|---|---|---|
| 문제 정의 | 숫자·범주·그룹 중 무엇을 원하는가? | task와 metric 기준 |
| feature/label | 입력과 정답은 각각 무엇인가? | `x`, `y` |
| split | 보지 않은 데이터 성능을 어떻게 확인할까? | `x_train`, `x_test`, `y_train`, `y_test` |
| preprocessing | 결측·범주·scale을 어떻게 처리할까? | 학습된 transformer와 변환 데이터 |
| fit | train data에서 어떤 규칙을 학습할까? | 메모리의 fitted model |
| predict | test feature에 어떤 결과를 낼까? | prediction·probability |
| evaluate | 업무 목적에 맞는 오류를 어떻게 볼까? | $R^2$/MSE 또는 분류 metric |
| persist/verify | 재사용할 artifact가 실제 남았는가? | model/CSV/graph file과 검증 결과 |

## 2026-07-08 회귀 사례

`auto-mpg`에서 `weight`를 feature, `mpg`를 label로 잡고 7:3으로 split했다. `LinearRegression.fit(x_train, y_train)` 뒤 test feature를 예측하고 $R^2$와 MSE를 계산했다. 다중회귀에서는 feature만 세 개로 늘었고 생명주기는 유지됐다.

## 2026-07-09 분류 사례

- SVM: Titanic feature를 전처리해 생존 label을 예측하고 confusion matrix·ROC/AUC를 계산하도록 작성
- KNN: 같은 종류의 feature/label과 평가 구조에서 K=5 이웃 vote 사용
- Decision Tree: 유방암 feature와 0/1 class를 사용해 entropy 기반 tree 학습·평가·해석

이 예들은 [[entities/scikit-learn|scikit-learn]] estimator의 `fit`·`predict` 인터페이스가 공통 lifecycle을 만든다는 점을 보여 준다.

## 2026-07-10~13 확장

- **text 분류:** tokenizer와 `CountVectorizer`도 fitted preprocessing 객체다. vocabulary는 train corpus에서 학습하고 새 mail에는 같은 vectorizer의 `transform()`만 적용한다.
- **신경망:** topology 정의→compile→fit→History→evaluate로 lifecycle이 확장된다. train·validation·test metric과 saved CSV·PNG·model file은 서로 다른 증거다.
- **군집:** 정답 label이 없으므로 split→정답 metric이 항상 같은 형태로 적용되지는 않는다. feature 선택·scaling→distance/K 설정→fit→cluster 해석·안정성 검토가 중심이다.
- **CNN:** layer 구조 code와 trained weight·test metric·graph artifact를 분리한다. topology만 만든 source를 학습 완료 model로 보지 않는다.

## train/test preprocessing의 올바른 순서

07-09 SVM·KNN·Decision Tree source는 전체 `x`에 StandardScaler를 fit한 다음 split한다. 원본 code는 보존하지만 현재 판단은 **data leakage가 있는 평가 순서**다.

안전한 기준은 다음과 같다.

1. 원본 feature와 label을 먼저 train/test로 나눈다.
2. 결측값 대체·범주 encoding·scaler처럼 데이터 분포를 학습하는 transformer는 train에만 fit한다.
3. train은 `fit_transform`, test는 같은 transformer의 `transform`만 사용한다.
4. test 결과를 보고 preprocessing이나 hyperparameter를 반복 선택하면 test도 사실상 학습에 사용된다. 선택은 validation 또는 cross-validation으로 분리한다.

scaler의 train `fit_transform` vs test `transform` 비교는 반복 혼동이지만, 이 lifecycle의 누수 방지 책임 안에서 충분히 설명되므로 별도 Comparison·Query를 만들지 않았다.

## 2026-07-20~21: 올바른 holdout에서 K-fold로

- 07-20 income 회귀는 `age`·`experience` feature와 `income` label을 7:3으로 나눠 기존 회귀 lifecycle을 새 데이터에 반복했다.
- 같은 날 iris SVM은 **먼저 8:2 split한 뒤** `StandardScaler`를 train에만 fit하고 test에는 같은 기준을 transform했다. 이는 07-09 source의 scaler-before-split 누수를 바로잡은 실제 순서 발전이다.
- 07-21 preference KNN은 전체 데이터에서 Min-Max 기준을 만든 뒤 split하므로 다시 leakage가 생긴다. 또한 같은 작은 test set으로 K를 고르고 최종 성능도 읽으면 test가 model 선택에 사용된다.
- sonar 신경망은 [[concepts/k-fold-cross-validation-generalization|10-fold cross-validation]]으로 매 fold 새 model을 만들고 loss·accuracy를 모은다. K개 metric 평균은 평가 요약이지 하나의 최종 model artifact가 아니다.

K-fold에서는 scaler·결측 대체·feature selector·vectorizer도 매 fold의 train subset에만 fit해야 한다. 전체 데이터로 전처리한 뒤 fold를 나누면 각 평가 fold의 정보가 학습에 섞인다. transformer와 estimator를 `Pipeline`으로 묶는 방식은 이 경계를 지키기 쉽다.

## StandardScaler를 정확히 이해하기

- 평균을 0, 표준편차를 1에 가깝게 맞춰 feature scale 차이를 줄인다.
- 거리·margin에 영향을 받는 KNN·SVM에는 중요하다.
- Decision Tree는 threshold 분할을 사용하므로 일반적으로 scale 변화에 덜 민감하고 표준화가 필수는 아니다.
- StandardScaler가 이상치를 제거하거나 영향력을 자동으로 줄이는 것은 아니다. 평균·표준편차를 사용하므로 이상치에 민감하다.

StandardScaler와 Min-Max의 선택 기준은 [[comparisons/standardization-vs-minmax-scaling|표준화 vs Min-Max scaling]]이 소유한다.

## 평가와 artifact의 증거 사다리

1. **source code 존재:** 실행 의도와 절차를 증명
2. **dataset 존재:** 입력 가능성을 증명
3. **text output/metric 보존:** 특정 실행 관찰을 증명
4. **model/CSV/graph 물리 파일:** 저장 결과가 남았음을 증명
5. **재현 실행·독립 검증:** 같은 조건에서 결과를 다시 얻었음을 증명

`fit`, `predict`, `savefig`, `to_csv` 호출이나 “저장되었습니다”라는 print만으로 다음 단계의 성공을 단정하지 않는다. ML-1 교육자료의 `dataOut`에는 해당 저장 결과가 없어 model·metric·graph artifact는 미확정이다.

### ML-3의 서로 다른 artifact 사례

- 07-14 Word2Vec train/save block은 주석 처리되어 model 생성 단계가 실행 code가 아니다.
- 07-15에는 Word2Vec build/train/save/load code와 text output이 있지만 물리 `toji.model`이 없다.
- 07-16에는 VGG16 probability graph 4개가 실제 존재하므로 graph artifact 단계는 확인된다.
- 같은 07-16의 `prediction_result.csv`는 저장 call만 있고 물리 file이 없어 미확정이다.

하나의 graph가 존재한다고 model download·전체 loop·CSV·현재 환경 재현까지 함께 성공한 것은 아니다. artifact 종류마다 독립적으로 확인한다.

## 자주 헷갈리는 점

- **fit과 predict:** fit은 train data에서 parameter를 학습하고, predict는 학습된 parameter로 새 입력의 결과를 계산한다.
- **test와 validation:** test는 마지막 일반화 평가용이다. 모델 선택을 반복하려면 validation/cross-validation이 필요하다.
- **재현성과 일반화:** 고정 `random_state`는 비교 재현에 유용하지만 한 split의 성능이 일반화 전체를 보장하지 않는다.
- **metric과 model file:** metric은 평가 결과이고 model file은 재사용 가능한 직렬화 artifact다.
- **Pandas 전처리와 estimator:** DataFrame 가공은 입력 준비이며 모델 학습 자체가 아니다.

## 선행·후속 연결

- 문제 선택: [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- 회귀 평가: [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]
- 분류 평가: [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- 첫 수업: [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]]
- 분류 적용: [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 Machine Learning 분류와 성능 평가]]
- text·신경망 적용: [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- 군집·CNN 적용: [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]
- NLP·Word2Vec 적용: [[summaries/2026-07-14-machine-learning-nlp-vectorization|2026-07-14 NLP 표현과 Word2Vec 입문]], [[summaries/2026-07-15-machine-learning-word2vec-bayesian-filter|2026-07-15 Word2Vec과 Bayesian filter 초안]]
- pretrained inference 적용: [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]]
- holdout 재방문: [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- 교차 검증: [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]], [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py`
- `raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py`
