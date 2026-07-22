---
title: BoW·TF-IDF·Word2Vec 텍스트 표현
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji-word2vec.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji_model_test.py
status: growing
confidence: high
---

# BoW·TF-IDF·Word2Vec 텍스트 표현

## 정의

텍스트 표현(text representation)은 token을 model이 계산할 숫자로 바꾸는 방법이다. BoW는 vocabulary별 출현 횟수, TF-IDF는 문서 안 빈도와 corpus 전체 희소성을 조합한 weight, Word2Vec은 주변 문맥 예측으로 학습한 dense vector를 사용한다.

## 왜 중요한가

같은 문장도 표현 방식에 따라 model이 볼 수 있는 정보가 달라진다. 07-10 `CountVectorizer`의 sparse count가 기준선이었다면, 07-14~15에는 흔한 단어의 영향 조절과 단어 간 의미상 가까움을 표현하는 방향으로 발전했다.

## 수업에서의 입력 구조

1. **corpus:** 여러 문서 또는 token sentence 집합
2. **token:** 형태소 분석·stopword 제거를 거친 단위
3. **vocabulary:** feature 또는 embedding을 갖는 token 집합
4. **vector:** count/weight/dense coordinate
5. **downstream task:** 감성 label 분류, 유사 단어 검색, 시각화

같은 tokenization 결과를 사용해도 vector의 값과 해석은 서로 다르다.

## 한눈에 비교

| 항목 | BoW/CountVectorizer | TF-IDF | Word2Vec |
|---|---|---|---|
| vector 대상 | 문서 | 문서 | 단어 |
| 값 | token count | TF×IDF weight | 학습된 dense coordinate |
| 형태 | 대개 sparse·vocabulary 크기 | 대개 sparse·vocabulary 크기 | dense·지정 차원 |
| 순서 | 직접 보존하지 않음 | 직접 보존하지 않음 | 주변 context를 학습 목표에 반영 |
| 유사 의미 | 직접 표현하지 않음 | 직접 표현하지 않음 | 비슷한 맥락 token을 가깝게 둘 수 있음 |
| 처음 보는 token | vocabulary 밖이면 무시 | vocabulary 밖이면 무시 | 학습 vocabulary 밖이면 vector 없음 |

이 표가 독립 검색 가치가 있지만 세 방식은 하나의 선택 축이므로 별도 Comparison 대신 이 Concept가 비교 책임을 가진다.

## N-gram

N-gram은 연속한 N개 token을 하나의 feature처럼 다룬다. unigram보다 짧은 순서를 반영할 수 있지만 vocabulary와 sparse matrix 차원이 빠르게 커진다. Word2Vec의 context window도 주변 token을 사용하지만, N-gram count feature와 동일한 모델은 아니다.

## CBOW를 BoW와 구분하기

- **BoW:** 문서를 vocabulary count vector로 표현한다.
- **CBOW:** 주변 context token들로 중심 token을 예측하는 Word2Vec 학습 architecture다.
- **Skip-gram:** 중심 token으로 주변 token을 예측하는 반대 방향의 대표 architecture다.

07-14 원문은 CBOW를 설명했지만 Skip-gram을 동일 깊이로 실습하지 않았다. 따라서 CBOW vs Skip-gram Comparison은 만들지 않고 개념 경계만 남긴다.

## TF-IDF 읽기

TF는 한 문서 안에서 token이 얼마나 자주 등장하는지, IDF는 corpus 전체에서 얼마나 드문지를 반영한다. 여러 문서에 거의 모두 등장하는 token은 IDF가 낮아질 수 있다. TF-IDF가 “중요도”라고 불려도 업무 의미를 이해하거나 label과의 인과를 자동으로 판단하는 값은 아니다.

## Word2Vec 학습과 사용

07-15 Gensim source는 token sentence에서 vocabulary를 만들고 epoch 학습한 뒤 model을 저장하도록 작성됐다. 별도 source는 model을 load해 vocabulary, vector, cosine similarity, `most_similar`를 조회한다.

- `build_vocab`: 학습 token 집합과 count 구조 준비
- `train`: 주변 문맥 예측으로 vector parameter 갱신
- `save`/`load`: 학습된 vocabulary·vector 재사용
- `similarity`: 두 vector 방향의 cosine similarity
- `most_similar`: 기준 vector와 가까운 token 검색

## model·artifact 경계

07-14의 Word2Vec 학습·저장 block은 주석 처리 상태다. 07-15에는 build/train/save/load code와 embedded output이 있지만 저장소에 `toji.model`은 없다. 따라서 source가 표현한 lifecycle과 text output은 설명할 수 있어도, 현재 물리 model을 재사용하거나 결과를 재현했다고 단정하지 않는다.

## 자주 헷갈리는 점

- **문서 vector vs 단어 vector:** BoW·TF-IDF의 한 행은 문서, Word2Vec의 한 vector는 token이 기본이다. 문서 분류에 Word2Vec을 쓰려면 token vector를 pooling하거나 별도 sequence model이 필요하다.
- **빈도 vs similarity:** 많이 나온 단어와 embedding에서 가까운 단어는 같은 개념이 아니다.
- **dense가 항상 우수한가:** task·corpus 크기·OOV·해석 가능성에 따라 count/TF-IDF가 더 적절할 수 있다.
- **CBOW와 BoW:** 이름만 비슷하고 출력·학습 목적이 다르다.

## 선행·후속 연결

- token 준비: [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]]
- count 기준선: [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화와 Naive Bayes 분류]]
- 수업: [[summaries/2026-07-14-machine-learning-nlp-vectorization|2026-07-14 NLP 표현과 Word2Vec 입문]], [[summaries/2026-07-15-machine-learning-word2vec-bayesian-filter|2026-07-15 Word2Vec과 Bayesian filter 초안]]
- library: [[entities/gensim|Gensim]]
- artifact 판단: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji-word2vec.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji_model_test.py`
