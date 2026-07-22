---
title: 분류 성능 평가와 Confusion Matrix·ROC/AUC
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/logisticRegression01.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py
status: growing
confidence: high
---

# 분류 성능 평가와 Confusion Matrix·ROC/AUC

## 정의

분류 성능 평가는 model이 예측한 class와 실제 label을 비교해 어떤 종류의 오류를 냈는지 측정하는 과정이다. Confusion Matrix는 binary classification에서 결과를 TP·FP·FN·TN으로 나누고, accuracy·precision·recall·F1 같은 지표의 공통 재료가 된다.

## 왜 중요한가

accuracy 하나만 보면 어떤 class를 놓쳤는지 알 수 없다. 암 탐지처럼 FN 비용이 큰 문제와 스팸 차단처럼 FP 비용이 큰 문제는 같은 accuracy라도 선택해야 할 model·threshold가 다르다. 2026-07-09 수업은 지표 정의를 먼저 배운 뒤 SVM·KNN·Decision Tree 평가 코드에 반복 적용했다.

## Confusion Matrix 읽기

| 실제 label \ 예측 | Positive | Negative |
|---|---:|---:|
| Positive | TP: 맞게 Positive | FN: 놓친 Positive |
| Negative | FP: 잘못 경보한 Positive | TN: 맞게 Negative |

- True/False는 정답 여부다.
- Positive/Negative는 예측 class다.
- 어느 class를 Positive로 둘지는 업무 목적에 따라 먼저 명시해야 한다.

## 주요 지표

### Accuracy

$$
\mathrm{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}
$$

전체 예측 중 맞힌 비율이다. class 불균형이 크면 다수 class만 예측해도 높아질 수 있다.

### Precision

$$
\mathrm{Precision}=\frac{TP}{TP+FP}
$$

Positive라고 예측한 것 중 실제 Positive 비율이다. 잘못된 경보(FP)를 줄이는 것이 중요할 때 우선한다.

### Recall

$$
\mathrm{Recall}=\frac{TP}{TP+FN}
$$

실제 Positive 중 찾아낸 비율이다. 놓침(FN)을 줄이는 것이 중요할 때 우선한다. TPR·sensitivity라고도 한다.

### F1 Score

$$
F1=2\cdot\frac{\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Precision}+\mathrm{Recall}}
$$

precision과 recall의 조화평균이다. 두 값 중 낮은 쪽의 영향을 크게 받지만, TN 비용은 직접 반영하지 않는다.

accuracy vs precision vs recall vs F1 비교는 이 페이지의 핵심 책임으로 흡수했다. 동일 confusion matrix에서 목적별 선택 기준을 함께 봐야 하므로 별도 Comparison을 만들지 않았다.

## threshold·ROC·AUC

class probability나 decision score를 threshold와 비교해 Positive/Negative를 정하면 threshold 변화에 따라 TP·FP·FN·TN도 달라진다.

- threshold를 낮추면 Positive 예측이 늘어 recall과 FPR이 함께 올라가기 쉽다.
- threshold를 높이면 Positive 예측이 줄어 FPR은 낮아지지만 FN이 늘 수 있다.
- ROC curve는 여러 threshold에서 x축 FPR, y축 TPR을 그린다.
- AUC는 ROC 아래 면적으로, 무작위 기준은 일반적으로 0.5이고 1에 가까울수록 양성과 음성의 순위 분리 능력이 좋다.

AUC는 특정 운영 threshold의 precision·recall이나 비용을 직접 알려 주지 않는다. class가 매우 불균형하면 Precision-Recall curve도 함께 보는 것이 유용하다.

## 수업 사례

### Titanic SVM

`SVC(probability=True)`로 생존 class와 class 1 probability를 예측하도록 했다. class 예측은 confusion matrix·classification report에, probability는 `roc_curve`와 `auc`에 사용했다.

### Titanic KNN

K=5의 예측값과 실제 label을 비교해 confusion matrix와 classification report를 만들도록 했다. 같은 metric을 사용하므로 SVM과 오류 형태를 비교할 수 있지만, 날짜 노트에는 실제 수치가 없다.

