---
title: Python
created: 2026-07-01
updated: 2026-07-03
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md
  - raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md
  - raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md
  - raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md
  - raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md
  - raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md
  - raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
status: growing
confidence: high
---

# Python

## 무엇인가

Python은 읽기 쉬운 문법과 풍부한 표준·외부 라이브러리를 가진 범용 프로그래밍 언어다. 이 위키에서는 과정 후반부에 데이터 처리·파일 입출력·정규표현식·JSON/XML·Pandas 분석 실습을 수행하는 언어로 등장한다.

## 이 위키에서의 맥락

2026-06-19~06-29에는 Pandas 이전 기초를 다졌다. 설치와 PyCharm, 기본 문법, 조건문·반복문, 컬렉션, 함수·모듈·패키지, 표준 라이브러리, 객체지향, 예외 처리, 파일 입출력, 정규표현식, XML/JSON을 순서대로 배웠다. 2026-06-30부터 Jupyter Notebook과 Pandas `Series`/`DataFrame`으로 전환되며, 2026-07-01~07-02에는 DataFrame 조회·CSV 입출력·결합·재구조화로 확장되었다. 2026-07-03에는 `groupby`, `agg`, `transform`, `pd.cut`, matplotlib 그래프로 범주별 집계와 시각화 흐름을 다뤘다.

## 핵심 기능 / 특징

- `print`, `input`, 문자열 함수, 형변환으로 기본 입출력과 데이터 변환을 수행한다.
- `if`, `for`, `while`, `range`로 실행 흐름을 제어한다.
- `list`, `tuple`, `dict`, `set`, comprehension으로 여러 데이터를 묶고 필터링한다.
- `def`, `lambda`, `map`, `filter`, 모듈·패키지로 코드를 재사용한다.
- `os`, `random`, `datetime`, `re`, `json`, `xml.etree.ElementTree`로 파일·날짜·패턴·구조화 데이터를 다룬다.
- `pip`로 Pandas, matplotlib 같은 Third Party 라이브러리를 설치해 데이터 분석 기능을 확장한다.
- Pandas의 `groupby`/`transform`과 matplotlib 그래프로 표 데이터를 요약·시각화한다.

## 학습 이력

- [[summaries/2026-06-19-python-setup-basic-syntax|2026-06-19 Python 설치와 기본 문법 입문]]
- [[summaries/2026-06-22-python-control-flow-collections|2026-06-22 Python 제어문과 컬렉션]]
- [[summaries/2026-06-23-python-dict-comprehension-builtins|2026-06-23 Python dict, comprehension, 내장 함수]]
- [[summaries/2026-06-24-python-functions-modules|2026-06-24 Python 함수, 람다, 모듈·패키지]]
- [[summaries/2026-06-25-python-standard-library-oop|2026-06-25 Python 표준 라이브러리와 객체지향]]
- [[summaries/2026-06-26-python-exception-file-regex|2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식]]
- [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]]
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]

## 관련 개념

- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-functions-modules-packages|Python 함수, 모듈, 패키지]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]
- [[concepts/python-oop-basics|Python 객체지향 기본]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/matplotlib|matplotlib]]

## 프로젝트/면접에서 설명할 관점

이 과정의 Python은 “순수 Python으로 텍스트·XML·JSON 데이터를 다루는 기본기를 만든 뒤, Pandas로 표 데이터를 더 효율적으로 조회·가공·결합·그룹화·시각화하는 데이터 처리 언어”로 설명할 수 있다.

## 출처

- `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md`
- `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md`
- `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md`
- `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md`
- `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md`
- `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md`
- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
