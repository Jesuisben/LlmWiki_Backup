---
title: Pandas DataFrame 결합과 재구조화
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md
status: growing
confidence: high
---

# Pandas DataFrame 결합과 재구조화

## 정의

Pandas에서 여러 `DataFrame`을 이어 붙이거나 공통 key로 병합하고, long format과 wide format 사이에서 표 모양을 바꾸는 흐름이다. 이 Vault에서는 2026-07-02에 `concat` → `merge` → `pivot`·`melt` → `pivot_table` 순서로 배웠다.

## 왜 중요한가

현실의 데이터는 한 표에 완성되어 있지 않다. 분기별 파일을 세로로 쌓거나, 학생 정보와 시험 점수를 같은 `id`로 연결하거나, 그래프가 읽기 쉬운 행×열 모양으로 바꿔야 한다. 07-01의 단일 표 조회·수정에서 07-03의 그룹 집계로 넘어가기 위한 중간 단계다.

## 수업에서의 발전 순서

1. 두 판매량 CSV의 columns 교집합·차집합을 먼저 확인했다.
2. `concat`으로 표를 행 또는 열 방향으로 이어 붙였다.
3. `merge`로 공통 열·여러 열·서로 다른 이름의 열·index를 기준으로 병합했다.
4. `indicator=True`의 `_merge`를 조회해 한쪽에만 있는 행을 찾았다.
5. `pivot`과 `melt`로 long/wide format을 왕복했다.
6. `pivot_table`에서 평균·합계 등 집계를 함께 적용하고 MultiIndex columns를 단일 이름으로 정리했다.

## 핵심 구분

| 기능 | 기준 | 수업 예시 | 결과를 읽는 법 |
|---|---|---|---|
| `concat` | 축과 공통 행·열 | 1·2분기 가전제품 판매량 | 표를 위아래 또는 좌우로 이어 붙임 |
| `merge` | key column 또는 index | 학생 정보와 시험 점수 | SQL JOIN처럼 같은 key의 행을 조립 |
| `pivot` | index·columns·values | 이름×품목 구매 내역 | 중복 조합이 없는 long data를 wide data로 변경 |
| `melt` | id column과 측정 column | 직원별 월 실적 | wide data를 관측값 중심 long data로 변경 |
| `pivot_table` | pivot + aggregate | 구·연도·월별 영화 매출 | 중복 조합을 집계해 요약표 생성 |

## 실제 수업 예제

- `concat`: 두 분기 판매량의 column 차이를 확인한 뒤 `axis=0`으로 행을 늘리고 `axis=1`로 열을 늘렸다. 원본 주석 중 `axis=1`을 “행이 늘어난다”고 설명한 부분은 실제 결과와 맞지 않으며, `axis=1`에서는 열이 늘어난다.
- `merge`: 학생과 점수를 `id`로 결합하고 `how`를 inner 기본값에서 outer·left·right로 바꿔 보존되는 행을 비교했다.
- 여러 key: 이름과 과목을 함께 key로 사용하고, 충돌하는 시험 column은 suffix로 중간·기말을 구분했다.
- index merge: 양쪽 `id`를 index로 읽고 `left_index=True`, `right_index=True`, `indicator=True`를 사용했다. `_merge == "left_only"`는 시험 점수 쪽에 대응 행이 없는 학생을 찾는 조건이었다.
- reshape: 과일 구매는 `pivot`, 직원별 월 실적은 `melt`, 영화 매출은 `pivot_table`로 모양과 집계를 바꿨다.

## 자주 헷갈리는 점

- `concat(join="inner")`의 inner는 공통 key로 행을 조립하는 `merge`의 inner와 같은 작업이 아니다. `concat`에서는 이어 붙이지 않는 축의 공통 label을 남긴다.
- `axis=0`은 행을 쌓아 행 수가 늘고, `axis=1`은 열을 붙여 열 수가 늘어난다.
- `on`·`left_on`·`right_on`은 column 기준이고, `left_index`·`right_index`는 index 기준이다.
- `pivot`은 같은 index-column 조합이 중복되면 바로 사용할 수 없다. 집계가 필요하면 `pivot_table`을 쓴다.
- `pivot_table`의 다중 집계 결과는 MultiIndex가 될 수 있으므로 저장·그래프 전에 column 이름을 단순화할 수 있다.
- 노트에 code가 작성되어 있고 일부 DataFrame 표현이 남아 있지만, 독립 `.ipynb` 파일은 raw에 없으므로 전체 notebook 재실행 성공까지 증명하지 않는다.

## 선행·후속 연결

- 선행: [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]의 index·columns·CSV·조회
- SQL 연결: [[concepts/oracle-join|Oracle JOIN]]의 key 결합과 inner/outer 보존 범위
- 후속: [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]의 그룹 요약·시각화
- 적용: [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]의 자전거·매장 데이터 결합

## 관련 수업

- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]

## 출처

- `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
