---
title: 2026-07-21 KNN과 K-fold 신경망 평가
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum, study-log]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721120235.png
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721121821.png
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721130355.png
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/likelyhood.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv
status: growing
confidence: high
---

# 2026-07-21 KNN과 K-fold 신경망 평가

## 한 줄 요약

14행 선호도 데이터로 KNN의 거리·이웃 투표와 K 선택을 실습하고, 5-fold 교육 도식으로 교차 검증 원리를 익힌 뒤 208행 sonar 데이터를 10개 stratified fold로 나눠 매 fold 새 신경망의 loss·accuracy를 평가·평균하는 code로 일반화 평가를 확장했다.

## 전체 교시·학습 순서

| 교시 | 학습 흐름 | 역할 |
|---|---|---|
| 1~3교시 | 선호도 표→Min-Max scaling→holdout split→KNN→여러 K 평가→confusion matrix | KNN을 추상 설명이 아니라 작은 다중 feature 분류에 적용했다. |
| 3교시 | 새 점→거리 계산→가까운 K개→다수결→예측 도식 | [[concepts/knn-distance-voting|KNN의 distance·voting]] 원리를 시각적으로 고정했다. |
| 3교시 | 과적합·일반화→5-fold 교육 도식 | 한 번의 split에만 맞춘 성능을 줄이는 평가 방법으로 이동했다. |
| 3~8교시 | sonar 60 feature→label encoding→10-fold→매 fold 신경망 생성·fit·evaluate→평균·graph 저장 code | K-fold를 실제 binary neural network 평가 loop에 연결했다. |

## 왜 이 흐름으로 배웠는가

07-09에는 KNN을 Titanic 분류기의 하나로 보았고 과적합을 개념으로 소개했다. 이날은 작은 preference dataset으로 distance·vote와 K 변화의 효과를 직접 드러낸 뒤, 한 holdout split에서 얻은 “최적 K”가 다른 데이터에도 일반화된다고 보장할 수 없다는 문제로 연결했다. 이어 K-fold에서 train/test 역할을 순환하고 fold별 metric을 평균하는 방법을 Keras 신경망에 적용했다.

## 대표 입력 → 처리 → 결과

### preference KNN

1. **입력:** `likelyhood.csv`는 header와 14개 data row, 7개 수치 feature, A/B/C label로 구성되며 결측은 없다. class 수는 A 5, B 4, C 5다.
2. **전처리:** 각 feature를 열별 Min-Max 식으로 0~1 범위에 맞춘다.
3. **분할:** 날짜 code는 8:2 holdout과 `random_state=100`을 사용한다.
4. **학습:** K=3 모델을 fit한 뒤 K=1,3,5,7,9의 test accuracy를 비교한다.
5. **선택·평가:** 가장 높은 holdout accuracy의 K로 새 모델을 만들고 prediction과 confusion matrix를 계산하도록 작성했다.
6. **저장 의도:** K별 accuracy 막대그래프와 confusion matrix heatmap PNG 저장 호출이 있다.

14개 표본에서 test는 매우 작으므로 “최고 정확도”는 그 split에서의 값일 뿐 안정적인 최적 K나 전체 model 품질을 증명하지 않는다. K를 같은 test set으로 고르고 다시 같은 test set으로 평가하면 test가 model 선택에 사용되는 편향도 생긴다.

### sonar 10-fold neural network

1. **입력:** `sonarTest.csv`는 header 없는 208행×61열이고, 앞 60열은 수치 feature, 마지막 열은 R 97개·M 111개 binary label이며 결측은 없다.
2. **label:** 문자열 R/M을 `LabelEncoder`로 숫자화한다.
3. **fold:** `StratifiedKFold(n_splits=10, shuffle=True, random_state=0)`가 class 비율을 고려해 train/test index를 10번 만든다.
4. **model:** 각 fold 안에서 `Sequential`을 새로 만들고 Dense 24 ReLU→Dense 10 ReLU→Dense 1 sigmoid를 구성한다.
5. **학습·평가:** 해당 fold train index로 200 epochs, batch 5 학습하고 test fold에서 loss와 accuracy를 한 번씩 얻는다.
6. **집계:** fold별 loss·accuracy list와 각각의 평균을 계산한다.
7. **저장 의도:** fold별 loss line, accuracy line/bar, loss+accuracy 이중축 PNG 네 개를 저장하도록 작성했다.

