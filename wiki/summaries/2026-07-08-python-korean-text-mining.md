---
title: 2026-07-08 Python 한국어 텍스트 마이닝
created: 2026-07-13
updated: 2026-07-13
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md
status: growing
confidence: high
---

# 2026-07-08 Python 한국어 텍스트 마이닝

## 한 줄 요약
KMDB Open API 활용 흐름을 간단히 확인하고, KoNLPy·Komoran·NLTK로 한국어 텍스트의 명사·빈도를 분석해 CSV·그래프·WordCloud로 표현했다.

## 배운 내용
KoNLPy는 JVM을 사용하므로 Java 실행 환경이 필요하다. Komoran에 사용자 사전을 주면 특정 복합어를 하나의 형태소로 처리할 수 있고, `nouns()`로 명사를 추출한다. 불용어는 자주 나오지만 분석 의미가 낮은 단어를 제거하는 목록이다.

## 실습 / 예제
텍스트 파일 → 사용자 사전 기반 형태소 분석 → 명사 목록 → 불용어 제거 → NLTK 빈도 계산 → Pandas DataFrame/CSV 저장 → 상위 단어 막대 그래프 → WordCloud 생성 순서로 진행했다. 단어 길이와 빈도 조건을 적용해 분석 대상 단어를 골랐다.

## 헷갈린 점 / 질문
- 형태소 분석은 단순 문자열 분할과 달리 언어 단위 분석이므로 사용자 사전·불용어의 품질이 결과에 영향을 준다.
- Java 경로는 개인 실행 환경 값이므로 위키에는 실제 경로를 보존하지 않고 JVM 의존성만 기록한다.

## 관련 페이지
- [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]]
- [[entities/konlpy|KoNLPy]]
- [[entities/matplotlib|matplotlib]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 웹 크롤링·지오코딩·시각화]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
