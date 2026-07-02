---
title: Python
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

# Python

## 무엇인가

Python은 읽기 쉬운 문법과 풍부한 라이브러리를 가진 범용 프로그래밍 언어다. 이 위키에서는 과정 후반부의 데이터 처리·분석 실습 언어로 등장하며, 특히 [[entities/pandas|Pandas]], [[entities/jupyter-notebook|Jupyter Notebook]], CSV 파일 처리, 그래프 시각화와 함께 사용된다.

## 이 위키에서의 맥락

사용자의 커리큘럼은 Java와 Spring/React 풀스택 프로젝트를 먼저 다룬 뒤 Python으로 넘어간다. 따라서 이 위키에서 Python은 “웹 백엔드 주력 언어”라기보다, 표 데이터와 파일을 다루고 분석하는 학습 단계로 기록된다.

2026-07-01 수업에서는 Pandas DataFrame을 만들고 조회·수정·계산·CSV 입출력·시각화하는 데 Python을 사용했다. 2026-07-02 수업에서는 여러 DataFrame을 `concat`, `merge`, `pivot`으로 결합·재구조화하는 데 Python을 사용했다.

## 핵심 기능 / 특징

- `import pandas as pd`, `import numpy as np`처럼 라이브러리를 불러와 데이터 처리를 확장한다.
- 리스트, 문자열, 조건식, 반복문 같은 기본 문법이 Pandas 실습 코드 안에서도 계속 사용된다.
- CSV 파일을 읽고 쓰는 자동화 작업에 적합하다.
- `matplotlib`과 함께 그래프를 그려 데이터를 시각적으로 확인할 수 있다.
- Jupyter Notebook에서 셀 단위로 실행 결과를 보며 학습하기 좋다.

## 학습 이력

### 2026-07-01: Pandas DataFrame 조회와 입출력

- `pd.DataFrame()`으로 표 데이터 생성
- `loc`/`iloc`로 행과 열 조회
- 조건에 맞는 데이터 수정
- `Series` 속성, 통계, 결측값 확인
- `Faker('ko_KR')`로 더미 데이터 생성
- `to_csv()`/`read_csv()`로 CSV 저장·불러오기
- `matplotlib`으로 선 그래프, 막대 그래프, pie 차트 작성

관련 요약: [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]

### 2026-07-02: DataFrame 결합과 재구조화

- `pd.concat()`으로 DataFrame 이어 붙이기
- `pd.merge()`로 공통 열/색인 기준 병합
- `how='outer'`, `left`, `right` 옵션 실습
- `left_on`/`right_on`, `left_index`/`right_index` 구분
- `indicator=True`와 `query()`로 매칭되지 않은 데이터 찾기
- `pivot()`으로 긴 형식 데이터를 넓은 형식으로 변환

관련 요약: [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]

## 관련 개념

- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 프로젝트/면접에서 설명할 관점

이 과정의 Python은 “웹 페이지를 만드는 언어”보다 “데이터를 읽고, 정리하고, 분석하기 위한 언어”로 설명하는 편이 정확하다. 특히 Pandas를 이용하면 CSV나 표 데이터를 SQL 테이블처럼 생각하면서도 Python 코드 안에서 직접 조작할 수 있다.

면접식으로 말하면 다음처럼 정리할 수 있다.

> Java/Spring 과정에서는 웹서비스의 백엔드 구조를 배웠고, Python 과정에서는 Pandas를 통해 CSV 기반 표 데이터를 조회·가공·결합·시각화하는 흐름을 학습했습니다.

## 출처

- `raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/Study/10. Python/2026.07.02(목)/2026.07.02(목).md`
