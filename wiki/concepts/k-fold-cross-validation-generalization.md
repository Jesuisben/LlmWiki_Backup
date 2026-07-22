---
title: K-fold 교차 검증과 일반화
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721130355.png
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv
status: growing
confidence: high
---

# K-fold 교차 검증과 일반화

## 정의

K-fold cross-validation은 데이터를 K개의 fold로 나누고, 매 반복마다 한 fold를 validation/test 역할로 두고 나머지 K-1개로 model을 학습해 K개의 평가 결과를 얻는 방법이다. 모든 sample이 한 번씩 평가 fold가 되므로 한 번의 train/test split보다 분할 우연에 덜 의존하는 성능 추정치를 얻을 수 있다.

## 왜 중요한가

과적합(overfitting)은 model이 train data의 pattern뿐 아니라 noise까지 지나치게 맞춰 unseen data 성능이 떨어지는 상태다. 목표는 train score를 최대화하는 것이 아니라 새로운 데이터에도 규칙이 유지되는 일반화(generalization)다. 07-09에는 과적합을 개념으로 배웠고, 07-20 holdout 복습 뒤 07-21에 K-fold 도식과 sonar neural network loop로 실제 평가 구조를 만들었다.

## 기본 절차

1. dataset을 K개 fold로 나눈다.
2. 첫 번째 fold를 평가용, 나머지를 train용으로 사용한다.
3. model을 새로 만들고 train fold들에 fit한다.
4. 남겨 둔 fold에서 metric을 계산한다.
5. 평가 fold를 바꾸며 K번 반복한다.
6. K개 metric의 평균과 변동성을 함께 본다.

매 fold에서 model을 새로 초기화해야 한다. 앞 fold에서 학습한 weight를 다음 fold에 이어 쓰면 평가 fold 정보가 간접적으로 섞이고 서로 독립적인 K개 평가가 아니다.

## train/test split과 K-fold 비교

| 항목 | 한 번의 holdout split | K-fold cross-validation |
|---|---|---|
| 분할 | train/test 한 번 | 평가 fold를 K번 순환 |
| metric | 한 개 | K개 분포와 평균 |
| 계산 비용 | 비교적 낮음 | model을 K번 학습해 높음 |
| 분할 우연 | 상대적으로 큼 | 여러 분할을 평균해 줄일 수 있음 |
| 용도 | 충분한 데이터의 빠른 기준선·최종 독립 test | model/hyperparameter 비교·작은 데이터의 안정적 추정 |

둘은 배타적이지 않다. 전체 데이터에서 독립 test를 먼저 떼어 두고, 남은 train 영역 안에서 K-fold로 model을 선택한 뒤 마지막에 test를 한 번 평가할 수 있다.

## 5-fold 도식과 10-fold code

`Pasted image 20260721130355.png`는 5개 block 중 주황색 한 block을 test로, 파란색 네 block을 train으로 순환해 결과 01~05의 산술 평균을 내는 **5-fold 설명도**다.

07-21 sonar code는 `n_fold=10`과 `StratifiedKFold(n_splits=10)`을 사용한다. 따라서 절차는 같지만 실제 설정은 다음처럼 다르다.

| 근거 | fold 수 | train/test 반복 |
|---|---:|---|
| 첨부 교육 도식 | 5 | 4개 train + 1개 test를 5번 |
| 날짜 sonar code | 10 | 9개 train + 1개 test를 10번 |

도식은 원리를 설명하며 code의 실행 결과나 정확한 10-fold 배치를 그린 것이 아니다.

## Stratified K-fold

분류 데이터에서 `StratifiedKFold`는 각 fold의 class 비율이 전체와 비슷하도록 나누려 한다. sonar dataset은 R 97개, M 111개로 완전히 같지는 않으므로 단순 분할보다 class 비율을 유지하는 것이 평가 변동을 줄이는 데 도움 된다.

- stratification은 class 비율을 다룬다.
- 같은 개체·시간·그룹에서 나온 sample의 독립성까지 자동 보장하지 않는다.
- time series나 동일 사용자 반복 측정에는 시간·group 전용 split이 필요할 수 있다.

## fold 내부 preprocessing과 leakage

K-fold에서 전처리는 fold 바깥에서 한 번 fit하는 것이 아니라 **각 fold 안에서 다시 fit**해야 한다.

1. 현재 fold의 train/test index를 얻는다.
2. 결측 대체, scaler, feature selector, text vectorizer를 train fold에만 fit한다.
3. train fold와 test fold를 같은 transformer로 transform한다.
4. 변환된 train으로 model을 fit하고 test fold를 evaluate한다.
5. 다음 fold에서는 transformer와 model을 새로 만든다.

전체 dataset으로 min/max·평균·vocabulary·선택 feature를 정한 뒤 cross-validation하면 모든 평가 fold의 정보가 preprocessing에 들어간다. scikit-learn에서는 transformer와 estimator를 `Pipeline`으로 묶고 cross-validation 함수에 넘기는 방식이 이 경계를 지키기 쉽다.

