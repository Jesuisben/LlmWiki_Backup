---
title: 2026-06-30 Python Pandas Series와 DataFrame 입문
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
status: growing
confidence: high
---

# 2026-06-30 Python Pandas Series와 DataFrame 입문

## 한 줄 요약

Jupyter Notebook에서 Pandas `Series`와 `DataFrame`의 기본 구조를 배우고, Oracle 테이블 감각을 Python 메모리 안의 표 데이터 처리로 연결했다.

## 배운 내용

Pandas 공식 문서, `Series` 생성자, `index`, `name`, `values`, `to_frame`, 문자열 index 조회, `iloc`, 슬라이싱, boolean indexing, Series 간 연산과 `NaN`, `fill_value`, `unique`, `value_counts(normalize=True)`, `isin`, matplotlib 그래프, DataFrame의 `index`/`columns`/`values`를 다뤘다.

## 핵심 개념

- [[entities/python|Python]]
- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 실습 / 예제

국가별 신용도 Series를 만들고 문자열 index로 조회·수정·슬라이싱했으며, `plot(kind="line")`, `plot(kind="bar")`로 그래프를 그렸다.

## 헷갈린 점 / 질문

`Series`는 1차원이고 `DataFrame`은 2차원이다. `myseries["미국"]`은 스칼라, `myseries[&#91;"미국"&#93;]`은 Series 형태를 반환한다.

## 관련 페이지

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
