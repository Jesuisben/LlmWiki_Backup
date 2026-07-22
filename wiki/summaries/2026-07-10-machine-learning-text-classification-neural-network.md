---
title: 2026-07-10 텍스트 분류와 신경망 입문
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum, study-log]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/CountVectorizer01.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/logisticRegression01.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistInfo.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNet.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNetGraph.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mailList.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/checkedMail.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/iris.csv
status: growing
confidence: high
---

# 2026-07-10 텍스트 분류와 신경망 입문

## 한 줄 요약

문자열을 단어 빈도 sparse vector로 바꿔 Naive Bayes로 분류하고, iris logistic regression을 거쳐 MNIST Dense network의 입력·label·loss·optimizer·activation·평가 구조로 확장했다.

## 전체 교시·학습 순서

| 교시 | 학습 흐름 | 왜 이 단계가 필요한가 |
|---|---|---|
| 1교시 | vector의 의미 → `CountVectorizer` 매개변수 → text를 Bag of Words로 변환 | 문자열은 모델이 직접 계산할 수 없으므로 수치 feature가 필요하다. |
| 2교시 | 조건부 확률·log → 한국어 mail tokenization → sparse vector → `MultinomialNB` spam 분류 | 벡터화된 단어 빈도를 실제 지도 분류에 연결했다. |
| 3교시 | iris 4개 feature → 표준화 → logistic regression 다중 분류·확률·confusion matrix | 전날 분류 lifecycle을 다른 estimator와 3-class 문제에 반복했다. |
| 4교시 | Keras model 구성 단계 → MNIST 입력·label 구조 확인 | 전통 ML estimator에서 layer를 쌓는 신경망으로 넘어갈 입력을 확인했다. |
| 5교시 | topology 사전 학습 | 입력층·은닉층·출력층 연결을 이해하기 위한 이론 구간이다. |
| 6교시 | gradient descent·optimizer·activation → MNIST Dense network 5개 구성 | layer 수와 optimizer가 달라져도 compile→fit→evaluate 구조가 유지됨을 보았다. |
| 7교시 | one-hot encoding 복습 | 0~9 정수 label을 10차원 categorical target으로 바꾸는 이유를 확인했다. |
| 8교시 | 기록 없음 | 별도 code·output·artifact 근거가 없다. |

## 왜 이 흐름으로 배웠는가

전날에는 표의 숫자 feature로 SVM·KNN·Tree를 학습했다. 이날은 먼저 text를 숫자 feature로 표현해야 같은 분류 골격을 적용할 수 있음을 배웠다. 이어 logistic regression으로 선형 score와 class probability를 확인한 뒤, 사람이 feature를 정해 주는 전통 ML에서 여러 Dense layer가 표현을 학습하는 [[concepts/neural-network-training-basics|신경망 학습 기초]]로 이동했다.

## 대표 입력 → 처리 → 결과

### mail 제목 → sparse vector → spam label

1. **입력:** `mailList.csv`의 86개 행은 제목과 label 두 열로 구성되고 결측은 없다. 별도 `checkedMail.csv`에는 새 제목 4개가 있다.
2. **처리:** Okt로 형태소를 공백 문자열로 결합하고 `CountVectorizer.fit_transform()`으로 문서×단어 빈도 sparse matrix를 만든다.
3. **학습:** 8:2 split 뒤 `MultinomialNB.fit()`으로 일반/스팸 label을 학습한다.
4. **결과 코드:** test accuracy를 계산하고 새 제목은 기존 vectorizer의 `transform()`만 거쳐 예측하도록 작성했다.

### iris → logistic regression class

- **feature:** 꽃받침 길이·너비, 꽃잎 길이·너비 4개
- **label:** 세 붓꽃 종 중 하나
- **처리:** 150행·5열, 결측 없는 CSV를 7:3으로 나누고 train에 scaler를 fit한 뒤 test에는 transform만 적용했다.
- **결과 코드:** train/test accuracy, class별 coefficient, sample class·probability, confusion matrix·classification report와 heatmap 저장 호출이 있다.

### MNIST → Dense network

- **입력:** 노트의 embedded 구조는 train 60,000개와 test 10,000개의 28×28 grayscale image, 정수 label 0~9다.
- **처리:** image를 784열로 펼쳐 0~1로 정규화하고 label을 10차원 one-hot vector로 바꾼다.
- **모델:** menu 1~5에서 hidden Dense layer 수, `rmsprop`/`adam`, ReLU·softmax 조합을 바꾼다.
- **학습·평가 코드:** categorical cross-entropy, accuracy, 5 epochs, validation 30%, test `evaluate()`와 CSV·graph 저장 호출이 있다.

## code·output·metric·history·artifact 증거 경계

