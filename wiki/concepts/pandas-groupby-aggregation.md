---
title: Pandas groupby와 집계
created: 2026-07-03
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# Pandas groupby와 집계

## 정의

Pandas `groupby()`는 `DataFrame`이나 `Series`를 특정 기준 컬럼별로 나눈 뒤, 각 그룹에 합계·평균·개수·최댓값 같은 계산을 적용하는 기능이다. “성별별 교통비 합계”, “출장지역별 평균 출장기간”, “성별/소득구간별 평균 소득”처럼 범주별 요약표를 만들 때 사용한다.

## 왜 중요한가

실제 데이터 분석에서는 전체 평균 하나보다 “어떤 집단에서 값이 높은지/낮은지”가 더 중요할 때가 많다. 2026-07-03 수업은 [[entities/pandas|Pandas]]의 `groupby`를 통해 단순 조회·결합을 넘어 분석용 요약표와 그래프를 만드는 단계로 넘어간다.

Oracle에서 `GROUP BY`와 집계 함수를 이미 배웠다면, Pandas `groupby().agg()`는 그 감각과 연결된다. 차이는 SQL은 DB 서버에 질의하고, Pandas는 Python 메모리 안의 `DataFrame` 객체를 조작한다는 점이다.

## 핵심 설명

### 기본 패턴

07-03 수업에서는 성별별 교통비 합계·건수에서 시작해 출장지역·성별별 교통비와 출장기간에 여러 집계 함수를 적용했다.

핵심 순서는 다음과 같다.

1. 기준 컬럼을 정한다.
2. 계산할 값 컬럼을 고른다.
3. 집계 함수로 요약한다.
4. 필요하면 `to_frame()`, `reset_index()`, 컬럼명 변경으로 결과를 보기 좋은 표로 만든다.

### agg와 사용자 정의 함수

`agg()`는 집계 함수를 하나 또는 여러 개 적용한다. 문자열 함수명(`"sum"`, `"mean"`)뿐 아니라 직접 만든 함수도 사용할 수 있다.

수업의 사용자 정의 함수는 각 group의 값이 하한·상한 사이인지 `between()`으로 판정하고 boolean 평균으로 비율을 구했다. 이 함수를 `agg()`에 추가 인수와 함께 전달했다.

이 예시는 각 성별 그룹에서 교통비가 1500~3500 사이에 들어가는 비율을 계산한다. `between(...).mean()`은 True/False를 1/0처럼 평균내는 방식이라 “조건을 만족하는 비율”을 구할 수 있다.

### 다중 색인 정리

여러 기준 컬럼으로 그룹화하거나 여러 집계 함수를 동시에 쓰면 행 또는 열에 다중 색인(MultiIndex)이 생긴다.

- 행 쪽 다중 색인: `groupby(['출장지역', '성별'])`
- 열 쪽 다중 색인: `.agg({'교통비':['sum', 'mean'], '출장기간':['mean', 'min']})`

수업에서는 `get_level_values()`, 한글 이름 매핑, 문자열 결합, `reset_index()`로 중첩 구조를 단순한 표로 바꿨다. 이 과정은 그래프나 CSV 저장 전에 자주 필요하다.

### agg vs transform

| 구분 | `agg()` | `transform()` |
|---|---|---|
| 결과 길이 | 그룹별 요약이므로 줄어들 수 있음 | 원본 행 수와 같음 |
| 주 용도 | 요약표 만들기 | 원본 데이터에 파생 컬럼 붙이기 |
| 수업 예시 | 성별 교통비 합계, 출장지역별 평균 | 이름·월별 첫 주 대비 점수 향상 비율 |

`transform()`은 그룹별 계산을 하되 결과를 원본 행마다 돌려주므로, `jumsu_score["향상_비율"] = ...`처럼 새 컬럼을 만들 때 적합하다.

### 연속형 변수 범주화

`pd.cut()`은 `소득`처럼 연속형 숫자 값을 구간으로 나눠 범주형 라벨을 붙인다.

수업에서는 음의 무한대부터 양의 무한대까지의 소득 구간과 저소득~고소득 label을 준비해 `pd.cut()` 결과를 파생 column으로 붙였다.

그 뒤 `groupby(['성별', '범주형소득'])`로 집계하면 숫자 범위를 사람이 읽기 쉬운 그룹으로 분석할 수 있다.

## 예시 흐름

복지 데이터는 `groupby` 평균 → `reset_index` → `pivot` → 수평 막대그래프 순서로 바꾸었다. 이는 “원본 데이터 → 범주별 평균 요약 → graph에 맞는 wide format → 시각화”로 이어지는 전형적인 분석 패턴이다.

공공 자전거 실습에서는 `자치구`·`대여구분코드`별 `대여건수`를 합산해 정렬한 뒤 `drop_duplicates()`로 그룹마다 가장 큰 항목을 남겼다. 즉 groupby 결과는 집계표 자체로 끝나지 않고 정렬·결측치 처리·그래프·지도 분석의 입력이 된다.

07-07 커피 매장 실습에서는 군구·브랜드별 매장 수와 서비스 제공 매장 분포를 집계했다. 다만 날짜 raw에는 생성 CSV·PNG·HTML이 없고 일부 결측 좌표·파일명 재사용 문제가 있으므로, code상 적용과 물리 artifact를 구분한다.

## 실행 증거 경계

- 07-03: groupby·agg·transform·cut code와 일부 표 표현이 있지만 독립 notebook·graph PNG는 없다.
- 07-06: 자전거 입력 CSV 한 개는 물리적으로 존재하지만 API 생성 CSV·지도 HTML은 없다.
- 07-07: groupby·plot·save code는 있으나 최종 저장 artifact는 없다.
- 따라서 이 페이지는 날짜별 발전과 분석 논리를 설명하며 전체 실행 성공을 주장하지 않는다.

## 자주 헷갈리는 점

- `groupby` 자체는 계산 결과가 아니라 “그룹으로 나뉜 객체”다. `sum()`, `mean()`, `agg()` 같은 계산을 붙여야 결과표가 나온다.
- `agg()` 결과는 그룹별 요약이라 원본보다 행 수가 줄어드는 것이 자연스럽다.
- `transform()`은 원본 행 수를 유지하므로 파생 컬럼 생성에 알맞다.
- 다중 색인은 오류가 아니라 여러 기준/여러 집계 결과를 표현한 구조다. 다만 초보자에게 복잡하므로 `reset_index()`와 컬럼명 정리로 단순화한다.
- `pd.cut()`으로 만든 범주형 컬럼은 실제 숫자 계산 결과가 아니라 구간 라벨이다.

## 관련 개념

- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 Python 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 Python 웹 크롤링, 지오코딩, 시각화]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-dataframe-reshape-merge|Pandas DataFrame 결합과 재구조화]]
- [[entities/pandas|Pandas]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]

## 출처

- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
