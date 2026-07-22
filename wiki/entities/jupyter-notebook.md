---
title: Jupyter Notebook
created: 2026-07-01
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md
  - raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
  - raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md
status: growing
confidence: high
---

# Jupyter Notebook

## 무엇인가

Jupyter Notebook은 코드 셀, 실행 결과, 표, 그래프, 설명을 한 화면에서 함께 다룰 수 있는 대화형 Python 학습 환경이다.

## 이 위키에서의 맥락

2026-06-29부터 07-03까지 Pandas 실습을 셀 단위로 진행했다. 07-06에는 VS Code에서 `.ipynb`를 열어 Python/Jupyter kernel을 선택하는 실행 환경도 확인했다. VS Code는 편집·실행 도구이고 Jupyter Notebook은 셀·출력·메타데이터를 담는 노트북 형식/환경이라는 점을 구분한다.

07-06~08의 날짜 노트는 API·crawl·text mining code를 notebook 셀 흐름처럼 보존하지만 독립 `.ipynb` 파일은 raw에 없다. 일부 표·오류 설명·PNG는 남아 있어 특정 실행 정황은 확인되나, 셀 metadata·실행 순서·kernel 상태가 없으므로 전체 notebook 재현성은 검증할 수 없다.

### 2026-06-30까지의 첫 사용

06-29에는 command prompt에서 notebook server를 시작하고 작업 폴더를 지정하는 절차를 정리했다. 06-30에는 code cell과 Markdown cell, `Ctrl + Enter`와 `Shift + Enter`, 저장 방식을 확인하며 Pandas Series를 셀 단위로 실행했다. Series 표와 graph 출력은 날짜 노트에 embedded되어 있고 graph PNG 2개가 남아 있지만, `.ipynb` file 자체는 직접 raw 재고에 없다. 따라서 notebook curriculum과 일부 결과는 확인되지만 전체 셀 실행 순서·재현성은 검증되지 않았다.

## 핵심 기능 / 특징

- 코드 셀을 하나씩 실행하며 중간 결과를 확인한다.
- `Ctrl + Enter`, `Shift + Enter`로 셀 실행 흐름을 조절한다.
- DataFrame 출력이 표 형태로 보여 Pandas 학습에 적합하다.
- Markdown 셀로 설명 제목과 실습 메모를 함께 남길 수 있다.
- matplotlib 그래프 결과를 노트북 안에서 바로 볼 수 있다.
- 완성 템플릿을 참고해 새 노트북에 직접 타이핑하면서 코드 흐름을 재현할 수 있다.

## 학습 이력

- [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]]
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 Python 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 Python 웹 크롤링, 지오코딩, 시각화]]
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 Python 한국어 텍스트 마이닝]]

## 관련 개념

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/matplotlib|matplotlib]]

## 자주 헷갈리는 점

- Jupyter Notebook은 Python 언어 자체가 아니라 Python 코드를 실행하고 기록하는 환경이다.
- `.ipynb` 파일은 일반 `.py` 파일과 달리 셀, 실행 결과, 메타데이터를 함께 저장한다.
- 셀을 순서대로 실행하지 않으면 변수 상태 때문에 결과가 헷갈릴 수 있다.
- 그래프와 표 결과가 이전 셀의 변수 상태에 의존하므로, 중간부터 실행할 때는 필요한 셀을 먼저 실행해야 한다.
- Notebook 서버가 실행되는 동안 cmd 창을 닫으면 안 된다.

## 출처

- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
