---
title: scikit-learn
created: 2026-07-22
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/CountVectorizer01.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/logisticRegression01.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_example.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/mdsAndDendrogram.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_clustering.py
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py
status: growing
confidence: high
---

# scikit-learn

## 무엇인가

scikit-learn은 Python에서 전처리, train/test 분리, 회귀·분류·군집 model, metric과 model 선택 도구를 일관된 API로 제공하는 Machine Learning library다. package/import 이름은 보통 `sklearn`이다.

## 이 위키에서의 맥락

2026-07-08 Machine Learning 시작일부터 독립적인 검색 가치가 생겼다. 한 함수만 사용한 것이 아니라 split, regression, scaling, SVM, KNN, Decision Tree, confusion matrix, classification report, ROC/AUC까지 이틀의 공통 toolkit 역할을 맡았기 때문이다.

## 첫 등장과 날짜별 학습 이력

### 2026-07-08 — 회귀 lifecycle

- `train_test_split`: feature와 label을 7:3 train/test로 분리
- `LinearRegression`: 단순·다중 선형회귀 fit·predict·score
- 역할: [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]를 code로 연결

### 2026-07-09 — 분류·전처리·평가 확장

- `StandardScaler`: feature scale 표준화
- `SVC`: RBF kernel SVM과 class probability
- `KNeighborsClassifier`: K=5 최근접 이웃 분류
- `DecisionTreeClassifier`: entropy·max depth 기반 tree
- `metrics`: confusion matrix·classification report·ROC/AUC

같은 `fit`·`predict` 관례 덕분에 model이 달라도 [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]를 반복할 수 있었다.

### 2026-07-10 — text·logistic regression

- `CountVectorizer`: text corpus에서 vocabulary를 학습하고 sparse feature matrix 생성
- `MultinomialNB`: 단어 빈도 feature로 mail 유형 분류
- `LogisticRegression`: iris 4개 feature로 3개 class와 확률 예측
- 역할: [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화]]와 분류 평가를 연결

### 2026-07-13 — clustering·MDS

- `KMeans`: 2차원 점과 도매 고객 구매액의 cluster 중심·label 생성
- `MDS`: 사전 계산 distance matrix를 2차원에 embedding
- `StandardScaler`: 구매액 feature의 scale을 맞춘 뒤 거리 기반 군집에 전달
- 역할: [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리]]를 code로 연결

### 2026-07-20~21 — 올바른 scaling·K 선택·cross-validation

- 07-20: income `LinearRegression`을 새 dataset에 반복하고, iris는 split 뒤 train에만 `StandardScaler.fit`한 다음 `SVC`를 평가했다.
- 07-21: preference에 `KNeighborsClassifier`를 적용해 여러 K의 holdout accuracy와 confusion matrix를 비교했다.
- 같은 날 `StratifiedKFold(n_splits=10)`로 sonar binary class 비율을 고려한 fold index를 만들고, 각 fold의 Keras model 평가를 반복했다.
- 역할: [[concepts/knn-distance-voting|KNN의 distance·voting]]과 [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증]]을 공통 model-selection API로 연결했다.

## 핵심 기능 / 특징

| 영역 | 07-08~21 수업에서 사용한 API | 책임 |
|---|---|---|
| data split | `model_selection.train_test_split` | 일반화 평가용 train/test 분리 |
| preprocessing | `preprocessing.StandardScaler` | feature 평균·표준편차 기반 scaling |
| regression | `linear_model.LinearRegression` | 연속 label 예측 |
| classification | `svm.SVC`, `neighbors.KNeighborsClassifier`, `tree.DecisionTreeClassifier` | 범주 label 예측 |
| metrics | `confusion_matrix`, `classification_report`, `roc_curve`, `auc` | 오류 유형·threshold 성능 평가 |
| tree interpretation | `feature_importances_`, `plot_tree`, `export_text` | 분할 중요도·규칙 확인 |
| text feature | `feature_extraction.text.CountVectorizer` | corpus vocabulary와 sparse count matrix 생성 |
| probabilistic classification | `naive_bayes.MultinomialNB`, `linear_model.LogisticRegression` | text count·iris 다중 class 분류 |
| clustering·embedding | `cluster.KMeans`, `manifold.MDS` | 중심 기반 군집과 distance 저차원 표현 |
| cross-validation | `model_selection.StratifiedKFold` | class 비율을 고려한 반복 train/test index 생성 |

## 도구 책임과 실행 환경 구분

- scikit-learn은 model·transformer·metric을 제공하는 library다.
- [[entities/jupyter-notebook|Jupyter Notebook]]이나 IDE는 code를 편집·실행·기록하는 환경이며 scikit-learn의 기능이 아니다.
- [[entities/pandas|Pandas]]는 표 데이터를 준비하고, [[entities/matplotlib|matplotlib]]·Seaborn은 결과를 시각화한다.
- 날짜 source의 import와 API 호출은 code 존재를 증명하지만 package 설치·전체 실행 성공을 증명하지 않는다.

## 수업 전반의 주의점

### estimator interface

- `fit(x_train, y_train)`: train data에서 parameter를 학습
- `predict(x_test)`: 학습된 model로 class 또는 연속값 예측
- `predict_proba(x_test)`: 지원하는 classifier에서 class probability 계산
- `score(...)`: estimator별 기본 지표를 반환하므로 의미를 확인해야 함

`LinearRegression.score`는 $R^2$이지만 classifier의 `score`는 보통 accuracy다. 같은 method 이름이 같은 metric을 뜻하지 않는다.

### preprocessing leakage

07-09 source들은 전체 feature에 scaler를 fit한 뒤 split한다. scikit-learn 사용 자체가 누수를 막아 주는 것은 아니다. split 후 train에만 transformer를 fit하고 test에는 transform만 해야 한다. 후속에는 `Pipeline`을 사용해 전처리와 model을 묶는 방법으로 확장할 수 있다.

### scaling 필요성 차이

SVM·KNN은 거리와 margin이 feature scale에 영향을 받으므로 scaling이 중요하다. Decision Tree는 값의 순서와 threshold로 분할하므로 일반적으로 scaling이 필수는 아니다.

## 실제 artifact 경계

관련 교육 source는 AST parse 가능하며 scikit-learn API 호출을 보존한다. 그러나 회귀·분류·군집·KNN·K-fold 실습에는 실행 stdout, 실제 metric 수치, 직렬화 model file, 저장 graph가 남아 있지 않다. 따라서 estimator가 정의·fit되도록 작성된 사실과 성공적으로 학습·평가·저장된 artifact를 구분한다.

## 관련 개념

- [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]
- [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- [[concepts/svm-margin-kernel-classification|SVM의 margin과 kernel 분류]]
- [[comparisons/standardization-vs-minmax-scaling|표준화 vs Min-Max scaling]]
- [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]]
- [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 Machine Learning 분류와 성능 평가]]
- [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]
- [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]]
- [[concepts/knn-distance-voting|KNN의 distance·voting]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]

## 프로젝트/면접에서 설명할 관점

“scikit-learn은 split·preprocessing·estimator·metric의 공통 API를 제공하지만, 데이터 누수 방지·metric 선택·artifact 검증은 사용자가 설계해야 한다. 수업에서는 회귀·분류에서 text vectorization·Naive Bayes·군집·KNN·K-fold까지 같은 interface를 확장했다”고 설명할 수 있다.

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/CountVectorizer01.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/logisticRegression01.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_example.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/mdsAndDendrogram.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_clustering.py`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py`
