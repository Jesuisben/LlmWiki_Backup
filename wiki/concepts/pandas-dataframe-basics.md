---
title: Pandas DataFrame 기본
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [python]
sources:
  - raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md
status: growing
confidence: medium
---

# Pandas DataFrame 기본

## 정의

Pandas DataFrame은 행과 열을 가진 표 형태의 데이터를 Python에서 다루기 위한 핵심 자료구조다.

## 왜 중요한가

CSV, Excel, 데이터베이스 조회 결과처럼 표 형태 데이터는 개발과 데이터 분석에서 자주 등장한다. DataFrame을 이해하면 조회, 필터링, 집계, 시각화로 확장하기 쉽다.

## 핵심 설명

- index: 행 이름 또는 행 위치를 나타낸다.
- columns: 열 이름을 나타낸다.
- Series: DataFrame의 한 열 또는 한 행처럼 1차원 데이터에 가깝다.
- 조회: 행/열 이름, 위치, 조건을 기준으로 데이터를 꺼낸다.
- 그래프: DataFrame/Series 데이터를 시각적으로 확인하는 데 사용한다.

## 예시

리스트와 columns/index 정보를 조합해 DataFrame을 만들고, 특정 열이나 행을 선택해 조회 문제를 해결한다.

## 자주 헷갈리는 점

- Python 리스트의 인덱스와 DataFrame의 index 라벨은 비슷해 보이지만 항상 같은 개념은 아니다.
- 행 기준 조회와 열 기준 조회의 문법이 다르므로 예제를 나눠 익혀야 한다.

## 관련 개념

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]

## 출처

- `raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md`
