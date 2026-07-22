---
title: Pandas DataFrame 기본
created: 2026-07-01
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md

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
- 결측값(`NaN`)과 데이터 타입 확인하기
- graph를 그리기 전에 index·columns·값의 모양 확인하기

Oracle에서 배운 테이블·행·열 감각과 연결하면 이해가 쉽다. 다만 SQL은 DB 서버에 질의하는 언어이고, Pandas DataFrame은 Python 메모리 안에서 표 데이터를 직접 조작하는 객체라는 차이가 있다.

이 페이지의 책임은 06-30의 Series·DataFrame 입문과 07-01의 단일 DataFrame 조회·수정·CSV·기초 통계까지다. 07-02의 결합·재구조화는 [[concepts/pandas-dataframe-reshape-merge|Pandas DataFrame 결합과 재구조화]], 07-03 이후 그룹 집계·외부 데이터 적용은 [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]와 [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]이 맡는다. 이 분할은 기존 200줄 경계 페이지에 계속 기능을 누적하지 않고 독립 검색 책임을 보존하기 위한 것이다.

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

### 07-01 그래프와 실행 근거

DataFrame에서 중구·마포구 두 columns를 골라 선그래프, 묶은 막대그래프, 1×2 subplot으로 표현했다. 날짜 폴더의 PNG 3개가 인접 code의 제목·축·범례·값 모양과 대응한다. 이는 세 graph artifact의 존재를 증명하지만 pie chart, CSV, notebook 전체 실행까지 증명하지 않는다. ^[raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md]

## 예시 흐름

### 단일 DataFrame 조회·수정

수업의 대표 흐름은 `loc["유관철":"연규희"]`로 label 범위의 행을 고르고, `loc[:, "은평구"]`로 전체 행의 한 열을 수정한 뒤, 용산구 값이 50 이하인 행의 노원구·은평구 값만 0으로 바꾸는 순서였다. 여러 line을 붙인 합성 code fence 대신 각 operation의 책임을 prose로 보존한다.

## 자주 헷갈리는 점

### `loc` vs `iloc`

- `loc`: 이름표를 보고 찾는다.
- `iloc`: 몇 번째 위치인지 보고 찾는다.

문자열 index는 당연히 `loc`로 찾지만, 숫자 index도 라벨일 수 있으므로 “숫자니까 무조건 `iloc`”라고 생각하면 안 된다.

### 행 선택 vs 열 선택

`myframe["열이름"]`은 열을 꺼낸다. 행을 꺼낼 때는 `myframe["행이름"]`이 아니라 보통 `myframe.loc["행이름"]`을 쓴다.

### `NaN` 처리

`NaN`은 “값이 없음”을 뜻한다. 새 행/열을 만들거나 서로 맞지 않는 DataFrame을 결합하면 생기기 쉽다. `fill_value`, `fillna()`, `isnull()`, `notnull()` 같은 함수로 확인·처리한다.

### 요구사항과 label 선택

07-01 수정 문제 하나는 요구한 사람과 실제 `loc` 선택 label이 달랐고, 표는 code가 고른 행이 바뀐 결과를 보였다. code가 실행되었다는 것과 요구사항을 만족했다는 것은 별도 검증 대상이다.

## 관련 개념

- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]]
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]
- [[concepts/pandas-dataframe-reshape-merge|Pandas DataFrame 결합과 재구조화]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
