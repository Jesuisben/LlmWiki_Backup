---
title: 2026-06-23 Python dict, comprehension, 내장 함수
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, curriculum]
sources:
  - raw/Study/10. Python/2026.06.23(화)/2026.06.23(화).md
status: growing
confidence: high
---

# 2026-06-23 Python dict, comprehension, 내장 함수

## 한 줄 요약

`dict`로 key-value 데이터를 다루고, 중첩 리스트·comprehension·내장 함수를 이용해 데이터 필터링·집계·정렬 흐름을 연습했다.

## 배운 내용

dict의 key 중복 불가/value 중복 가능, `in`, `keys()`, `values()`, `items()`, `get(key, default)`, `clear()`, 중첩 리스트, list comprehension, `sum`, `min`, `max`, `set`, `bin`, `oct`, `hex`, `eval`, `round`, `all`, `any`, `ord`, `chr`, `pow`, `zip`, `sorted`를 다뤘다.

## 핵심 개념

- [[entities/python|Python]]
- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 실습 / 예제

빵 가격 사전에 없는 품목을 추가하고 가격을 수정했으며, 학생 중첩 리스트에서 주민번호·점수·나이·성별·총점·평균·학점을 계산했다.

## 헷갈린 점 / 질문

`dict[key]`는 key가 없으면 `KeyError`가 나지만 `get(key, default)`는 기본값을 돌려준다. comprehension은 짧지만 반복문과 조건문의 위치를 읽어야 한다.

## 관련 페이지

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처

- `raw/Study/10. Python/2026.06.23(화)/2026.06.23(화).md`