## feature·label·split·fold 구조

| 사례 | feature | label | 분리 구조 | 결과 해석 |
|---|---|---|---|---|
| preference KNN | 7개 선호 특성 | A/B/C | 한 번의 80/20 holdout | 그 split의 accuracy와 matrix |
| sonar neural network | 60개 sonar 신호 | R/M | stratified 10-fold | 10개 fold loss·accuracy와 평균 |

K-fold에서 각 행은 한 번 test fold에 들어가지만, 매 반복의 모델은 서로 다른 train subset에서 학습한 별도 모델이다.

## 첨부 3개 실제 픽셀과 MD·code 대응

### KNN 최근접 이웃 vote 도식

`Pasted image 20260721120235.png`에는 파란 구매자 점, 빨간 비구매자 점, 새 녹색 점, 녹색·빨간 반경 원이 있다. 녹색 원 안의 가까운 이웃과 더 넓은 빨간 원의 이웃 구성이 달라 K에 따라 vote 결과가 달라질 수 있음을 보여 준다. 오른쪽 문구도 “녹색은 구매자일까/비구매자일까, 녹색에 가장 가까운 항목”을 묻는다. 이는 교육 개념도이지 preference code의 실제 prediction plot이 아니다.

### neural network topology 도식

`Pasted image 20260721121821.png`는 입력 `i1`, `i2`, hidden 1·2의 `h11 … h1n`, output `o1`을 완전 연결 화살표로 그린다. hidden에는 ReLU, output에는 sigmoid가 표시된다. 실제 code는 입력 feature 60개, hidden unit 24·10개, output 1개이므로 그림의 2개 입력과 생략 기호는 **개념 축약 표현**이지 실제 node 수를 1:1로 그린 topology가 아니다.

### 5-fold cross-validation 도식

`Pasted image 20260721130355.png`는 dataset을 5개 block으로 나누고 파란 4개 train block과 주황 1개 test block을 다섯 행에서 순환한다. 결과 01~05를 얻어 “5개의 산술 평균”을 내는 구조다. 절차는 code와 같지만 그림은 **5-fold**, 날짜 code는 `n_splits=10`인 **10-fold**다. 그림의 fold 수를 code 실행 설정으로 옮겨 쓰면 안 된다.

## fold별 metric·평균·전체 품질 구분

- fold별 loss/accuracy는 해당 반복의 train subset과 test fold에서 새로 학습한 한 모델의 평가다.
- 평균은 10개 평가의 중심 수준이며 한 split보다 덜 우연적일 수 있다.
- 표준편차·범위가 없으면 fold 간 변동성을 충분히 알 수 없다.
- cross-validation 평균은 운영용 최종 model artifact가 아니다. 전체 데이터 재학습·독립 test 평가·재현성 확인이 별도로 필요하다.
- accuracy만으로 R/M class별 FP·FN 비용이나 calibration을 알 수 없다.

## fold 내부 preprocessing과 leakage

sonar 날짜 code는 “이미 표준화로 만들어진 데이터”라고 설명하고 별도 scaler를 fit하지 않는다. 이 설명은 물리 CSV의 각 feature가 어떤 과정으로 표준화되었는지, 그 통계가 전체 데이터에서 계산됐는지까지 증명하지 않는다.

일반 원칙은 다음과 같다.

1. 각 fold의 train/test index를 먼저 정한다.
2. 결측 대체·encoding vocabulary·scaler처럼 분포를 학습하는 전처리는 **그 fold의 train subset에만 fit**한다.
3. test fold에는 같은 transformer의 `transform`만 적용한다.
4. 모든 데이터에 전처리를 fit한 뒤 K-fold를 돌리면 각 test fold의 정보가 train 과정에 새어 든다.
5. scikit-learn `Pipeline`처럼 전처리와 estimator를 묶으면 fold 내부 fit을 강제하기 쉽다.

## code·output·metric·history·model·graph·artifact 경계

