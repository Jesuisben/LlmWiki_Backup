---
title: Jupyter Notebook
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

# Jupyter Notebook

## 무엇인가

Jupyter Notebook은 코드 셀, 실행 결과, 표, 그래프, 설명을 한 화면에서 함께 다룰 수 있는 대화형 Python 학습 환경이다. 이 위키에서는 Pandas 실습 파일인 `.ipynb`를 실행하고 따라 작성하는 도구로 등장한다.

## 이 위키에서의 맥락

2026-07-01 수업에서는 `ch13_pandas - pandastest02.ipynb`, `Chap03.InputOutput.ipynb` 같은 노트북에서 Pandas DataFrame 조회, CSV 입출력, Series 통계, 그래프를 실습했다.

2026-07-02 수업에서는 `Chap07.Data Reshape.ipynb`를 완성 템플릿으로 참고하되, `ch13_pandas` 폴더에 새 파일을 만들어 직접 타이핑하며 `concat`, `merge`, `pivot`을 연습했다.

따라서 이 과정의 Jupyter Notebook은 단순 편집기가 아니라, 데이터 처리 코드를 작은 셀 단위로 실행하고 바로 결과를 확인하는 학습 환경이다.

## 핵심 기능 / 특징

- 코드 셀을 하나씩 실행하며 중간 결과를 바로 확인할 수 있다.
- DataFrame 출력이 표 형태로 보여 Pandas 학습에 적합하다.
- `matplotlib` 그래프 결과를 노트북 안에서 바로 볼 수 있다.
- 실습 템플릿을 참고해 새 노트북에 직접 타이핑하며 학습할 수 있다.
- 코드, 결과, 주석, 설명이 함께 남기 때문에 복습 자료로 쓰기 좋다.

## 학습 이력

### 2026-07-01

- `ch13_pandas - pandastest02.ipynb`에서 DataFrame 조회 문제 실습
- `Chap03.InputOutput.ipynb`에서 CSV 저장/불러오기, Series 속성, 통계, 결측값, 그래프 실습
- DataFrame을 출력하면 표 형태로 바로 확인하는 흐름을 익힘

관련 요약: [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]

### 2026-07-02

- `Chap07.Data Reshape.ipynb` 템플릿을 바탕으로 새 노트북 파일 생성
- `concat`, `merge`, `pivot` 코드를 직접 타이핑하며 데이터 결합과 재구조화 실습
- CSV 파일을 읽고 결합 결과를 셀 출력으로 확인

관련 요약: [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]

## 관련 개념

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 자주 헷갈리는 점

- Jupyter Notebook은 Python 언어 자체가 아니라 Python 코드를 실행하고 기록하는 환경이다.
- `.ipynb` 파일은 일반 `.py` 파일과 달리 셀, 실행 결과, 메타데이터를 함께 저장한다.
- 셀을 순서대로 실행하지 않으면 이전 셀에서 만든 변수 상태 때문에 결과가 헷갈릴 수 있다.
- 템플릿 노트북을 그대로 보는 것과 새 노트북에 직접 타이핑해 보는 것은 학습 효과가 다르다. 원본 수업은 직접 타이핑하는 방식을 강조했다.

## 프로젝트/면접에서 설명할 관점

Jupyter Notebook은 데이터 분석 학습에서 “실험 노트”에 가깝다. Pandas 코드 한 조각을 실행하고, DataFrame 표와 그래프 결과를 바로 보면서 데이터 처리 과정을 단계적으로 확인할 수 있다.

## 출처

- `raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/Study/10. Python/2026.07.02(목)/2026.07.02(목).md`
