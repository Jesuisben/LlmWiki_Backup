---
title: KoNLPy
created: 2026-07-13
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
status: growing
confidence: high
---

# KoNLPy

## 무엇인가

KoNLPy는 한국어 형태소 분석을 위한 Python 라이브러리다.

## 이 위키에서의 맥락

2026-07-08 Python 수업에서 처음 등장했다. Komoran analyzer에 사용자 사전을 전달해 복합어 인식을 보정하고, speech text에서 명사를 추출하는 한국어 text mining 실습에 사용했다. JVM 의존성이 있어 Java 실행 환경이 필요하다.

## 실제 수업 역할

1. text와 사용자 사전 file을 입력으로 받는다.
2. Komoran의 `nouns()`로 명사 token list를 만든다.
3. 불용어 제거·NLTK 빈도 계산·Pandas CSV·matplotlib/WordCloud의 입력으로 넘긴다.

사용자 사전은 token 경계를 보정하고 불용어는 분석 후 token을 제거하므로 역할이 다르다.

### 2026-07-10~16 Machine Learning 확장

- 07-10에는 Okt로 mail 제목을 형태소 token 문자열로 바꿔 CountVectorizer·MultinomialNB 입력에 넘겼다.
- 07-14에는 영화 review 자체가 아니라 《토지》 corpus를 Okt 형태소·품사 기준 token sentence로 바꿨다.
- 07-15에는 전날 준비한 token corpus를 이어 Gensim Word2Vec 입력으로 사용했다.
- 07-15~16 Bayesian mail filter에서는 Komoran으로 text를 word count·category score 단위로 나누는 전처리를 담당했다.

KoNLPy는 token을 만들지만 Word2Vec vector 학습·Bayesian score·MLP parameter 학습은 각각 Gensim과 classifier/model의 책임이다.

## 설치·실행 증거 경계

노트에는 package 설치 명령과 JVM용 Java 위치 설정 code가 있지만 설치 성공 output은 없다. 개인 환경 경로는 위키에 보존하지 않는다. 빈도·CSV·PNG 저장 code도 있으나 생성 artifact가 날짜 raw에 없으므로 전체 pipeline 성공을 단정하지 않는다.

## 자주 헷갈리는 점

- KoNLPy는 library이고 Komoran은 그 안에서 사용하는 analyzer 중 하나다.
- `nouns()` 결과는 analyzer·사전·입력 text에 따라 달라진다.
- Java가 설치되어 있다는 사실과 현재 Python process에서 JVM이 정상 시작되는 것은 별도다.
- WordCloud는 KoNLPy 기능이 아니라 후속 frequency dictionary 시각화다.

## 관련 개념
- [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]]
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 한국어 텍스트 마이닝]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/text-representation-bow-tfidf-word2vec|BoW·TF-IDF·Word2Vec 텍스트 표현]]
- [[entities/gensim|Gensim]]

## 프로젝트/면접에서 설명할 관점

“KoNLPy는 한국어 text를 형태소 token으로 바꾸는 전처리 계층이며, CountVectorizer·Gensim·Bayesian classifier가 각각 vector·embedding·score를 학습한다. analyzer 실행과 후속 model·artifact 성공은 별도 증거다”라고 설명할 수 있다.

## 출처
- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
