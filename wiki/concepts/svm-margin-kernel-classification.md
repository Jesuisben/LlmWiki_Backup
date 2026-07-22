---
title: SVM의 margin과 kernel 분류
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py
status: growing
confidence: high
---

# SVM의 margin과 kernel 분류

## 정의

Support Vector Machine(SVM)은 class 사이를 나누는 decision boundary 가운데 가까운 sample과의 **margin**을 크게 만드는 경계를 찾는 지도 학습 알고리즘이다. 분류용 구현은 SVC(Support Vector Classification)이며, 수업에서는 2026-07-09 Titanic binary classification과 07-20 iris 3-class classification에 반복 적용했다.

## 왜 중요한가

SVM은 단순히 “분류기 하나”로만 보면 `C`, `gamma`, kernel, scaling이 왜 필요한지 연결하기 어렵다. 이 페이지는 [[concepts/classification-evaluation-metrics|분류 성능 평가]]가 소유하는 metric과 [[concepts/machine-learning-model-lifecycle|모델 생명주기]]가 소유하는 split·전처리 순서에서 분리해, **SVM이 어떤 경계를 만들고 hyperparameter가 그 경계를 어떻게 바꾸는가**를 설명한다.

## 핵심 용어

| 용어 | 의미 |
|---|---|
| hyperplane | feature 공간에서 class를 나누는 decision boundary |
| margin | boundary와 가장 가까운 train sample 사이의 여유 폭 |
| support vector | boundary와 가까워 margin 결정에 직접 영향을 주는 sample |
| kernel | 원래 공간에서 선형 분리가 어려운 관계를 다른 feature 공간의 내적으로 계산하는 방법 |
| RBF kernel | 가까운 sample의 영향이 크도록 방사형 기저 함수를 사용하는 비선형 kernel |

margin이 크면 작은 입력 변화에도 class가 쉽게 바뀌지 않는 경계를 기대할 수 있다. 그러나 실제 일반화 성능은 데이터 품질·feature·hyperparameter·평가 절차를 함께 봐야 하며, margin 하나만으로 보장되지 않는다.

## `C`와 `gamma`

### `C`: margin과 train 오류의 균형

- `C`가 크면 train 오류에 강한 penalty를 주어 더 많은 sample을 맞히려 하고, margin이 좁고 복잡해질 수 있다.
- `C`가 작으면 일부 train 오류를 더 허용하면서 넓은 margin을 택할 수 있다.
- 너무 크면 noise까지 맞추는 과적합, 너무 작으면 경계가 지나치게 단순한 과소적합 위험이 있다.

### `gamma`: RBF 영향 반경

- `gamma`가 크면 각 sample의 영향 반경이 좁아져 경계가 세밀하고 복잡해질 수 있다.
- `gamma`가 작으면 영향이 넓게 퍼져 더 부드러운 경계가 만들어질 수 있다.
- `C`와 `gamma`는 서로 독립된 절대 정답이 아니며 validation이나 cross-validation으로 함께 선택해야 한다.

07-20 source는 `SVC(kernel='rbf', C=1, gamma=0.1)`을 사용하고 `C=8`, `C=100` 후보를 주석으로 남겼다. 이는 후보 code일 뿐 세 값의 실제 성능 비교 결과는 아니다.

## scaling이 중요한 이유

SVM의 boundary는 feature 좌표와 내적·거리에 영향을 받는다. 한 feature의 숫자 범위가 다른 feature보다 훨씬 크면 그 축이 경계에 과도한 영향을 줄 수 있어 scaling이 중요하다.

- 07-09 Titanic code는 `StandardScaler`를 전체 feature에 fit한 뒤 split해 test 통계가 섞이는 leakage가 있다.
- 07-20 iris code는 먼저 8:2 split하고 train에만 scaler를 fit한 뒤 test에는 같은 scaler로 transform해 순서를 바로잡았다.
- StandardScaler는 scale을 맞추지만 이상치를 제거하지 않으며 평균·표준편차를 사용하므로 이상치에 민감하다.

StandardScaler와 Min-Max 선택 자체는 [[comparisons/standardization-vs-minmax-scaling|표준화 vs Min-Max scaling]]이 소유한다.

## 수업 사례

### 2026-07-09 Titanic SVM

1. 생존 여부를 binary label로 둔다.
2. 객실·성별·나이·가족·승선항 feature를 결측 처리하고 범주를 one-hot encoding한다.
3. RBF `SVC(probability=True)`를 fit한다.
4. class prediction은 confusion matrix·classification report에, class 1 probability는 ROC/AUC에 사용하도록 작성했다.

이 source는 scaling-before-split 누수가 있으므로 metric이 보존됐더라도 올바른 일반화 평가로 그대로 확정하면 안 된다.

### 2026-07-20 iris SVM

1. 꽃받침·꽃잎 수치 feature 4개와 species label을 사용한다.
2. label을 encoding하고 8:2 train/test로 먼저 분리한다.
3. train 기준 StandardScaler를 train·test에 적용한다.
4. RBF `SVC(C=1, gamma=0.1)`을 fit하고 accuracy·confusion matrix·classification report를 계산하도록 작성했다.

두 번째 사례의 핵심 발전은 SVM 종류가 새로워진 것이 아니라 전처리의 학습 범위를 train으로 제한한 점이다.

## KNN·Decision Tree와 구분

- [[concepts/knn-distance-voting|KNN]]은 query 주변 K개 train sample의 vote로 예측한다.
- SVM은 support vector가 결정하는 margin 기반 boundary로 예측한다.
- Decision Tree는 feature threshold 질문을 반복해 영역을 분할한다.
- KNN과 SVM은 scale에 민감할 수 있지만 판단 원리가 같지는 않다. Tree는 값의 순서와 threshold를 사용하므로 일반적으로 scaling이 필수는 아니다.

## code·metric·model·artifact 경계

- `SVC(...)`와 `fit()` code는 model 구성·학습 절차를 증명한다.
- `predict`, confusion matrix, ROC/AUC 호출은 평가 의도를 증명한다.
- 특정 accuracy·AUC가 출력되었다거나 한 `C`가 우수했다는 수치는 보존되지 않았다.
- `savefig` 호출은 graph 저장 의도이며 물리 PNG가 없으면 artifact 성공이 아니다.
- 메모리의 fitted SVC와 직렬화된 model file은 다르며 저장 model은 확인되지 않았다.

## 자주 헷갈리는 점

- **support vector는 모든 train row가 아니다.** boundary 가까이에서 margin을 결정하는 sample이다.
- **kernel은 원본 데이터를 직접 새 파일로 변환하는 단계가 아니다.** feature 공간의 관계를 계산하는 함수다.
- **`C`가 클수록 무조건 좋지 않다.** train 오류와 margin 사이 trade-off가 달라진다.
- **probability=True와 class prediction은 다르다.** probability는 ROC/AUC 등에 쓰이고 class는 threshold·decision rule을 거친 결과다.
- **scaling과 leakage는 별개다.** scaling 방법이 맞아도 test까지 포함해 fit하면 평가 순서가 잘못된다.

## 선행·후속 연결

- 문제 유형: [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- lifecycle: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 평가: [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- 첫 적용: [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 분류와 성능 평가]]
- 재방문: [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- 도구: [[entities/scikit-learn|scikit-learn]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py`
