---
title: 2026-07-03 Python Pandas groupby와 시각화
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, study-log]
sources:
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
status: growing
confidence: high
---

# 2026-07-03 Python Pandas groupby와 시각화

## 한 줄 요약

[[entities/pandas|Pandas]]에서 `groupby()`로 범주별 데이터를 집계하고, 다중 색인을 정리한 뒤, `transform`, `pd.cut`, [[entities/matplotlib|matplotlib]] 그래프로 분석 결과를 확인한 날이다.

## 커리큘럼 위치

- 이전 수업([[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02]])에서는 `concat`, `merge`, `pivot`으로 여러 `DataFrame`을 결합·재구조화했다.
- 이날은 “표를 합치는 단계”에서 “표를 범주별로 요약하고 시각화하는 단계”로 넘어갔다.
- Oracle의 `GROUP BY`/집계 함수 감각이 Pandas의 `groupby().agg()`와 연결된다.
- 다음 흐름에서는 이런 전처리·집계·시각화 패턴을 실제 데이터 분석 문제에 반복 적용하게 된다.

## 배운 내용

### 1. Data Grouping 실습 방식

수업은 `ch13_pandas` 폴더에 새 Jupyter Notebook을 만들고, 완성 템플릿인 `Chap08.Data Grouping.ipynb`를 참고해 직접 타이핑하는 방식으로 진행했다. 목적은 완성본을 보는 것이 아니라 `groupby` 메커니즘을 손으로 따라가며 익히는 데 있었다. ^[raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md]

### 2. 범주형 데이터와 groupby 집계

출장 내역 CSV인 `payment07.csv`를 읽고, 성별·출장지역 같은 범주형 컬럼을 기준으로 `교통비`, `출장기간`을 집계했다.

```python
payment = pd.read_csv(filename, encoding='UTF-8')
mygrouping = payment.groupby("성별")["교통비"]
mygrouping.sum().to_frame()
mygrouping.count().to_frame()
```

이 흐름은 “전체 데이터에서 성별이라는 기준으로 그룹을 나눈 뒤, 각 그룹의 교통비 합계와 건수를 계산한다”는 뜻이다. SQL의 `GROUP BY 성별`과 비슷하게 이해할 수 있다.

### 3. agg로 여러 컬럼·여러 집계 함수 적용

`agg()`는 하나의 집계 함수만 쓰는 단계에서 여러 집계 기준을 한 번에 적용하는 단계로 확장해 준다.

```python
mydict = {'교통비':['sum', 'mean', 'max'], '출장기간':['mean', 'min']}
groupdata = payment.groupby(['출장지역', '성별']).agg(mydict).astype(int)
```

이 결과는 행 쪽에는 `출장지역`, `성별`이 중첩 색인으로 생기고, 열 쪽에는 `교통비_sum`, `출장기간_mean`처럼 다층 컬럼 구조가 만들어질 수 있다.

### 4. 중첩 색인과 컬럼 이름 정리

다중 집계를 하면 결과가 풍부해지는 대신 색인이 복잡해진다. 수업에서는 `get_level_values()`로 바깥/안쪽 컬럼 레벨을 꺼내고, 영어 집계 함수명을 한글로 바꾼 뒤 컬럼명을 단일 문자열로 합쳤다.

```python
outer_column = groupdata.columns.get_level_values(0)
inner_column = groupdata.columns.get_level_values(1)
inner_column = [hangul_dict[item] for item in inner_column.tolist()]
groupdata.columns = outer_column + '_' + inner_column
groupdata.reset_index()
```

`reset_index()`는 중첩된 행 색인을 일반 컬럼으로 풀어 주기 때문에, 이후 저장·그래프·보고서 작성에서 더 다루기 쉬운 표가 된다.

### 5. 사용자 정의 집계 함수와 groupby 객체

`agg()`에는 내장 집계 함수뿐 아니라 직접 만든 함수도 넣을 수 있다. 예를 들어 교통비가 특정 범위에 들어가는 비율을 계산하는 함수를 만들어 성별 또는 출장지역별로 적용했다.

```python
def get_range_limit(x, lower, upper):
    return x.between(lower, upper).mean()

result = payment.groupby(['성별'])['교통비'].agg(get_range_limit, 1500, upper=3500)
```

