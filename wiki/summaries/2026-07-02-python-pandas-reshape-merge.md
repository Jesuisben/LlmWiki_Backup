---
title: 2026-07-02 Python Pandas 데이터 결합과 재구조화
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [python, study-log]
sources:
  - raw/Study/10. Python/2026.07.02(목)/2026.07.02(목).md
status: seed
confidence: high
---

# 2026-07-02 Python Pandas 데이터 결합과 재구조화

## 한 줄 요약

[[entities/pandas|Pandas]]에서 여러 CSV 기반 `DataFrame`을 `concat`, `merge`, `pivot`으로 결합·재구조화하고, SQL JOIN과 비슷한 데이터 연결 방식을 Python 코드로 실습한 날이다.

## 커리큘럼 위치

- 이전 수업([[summaries/2026-07-01-python-pandas-dataframe|2026-07-01]])에서는 단일 DataFrame을 만들고 조회·수정·통계·시각화하는 방법을 배웠다.
- 이날은 여러 DataFrame을 합치거나, 긴 형식(long format)의 데이터를 넓은 형식(wide format)으로 바꾸는 단계로 확장했다.
- Oracle에서 배운 JOIN 감각이 Pandas의 `merge`와 연결된다.

## 배운 내용

### 1. Chap07.Data Reshape 실습 방식

수업은 `Chap07.Data Reshape.ipynb` 완성 템플릿을 직접 수정하는 방식이 아니라, `ch13_pandas` 폴더에 새 Jupyter Notebook 파일을 만들어 직접 타이핑해 보는 방식으로 진행했다. 즉, 단순 복사보다 “코드를 따라 치면서 DataFrame 변형 흐름을 익히는 것”이 목적이었다. ^[raw/Study/10. Python/2026.07.02(목)/2026.07.02(목).md]

### 2. concat: DataFrame 이어 붙이기

가전제품 판매량 CSV 두 개를 읽어 `homeware01`, `homeware02`로 만든 뒤 `pd.concat()`을 실습했다.

- `axis=0`: 행 방향으로 이어 붙인다. 행이 늘어난다.
- `axis=1`: 열 방향으로 이어 붙인다. 열이 늘어난다.
- `join="outer"`: 합집합 기준이다. 기본값이다.
- `join="inner"`: 교집합 기준이다. 양쪽에 공통으로 있는 행/열만 남긴다.

원본 노트에는 `intersection()`과 `difference()`로 두 DataFrame의 컬럼 공통점·차이점을 먼저 확인하는 흐름이 나온다. 이는 합치기 전에 “두 표의 구조가 얼마나 맞는지”를 점검하는 단계다.

중복 컬럼을 구분하기 위해 다음처럼 컬럼명을 바꾸는 실습도 했다.

- 직접 지정: `homeware01.columns = ["미니오븐01", "전기밥솥01", ...]`
- 리스트 컴프리헨션: `homeware02.columns = [item + "02" for item in homeware02.columns]`

### 3. merge: 공통 열 기준으로 조립하기

학생 정보 CSV와 시험 점수 CSV를 읽은 뒤 `pd.merge(student, jumsu, on='id')`로 결합했다. `merge`는 SQL의 JOIN과 매우 비슷하다.

- `on='id'`: 양쪽 DataFrame에 공통으로 있는 `id` 열을 기준으로 병합한다.
- `how='outer'`: 양쪽 전체를 최대한 보존한다.
- `how='left'`: 왼쪽 DataFrame 기준으로 병합한다.
- `how='right'`: 오른쪽 DataFrame 기준으로 병합한다.
- `left_on`, `right_on`: 양쪽 기준 열 이름이 다를 때 사용한다.

이날 수업은 Oracle JOIN 학습과 연결해서 이해하면 좋다. SQL에서 `JOIN ... ON`으로 테이블을 결합하듯, Pandas에서는 `pd.merge(..., on=...)`으로 DataFrame을 결합한다.

### 4. 여러 컬럼 기준 merge와 suffixes

`on_condition = ["이름", "과목"]`처럼 여러 컬럼을 기준으로 병합하는 예제가 나왔다. 같은 사람이라도 과목이 다르면 다른 행이므로, 병합 기준을 하나가 아니라 여러 개로 잡아야 한다.

또한 양쪽 DataFrame에 같은 이름의 컬럼이 있을 때 Pandas는 기본적으로 `_x`, `_y` 접미사를 붙인다. 수업에서는 다음처럼 직접 접미사를 지정했다.

```python
pd.merge(data01, data02, on=on_condition, how='outer', suffixes=('_중간', '_기말'))
```

이 예제는 “중간고사 점수”와 “기말고사 점수”처럼 같은 컬럼명이라도 의미가 다를 때 이름 충돌을 피하는 방법을 보여준다.

### 5. index 기준 merge와 indicator

`pd.read_csv(..., index_col='id')`로 읽으면 `id` 열이 행 색인이 된다. 이 경우에는 열 기준 옵션인 `on`, `left_on`, `right_on` 대신 다음 옵션을 사용한다.

- `left_index=True`
- `right_index=True`

`indicator=True`를 주면 `_merge` 컬럼이 생기고, 각 행이 양쪽 모두에서 왔는지, 왼쪽에만 있는지, 오른쪽에만 있는지 확인할 수 있다.

수업에서는 다음처럼 시험을 보지 않은 학생을 찾는 흐름도 다뤘다.

```python
m_result = result.query('_merge == "left_only"')
```

이것은 데이터 분석에서 “누락된 매칭”을 찾는 중요한 패턴이다.

### 6. pivot: 긴 형식을 넓은 형식으로 바꾸기

마지막으로 `pivotFile.csv`를 읽고 `pivot()`을 사용했다.

- 긴 형식(long format): `name`, `item`, `value`처럼 관측값이 여러 행으로 쌓인 형태
- 넓은 형식(wide format): `item` 값들이 열 이름으로 펼쳐진 형태

예시는 다음 흐름이다.

```python
pivot_data = data.pivot(index="name", columns="item", values="value")
pivotData = data.pivot(index='name', columns='item', values=['value', 'qty'])
```

`pivot`은 보고서나 그래프를 만들기 전에 데이터를 보기 좋은 표 형태로 바꾸는 데 자주 쓰인다.

## 핵심 개념

- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]: 단일 DataFrame 조작에서 여러 DataFrame 결합과 재구조화로 확장된다.
- [[entities/pandas|Pandas]]: CSV 읽기, `concat`, `merge`, `pivot`을 통해 데이터 전처리 도구 역할을 한다.
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]: Pandas `merge`는 SQL JOIN 감각과 연결해 이해할 수 있다.

## 헷갈린 점 / 질문

- `concat`은 보통 “그냥 이어 붙이기”에 가깝고, `merge`는 “기준 열/색인이 같은 것끼리 조립하기”에 가깝다.
- `axis=0`은 행 방향, `axis=1`은 열 방향이지만, 결과적으로 “행이 늘어나는지/열이 늘어나는지”로 확인하면 덜 헷갈린다.
- `join="inner"`는 교집합, `join="outer"`는 합집합이다. SQL의 INNER JOIN/OUTER JOIN 감각과 연결된다.
- `on`, `left_on`, `right_on`은 열 기준 병합이고, `left_index`, `right_index`는 행 색인 기준 병합이다.
- `pivot`은 단순 병합이 아니라 데이터의 모양 자체를 바꾸는 작업이다.

## 관련 페이지

- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 출처

- `raw/Study/10. Python/2026.07.02(목)/2026.07.02(목).md`
