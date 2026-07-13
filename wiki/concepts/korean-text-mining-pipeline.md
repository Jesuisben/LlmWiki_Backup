---
title: 한국어 텍스트 마이닝 파이프라인
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md
status: growing
confidence: high
---

# 한국어 텍스트 마이닝 파이프라인

## 정의
한국어 텍스트를 형태소 단위로 분석해 의미 있는 단어를 추출하고, 빈도표·그래프·워드클라우드로 표현하는 데이터 처리 흐름이다.

## 핵심 설명
수업에서는 텍스트 파일을 읽고 Komoran의 `nouns()`로 명사를 추출했다. 사용자 사전으로 복합어 인식을 보정하고, 불용어를 제거한 뒤 NLTK 빈도 결과를 Pandas DataFrame/CSV로 저장했다. 길이·빈도 조건을 통과한 단어는 matplotlib 막대 그래프와 WordCloud로 시각화했다.

## 자주 헷갈리는 점
형태소 분석은 단순 `split()`이 아니며, 사용자 사전과 불용어가 결과를 바꾼다. KoNLPy는 JVM에 의존하므로 실행 PC의 Java 환경을 확인하지만, 개인 경로 자체는 문서에 보존하지 않는다.

## 관련 개념
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 한국어 텍스트 마이닝]]
- [[entities/konlpy|KoNLPy]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