또한 `grouped.groups`, `grouped.ngroups`, `get_group()`과 반복문을 통해 `DataFrameGroupBy` 객체가 내부적으로 “그룹 key → 부분 DataFrame” 구조를 가진다는 점을 확인했다.

### 6. transform으로 원본 행 수를 유지한 파생 컬럼 만들기

시험 성적표에서는 이름·월별로 그룹을 나눈 뒤, 매월 첫 주 대비 시험 점수 향상 비율을 계산했다.

```python
def jumsu_rate(jumsu):
    return 100*(jumsu - jumsu.iloc[0]) / jumsu.iloc[0]

pct_jumsu_score = jumsu_score.groupby(["이름", "월"])["점수"].transform(jumsu_rate)
jumsu_score["향상_비율"] = pct_jumsu_score.round(4)
```

여기서 `transform()`은 `agg()`처럼 그룹별 결과를 한 줄로 줄이지 않고, 원본 행 개수와 같은 길이의 결과를 돌려준다. 그래서 계산 결과를 원본 `DataFrame`의 새 컬럼으로 붙이기 좋다.

### 7. 연속형 변수의 범주화와 그래프

복지 데이터에서는 `소득`처럼 연속형 숫자 데이터를 구간으로 나누어 범주형 데이터로 바꾸고, 성별·소득구간별 평균을 그래프로 확인했다.

```python
bins = [-np.inf, 200, 500, 700, 1000, np.inf]
mylabels = ['저소득', '중저소득', '중소득', '중고소득', '고소득']
welfare.loc[:, '범주형소득'] = pd.cut(welfare['소득'], bins=bins, labels=mylabels)
chartdata = welfare.groupby(['성별', '범주형소득'], observed=False)['소득'].mean().to_frame()
```

이후 `pivot()`으로 그래프에 적합한 형태로 바꾸고, `plot(kind='barh')`로 성별·소득구간별 평균 소득을 비교했다.

### 8. matplotlib 기반 시각화

수업에서는 Pandas의 `plot()`과 matplotlib 설정을 함께 사용했다.

- 결혼 유무별 소득 평균: pie chart
- 소득과 나이: scatter plot
- 결혼 유무별 소득 분포: box plot
- 소득 분포: histogram
- 성별/범주형소득별 평균 소득: horizontal bar chart

그래프는 “데이터를 예쁘게 보여주는 부가 기능”이 아니라, 집계 결과를 눈으로 검증하고 이상치·분포·비교 구조를 빠르게 파악하는 도구로 쓰였다.

## 핵심 개념

- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]: 범주별로 데이터를 나누고 합계·평균·개수·사용자 정의 계산을 적용하는 패턴
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]: 조회·수정·결합 이후 그룹화와 시각화로 확장된다.
- [[entities/pandas|Pandas]]: `groupby`, `agg`, `transform`, `cut`, `pivot`, `plot`을 이용한 표 데이터 분석 도구
- [[entities/matplotlib|matplotlib]]: Pandas 결과를 파이·산점도·박스플롯·히스토그램·막대 그래프로 확인하는 시각화 라이브러리
- [[entities/jupyter-notebook|Jupyter Notebook]]: 코드, 표, 그래프 결과를 셀 단위로 확인한 학습 환경

## 헷갈린 점 / 질문

- `groupby().agg()`는 그룹별 결과를 요약해 행 수가 줄어들 수 있지만, `groupby().transform()`은 원본 행 수를 유지해 새 컬럼으로 붙이기 좋다.
- 여러 컬럼과 여러 집계 함수를 동시에 쓰면 행/열에 다중 색인이 생길 수 있다. 이때 `reset_index()`와 컬럼명 단일화가 필요하다.
- `pd.cut()`은 숫자를 계산하는 함수라기보다 연속형 값을 구간 라벨로 바꾸는 범주화 도구다.
- `pivot()`은 집계 함수가 아니라 이미 있는 값을 행×열 표로 재배치하는 함수다. 중복 조합이 있으면 별도 집계가 필요하다.
- 그래프를 그리기 전에는 데이터가 그래프에 맞는 “넓은 형식”인지, index/columns가 의도한 축인지 확인해야 한다.

## 관련 페이지

- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 출처

- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
