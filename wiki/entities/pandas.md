---
title: Pandas
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
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
status: growing
confidence: high
---

# Pandas

## 무엇인가

Pandas는 Python에서 표 형태 데이터를 다루기 위한 대표 Third Party 라이브러리다. 핵심 자료구조는 1차원 `Series`와 2차원 `DataFrame`이며, CSV 입출력, 조회, 조건 필터링, 통계, 결측값 처리, 데이터 결합, 재구조화, 시각화 준비에 사용된다.

## 이 위키에서의 맥락

2026-06-29~07-03에는 Series/DataFrame, 조회·CSV·결합·집계·그래프를 익혔다. 07-06~07에는 공공 자전거·커피 매장 데이터를 DataFrame으로 만들고 문자열·결측치·index를 정리한 뒤 `merge`, `concat`, `pivot_table`, `groupby`와 지도·차트 분석에 적용했다. 07-08~09 Machine Learning에서는 입력 탐색·결측 처리·feature/label 선택·one-hot encoding과 prediction 비교표를 만드는 model 전후의 표 데이터 계층을 담당했다.

### 첫 등장과 첫 실습

06-29에는 Pandas를 Third Party library로 소개하고 `pip` 설치와 Jupyter 실행 절차를 준비했다. 06-30에는 `Series`를 list·dict에서 생성해 `index`·`values`·`dtype`을 확인하고, label/position 조회, boolean filtering, index 정렬 산술, `NaN`, `value_counts`·`isin`을 실습했다. 마지막에 `DataFrame`의 행·열·2차원 값 구조로 이동했다.

06-30 노트가 참조하는 국가별 신용도 선그래프와 막대그래프 PNG 2개는 Series 시각화 결과가 저장되었다는 artifact 근거다. 이는 Pandas 전체 실습 또는 notebook 전체 재실행 성공의 근거로 확대하지 않는다.

## 핵심 기능 / 특징

- `Series`: 1차원 자료구조. Oracle 테이블의 한 행 또는 한 열처럼 이해할 수 있다.
- `DataFrame`: 여러 Series가 모인 2차원 표 데이터. `index`, `columns`, `values`를 가진다.
- CSV 입출력: `read_csv()`, `to_csv()`로 파일과 표 데이터를 연결한다.
- 데이터 결합: `concat`, `merge`, `pivot`으로 이어 붙이기, JOIN식 병합, 재구조화를 수행한다.
- 그룹화와 집계: `groupby`, `agg`, `transform`, `pd.cut`으로 범주별 요약과 파생 컬럼을 만든다.
- 시각화 준비: `plot()`과 matplotlib를 이용해 파이·산점도·박스플롯·히스토그램·막대 그래프를 그린다.

## 학습 이력

- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]]
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 Python 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 Python 웹 크롤링, 지오코딩, 시각화]]
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 Python 한국어 텍스트 마이닝]]
- [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]] — `auto-mpg` 탐색·결측 처리·feature/label 표 구성
- [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 Machine Learning 분류와 성능 평가]] — Titanic one-hot encoding과 유방암 데이터 전처리·예측 비교표

07-06~08에는 API·웹·text를 표로 바꾸는 공통 중간 layer 역할을 했다. 입력은 정적 대여소 CSV, JSON row list, 파싱한 매장 list, 명사 빈도 list였고, 출력은 결합·집계·시각화에 맞는 DataFrame이었다. 07-06의 정적 CSV 외에는 노트에서 생성하도록 작성한 CSV가 날짜 raw에 남아 있지 않으므로 save call과 저장 성공을 구분한다.

07-08~09에는 Pandas가 model 자체를 학습한 것이 아니라 원본 데이터를 `DataFrame`으로 읽고 결측·범주를 정리해 scikit-learn 입력으로 넘기며, label·prediction·squared error 또는 정답 비교표를 다시 구성했다. Pandas 전처리와 estimator의 `fit` 책임은 구분한다.

07-10에는 mail·iris CSV를 읽고 label·feature를 분리했으며 MNIST test score를 CSV로 만들도록 작성했다. 07-13에는 도매 고객 440행·8열 CSV를 읽어 6개 구매액 feature를 군집 입력으로 넘기고 cluster별 평균·행 수를 집계했다. `DataFrame` 생성·`to_csv` 호출과 실제 결과 CSV artifact는 구분하며 ML-2 교육자료 `dataOut`에는 결과 파일이 없다.

07-16에는 VGG16이 decode한 image filename·class ID·label·probability를 한 행씩 DataFrame에 누적하고 prediction CSV로 저장하도록 작성했다. 물리 CSV가 없으므로 Pandas 표 조립·저장 호출은 확인되지만 저장 성공은 미확정이다.

07-20에는 income 20행 표의 자료형·기초 통계·결측·중복·상관계수를 확인하고, `age`·`experience` feature와 `income` label을 선택했다. test label·prediction·squared error를 DataFrame으로 묶어 CSV 저장을 시도했지만 물리 결과는 없다. 07-21에는 preference 14행의 일곱 feature와 A/B/C label을 분리하고 Min-Max 변환·class 빈도를 확인했으며, sonar 208행의 60 feature·R/M label을 NumPy 배열로 넘겼다. Pandas는 입력·결과표 계층이고 KNN·신경망 학습 자체는 아니다.

## 관련 개념

- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-dataframe-reshape-merge|Pandas DataFrame 결합과 재구조화]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/matplotlib|matplotlib]]
- [[entities/python|Python]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[entities/scikit-learn|scikit-learn]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화와 Naive Bayes 분류]]
- [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리·hierarchical clustering·KMeans]]
- [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]]
- [[concepts/knn-distance-voting|KNN의 distance·voting]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 자주 헷갈리는 점

- Pandas의 `DataFrame`은 SQL 테이블처럼 생겼지만 DB 안의 테이블이 아니라 Python 메모리 안의 객체다.
- `Series` 하나는 1차원이고, `DataFrame`은 2차원이다.
- `concat`은 이어 붙이기, `merge`는 기준 키로 조립하기에 가깝다.
- Pandas는 Python 내장 모듈이 아니라 `pip`로 설치하는 외부 라이브러리다.
- `agg()`는 그룹별 요약표를 만들고, `transform()`은 원본 행 수를 유지해 새 컬럼을 붙이는 데 적합하다.
- 그래프가 이상하게 나오면 먼저 index/columns와 데이터 형태가 그래프 목적에 맞는지 확인해야 한다.

## 프로젝트/면접에서 설명할 관점

“Pandas는 입력 표를 읽고 feature/label·결측·범주를 정리하며 prediction·metric을 결과표로 조립하는 계층이다. estimator의 parameter 학습과 `to_csv`의 물리 artifact 성공은 각각 별도 책임이다”라고 설명할 수 있다.

## 출처

- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
