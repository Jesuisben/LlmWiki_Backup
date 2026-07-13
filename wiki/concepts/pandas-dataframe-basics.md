---
title: Pandas DataFrame 기본
created: 2026-07-01
updated: 2026-07-13
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md
  - raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# Pandas DataFrame 기본

## 정의

Pandas `DataFrame`은 행(row)과 열(column)을 가진 2차원 표 데이터를 Python에서 다루기 위한 핵심 자료구조다. Excel 표, CSV 파일, SQL 조회 결과처럼 “열 이름이 있고 여러 행이 쌓인 데이터”를 코드로 조회·수정·계산·결합·시각화할 때 사용한다.

## 왜 중요한가

국비지원 과정에서 Python은 단순 문법 학습을 넘어 데이터 처리 도구로 등장했다. [[entities/pandas|Pandas]]의 DataFrame을 이해하면 다음 작업을 할 수 있다.

- CSV 파일을 읽어 표 형태로 다루기
- 특정 행/열을 조회하고 값 수정하기
- 조건에 맞는 데이터만 필터링하기
- 여러 표를 이어 붙이거나 JOIN처럼 병합하기
- 결측값(`NaN`)과 데이터 타입 확인하기
- 그래프를 그리기 좋은 형태로 데이터 바꾸기
- `groupby`, `agg`, `transform`, `pd.cut`으로 범주별 집계와 파생 컬럼 만들기

Oracle에서 배운 테이블·행·열 감각과 연결하면 이해가 쉽다. 다만 SQL은 DB 서버에 질의하는 언어이고, Pandas DataFrame은 Python 메모리 안에서 표 데이터를 직접 조작하는 객체라는 차이가 있다.

7월 6~7일에는 공공 자전거·커피 매장 데이터를 실제 DataFrame으로 만들었다. 이때 `rename`, 문자열 치환, `dropna`, `set_index`로 결합 기준을 정리한 뒤 `merge`·`concat`·`pivot_table`·`groupby`로 분석용 표를 만들었다.

## 핵심 설명

### DataFrame, Series, Index

- `DataFrame`: 행과 열을 가진 2차원 표
- `Series`: DataFrame의 한 열 또는 한 행처럼 다룰 수 있는 1차원 데이터
- `index`: 행 이름 또는 행 위치 정보
- `columns`: 열 이름 정보

2026-07-01 수업에서는 사람 이름을 `index`, 지역명을 `columns`로 두고 영업 실적 표를 만들었다. `np.reshape`로 리스트를 5×5 배열 형태로 바꾼 뒤 `pd.DataFrame(..., index=..., columns=...)`로 DataFrame을 구성했다. ^[raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md]

### loc와 iloc

DataFrame 조회의 핵심은 `loc`와 `iloc`를 구분하는 것이다.

| 구분 | 기준 | 예시 | 의미 |
|---|---|---|---|
| `loc` | 라벨 이름 | `myframe02.loc["연규희"]` | 행 이름이 `연규희`인 데이터 |
| `iloc` | 숫자 위치 | `myframe02.iloc[1]` | 1번 위치의 행 |
| 열 선택 | 열 이름 | `myframe02["용산구"]` | `용산구` 열 |
| 전체 행/열 | `:` | `myframe02.loc[:, "은평구"]` | 모든 행의 `은평구` 열 |

초보자가 자주 헷갈리는 포인트는 “행 이름이 숫자처럼 보여도 `loc`는 라벨, `iloc`는 위치”라는 점이다. 예를 들어 index 라벨이 `1`인 것과 1번째 위치는 다른 개념일 수 있다.

### 조건 필터링과 값 수정

Pandas에서는 조건식을 만들면 boolean Series가 생기고, 이것을 필터처럼 사용할 수 있다.

```python
myframe02.loc[myframe02["용산구"] <= 50, ["노원구", "은평구"]] = 0
```

이 코드는 “용산구 실적이 50 이하인 행들만 골라서, 그 행들의 노원구·은평구 값을 0으로 바꾼다”는 뜻이다. SQL의 `WHERE 용산구 <= 50`처럼 조건으로 행을 고르는 감각과 비슷하다.

### axis와 산술 연산

`DataFrame.add()` 같은 연산에서 `axis`는 Series와 DataFrame을 어느 축 기준으로 맞출지 결정한다.

- `axis=0`: Series index를 DataFrame의 행 index와 맞춘다.
- `axis=1`: Series index를 DataFrame의 column 이름과 맞춘다.

DataFrame끼리 연산할 때는 행/열 이름이 맞는 위치끼리 계산된다. 한쪽에만 있는 값은 `fill_value=0`으로 보완할 수 있지만, 양쪽 모두 없으면 `NaN`이 남는다.

### reindex, drop, rename

- `reindex(index=...)`: 행 index를 새 기준으로 재배열하거나 추가한다.
- `reindex(columns=...)`: columns를 새 기준으로 재배열하거나 추가한다.
- `drop(..., axis='index')`: 행 삭제
- `drop(..., axis='columns')`: 열 삭제
- `rename(index=..., columns=...)`: 행/열 이름 변경

`reindex`는 기존 표를 새 틀에 맞추는 작업이다. 새로 생긴 행/열에는 값이 없으므로 기본적으로 `NaN`이 생기고, `fill_value`를 주면 기본값을 채울 수 있다.

### CSV 입출력과 인코딩