| 층 | 확인된 범위 | 확인되지 않은 범위 |
|---|---|---|
| 날짜 MD code | KNN holdout·K 선택과 sonar 10-fold neural loop·graph save code | 전체 runtime 성공 |
| 독립 source | KNN·K-fold `.py` 2개 AST parse 가능 | 날짜 MD와 같은 version·입력으로 실행됨 |
| dataset | preference 14×8, sonar 208×61 구조 확인 | 날짜 code가 모든 row를 끝까지 처리함 |
| metric | score/evaluate와 fold list·평균 계산 code | 실제 fold별 수치·평균 |
| history | sonar code는 `fit` 반환 History를 저장하지 않음 | epoch별 train/validation curve |
| model | 매 fold 메모리 model 생성 code | 직렬화 model·최종 전체-data model |
| graph | `savefig` 호출 4개 및 KNN graph 호출 | `dataOut`에 PNG가 없어 실제 graph artifact 없음 |

## 실제 오류·불일치·미확정 실행

- 날짜 preference code는 8:2·고정 seed·홀수 K 1~9·best K 재학습이지만 독립 `knn_likelyhood.py`는 7:3·seed 없음·K 1~3이고 마지막 loop model로 예측한다. 같은 학습 주제의 다른 code version이며 날짜 실행을 독립 source가 그대로 증명하지 않는다.
- preference code는 split 전에 전체 14행으로 각 열의 min/max를 계산한다. test 분포가 전처리에 섞이는 leakage다. split 후 train min/max로 fit하고 test에는 같은 기준을 적용해야 한다.
- 날짜 sonar code는 `sonarTest.csv`와 public `tensorflow.keras` import, graph 4개 저장을 사용한다. 독립 `sonarTestKFold.py`는 실제로 `surgeryTest.csv`를 읽고 `tensorflow.python.keras`를 import하며 평균 출력에서 끝난다.
- 두 dataset은 동일하지 않다. sonar는 208×61·R/M, surgery는 470×18·0/1이며 byte hash도 다르다. 독립 source 주석은 R/M이라고 적었지만 실제 지정 파일 label은 0/1이다.
- topology 그림의 입력 2개와 hidden 생략 노드는 60-24-10-1 code를 축약한 것이며 실제 unit 수 불일치가 model 오류를 뜻하지는 않는다.
- `fit`, `evaluate`, `savefig` 호출은 실행·metric·저장 성공을 자동 증명하지 않는다. 실제 stdout·History·PNG·직렬화 model은 보존되지 않았다.

## 헷갈린 점과 정확한 구분 기준

- **K와 fold 수:** KNN의 K는 투표할 이웃 수이고, K-fold의 K는 데이터를 나눌 fold 수다.
- **holdout vs K-fold:** holdout은 한 분할의 test 성능, K-fold는 여러 순환 분할의 평가 분포와 평균을 본다.
- **5-fold 그림 vs 10-fold code:** 같은 절차를 설명하지만 실행 설정이 다르다.
- **fold 평균 vs 최종 모델:** 평균은 평가 요약이지 저장된 하나의 모델이 아니다.
- **loss·accuracy·History:** fold의 `evaluate` loss/accuracy와 epoch별 History는 다른 기록이다. 이날은 History를 변수에 보존하지 않는다.
- **graph code vs graph artifact:** 저장 함수가 있어도 물리 PNG가 없으면 graph는 계획/code-only다.

## 이전·다음 학습 연결

- 이전: [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]에서 holdout과 train-only scaling을 복습했다.
- KNN 선행: [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 분류와 성능 평가]]
- 신경망 선행: [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- 과목 마무리: 07-08~21 전체 날짜에서 반복된 lifecycle·평가·artifact 경계를 과목 통합 고정점으로 교차 검증한다.

## 관련 페이지

- [[concepts/knn-distance-voting|KNN의 distance·voting]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/neural-network-training-basics|신경망 학습 기초]]
- [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- [[entities/scikit-learn|scikit-learn]]
- [[entities/keras|Keras]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721120235.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721121821.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721130355.png`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/d.clsss.knn/knn_likelyhood.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/sonarTestKFold.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/likelyhood.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/sonarTest.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/surgeryTest.csv`
