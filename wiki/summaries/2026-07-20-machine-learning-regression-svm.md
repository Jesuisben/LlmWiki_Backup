---
title: 2026-07-20 소득 다중회귀와 iris SVM 재방문
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum, study-log]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/multiple_linear_regression_dataset.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/iris.csv
status: growing
confidence: high
---

# 2026-07-20 소득 다중회귀와 iris SVM 재방문

## 한 줄 요약

Python의 데이터 수집·Pandas 흐름을 복습한 뒤 나이·경력으로 소득을 예측하는 다중 선형회귀와 iris SVM을 다시 구현하며, feature/label→split→train 기준 전처리→fit→predict→evaluate 순서를 더 정확하게 고정했고 OCR은 풀이·결과 없는 과제로 남겼다.

## 전체 교시·학습 순서

| 교시 | 학습 흐름 | 복습과 발전 |
|---|---|---|
| 1교시 | 공공데이터·웹 크롤링·직접 수집·Kaggle | [[summaries/2026-07-06-python-public-data-bicycle-analysis|Python 외부 데이터 수집]]을 ML 입력 확보 관점에서 복습했다. |
| 1~3교시 | income dataset 탐색→상관·산점도→다중회귀→평가·저장 code | 07-08의 다중회귀 골격을 `age`, `experience`→`income`이라는 새 데이터로 반복했다. |
| 3~6교시 | iris 구조→label encoding→8:2 split→train 기준 StandardScaler→SVC→분류 평가 | 07-09 SVM을 다시 다루되 scaler를 split 뒤 train에만 fit하도록 순서를 바로잡았다. |
| 7교시 | SVM 광학 문자 인식(OCR) 실습 과제 | “실습 해보기”, 다음 날 풀이 예정만 기록됐다. |
| 8교시 | 자습 | 추가 풀이·출력·artifact가 없다. |

## 왜 이 흐름으로 배웠는가

ML-1~3에서 여러 모델을 배운 뒤에도 모델 품질은 입력 데이터와 평가 순서에 달려 있다. 먼저 데이터 수집 경로와 Pandas 탐색을 복습하고, 회귀에서 feature 수가 늘어나도 lifecycle이 유지되는지 확인했다. 이어 거리·margin에 scale이 중요한 SVM으로 넘어가 **split 이전 전체 데이터 전처리**와 **split 이후 train 기준 전처리**의 차이를 실제 code 순서로 확인했다. 다음 날에는 한 번의 holdout 평가를 여러 fold 평가로 확장한다.

## 대표 입력 → 처리 → 결과

### 소득 다중 선형회귀

1. **입력:** `multiple_linear_regression_dataset.csv`는 header 포함 21줄이며 data row는 20개, 열은 `age`, `experience`, `income`, 결측 cell은 0개다.
2. **탐색:** `info`, `describe`, 결측·중복, pairplot, 상관계수 heatmap, 두 feature와 income의 산점도를 확인하도록 작성했다.
3. **구조:** `age`·`experience`가 feature `x`, `income`이 연속 label `y`다.
4. **분할·학습:** 7:3 holdout split 뒤 `LinearRegression`을 train data에 fit한다.
5. **예측·평가:** test prediction, $R^2$, 두 회귀계수, 절편, 행별 squared error와 평균 MSE를 계산한다.
6. **저장 의도:** pairplot·heatmap·scatter·regplot PNG와 `test_preds.csv` 저장 호출이 있다.

이 과정은 [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]의 07-08 `auto-mpg` 사례에서 feature와 dataset만 바꾼 재적용이다. 20개 표본의 holdout 결과 하나만으로 안정적인 일반화 성능을 확정할 수는 없다.

### iris SVM

1. **입력:** `iris.csv`는 header와 150개 data row, 4개 수치 feature와 `Species` label로 구성되며 세 class가 50개씩이고 결측은 없다.
2. **변환:** 네 feature를 실수 배열로, 문자열 종 label을 `LabelEncoder`로 숫자화한다.
3. **분할:** feature·label을 8:2 train/test로 먼저 나눈다.
4. **scaling:** `StandardScaler`는 `x_train`에만 fit하고, train과 test는 같은 평균·표준편차 기준으로 transform한다.
5. **모델:** RBF `SVC(C=1, gamma=0.1)`를 train에 fit하고 test를 예측한다.
6. **평가:** prediction/label 일치표, accuracy, confusion matrix, classification report를 계산하도록 작성했다.

07-09 분류 source의 scaler-before-split 누수를 이날 iris code가 올바른 순서로 고친 점이 실제 발전이다. 다만 code 존재가 실행 결과나 특정 정확도를 증명하지는 않는다.

