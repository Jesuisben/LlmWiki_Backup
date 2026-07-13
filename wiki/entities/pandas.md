---
title: Pandas
created: 2026-07-01
updated: 2026-07-13
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md
  - raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# Pandas

## 무엇인가

Pandas는 Python에서 표 형태 데이터를 다루기 위한 대표 Third Party 라이브러리다. 핵심 자료구조는 1차원 `Series`와 2차원 `DataFrame`이며, CSV 입출력, 조회, 조건 필터링, 통계, 결측값 처리, 데이터 결합, 재구조화, 시각화 준비에 사용된다.

## 이 위키에서의 맥락

2026-06-29~07-03에는 Series/DataFrame, 조회·CSV·결합·집계·그래프를 익혔다. 07-06~07에는 공공 자전거·커피 매장 데이터를 DataFrame으로 만들고 문자열·결측치·index를 정리한 뒤 `merge`, `concat`, `pivot_table`, `groupby`와 지도·차트 분석에 적용했다.

## 핵심 기능 / 특징

- `Series`: 1차원 자료구조. Oracle 테이블의 한 행 또는 한 열처럼 이해할 수 있다.
- `DataFrame`: 여러 Series가 모인 2차원 표 데이터. `index`, `columns`, `values`를 가진다.
- CSV 입출력: `read_csv()`, `to_csv()`로 파일과 표 데이터를 연결한다.
- 데이터 결합: `concat`, `merge`, `pivot`으로 이어 붙이기, JOIN식 병합, 재구조화를 수행한다.
- 그룹화와 집계: `groupby`, `agg`, `transform`, `pd.cut`으로 범주별 요약과 파생 컬럼을 만든다.
- 시각화 준비: `plot()`과 matplotlib를 이용해 파이·산점도·박스플롯·히스토그램·막대 그래프를 그린다.

## 학습 이력

- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]]
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]

## 관련 개념

- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/matplotlib|matplotlib]]
- [[entities/python|Python]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 자주 헷갈리는 점

- Pandas의 `DataFrame`은 SQL 테이블처럼 생겼지만 DB 안의 테이블이 아니라 Python 메모리 안의 객체다.
- `Series` 하나는 1차원이고, `DataFrame`은 2차원이다.
- `concat`은 이어 붙이기, `merge`는 기준 키로 조립하기에 가깝다.
- Pandas는 Python 내장 모듈이 아니라 `pip`로 설치하는 외부 라이브러리다.
- `agg()`는 그룹별 요약표를 만들고, `transform()`은 원본 행 수를 유지해 새 컬럼을 붙이는 데 적합하다.
- 그래프가 이상하게 나오면 먼저 index/columns와 데이터 형태가 그래프 목적에 맞는지 확인해야 한다.

## 출처

- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
