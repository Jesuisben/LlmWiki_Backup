---
title: 2026-07-14 NLP 표현과 Word2Vec 입문
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/movie_review.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/BEXX0003.txt
status: growing
confidence: high
---

# 2026-07-14 NLP 표현과 Word2Vec 입문

## 한 줄 요약

형태소·token·불용어에서 출발해 BoW·N-gram·TF-IDF·Word2Vec의 표현 차이를 배운 뒤, 영화 리뷰 감성 분류와 《토지》 전처리로 text를 실제 model 입력으로 바꾸는 흐름을 연결했다.

## 전체 교시·학습 순서

1. NLP와 morphology, 형태소 분석이 필요한 이유
2. tokenization과 stopword 제거
3. Bag of Words(BoW)와 CBOW 용어
4. N-gram으로 연속 token 문맥 보강
5. TF-IDF로 문서별 중요도 가중
6. Word2Vec으로 주변 문맥에서 dense embedding 학습
7. 앞선 `CountVectorizer`와 표현 방식 비교
8. 영화 리뷰 text→CountVectorizer의 BoW→MLPClassifier 감성 분류
9. 《토지》 corpus를 정제·형태소 분석해 Word2Vec 입력 token sentence 준비

## 왜 이 흐름으로 배웠는가

[[summaries/2026-07-10-machine-learning-text-classification-neural-network|07-10]]에는 단어 출현 횟수를 sparse vector로 바꿔 Naive Bayes에 넣었다. 이날은 “단어 수만 세면 문맥과 의미 관계를 어떻게 놓치는가”를 출발점으로 N-gram·TF-IDF·Word2Vec까지 표현력을 확장했다. 뒤의 감성 분류는 같은 BoW 입력을 MLPClassifier에 연결한 사례이고, 《토지》 전처리는 다음 날 Word2Vec 학습·load·similarity 실습의 입력 준비다.

## 대표 입력 → 처리 → 결과

### 영화 리뷰 감성 분류

- **입력:** `text`, `label` 두 열의 30개 review. label은 1/0 각각 15개이고 빈 cell은 없다.
- **처리:** `CountVectorizer.fit_transform()`으로 review를 BoW sparse matrix로 바꾸고 `MLPClassifier`를 label에 fit한다.
- **결과:** 새 문장 5개를 기존 vectorizer로 transform한 뒤 Positive/Negative를 예측하도록 작성됐고, 원문에는 그 문장별 prediction text가 포함된다. 별도 accuracy·probability는 보존되지 않았으며 현재 환경 재현 결과도 아니다.

### 《토지》 전처리

- **입력:** UTF-8 계열 5,882줄·793,414 bytes의 `BEXX0003.txt` corpus.
- **처리:** 제목·주석성 행 제거, regex 정제, Okt 형태소 분석, 특정 품사 token 선택, stopword 제거.
- **의도한 결과:** sentence별 token list와 Word2Vec 학습용 text file. persistence/model block 전체가 주석 처리되어 저장 의도만 확인되며 저장 파일은 없다.

## 표현 방식의 정확한 구분

| 방식 | 기본 단위 | 값 | 문맥·의미 처리 |
|---|---|---|---|
| BoW/CountVectorizer | vocabulary term | 문서 내 count | 순서와 유사 의미를 직접 보존하지 않음 |
| N-gram | 연속 N개 token | 묶음의 count | 짧은 순서를 반영하지만 차원 증가 |
| TF-IDF | vocabulary term | TF×IDF weight | 여러 문서에 흔한 단어의 가중치를 낮춤 |
| Word2Vec | token | dense vector | 주변 token 예측을 통해 유사 사용 맥락을 가까이 배치 |

원문의 CBOW 설명과 BoW는 이름이 비슷하지만 같은 것이 아니다. BoW는 문서 표현이고, CBOW는 주변 context로 중심 단어를 예측하는 Word2Vec 학습 방식이다. Skip-gram은 이날 직접 비교 실습이 없어 별도 Comparison을 만들지 않았다.

## code·output·model·artifact 증거 경계

- NLP 설명과 표는 이론이며 Python 실행 code가 아니다.
- 영화 리뷰의 CountVectorizer·MLPClassifier·`fit`·`predict`는 작성 code다.
- 새 문장 5개의 prediction 문장은 embedded text output이며 독립 재실행 결과가 아니다.
- 《토지》 전처리 뒤 file write와 Word2Vec 생성·저장 block 전체는 **주석 처리**되어 있다. 따라서 이날 token file이나 `toji.model`이 생성됐다고 볼 수 없다.
- 교육자료 `dataOut`에도 `toji.tokens`, `toji.wakati`, `toji.model`이 없다.

## 실제 오류·불일치·미확정 실행

- 원문은 BoW 설명 뒤에 CBOW를 이어 적어 둘을 혼동하기 쉽다. 문서 count 표현과 Word2Vec 학습 목적을 분리해야 한다.
- `fit`·`predict` 실행 code와 주석 처리된 file write·model save 의도는 증거 수준이 다르며, dependency·JVM·corpus 처리·학습·저장 성공도 각각 확인해야 한다.
- 개인 Java 환경 경로는 일반화할 수 없는 식별값이므로 위키에 옮기지 않았다.

## 헷갈린 점 / 질문

- **tokenization vs stopword:** 전자는 문장을 단위로 나누고, 후자는 만들어진 token 중 분석 목적에 덜 유용한 것을 제외한다.
- **count vs TF-IDF:** 둘 다 같은 vocabulary 열을 가질 수 있지만 cell 값의 의미가 다르다.
- **Word2Vec vs sentiment model:** Word2Vec은 주변 문맥에서 dense token 표현을 학습하고, 이날 감성 MLPClassifier는 CountVectorizer의 sparse BoW로 review label을 예측한다.
- **BoW MLP vs Word2Vec:** 둘 다 text를 숫자로 다루지만 입력 표현·학습 목표·artifact가 같지 않다.

## 이전·다음 연결

- 이전: [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화와 Naive Bayes 분류]], [[concepts/neural-network-training-basics|신경망 학습 기초]]
- 현재 개념: [[concepts/text-representation-bow-tfidf-word2vec|BoW·TF-IDF·Word2Vec 텍스트 표현]]
- 한국어 처리: [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]], [[entities/konlpy|KoNLPy]]
- 다음: [[summaries/2026-07-15-machine-learning-word2vec-bayesian-filter|2026-07-15 Word2Vec과 Bayesian filter 초안]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/movie_review.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/BEXX0003.txt`