07-21 sonar 날짜 code는 입력이 이미 표준화됐다고 서술하지만, 현재 물리 CSV만으로 원래 scaling 통계가 어느 범위에서 계산됐는지는 확인되지 않는다. 따라서 누수 없음으로 확정하지 않는다.

## 수업 사례: sonar neural network

- input: header 없는 208×61 CSV의 수치 feature 60개
- label: Rock/Mine 문자열 1개를 encoding한 binary target
- split: shuffle과 seed를 가진 stratified 10-fold
- topology: Dense 24 ReLU→Dense 10 ReLU→Dense 1 sigmoid
- 학습: fold마다 새 model, 200 epochs, batch size 5
- 평가: test fold의 binary cross-entropy loss와 accuracy
- 집계: loss 10개·accuracy 10개와 각각의 평균
- 저장 의도: fold별 loss/accuracy graph 4개

이 code는 [[concepts/neural-network-training-basics|신경망 학습 기초]]를 한 번의 holdout이 아니라 반복 평가에 적용한 사례다.

## fold별 metric과 평균을 읽는 법

- fold별 metric은 서로 다른 train/test subset에서 학습한 서로 다른 model의 결과다.
- 평균 accuracy는 일반적인 중심 수준을 요약하지만 class별 오류를 숨길 수 있다.
- 평균 loss는 confidence까지 반영할 수 있어 accuracy와 다른 순위를 낼 수 있다.
- 평균만 있고 표준편차·최솟값·최댓값이 없으면 분할 민감도를 충분히 알 수 없다.
- K-fold 결과는 하나의 배포 model이 아니다. 선택 뒤 전체 train data로 최종 model을 다시 학습하고 독립 test나 운영 검증을 거쳐야 한다.

### holdout metric vs fold 평균

한 holdout의 accuracy와 K-fold 평균 accuracy는 같은 종류의 숫자처럼 보여도 평가 절차가 다르다. 데이터 범위, preprocessing, random seed, class 분포, hyperparameter 선택 과정이 같지 않으면 숫자를 직접 우열 비교하면 안 된다.

## code·metric·History·model·graph·artifact 경계

| 근거 | 증명하는 것 | 증명하지 않는 것 |
|---|---|---|
| `StratifiedKFold` loop code | 10번 분할·학습·평가하려는 절차 | loop의 runtime 성공 |
| `cost`·`accuracy` append | fold metric을 모을 의도 | 실제 list 값·평균 수치 |
| `model.fit` | fold별 parameter 학습 호출 | History가 보존됐다는 사실 |
| `model.evaluate` | fold test loss·accuracy 계산 호출 | 높은 일반화 성능 |
| `savefig` | graph 저장 의도 | 물리 PNG artifact |
| serialized model 없음 | 최종 배포 model artifact 미확인 | 메모리 model이 한 번도 생성되지 않았다는 뜻 |

날짜 code는 `fit()` 반환값을 변수에 저장하지 않으므로 epoch별 History는 보존하지 않는다. `dataOut`에도 해당 PNG가 없어 graph artifact는 확인되지 않는다.

## 독립 source와 날짜 code의 불일치

교육자료 `sonarTestKFold.py`라는 filename과 내부 내용은 일치하지 않는다.

- 날짜 code: `sonarTest.csv`, 208×61, R/M, public `tensorflow.keras`, graph 4개 포함
- 독립 source: `surgeryTest.csv`, 470×18, 0/1, `tensorflow.python.keras`, 평균 출력에서 종료
- 독립 source 주석은 label을 R/M이라고 적지만 지정된 surgery dataset의 실제 label은 0/1이다.

따라서 독립 source는 K-fold neural loop의 변형을 보여 주는 보조 자료일 뿐, 날짜 sonar code의 동일 실행본이나 결과 증거가 아니다.

## 자주 헷갈리는 점

- **KNN의 K와 K-fold의 K:** 이웃 수와 데이터 분할 수로 완전히 다른 hyperparameter다.
- **validation fold와 최종 test:** model 선택에 cross-validation을 썼다면 별도 test는 마지막 확인용으로 남겨야 한다.
- **평균과 안정성:** 평균 하나만으로 fold 간 편차를 알 수 없다.
- **cross-validation과 학습 완료:** K개 model을 평가한 것이 최종 model 저장을 뜻하지 않는다.
- **preprocessing code 없음과 누수 없음:** 이미 전처리된 dataset이라면 그 생성 과정까지 봐야 누수 여부를 판단할 수 있다.
- **5-fold image와 10-fold run:** 원리 설명과 실행 설정을 분리한다.

## 선행·후속 연결

- 공통 lifecycle: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 분류 metric: [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- 신경망: [[concepts/neural-network-training-basics|신경망 학습 기초]]
- KNN 선택: [[concepts/knn-distance-voting|KNN의 distance·voting]]
- holdout 복습: [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- 적용 수업: [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]]
- 도구: [[entities/scikit-learn|scikit-learn]], [[entities/keras|Keras]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721130355.png`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv`