## feature·label·split 구조

| 사례 | feature | label | split | 평가 단위 |
|---|---|---|---|---|
| income 회귀 | `age`, `experience` | 연속값 `income` | 70% train / 30% test | test $R^2$, MSE |
| iris SVM | 꽃받침·꽃잎 4개 수치 | 3개 species class | 80% train / 20% test | test accuracy·matrix·report |

회귀와 분류는 같은 split→fit→predict 골격을 공유하지만 label 형태와 metric이 다르다.

## code·output·metric·model·graph·artifact 경계

| 층 | 확인된 범위 | 확인되지 않은 범위 |
|---|---|---|
| 날짜 MD code | 두 pipeline과 저장 호출이 연속 code로 보존됨 | 수업 환경에서 전체 runtime 성공 |
| 독립 source | 회귀·SVM `.py` 2개가 AST parse 가능 | dependency·font·상대경로·fit 성공 |
| dataset | income 20×3, iris 150×5 구조와 결측·class 확인 | 모든 행이 수업 실행에서 처리됨 |
| output·metric | `print`·metric 계산 code가 존재 | 실제 $R^2$, MSE, accuracy, matrix 수치 |
| model | 메모리 model을 fit하는 code가 존재 | 직렬화 model artifact |
| graph·CSV | `savefig`·`to_csv` 호출이 존재 | `dataOut`·`dataout`에 해당 물리 결과가 없어 저장 성공 미확정 |

날짜 MD의 회귀 code는 `../dataOut/`, 독립 source는 `./../dataout/`을 사용해 대소문자·상대경로가 다르다. 어느 경로에도 결과 파일이 없으므로 저장 메시지나 호출만으로 artifact 성공을 단정하지 않는다.

## 실제 오류·불일치·미확정 실행

- 날짜의 회귀 주석 “10세트는 따로 빼둠”과 실제 `test_size=0.3`은 일치하지 않는다. 20개 표본이면 설정상 약 30% test이지 고정 10개 분리가 아니다.
- 독립 회귀 source는 코드 주석에서 “단순 회귀”라고 부르지만 feature가 `age`, `experience` 두 개이므로 실제 모델은 다중 선형회귀다.
- 날짜 SVM code의 scatter 함수 주석은 `row[0]`을 꽃받침 길이와 너비 모두로 적었지만 실제 산점도는 `row[0]`, `row[1]`을 사용한다.
- 날짜 MD와 독립 source 모두 metric·저장 code만 있고 실제 stdout·PNG·CSV·model file은 없다.
- OCR은 문제 제목과 “실습 해보기/내일 풀이”만 있다. 풀이 code, 실행 output, OCR image, metric, model, graph artifact가 없으므로 완료 실습으로 분류하지 않는다.

## 헷갈린 점과 정확한 구분 기준

- **다중회귀 재방문:** 새 알고리즘이 아니라 기존 회귀 lifecycle을 새 feature·label에 적용한 발전이다.
- **SVM 재방문:** SVC 자체 설명의 반복보다 split 뒤 train에 scaler를 fit하는 누수 방지 순서가 핵심 발전이다.
- **전처리와 모델 학습:** scaler가 평균·표준편차를 학습하는 `fit`과 SVC가 decision boundary를 학습하는 `fit`은 서로 다른 객체의 학습이다.
- **metric과 artifact:** 화면에 계산할 metric, 메모리 model, 저장 PNG·CSV는 각각 독립적으로 존재를 확인해야 한다.
- **과제와 완료:** 과제 문구만 있으면 시도 의도만 확인되며, 풀이·출력·artifact가 있어야 완료 범위를 더 높게 판정할 수 있다.

## 이전·다음 학습 연결

- 이전: [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|2026-07-16 Bayesian filter와 VGG16]]까지 text/image model을 확장한 뒤 전통 회귀·SVM의 평가 순서를 복습했다.
- 회귀 선행: [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]]
- 분류 선행: [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 분류와 성능 평가]]
- 다음: [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 교차 검증]]에서 holdout 하나를 여러 fold 평가로 확장한다.

## 관련 페이지

- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]
- [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- [[concepts/svm-margin-kernel-classification|SVM의 margin과 kernel 분류]]
- [[comparisons/standardization-vs-minmax-scaling|표준화 vs Min-Max scaling]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]
- [[entities/scikit-learn|scikit-learn]]
- [[entities/pandas|Pandas]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/age_experience_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/multiple_linear_regression_dataset.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/iris.csv`
