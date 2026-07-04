---
title: 2026-06-24 Python 함수, 람다, 모듈·패키지
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, curriculum]
sources:
  - raw/Study/10. Python/2026.06.24(수)/2026.06.24(수).md
status: growing
confidence: high
---

# 2026-06-24 Python 함수, 람다, 모듈·패키지

## 한 줄 요약

`def`, 기본 매개변수, 위치/키워드 인수, `*args`/`**kwargs`, `lambda`, `filter`, `map`, 모듈·패키지 import를 배우며 코드를 재사용 가능한 단위로 나누기 시작했다.

## 배운 내용

`enumerate`, 사용자 정의 함수, 기본 매개변수, 위치 인수와 키워드 인수, 가변 위치 인수 `*items`, 가변 키워드 인수 `**keyword`, `lambda`, `filter`, `map`, `__name__ == "__main__"`, 모듈과 패키지 import 방식을 학습했다.

## 핵심 개념

- [[entities/python|Python]]
- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 실습 / 예제

랜덤 정수 리스트를 반환하는 `randomGen`, 기본 점수가 있는 `sungjukInfo`, 문자열 분리/결합 함수를 모듈로 만든 뒤 다른 파일에서 import하는 실습을 했다.

## 헷갈린 점 / 질문

위치 인수 뒤에 키워드 인수는 가능하지만 반대는 안 된다. `map(func, data)`처럼 함수 객체를 넘길 때는 `func()`가 아니라 `func`를 쓴다.

## 관련 페이지

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처

- `raw/Study/10. Python/2026.06.24(수)/2026.06.24(수).md`
