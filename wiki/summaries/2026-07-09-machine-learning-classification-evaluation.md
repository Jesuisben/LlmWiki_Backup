---
title: 2026-07-09 Machine Learning 분류와 성능 평가
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum, study-log]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/breast-cancer-wisconsin.data.txt
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(실습).pdf
status: growing
confidence: high
---

# 2026-07-09 Machine Learning 분류와 성능 평가

## 한 줄 요약

분류 결과를 confusion matrix·accuracy·precision·recall·F1·ROC/AUC로 읽은 뒤, Titanic SVM/KNN과 유방암 Decision Tree 코드에 같은 전처리→학습→예측→평가 구조를 적용했다.

## 전체 교시·학습 순서

| 교시 | 학습 흐름 | 역할 |
|---|---|---|
| 1교시 | class·confusion matrix·분류 지표 → SVM | 무엇을 예측하고 결과를 어떻게 평가하는지 먼저 정했다. |
| 2교시 | Titanic 전처리·SVM·confusion matrix·ROC/AUC | 이론 지표를 첫 분류 파이프라인에 연결했다. |
| 3교시 | threshold·TPR/FPR·ROC·AUC | 단일 class 예측을 확률과 임계값 관점으로 확장했다. |
| 4교시 | KNN·K 선택·과적합·일반화 | 거리 기반 분류와 train 성능만 믿으면 안 되는 이유를 배웠다. |
| 5교시 | Titanic KNN → Decision Tree·entropy·information gain·ensemble | 다른 분류기의 판단 원리를 비교했다. |
| 6교시 | 유방암 데이터 Decision Tree·특성 중요도·트리 규칙 | 실제 표 데이터에서 tree 학습·평가·해석 코드를 작성했다. |
| 7~8교시 | 자습 | 별도 실행 결과나 artifact는 기록되지 않았다. |

## 왜 이 흐름으로 배웠는가

전날 선형회귀는 연속 숫자를 예측하고 $R^2$·MSE로 평가했다. 이날은 범주 label을 예측하므로 먼저 [[concepts/classification-evaluation-metrics|분류 성능 평가]]의 TP·FP·FN·TN을 배운 뒤, SVM·KNN·Decision Tree에 같은 [[concepts/machine-learning-model-lifecycle|모델 생명주기]]를 반복 적용했다. 알고리즘이 달라도 feature/label 준비, train/test 분리, fit, predict, evaluate라는 골격은 유지된다는 점이 핵심이다.

## 대표 입력 → 처리 → 결과

### Titanic SVM

- **입력:** Seaborn의 Titanic dataset에서 생존 여부를 label로 사용한다. repository의 별도 `titanic.csv`가 아니라 `sns.load_dataset('titanic')` 호출이 입력 경로다.
- **처리:** 중복 제거, `deck`·`embark_town` 제거, `age` 결측 행 제거, `embarked` 최빈값 대체, 성별·승선항 원-핫 인코딩, 표준화, 7:3 split을 작성했다.
- **모델·평가:** RBF kernel `SVC(probability=True)`를 fit하고 class 예측, confusion matrix, classification report, class 1 확률 기반 ROC/AUC를 계산하도록 했다.

### Titanic KNN

같은 종류의 전처리 뒤 `KNeighborsClassifier(n_neighbors=5)`를 fit했다. 예측값·정답·일치 여부 표와 confusion matrix·classification report를 만들도록 작성해, SVM과 동일한 데이터/평가 골격에서 알고리즘만 바꾸는 연습이 됐다.

### 유방암 Decision Tree

1. **입력:** header 포함 700줄·11열 물리 dataset에서 `class`를 label로 사용한다. `bare_nuclei`에는 `?` 16개가 있다.
2. **처리:** class 2/4를 0/1로 매핑하고 중복을 제거하며, `?`를 결측값으로 바꿔 해당 행을 제거한 뒤 8개 feature를 선택했다.
3. **모델:** `DecisionTreeClassifier(criterion='entropy', max_depth=5)`를 fit하고 예측했다.
4. **결과 코드:** confusion matrix·classification report, feature importance, tree depth·leaf count·분기 규칙과 여러 저장 호출이 작성됐다.

## 분류 알고리즘의 판단 기준

| 알고리즘 | 이날 배운 핵심 | 주의점 |
|---|---|---|
| SVM | class 사이 margin이 큰 hyperplane을 찾고 kernel로 비선형 경계를 다룬다. | `C`, `gamma`, kernel과 scaling이 경계에 영향을 준다. |
| KNN | 새 점에서 가까운 K개 이웃의 vote로 class를 정한다. | 거리 scale과 K 선택에 민감하고 예측 시 전체 이웃 탐색 비용이 든다. |
| Decision Tree | feature 질문으로 impurity를 줄이며 leaf까지 분할한다. | 깊은 tree는 과적합하기 쉬우며 scaling이 원리상 필수는 아니다. |

## code·output·metric·model·artifact 증거 경계

