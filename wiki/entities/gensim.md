---
title: Gensim
created: 2026-07-22
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji-word2vec.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji_model_test.py
status: growing
confidence: high
---

# Gensim

## 무엇인가

Gensim은 corpus 기반 topic modeling과 vector-space model을 다루는 Python library다. 이 위키에서는 2026-07-14~15에 `Word2Vec` model을 build·train·save·load하고 token vector와 similarity를 조회하는 API로 등장했다.

## 이 위키에서의 맥락

KoNLPy가 한국어 문장을 형태소 token으로 나누는 전처리를 담당했다면, Gensim은 token sentence를 입력받아 embedding parameter를 학습하고 재사용하는 model 계층을 담당했다. [[entities/matplotlib|matplotlib]]과 WordCloud는 그 유사 단어 결과를 시각화했다.

## 첫 등장과 날짜별 역할

### 2026-07-14

- Word2Vec·CBOW 개념 소개
- 《토지》 corpus를 형태소 token sentence로 준비
- model build/train/save block은 주석 처리 상태

### 2026-07-15

- `Word2Vec` 객체에 token sentence 입력
- `build_vocab`과 epoch 학습 code
- `save` 후 별도 source에서 `load`
- vocabulary key·vector·`similarity`·`most_similar` 조회
- 유사도 bar chart·WordCloud 연결

## 핵심 API와 책임

| API/속성 | 책임 |
|---|---|
| `Word2Vec(...)` | architecture·vector size·window·worker 등 설정 |
| `build_vocab` | corpus token을 세어 vocabulary 구성 |
| `train` | context prediction으로 vector parameter 갱신 |
| `save`/`load` | model artifact 직렬화·복원 |
| `wv.index_to_key` | 학습 vocabulary 순서 조회 |
| `wv[token]` | token vector 조회 |
| `wv.similarity` | 두 token vector의 cosine similarity |
| `wv.most_similar` | 가까운 token과 score 검색 |

## 실행·artifact 경계

import와 API 호출은 Gensim을 사용하려는 source를 증명하지만 package 설치·학습 성공을 증명하지 않는다. embedded vector·similarity output이 남아 있어 실행 정황은 있으나 저장소에 `toji.model`이 없다. 따라서 현재 model load 재현 가능성은 미확정이다.

## 자주 헷갈리는 점

- Gensim은 형태소 analyzer가 아니다. 한국어 token 준비는 [[entities/konlpy|KoNLPy]] 등 별도 도구의 책임이다.
- vocabulary가 있다는 것과 모든 원문 단어가 vector를 가진다는 것은 다르다. filtering 조건에 따라 OOV가 생긴다.
- similarity는 embedding 관계이며 감성 label probability가 아니다.
- WordCloud graph는 Gensim model 자체가 아니라 조회 결과를 받은 별도 시각화다.

## 관련 개념

- [[concepts/text-representation-bow-tfidf-word2vec|BoW·TF-IDF·Word2Vec 텍스트 표현]]
- [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[summaries/2026-07-14-machine-learning-nlp-vectorization|2026-07-14 NLP 표현과 Word2Vec 입문]]
- [[summaries/2026-07-15-machine-learning-word2vec-bayesian-filter|2026-07-15 Word2Vec과 Bayesian filter 초안]]

## 프로젝트/면접에서 설명할 관점

“Gensim은 tokenized corpus에서 Word2Vec vocabulary와 embedding을 학습하고 similarity를 조회·저장하는 library다. 형태소 분석·시각화와 책임이 다르며, source의 save/load code와 실제 model artifact 존재는 따로 검증해야 한다”고 설명할 수 있다.

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji-word2vec.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/toji_model_test.py`
