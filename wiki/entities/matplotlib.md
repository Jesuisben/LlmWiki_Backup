---
title: matplotlib
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [python]
sources:
  - raw/Study/10. Python/2026.07.03(금)/2026.07.03(금).md
status: seed
confidence: high
---

# matplotlib

## 무엇인가

matplotlib은 Python에서 그래프를 그리는 대표 시각화 라이브러리다. 이 위키에서는 [[entities/pandas|Pandas]]로 만든 집계 결과를 파이 차트, 산점도, 박스 플롯, 히스토그램, 막대 그래프로 확인하는 도구로 등장한다.

## 이 위키에서의 맥락

2026-06-30~07-01 수업에서는 Pandas `plot()`으로 기초 그래프를 맛봤고, 2026-07-03에는 복지 데이터와 소득 데이터를 이용해 본격적으로 여러 그래프 유형을 사용했다. 특히 `plt.rc('font', family='Malgun Gothic')`로 한글 폰트를 지정하고, `plt.title()`, `plt.xlabel()`, `plt.legend()` 같은 설정을 함께 다뤘다. ^[raw/Study/10. Python/2026.07.03(금)/2026.07.03(금).md]

## 핵심 기능 / 특징

- `import matplotlib.pyplot as plt` 형태로 주로 사용한다.
- Pandas `DataFrame.plot()`/`Series.plot()`은 내부적으로 matplotlib를 활용한다.
- `kind='pie'`, `kind='scatter'`, `kind='hist'`, `kind='barh'`처럼 그래프 유형을 지정할 수 있다.
- `plt.boxplot()`으로 그룹별 분포와 이상치를 확인하는 박스 플롯을 그릴 수 있다.
- `plt.rc('font', family='Malgun Gothic')`처럼 한글 표시를 위한 폰트 설정이 필요할 수 있다.

## 학습 이력

- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]] — Pandas와 함께 그래프 학습이 시작됨
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]] — Series 통계와 pie chart 흐름
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]] — 파이·산점도·박스플롯·히스토그램·막대 그래프 실습

## 관련 개념

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]

## 자주 헷갈리는 점

- Pandas의 `.plot()`과 matplotlib는 별개처럼 보이지만, Pandas 그래프는 matplotlib 위에서 그려지는 경우가 많다.
- 그래프가 이상하게 나오면 코드보다 먼저 데이터의 index/columns 구조가 그래프에 맞는지 확인해야 한다.
- 한글 제목·축·범례가 깨질 때는 폰트 설정 문제일 수 있다.
- pie chart는 비율 비교에, scatter는 두 숫자 변수 관계에, box plot은 분포와 이상치에, histogram은 한 변수의 분포에 적합하다.

## 출처

- `raw/Study/10. Python/2026.07.03(금)/2026.07.03(금).md`
