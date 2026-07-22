---
title: 한국어 텍스트 마이닝 파이프라인
created: 2026-07-13
updated: 2026-07-22
type: concept
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

# 한국어 텍스트 마이닝 파이프라인

## 정의

한국어 text를 형태소 단위로 분석해 의미 있는 token을 추출하고, 빈도표·그래프·WordCloud 또는 Machine Learning vector로 바꾸는 데이터 처리 흐름이다. 이 Vault에서는 2026-07-08 Python 수업에서 처음 등장했고, 07-10 mail 분류와 07-14~15 《토지》 Word2Vec corpus, 07-16 Bayesian filter로 확장됐다.

## 왜 중요한가

자연어는 CSV처럼 이미 행·열로 정리되어 있지 않다. 형태소 분석과 filtering으로 text를 count 가능한 feature로 바꾸는 과정은 같은 날 시작한 Machine Learning의 feature extraction·classification으로 이어지는 선행 경험이다.

## 핵심 설명

### 입력

- 분석 대상 speech text
- 복합어 인식을 보정하는 사용자 사전
- 분석 의미가 낮은 token을 제거하는 불용어 목록
- WordCloud 모양과 색을 정하는 mask image

### 처리

text 읽기 → Komoran `nouns()` 명사 추출 → 불용어 제거 → NLTK 빈도 계산 → 상위 항목 선택 → 길이·빈도 조건 filtering → Pandas DataFrame 또는 frequency dict 변환 순서다.

### 의도한 결과와 증거

code는 빈도 CSV, 상위 단어 막대그래프 PNG, mask 기반 WordCloud PNG를 저장하도록 작성되었다. 그러나 날짜 폴더에 생성 CSV·PNG·독립 notebook은 없고, “저장 완료” 문구도 프로그램이 출력하도록 작성한 문자열이다. 따라서 pipeline과 산출물 형식은 확인되지만 전체 실행 성공은 확정하지 않는다.

## 자주 헷갈리는 점

- 형태소 분석은 공백 기준 `split()`이 아니다. analyzer와 사용자 사전이 token 경계를 바꾼다.
- 불용어 제거는 형태소 분석 이후의 filtering이다. 사용자 사전과 역할이 다르다.
- 집합 차이는 제거된 token 종류를 보여 주지만 각 token의 제거 횟수는 보존하지 않는다.
- 상위 500개를 먼저 고른 뒤 길이·빈도 조건을 적용하므로 최종 단어 수는 500보다 작을 수 있다.
- KoNLPy/Komoran은 JVM에 의존한다. 설치 명령이나 개인 Java 경로가 있다고 실행 성공을 단정하지 않는다.
- WordCloud 생성과 `savefig` 성공은 별도이며 font·mask·출력 폴더도 검증해야 한다.

## 2026-07-10~16 분류·Word2Vec 입력으로의 확장

07-10 mail 분류는 Okt 형태소를 CountVectorizer의 sparse count 입력으로 바꿨다. 《토지》 text에서는 regex 정제→Okt 형태소 분석→품사 선택→stopword 제거→문장별 token list의 순서로 Word2Vec 입력을 준비했다. 07-16 Bayesian filter는 Komoran token을 category별 count와 확률 계산으로 연결했다.

형태소 분석 결과, token file write, Gensim model train/save는 서로 다른 단계다. 원문에 code와 embedded output이 있어도 교육자료 `dataOut`에 token·model artifact가 없으므로 전체 pipeline 성공으로 확대하지 않는다.

## 선행·후속 연결

- 선행: [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]의 text I/O와 regex
- 표 변환: [[entities/pandas|Pandas]] DataFrame과 CSV
- 시각화: [[entities/matplotlib|matplotlib]]와 WordCloud
- 분류 적용: [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화와 Naive Bayes 분류]], [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류]], [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|2026-07-16 Bayesian filter 완성]]
- 표현 확장: [[concepts/text-representation-bow-tfidf-word2vec|BoW·TF-IDF·Word2Vec 텍스트 표현]]과 [[entities/gensim|Gensim]]

## 관련 개념
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 한국어 텍스트 마이닝]]
- [[entities/konlpy|KoNLPy]]
- [[entities/pandas|Pandas]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