수업에서는 `Faker('ko_KR')`로 더미 데이터를 만든 뒤 `to_csv()`로 저장하고 `read_csv()`로 다시 읽었다.

- `to_csv()`: DataFrame을 CSV 파일로 저장
- `read_csv()`: CSV 파일을 DataFrame으로 읽기
- `encoding='CP949'`: Excel/Windows 환경에서 한글 CSV를 다룰 때 자주 사용
- `index_col=0` 또는 `index_col='사원명'`: 특정 열을 index로 읽기

인코딩이 맞지 않으면 한글이 깨진다. Python 데이터 처리 실습에서 `UTF-8`과 `CP949`를 구분하는 이유가 여기에 있다.

### concat, merge, pivot

2026-07-02 수업에서는 단일 DataFrame 조작을 넘어 여러 DataFrame을 결합하고 모양을 바꾸는 작업을 했다. ^[raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md]

| 함수 | 목적 | 수업 예시 |
|---|---|---|
| `pd.concat()` | DataFrame을 행 또는 열 방향으로 이어 붙임 | 1분기/2분기 가전제품 판매량 결합 |
| `pd.merge()` | 공통 열/색인을 기준으로 JOIN처럼 병합 | 학생 정보와 시험 점수 병합 |
| `pivot()` | 긴 형식 데이터를 넓은 표로 재구성 | 과일 구매 내역을 이름×품목 표로 변환 |

`merge`는 Oracle에서 배운 JOIN과 연결해서 이해하면 좋다. `on`, `left_on`, `right_on`은 열 기준이고, `left_index`, `right_index`는 행 색인 기준이다.

### groupby, agg, transform, cut

2026-07-03 수업에서는 DataFrame을 단순히 조회·결합하는 데서 더 나아가 범주별로 요약하고 그래프로 확인하는 흐름을 다뤘다. ^[raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md]

| 기능 | 목적 | 수업 예시 |
|---|---|---|
| `groupby()` | 기준 컬럼별로 그룹을 나눔 | 성별별 교통비, 출장지역/성별별 출장기간 |
| `agg()` | 그룹별 집계 함수 적용 | `sum`, `mean`, `max`, 사용자 정의 함수 |
| `transform()` | 원본 행 수를 유지한 그룹별 계산 | 이름·월별 첫 주 대비 시험 점수 향상 비율 |
| `pd.cut()` | 연속형 숫자를 구간 라벨로 범주화 | 소득을 저소득~고소득 구간으로 나누기 |
| `plot()` | 집계 결과를 그래프로 확인 | pie, scatter, box, hist, barh |

`agg()`는 그룹별 요약표를 만들기 때문에 행 수가 줄어들 수 있고, `transform()`은 원본과 같은 길이의 결과를 돌려주므로 새 파생 컬럼을 붙일 때 유용하다.

## 예시 흐름

### 단일 DataFrame 조회·수정

```python
myframe02.loc["유관철":"연규희"]
myframe02.loc[:, "은평구"] = 60
myframe02.loc[myframe02["용산구"] <= 50, ["노원구", "은평구"]] = 0
```

이 흐름은 “라벨로 행 범위를 고르고, 전체 행의 특정 열을 수정하고, 조건에 맞는 일부 행/열을 수정하는” 대표 패턴이다.

### 여러 DataFrame 결합

```python
pd.concat([homeware01, homeware02], axis=0)
pd.merge(student, jumsu, on="id", how="outer")
data.pivot(index="name", columns="item", values="value")
cols = ["교통비", "출장기간"]
payment.groupby(["출장지역", "성별"])[cols].agg(["sum", "mean"])
```

이 흐름은 “표를 이어 붙이고, 기준 열로 병합하고, 보고서 형태로 재구조화한 뒤, 범주별로 집계하는” Pandas 데이터 전처리의 기본 패턴이다.

## 자주 헷갈리는 점

### `loc` vs `iloc`

- `loc`: 이름표를 보고 찾는다.
- `iloc`: 몇 번째 위치인지 보고 찾는다.

문자열 index는 당연히 `loc`로 찾지만, 숫자 index도 라벨일 수 있으므로 “숫자니까 무조건 `iloc`”라고 생각하면 안 된다.

### 행 선택 vs 열 선택

`myframe["열이름"]`은 열을 꺼낸다. 행을 꺼낼 때는 `myframe["행이름"]`이 아니라 보통 `myframe.loc["행이름"]`을 쓴다.

### `concat` vs `merge`

- `concat`: 표를 위아래/좌우로 붙이는 느낌
- `merge`: 공통 키가 같은 행끼리 찾아 조립하는 느낌

`merge`는 SQL JOIN과 비슷하고, `concat`은 파일 여러 개를 이어 붙이는 감각에 가깝다.

### `NaN` 처리

`NaN`은 “값이 없음”을 뜻한다. 새 행/열을 만들거나 서로 맞지 않는 DataFrame을 결합하면 생기기 쉽다. `fill_value`, `fillna()`, `isnull()`, `notnull()` 같은 함수로 확인·처리한다.

### `agg()` vs `transform()`

`agg()`는 그룹별 요약표를 만들고, `transform()`은 원본 행 수를 유지한다. 그래서 평균표·합계표처럼 보고용 결과가 필요하면 `agg()`, 원본 데이터에 “향상_비율” 같은 새 컬럼을 붙이고 싶으면 `transform()`을 먼저 떠올리면 좋다.

## 관련 개념

- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]]
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
