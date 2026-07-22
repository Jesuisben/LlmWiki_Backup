---
title: Python
created: 2026-07-01
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md
  - raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md
  - raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md
  - raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md
  - raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md
  - raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md
  - raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
  - raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
status: growing
confidence: high
---

# Python

## 무엇인가

Python은 읽기 쉬운 문법과 풍부한 표준·외부 라이브러리를 가진 범용 프로그래밍 언어다. 이 위키에서는 과정 후반부에 데이터 처리·파일 입출력·정규표현식·JSON/XML·Pandas 분석 실습을 수행하는 언어로 등장한다.

## 이 위키에서의 맥락

2026-06-19~06-29에는 Pandas 이전 기초를 다졌다. 이후 Jupyter/Pandas에서 DataFrame 조회·결합·집계·시각화로 확장했고, 2026-07-06~08에는 Open API·웹 크롤링·지오코딩·지도와 한국어 텍스트 마이닝으로 실제 외부 데이터를 수집·정제·표현했다. 같은 07-08 오후부터는 Python이 [[entities/scikit-learn|scikit-learn]] model과 전처리·평가 API를 조립하는 Machine Learning 실행 언어로 확장됐다.

### 2026-06-30까지의 기초 학습

- 06-19: 실행 환경, 출력·입력·형변환·연산·문자열·slicing
- 06-22~23: 조건·반복, list/tuple/dict/set, comprehension·내장 함수
- 06-24~25: 함수·lambda·module/package, 표준 library, class·상속·Has-A
- 06-26~29: 예외·file I/O·regex·XML/JSON, `pip`와 Jupyter 준비
- 06-30: Jupyter에서 Pandas Series를 조회·계산·필터링·시각화하고 DataFrame 구조에 진입

이 구간은 순수 Python collection과 file 처리에서, label이 있는 Series/DataFrame으로 넘어가는 하나의 학습 단계다. 06-30의 국가별 그래프 PNG 2개는 시각화 결과 artifact가 남아 있음을 보여 주지만 전체 notebook 실행을 증명하지는 않는다.

## 핵심 기능 / 특징

- `print`, `input`, 문자열 함수, 형변환으로 기본 입출력과 데이터 변환을 수행한다.
- `if`, `for`, `while`, `range`로 실행 흐름을 제어한다.
- `list`, `tuple`, `dict`, `set`, comprehension으로 여러 데이터를 묶고 필터링한다.
- `def`, `lambda`, `map`, `filter`, 모듈·패키지로 코드를 재사용한다.
- `os`, `random`, `datetime`, `re`, `json`, `xml.etree.ElementTree`로 파일·날짜·패턴·구조화 데이터를 다룬다.
- `pip`로 Pandas, matplotlib 같은 Third Party 라이브러리를 설치해 데이터 분석 기능을 확장한다.
- Pandas의 `groupby`/`transform`과 matplotlib 그래프로 표 데이터를 요약·시각화한다.
- `requests`·Selenium·BeautifulSoup으로 외부 JSON·HTML을 수집하고 Folium으로 좌표를 지도화한다.
- KoNLPy·NLTK로 한국어 text를 token·빈도 데이터로 바꾼다.

### 2026-07-01~08 데이터 처리 확장

- 07-01: 단일 DataFrame 조회·수정·산술·CSV·기초 통계와 graph artifact 3개
- 07-02: `concat`·`merge`·`pivot`·`melt`·`pivot_table`로 결합·재구조화
- 07-03: `groupby`·`agg`·`transform`·`cut`과 여러 chart code
- 07-06: 공공 API JSON·대여소 CSV를 수집·정제·병합·지도화하는 code
- 07-07: Selenium/BeautifulSoup·지오코딩·커피 매장 지도·chart code
- 07-08: Komoran·NLTK·Pandas·WordCloud를 잇는 한국어 text mining code

07-01 PNG 3개와 07-06 교육자료 CSV는 물리 artifact지만, 나머지 `to_csv`·`save`·`plot`·request 호출의 결과 파일은 날짜 raw에 없다. 설치 명령·code 작성·text output·물리 artifact를 구분하며 전체 notebook 재실행 성공을 주장하지 않는다.

### 2026-07-08~09 Machine Learning 전환

- 07-08: `auto-mpg` 입력을 전처리하고 `LinearRegression`의 train/test split·fit·predict·$R^2$·MSE 흐름을 작성했다.
- 07-09: Titanic SVM/KNN과 유방암 Decision Tree에서 one-hot encoding·scaling·분류 metric·ROC/AUC·tree 해석 code를 작성했다.
- 두 날짜의 독립 Python source 4개는 AST parse 오류가 없지만 실행 stdout·직렬화 model·저장 graph가 없으므로 code 작성과 실행·artifact 성공을 구분한다.

### 2026-07-10~13 text·신경망·군집·CNN 확장

