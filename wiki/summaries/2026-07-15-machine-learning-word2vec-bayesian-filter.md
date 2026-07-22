---
title: 2026-07-15 Word2Vec과 Bayesian filter 초안
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji-word2vec.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji_model_test.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/bayes_test.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mail_data.csv
status: growing
confidence: high
---

# 2026-07-15 Word2Vec과 Bayesian filter 초안

## 한 줄 요약

전날 준비한 《토지》 token으로 Gensim Word2Vec의 학습/save/load·vocabulary·similarity·WordCloud 흐름을 작성하고, Bayesian mail filter의 tokenization·`fit()` 골격까지 진행했다.

## 전체 교시·학습 순서

1. 《토지》 원문을 문장별 token으로 변환
2. token sentence를 Word2Vec 학습 corpus로 구성
3. `Word2Vec` 생성자 기반 학습·`save`와 `load` code 작성
4. vocabulary key·vector와 단어 간 similarity 조회
5. 유사도 상위 단어를 bar chart와 WordCloud로 표현
6. Naive Bayes의 prior·likelihood·posterior 복습
7. `BayesianFilter`의 tokenization과 `fit()` 골격 작성
8. `increase_word()`·`sample()`이 `pass`여서 count·score·predict가 미완성인 상태 확인

## 왜 이 흐름으로 배웠는가

[[summaries/2026-07-14-machine-learning-nlp-vectorization|07-14]]가 token과 표현 방식의 이론·입력 준비였다면, 이날은 Word2Vec model 객체를 만들고 다시 읽어 vocabulary와 similarity를 사용하는 lifecycle로 이동했다. 마지막 Bayesian filter는 [[concepts/text-vectorization-naive-bayes-classification|07-10 MultinomialNB]]의 library API를 확률 count 관점에서 직접 구현해 보는 단계이며, 다음 날 완성본과 대비된다.

## 대표 입력 → 처리 → 결과

### Word2Vec

- **입력:** 《토지》에서 만든 문장별 token list.
- **처리:** token sentence를 Gensim `Word2Vec` 생성자에 전달해 학습 → model save → 독립 source에서 load.
- **결과 형태:** token vocabulary, dense vector, `similarity`, `most_similar`, bar chart와 WordCloud.

원문에는 vocabulary·vector·유사 단어를 출력하는 code가 있지만 실제 숫자·목록 output은 보존되지 않았다. 현재 저장소에도 `toji.model`이 없으므로 학습·저장·load 성공은 미확정이다.

### Bayesian filter 초안

- **입력:** `mail_data.csv`의 `text`, `category` 40행. `광고`/`일반` 각각 20행이며 빈 cell은 없다.
- **처리:** 형태소를 token으로 분해하고 `fit()`에서 각 token을 `increase_word()`에 전달하는 골격까지 작성했다.
- **결과:** `increase_word()`와 `sample()`이 `pass`이고 category count·score·predict method도 아직 없어 count와 분류가 모두 미완성이다.

## code 상태와 artifact 경계

| 근거 | 확인 가능한 것 | 확인할 수 없는 것 |
|---|---|---|
| 생성자 기반 train/save code | model 생성·학습·저장 의도 | dependency·학습·저장 성공 |
| load/similarity code | 저장 model 재사용 절차 | 현재 `toji.model` load 가능성 |
| vocabulary·similarity 출력 code | 출력하려는 값의 종류 | 실제 숫자·목록 output과 code version·환경 연결 |
| `pass`가 있는 Bayesian source | tokenization·`fit()` 호출 골격 | count·score·predict 완성 및 정확도 |
| `savefig`·WordCloud code | graph 저장 의도 | 물리 PNG 존재 |

교육자료 `dataOut`은 비어 있고 `toji.tokens`, `toji.wakati`, `toji.model`, Word2Vec/WordCloud PNG가 없다. source tree에도 `.model` 파일이 없다.

## WordCloud가 보여 주는 것

WordCloud는 model의 유사 단어와 score를 frequency dictionary처럼 받아 시각적으로 크게 표시한다. 단어가 크게 보이는 것은 이 실습에서 전달한 유사도 값이 크다는 뜻이지 corpus 원빈도나 분류 중요도가 높다는 뜻은 아니다.

## 실제 오류·불일치·미확정 실행

- 원문에는 model 저장·load·출력 code가 있지만 실제 output과 물리 `toji.model`은 없다. code·output·artifact를 분리한다.
- Bayesian 초안은 class와 `fit()` 골격이 있어도 `increase_word()`·`sample()`이 `pass`이고 category count·score·predict가 없어 classifier 완성본이 아니다.
- 개인 Java 환경 경로는 위키에서 비노출 처리했다.
- 독립 Python source 3개는 정적 AST parse가 성공했지만 import·실행 검증은 하지 않았다.

## 헷갈린 점 / 질문

- **vocabulary와 vector:** vocabulary는 학습된 token 집합, vector는 각 token에 대응하는 숫자 좌표다.
- **similarity와 확률:** cosine similarity는 embedding 방향의 가까움이며 분류 probability가 아니다.
- **save/load code와 artifact:** 호출이 존재해도 file이 물리적으로 남았는지 확인해야 재사용 가능하다고 말할 수 있다.
- **초안과 완성본:** class 이름보다 method body와 반환 경로를 확인해야 한다.

## 이전·다음 연결

- 이전: [[summaries/2026-07-14-machine-learning-nlp-vectorization|2026-07-14 NLP 표현과 Word2Vec 입문]]
- 표현 개념: [[concepts/text-representation-bow-tfidf-word2vec|BoW·TF-IDF·Word2Vec 텍스트 표현]]
- library: [[entities/gensim|Gensim]], [[entities/konlpy|KoNLPy]]
- 다음: [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|2026-07-16 Bayesian filter 완성과 사전 학습 모델]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji-word2vec.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji_model_test.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/bayes_test.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mail_data.csv`