### 유방암 Decision Tree

class 2/4를 0/1로 바꾸고 tree 예측을 confusion matrix·classification report로 평가하도록 했다. 의료 예시는 FN과 FP의 비용이 다르므로 “둘 다 줄이면 된다”보다 어떤 오류가 더 치명적인지 먼저 정해야 한다.

### 2026-07-10 spam·iris 분류

- spam source는 test prediction과 label로 accuracy를 계산하도록 작성했지만 confusion matrix가 없어 일반 mail을 막은 FP와 spam을 놓친 FN을 따로 보존하지 않는다.
- iris logistic regression은 세 class의 confusion matrix·classification report를 만들도록 작성했다. multiclass에서는 class별 one-vs-rest 관점과 macro·weighted average를 함께 읽어야 한다.
- 두 source 모두 metric 호출은 있지만 실제 matrix·report·accuracy 수치가 보존되지 않아 model 우수성을 확정하지 않는다.

### 2026-07-20~21 SVM·KNN·sonar 평가

- 07-20 iris SVM은 세 class의 accuracy·confusion matrix·classification report를 계산하도록 작성했다. 07-09보다 중요한 발전은 metric 종류보다 split 뒤 train에 scaler를 fit하는 올바른 평가 순서다.
- 07-21 preference KNN은 A/B/C class의 holdout accuracy와 confusion matrix를 만든다. 14개 sample의 작은 test set으로 K까지 선택하므로 최고 accuracy를 안정적인 model 품질로 확대하지 않는다.
- sonar neural network는 10개 fold 각각의 binary cross-entropy loss와 accuracy를 모아 평균낸다. fold 평균 accuracy는 한 holdout보다 여러 분할을 반영하지만, R/M별 FP·FN이나 fold 간 표준편차를 대신하지 않는다.

holdout metric과 fold 평균은 평가 절차가 다르다. 같은 dataset·전처리·선택 과정이 아니면 숫자만 직접 비교하지 않는다. 자세한 분할·평균 책임은 [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]가 소유한다.

## macro·weighted average를 읽는 기준

`classification_report`는 class별 precision·recall·F1 외에 평균도 낸다.

- macro average: class별 값을 동일 가중치로 평균해 소수 class 성능을 드러낸다.
- weighted average: 각 class support만큼 가중해 전체 데이터 분포를 반영한다.
- binary classification에서는 Positive class의 지표와 confusion matrix를 함께 확인한다.

## 자주 헷갈리는 점

- **precision과 recall의 분모:** precision은 “Positive라고 예측한 집합”, recall은 “실제로 Positive인 집합”에서 시작한다.
- **FPR과 FN rate:** FPR은 실제 Negative 중 잘못 Positive, FNR은 실제 Positive 중 놓친 비율이다.
- **ROC와 confusion matrix:** confusion matrix는 한 threshold의 결과, ROC는 threshold를 이동한 여러 결과다.
- **AUC와 accuracy:** 서로 다른 질문에 답한다. AUC가 높아도 현재 threshold의 accuracy나 recall이 목적에 맞지 않을 수 있다.
- **metric 호출과 실제 결과:** code에 `classification_report`·`auc`가 있어도 stdout·artifact가 없으면 실제 수치나 우수성을 주장할 수 없다.

## 선행·후속 연결

- 문제 유형: [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- 안전한 평가 순서: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 수업: [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 Machine Learning 분류와 성능 평가]]
- 확장 수업: [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- SVM 재방문: [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- KNN·fold 평가: [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]], [[concepts/knn-distance-voting|KNN의 distance·voting]]
- 도구: [[entities/scikit-learn|scikit-learn]]
- 회귀 지표 대비: [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_titanic.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/e.clsss.decision_tree/breast_cancer_tree_classification.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/logisticRegression01.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf` — confusion matrix·지표·ROC/AUC 정의 보조
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/c.clsss.svm/svm_iris_data.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py`