| 증거 | 확인된 범위 | 확인되지 않은 범위 |
|---|---|---|
| 날짜 MD·독립 `.py` 3개 | 전처리·fit·predict·metric·save 코드가 존재하고 AST parse 오류 0개 | dependency·network dataset 로드·전체 실행 성공 |
| 교육 dataset | 유방암 입력 파일의 header·행/열·`?` 구조 확인 | 이날 code가 끝까지 성공 처리했는지 |
| metric 호출 | confusion matrix·report·ROC/AUC 계산 의도 | 실제 matrix·accuracy·AUC 수치 |
| model 객체 | SVM·KNN·Tree 학습 시도 코드 | 직렬화된 model artifact |
| `savefig` 호출 | 여러 PNG 저장 의도 | 교육자료 `dataOut`에 결과 파일이 없어 실제 저장 성공은 미확정 |

날짜 노트에는 실행 stdout, confusion matrix 수치, classification report, ROC/AUC 수치, 저장 PNG가 보존되지 않았다. 따라서 “모델 성능이 좋았다”거나 특정 feature가 실제 최상위였다고 결과로 확정하지 않는다.

## 실제 오류·불일치·미확정 실행

### ensemble 표의 label 이동 오류

날짜 원문의 세 표는 제목과 내용이 한 칸씩 어긋난다.

| 원본 표기 | 원본 내용 | 현재 판단 | 판단 근거 |
|---|---|---|---|
| 보팅(Voting) | bootstrap식 무작위 표본으로 여러 모델을 학습하고 Random Forest를 예로 듦 | **Bagging 설명** | 이론 교안 246~248쪽에서 Bagging을 표본 재추출·Random Forest로 설명 |
| 배깅(Bagging) | 약한 학습기를 순차 학습하며 AdaBoost·XGBoost 등을 예로 듦 | **Boosting 설명** | 이론 교안은 Boosting을 이전 오류에 집중하는 순차 결합으로 설명 |
| 부스팅(Boosting) | 여러 모델 예측을 hard/soft voting으로 결합 | **Voting 설명** | 이론 교안은 Voting을 서로 다른 모델 예측의 다수결·확률 평균으로 설명 |

raw는 수정하지 않고, 이 위키에서 제목과 설명의 올바른 대응만 교정한다.

### preprocessing leakage

SVM·KNN·Decision Tree code는 모두 전체 `x`에 `StandardScaler.fit()`을 적용한 뒤 train/test를 나눈다. 이러면 test 통계가 전처리에 섞이는 **data leakage**가 생긴다. 올바른 평가 흐름은 먼저 split하고 train에만 scaler를 fit한 뒤 train에는 `fit_transform`, test에는 같은 scaler의 `transform`만 적용하는 것이다. 이 판단은 [[concepts/machine-learning-model-lifecycle|모델 생명주기]]에 흡수했고 별도 Comparison·Query는 만들지 않았다.

추가로 날짜 주석의 “표준화가 이상치 영향을 줄인다”는 설명은 부정확하다. StandardScaler는 평균·표준편차를 사용해 scale을 맞추지만 이상치 자체에 민감하다.

- Decision Tree code의 `train_features` 위 주석은 이를 “종속 변수들”이라고 부르지만, 실제로는 model 입력에 쓰는 **독립 feature** 목록이다. 종속 label은 `y = df['class']`다.
- 같은 구간은 `DecisionTreeClassifier`의 이론 교안 위치를 114쪽으로 적었지만, 현재 이론 PDF의 Decision Tree 본문은 238쪽부터 확인된다. 날짜 원문의 page 표기는 현재 PDF와 불일치한다.
- 세 실습 모두 실제 Traceback→수정→성공 재실행 연쇄가 보존되지 않았다. AST 통과는 문법 구조 확인일 뿐 runtime 성공 증거가 아니다.

## 헷갈린 점과 정확한 구분 기준

- **True/False:** 예측이 정답과 맞았는지다. **Positive/Negative:** 모델이 어느 class로 예측했는지다.
- **Accuracy:** 전체 정답 비율이다. class 불균형이 크면 다수 class만 맞혀도 높아질 수 있다.
- **Precision:** Positive라고 예측한 것 중 정답 비율이므로 FP 비용이 클 때 중요하다.
- **Recall:** 실제 Positive를 놓치지 않은 비율이므로 FN 비용이 클 때 중요하다.
- **F1:** precision과 recall의 조화평균이다. 어느 오류가 더 중요한지는 업무 비용으로 결정해야 한다.
- **ROC/AUC:** threshold를 바꾸며 TPR과 FPR의 trade-off를 본다. AUC 하나가 운영 threshold나 class별 오류 비용을 대신하지 않는다.
- **과적합:** train 성능이 높은 것이 목표가 아니라 보지 못한 데이터에서도 성능이 유지되는 일반화가 목표다.

## 이전·다음 학습 연결

- 이전: [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]]의 feature/label·split·fit·predict·evaluate 골격을 범주 예측으로 바꿨다.
- 다음: 2026-07-10에는 text를 vector로 바꿔 Naive Bayes로 분류하고, logistic regression과 Keras/MNIST로 분류 표현을 확장한다.

## 관련 페이지

- [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- [[concepts/svm-margin-kernel-classification|SVM의 margin과 kernel 분류]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[comparisons/standardization-vs-minmax-scaling|표준화 vs Min-Max scaling]]
- [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- [[entities/scikit-learn|scikit-learn]]
- [[entities/pandas|Pandas]]
- [[entities/matplotlib|matplotlib]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/breast-cancer-wisconsin.data.txt`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf` — 평가·알고리즘·ensemble 용어 대조
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(실습).pdf` — SVM·KNN·Tree 실습 source 위치 보조