- 07-10: 한국어 mail tokenization·sparse vector·Naive Bayes, iris logistic regression, MNIST Dense network의 compile→fit→evaluate code
- 07-13: SciPy distance·linkage, MDS·KMeans, Keras Conv2D·Pooling·Dropout topology code
- 관련 독립 Python source 12개는 import·실행 없이 AST parse 12/12를 통과했다. 이는 문법 구조만 확인하며 dependency·dataset download·fit·save 성공은 증명하지 않는다.

### 2026-07-14~16 NLP·Word2Vec·pretrained model 확장

- 07-14: 형태소·stopword·BoW/TF-IDF/Word2Vec 이론에서 sentiment MLP와 《토지》 전처리로 연결
- 07-15: Gensim Word2Vec build/load·similarity·WordCloud와 Bayesian filter 초안
- 07-16: Bayesian score/predict 완성, Keras VGG16 image preprocessing·prediction·graph/CSV 저장 code
- 관련 독립 Python source 7개는 import 없이 AST parse 7/7을 통과했다. `toji.model`과 prediction CSV는 없고, VGG16 probability graph 4개만 물리 artifact로 확인됐다.

### 2026-07-20~21 회귀·SVM 재방문과 교차 검증

- 07-20: income 다중회귀의 탐색→split→fit→$R^2$/MSE와 iris의 split→train-only scaling→SVM 평가 code
- 07-21: preference KNN의 Min-Max·K 선택과 sonar 10-fold Dense network의 fold별 loss·accuracy 평균·graph code
- 관련 독립 source 4개는 import 없이 AST parse 4/4를 통과했다. 날짜 code와 source의 dataset·split·import·graph 범위가 다른 version 차이가 있으며 실제 metric·CSV·PNG·model artifact는 없다.

## 학습 이력

- [[summaries/2026-06-19-python-setup-basic-syntax|2026-06-19 Python 설치와 기본 문법 입문]]
- [[summaries/2026-06-22-python-control-flow-collections|2026-06-22 Python 제어문과 컬렉션]]
- [[summaries/2026-06-23-python-dict-comprehension-builtins|2026-06-23 Python dict, comprehension, 내장 함수]]
- [[summaries/2026-06-24-python-functions-modules|2026-06-24 Python 함수, 람다, 모듈·패키지]]
- [[summaries/2026-06-25-python-standard-library-oop|2026-06-25 Python 표준 라이브러리와 객체지향]]
- [[summaries/2026-06-26-python-exception-file-regex|2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식]]
- [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- [[summaries/2026-06-30-python-pandas-series-dataframe-intro|2026-06-30 Python Pandas Series와 DataFrame 입문]]
- [[summaries/2026-07-01-python-pandas-dataframe|2026-07-01 Python Pandas DataFrame 조회와 입출력]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]
- [[summaries/2026-07-03-python-pandas-groupby-visualization|2026-07-03 Python Pandas groupby와 시각화]]
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 Python 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 Python 웹 크롤링, 지오코딩, 시각화]]
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 Python 한국어 텍스트 마이닝]]
- [[summaries/2026-07-08-python-subject-review|Python 총정리]]
- [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]]
- [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 Machine Learning 분류와 성능 평가]]
- [[summaries/2026-07-10-machine-learning-text-classification-neural-network|2026-07-10 텍스트 분류와 신경망 입문]]
- [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]
- [[summaries/2026-07-14-machine-learning-nlp-vectorization|2026-07-14 NLP 표현과 Word2Vec 입문]]
- [[summaries/2026-07-15-machine-learning-word2vec-bayesian-filter|2026-07-15 Word2Vec과 Bayesian filter 초안]]
- [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|2026-07-16 Bayesian filter 완성과 사전 학습 모델]]
- [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]]

## 관련 개념

- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-functions-modules-packages|Python 함수, 모듈, 패키지]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]
- [[concepts/python-oop-basics|Python 객체지향 기본]]
- [[concepts/python-exception-handling|Python 예외 처리]]
- [[concepts/python-regular-expression|Python 정규표현식]]
- [[concepts/python-structured-data-xml-json|Python XML/JSON 구조화 데이터 처리]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/matplotlib|matplotlib]]
- [[entities/scikit-learn|scikit-learn]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화와 Naive Bayes 분류]]
- [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리·hierarchical clustering·KMeans]]
- [[entities/keras|Keras]]
- [[entities/gensim|Gensim]]
- [[entities/vgg16|VGG16]]
- [[concepts/knn-distance-voting|KNN의 distance·voting]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]

## 프로젝트/면접에서 설명할 관점

이 과정의 Python은 “순수 Python으로 텍스트·XML·JSON 데이터를 다루는 기본기를 만든 뒤, Pandas로 표 데이터를 처리하고 scikit-learn·Keras·KoNLPy·Gensim을 조립해 Machine Learning pipeline을 구현한 실행 언어”로 설명할 수 있다. source 작성·AST 통과·실제 runtime·artifact 성공은 서로 다른 증거다.

## 출처

- `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md`
- `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md`
- `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md`
- `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md`
- `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md`
- `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md`
- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
- `raw/KoreaICT/10. Python/2026.07.02(목)/2026.07.02(목).md`
- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