| 증거 | 확인된 사실 | 확대하면 안 되는 주장 |
|---|---|---|
| 날짜 MD의 sparse matrix block | 86×139, stored element 439라는 embedded 예시가 기록됨 | 현재 source를 이날 환경에서 다시 실행해 얻은 stdout이라는 단정 |
| 관련 `.py` 7개 | 모두 AST parse 가능하고 vectorize·fit·evaluate·save 계열 호출이 작성됨 | dependency·JVM·MNIST download·전체 runtime 성공 |
| CSV 3개 | mail 86행×2열, checked mail 4행×1열, iris 150행×5열과 결측 0을 확인 | 모든 행이 실제 수업 실행에서 끝까지 처리됐다는 단정 |
| `fit_hist.history` 접근 | 학습 history를 사용할 code가 존재 | epoch별 실제 loss·accuracy 값이 보존됐다는 단정 |
| `score`·metric 호출 | 평가 계산 의도가 존재 | 특정 정확도·우수성·일반화 성능 |
| `to_csv`·`savefig` | 결과 저장 의도가 존재 | `dataOut`이 비어 있으므로 CSV·PNG 물리 artifact 저장 성공 |
| memory model 객체 | fit/evaluate 대상으로 작성됨 | 직렬화된 model file 존재 |

## 실제 오류·불일치·미확정 실행

- spam source에는 개인 Java 환경 경로가 직접 적혀 있으나 이 위키에는 재출력하지 않고 **[REDACTED]**로만 처리한다. 해당 경로 설정과 import는 KoNLPy/JVM 실행 성공을 증명하지 않는다.
- `CountVectorizer01.py`의 마지막 주석은 2차원 배열 안의 한 행 `[0, 1, 1]`을 설명하면서 첫 단어의 빈도를 0이라고 서술하지만, 어느 vocabulary 순서의 어느 문장을 가리키는지 함께 확인해야 한다.
- logistic source는 출력 폴더를 `dataout`으로 적고 뒤에서는 heatmap 저장을 시도한다. 물리 graph가 없으므로 저장 성공은 미확정이다.
- MNIST source 주석의 `744 = 28 * 28`은 산술 오기이며 실제 계산 결과는 **784**다.
- `mnistNeuralNet.py`가 만드는 이름은 `mnist_result_01.csv` 형식인데 독립 graph source는 `mnistResult01.csv` 형식을 읽는다. 현재 상태 그대로는 앞 단계 출력과 graph 입력 이름이 일치하지 않는다.
- Keras 소개의 `compile()`은 loss·optimizer·metric 등 학습 설정을 구성하는 단계이지 일반적인 의미의 독립 “바이너리 객체 생성” 증거가 아니다.

## 헷갈린 점과 정확한 구분 기준

- **sparse matrix와 dense array:** sparse 표현은 0이 아닌 위치와 값만 효율적으로 저장한다. `.toarray()`는 작은 예시 확인에는 편하지만 큰 corpus에서는 메모리를 크게 쓸 수 있다.
- **vectorizer fit과 model fit:** vectorizer fit은 vocabulary를 만들고, classifier fit은 vector와 label 관계를 학습한다. 새 mail에는 둘 다 다시 fit하지 않는다.
- **logistic regression이 분류인 이유:** 이름에 regression이 있지만 선형 score를 sigmoid/softmax 계열 확률로 바꿔 class를 결정하는 분류 모델이다.
- **one-hot이 항상 필수인가:** categorical cross-entropy와 one-hot 조합에서는 필요하지만, sparse categorical loss를 쓰면 정수 label도 사용할 수 있다.
- **train·validation·test metric:** train은 학습 데이터, validation은 epoch·모델 선택 관찰, test는 마지막 일반화 평가다. 서로 같은 성능 증거가 아니다.
- **history·metric·model artifact:** history 객체, test score, 메모리 model, 저장 CSV·PNG·직렬화 model file은 서로 다른 산출물이다.

## 이전·다음 학습 연결

- 이전: [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 분류와 성능 평가]]의 split→fit→predict→metric 골격과 leakage 기준을 text·logistic regression에 반복했다.
- 다음: [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]에서는 label 없는 구조 탐색으로 이동한 뒤, Dense network를 이미지의 공간 구조를 이용하는 CNN으로 확장한다.
- ML-3 연결: [[summaries/2026-07-14-machine-learning-nlp-vectorization|07-14]]부터 tokenization·BoW·TF-IDF·Word2Vec와 감성 분류를 더 깊게 다룬다.

## 관련 페이지

- [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화와 Naive Bayes 분류]]
- [[concepts/neural-network-training-basics|신경망 학습 기초]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- [[entities/scikit-learn|scikit-learn]]
- [[entities/keras|Keras]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/CountVectorizer01.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/g.logstic/logisticRegression01.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistInfo.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNet.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/h.softmax/mnistNeuralNetGraph.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/Utility/keras_graph_util.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mailList.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/checkedMail.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/iris.csv`
