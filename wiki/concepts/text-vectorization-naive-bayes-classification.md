---
title: 텍스트 벡터화와 Naive Bayes 분류
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/CountVectorizer01.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mailList.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/checkedMail.csv
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/bayes_test.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mail_data.csv
status: growing
confidence: high
---

# 텍스트 벡터화와 Naive Bayes 분류

## 정의

텍스트 벡터화(text vectorization)는 문장을 model이 계산할 수 있는 숫자 feature로 바꾸는 과정이다. 2026-07-10 수업에서는 `CountVectorizer`가 corpus에서 vocabulary를 학습하고, 각 문서의 단어 출현 횟수를 Bag of Words(BoW) sparse vector로 만들었다. `MultinomialNB`는 이 빈도 feature와 label의 조건부 확률을 학습해 mail 유형을 분류했다.

## 왜 중요한가

문자열 자체에는 model이 곱하고 더할 고정 열이 없다. 먼저 같은 vocabulary 기준으로 모든 문서를 같은 feature 공간에 놓아야 train mail과 새 mail을 비교할 수 있다. 이 구조는 07-14 이후 TF-IDF·Word2Vec를 이해하는 기준선이 된다.

## 입력 → 처리 → 결과

1. **입력:** 제목 text와 일반/스팸 label
2. **tokenization:** Okt 형태소를 공백으로 결합
3. **vectorizer fit:** train corpus에서 단어→열 index vocabulary 생성
4. **transform:** 각 문서를 document×term sparse matrix로 변환
5. **split·fit:** vector와 label을 나눠 Multinomial Naive Bayes 학습
6. **predict:** 새 mail은 기존 tokenizer와 vectorizer로 transform한 뒤 class 예측
7. **evaluate:** test label과 prediction으로 accuracy 계산

물리 `mailList.csv`는 86행·2열이고 결측이 없다. `checkedMail.csv`에는 별도 제목 4개가 있다. 파일 구조는 입력 가능성을 증명하지만 실제 JVM·KoNLPy·학습 실행 성공까지 증명하지 않는다.

## CountVectorizer의 핵심

| 요소 | 책임 | 주의점 |
|---|---|---|
| `fit` | corpus에서 vocabulary 학습 | test·새 문서까지 넣어 vocabulary를 만들면 평가 정보가 샐 수 있음 |
| `transform` | 기존 vocabulary 기준으로 빈도 vector 생성 | 처음 보는 단어는 vocabulary에 없으므로 표현되지 않음 |
| `fit_transform` | fit과 transform을 연속 수행 | train 입력에 사용하고 새 mail에는 재사용하지 않음 |
| `min_df` | 일정 문서 수 이상 등장한 token만 유지 | 희귀 단어 제거와 정보 손실의 trade-off |
| `stop_words` | 분석에서 제외할 token 지정 | 업무에 중요한 부정어까지 제거하지 않도록 주의 |
| `ngram_range` | 연속 token 묶음을 feature로 사용 | 문맥 표현은 늘지만 차원도 커짐 |

## sparse vector를 읽는 법

문서×단어 matrix는 대부분 0이므로 non-zero 좌표와 값만 저장하는 sparse 형식이 효율적이다. `(0, 107) 1`은 0번째 문서의 107번째 vocabulary token이 한 번 나타났다는 뜻이다. 열 번호의 의미는 반드시 해당 vectorizer의 vocabulary와 함께 읽어야 한다.

날짜 MD의 86×139·stored element 439 block은 embedded 예시다. source와 dataset 구조에는 대응하지만 현재 환경에서 재실행해 얻은 stdout으로 단정하지 않는다.

## Naive Bayes 분류

Naive Bayes는 class가 주어졌을 때 feature가 나타날 조건부 확률을 이용한다. Multinomial 변형은 단어 빈도처럼 0 이상의 count feature에 자주 사용된다. “Naive”는 class가 주어졌을 때 feature들이 조건부 독립이라는 강한 가정을 뜻하며, 현실 문장의 단어가 실제로 독립이라는 뜻은 아니다.

아주 작은 확률을 계속 곱하면 underflow가 생길 수 있어 구현은 log probability를 사용한다. log를 취하면 곱셈이 덧셈으로 바뀌고 class 사이 비교 순서는 유지된다.

## 수업 사례

- `CountVectorizer01.py`: 작은 text file을 읽어 vocabulary·token 목록·문장별 dense count array를 확인
- `spam-mail_check.py`: 한국어 형태소→sparse vector→train/test split→MultinomialNB→새 제목 분류
- 대표 model lifecycle: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]의 feature/label→split→fit→predict→evaluate를 text에 적용

## 2026-07-15 초안과 07-16 완성본

ML-3에서는 library classifier를 호출하는 수준에서 한 단계 내려가 Bayesian filter의 count와 score를 직접 구현했다. `mail_data.csv`는 `text`, `category` 40행으로 광고/일반 label이 각각 20개다.

| 책임 | 07-15 초안 | 07-16 완성본 |
|---|---|---|
| token·word count | 구현 | 유지 |
| category count·train | 구현 | 유지 |
| category별 score | `pass` | prior와 token likelihood를 log로 누적 |
| predict | `pass` | 최대 score category 반환 |

Laplace smoothing은 보지 못한 token의 likelihood가 0이 되는 것을 막는다. 그러나 작은 training set의 일반화 성능을 보장하지 않으며, 원문에는 독립 accuracy·confusion matrix가 없다. 초안 class 존재와 완성 classifier는 method body로 구분한다.

## 자주 헷갈리는 점

- **token과 vocabulary:** token은 문서에서 자른 단위이고 vocabulary는 학습 corpus에서 model feature로 채택한 token 집합이다.
- **문서 빈도와 단어 빈도:** document frequency는 token이 등장한 문서 수, term frequency는 한 문서 안 출현 횟수다.
- **CountVectorizer와 TF-IDF:** CountVectorizer는 횟수, TF-IDF는 문서 내 빈도와 corpus 희소성을 함께 반영한다. [[concepts/text-representation-bow-tfidf-word2vec|BoW·TF-IDF·Word2Vec 텍스트 표현]]이 ML-3의 비교 책임을 가진다.
- **vectorizer와 classifier:** vocabulary를 만드는 학습과 class 관계를 배우는 학습은 서로 다른 fitted 객체다.
- **accuracy와 spam 품질:** 일반 mail을 spam으로 잘못 막는 FP와 spam을 놓치는 FN의 비용은 [[concepts/classification-evaluation-metrics|분류 성능 평가]]로 따로 본다.
- **개인 환경 설정:** 원본의 로컬 Java 경로는 재현 가능한 일반 설정이 아니며 이 페이지에는 **[REDACTED]**로만 남긴다.

## 선행·후속 연결

- 선행: [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]]의 형태소·불용어·빈도 처리
- 수업: [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- 실행 구조: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 후속 수업: [[summaries/2026-07-15-machine-learning-word2vec-bayesian-filter|07-15 초안]], [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|07-16 완성본]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/CountVectorizer01.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/f.clsss.naive_bayes/spam-mail_check.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mailList.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/checkedMail.csv`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/bayes_test.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mail_data.csv`
