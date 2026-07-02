---
title: Pandas
created: 2026-07-01
updated: 2026-07-02
type: entity
tags: [python]
sources:
  - raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md
  - raw/Study/10. Python/2026.07.02(목)/2026.07.02(목).md
status: growing
confidence: high
---

# Pandas

## 무엇인가

Pandas는 Python에서 표 형태 데이터를 다루기 위한 대표 라이브러리다. 핵심 자료구조는 1차원 `Series`와 2차원 `DataFrame`이며, CSV 입출력, 조회, 조건 필터링, 통계, 결측값 처리, 데이터 결합, 재구조화, 시각화 준비에 사용된다.

## 이 위키에서의 맥락

이 위키에서 Pandas는 2026-07-01 Python 수업부터 본격 등장한다. 사용자는 Jupyter Notebook에서 `pd.DataFrame`, `loc`, `iloc`, `to_csv`, `read_csv`, `plot` 등을 실습했고, 2026-07-02에는 `concat`, `merge`, `pivot`으로 여러 DataFrame을 결합하고 모양을 바꾸는 단계로 확장했다.

즉 Pandas는 이 과정에서 “Python 문법을 실제 데이터 처리 문제에 적용하는 도구” 역할을 한다.

## 핵심 기능 / 특징

### 1. 표 데이터 만들기와 조회

- `pd.DataFrame(...)`: 리스트/NumPy 배열을 표 형태로 구성
- `index`: 행 이름
- `columns`: 열 이름
- `loc`: 라벨 기반 조회
- `iloc`: 위치 기반 조회

수업에서는 사람 이름과 지역명을 이용해 영업 실적 표를 만들고, 특정 행/열을 조회하거나 값을 수정했다.

### 2. Series와 통계

DataFrame에서 열 하나를 꺼내면 보통 `Series`가 된다. 수업에서는 `payment['교통비']`, `payment.교통비`처럼 Series를 추출하고 다음 기능을 확인했다.

- `size`, `shape`, `count()`
- `dtype`, `hasnans`
- `mean()`, `median()`, `std()`, `sum()`, `describe()`
- `value_counts()`
- `isnull()`, `notnull()`, `fillna()`

### 3. 파일 입출력

- `to_csv()`: DataFrame을 CSV 파일로 저장
- `read_csv()`: CSV 파일을 DataFrame으로 읽기
- `encoding='CP949'`: 한국어 Windows/Excel 환경의 CSV 파일에서 중요
- `index_col`: 특정 열을 행 색인으로 사용

### 4. 데이터 결합과 재구조화

2026-07-02 수업에서는 Pandas가 단순 표 조회 도구를 넘어 데이터 전처리 도구로 쓰였다.

- `pd.concat()`: 여러 DataFrame을 행/열 방향으로 이어 붙임
- `pd.merge()`: SQL JOIN처럼 공통 열 또는 index 기준으로 병합
- `pivot()`: 긴 형식 데이터를 넓은 형식 표로 변환
- `intersection()`, `difference()`: 결합 전 Index/columns의 공통점과 차이 확인
- `suffixes`: 같은 이름의 컬럼 충돌 해결
- `indicator=True`: 병합 결과의 출처 확인

## 학습 이력

### [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]

단일 DataFrame을 중심으로 조회·수정·통계·CSV 입출력·그래프를 배웠다. 특히 `loc`/`iloc`와 조건 필터링은 이후 모든 Pandas 작업의 기본이 된다.

### [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]

여러 DataFrame을 합치는 `concat`, SQL JOIN과 닮은 `merge`, 표 모양을 바꾸는 `pivot`을 배웠다. Oracle JOIN을 배운 뒤라면 `merge`의 의미를 더 쉽게 연결할 수 있다.

## 관련 개념

- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[entities/python|Python]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 자주 헷갈리는 점

- Pandas의 `DataFrame`은 SQL 테이블처럼 생겼지만, DB 안의 테이블이 아니라 Python 메모리 안의 객체다.
- `concat`과 `merge`는 둘 다 합치기지만, `concat`은 이어 붙이기, `merge`는 기준 키로 조립하기에 가깝다.
- `axis=0`/`axis=1`은 말로만 외우기보다 결과가 행 방향으로 늘어나는지, 열 방향으로 늘어나는지 함께 확인해야 한다.
- `NaN`은 단순 문자열이 아니라 결측값이므로 통계나 저장 전에 처리 여부를 판단해야 한다.

## 프로젝트/면접에서 설명할 관점

Pandas는 “CSV나 엑셀처럼 생긴 데이터를 Python 코드로 다루는 도구”라고 설명하면 좋다. 이 과정에서는 데이터 조회·수정뿐 아니라 여러 파일을 합치고, SQL JOIN과 비슷한 병합을 수행하고, 그래프를 그리기 좋은 형태로 데이터를 바꾸는 데 사용했다.

## 출처

- `raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/Study/10. Python/2026.07.02(목)/2026.07.02(목).md`
