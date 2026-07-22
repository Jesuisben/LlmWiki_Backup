---
title: matplotlib
created: 2026-07-03
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203348.png
  - raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203436.png
  - raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
  - raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
status: growing
confidence: high
---

# matplotlib

## 무엇인가

matplotlib은 Python에서 그래프를 그리는 대표 시각화 라이브러리다. 이 위키에서는 [[entities/pandas|Pandas]]로 만든 집계 결과를 파이 차트, 산점도, 박스 플롯, 히스토그램, 막대 그래프로 확인하는 도구로 등장한다.

## 이 위키에서의 맥락

Pandas 집계 결과에서 시작해 자전거·커피 매장·단어 빈도 데이터의 막대·파이·산점도·분포 그래프까지 확장했다. 07-08~09 Machine Learning에서는 상관 heatmap·회귀선·label/prediction 산점도, confusion matrix·ROC curve·feature importance·tree 시각화의 출력 도구로 사용됐다. 한글 표기를 위해 `Malgun Gothic` 설정을 반복 사용했다.

### 2026-06-30 첫 시각화

06-29에는 matplotlib 설치·제거 command가 Jupyter/Pandas 준비 과정에 기록되어 있으나 최종 설치 상태는 보존되지 않았다. ^[raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md]

06-30에는 Pandas `Series.plot()`으로 같은 국가별 신용도 데이터를 선그래프와 막대그래프로 표현했다. 노트에 직접 연결된 PNG 2개는 각각 7개 국가 label과 신용도 y축을 가진다. 막대그래프는 인접 code와 대응도가 높지만, 선그래프는 code 제목·text 반환값·PNG 픽셀 제목의 철자와 띄어쓰기가 달라 현재 보이는 cell의 정확한 산출물이라고 단정할 수 없다. 두 PNG는 graph artifact 존재의 근거이며 전체 Jupyter/Pandas 실행 성공의 근거는 아니다. ^[raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md]

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
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 Python 공공데이터 API와 자전거 분석]] — 대여소·거치대·거치율 chart code
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 Python 웹 크롤링, 지오코딩, 시각화]] — 매장 분포와 서비스 제공 현황 chart code
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 Python 한국어 텍스트 마이닝]] — 상위 단어 bar chart와 WordCloud 출력 연결
- [[summaries/2026-07-08-machine-learning-foundations-linear-regression|2026-07-08 Machine Learning 기초와 선형회귀]] — 회귀 탐색·평가 graph 저장 code
- [[summaries/2026-07-09-machine-learning-classification-evaluation|2026-07-09 Machine Learning 분류와 성능 평가]] — confusion matrix·ROC·tree graph 저장 code

07-01의 PNG 3개는 인접 code와 대응하는 실제 graph artifact다. 반면 07-03·06·07·08 날짜 폴더에는 저장 chart 파일이 없고, 07-07에는 같은 PNG 이름을 재사용하는 code도 있다. `plot`·`savefig` 호출과 물리 artifact·정상 rendering을 구분한다.

ML-1의 07-08~09 source에도 여러 `savefig` 호출과 “저장되었습니다” 출력문이 있지만 교육자료 `dataOut`에 해당 PNG가 없다. 따라서 시각화 code의 존재만 기록하고 실제 graph artifact나 전체 model 실행 성공으로 확대하지 않는다.

ML-2의 07-10에는 iris confusion matrix heatmap과 MNIST history graph를, 07-13에는 KMeans 중심 이동·dendrogram·MDS·cluster 산점도와 CNN history graph를 그리도록 작성했다. 관련 Python source의 `savefig`·utility 호출은 있으나 `dataOut`에 물리 PNG가 없어 실제 metric curve·cluster graph·저장 성공은 미확정이다.

ML-3의 07-15에는 Word2Vec 유사 단어 bar chart와 WordCloud 저장 code가 있지만 물리 결과가 없다. 07-16에는 VGG16 top-10 probability graph 4개가 날짜 첨부로 실제 존재하며 입력 image·class label과 4/4 대응한다. probability graph의 `savefig` 이름도 첨부 filename과 일치하지만, graph 존재를 model download·CSV·전체 실행 성공으로 확대하지 않는다. 별도 `pretrained_model_<입력명>` 호출은 resize된 입력 image 재저장용이며 해당 artifact는 확인되지 않았다.

ML-4의 07-20에는 income pairplot·상관 heatmap·feature scatter·정답/예측 regplot과 iris scatter·confusion matrix 저장 code가 있다. 07-21에는 preference K별 accuracy·confusion matrix, sonar fold별 loss·accuracy line/bar·이중축 graph 네 개를 저장하도록 작성했다. 교육자료의 `dataOut`·`dataout`에는 해당 결과가 없으므로 모두 graph code·저장 의도이며 물리 artifact는 아니다. 07-21 첨부 3개는 KNN·topology·5-fold 교육 도식으로, matplotlib 실습 출력과 구분한다.

## 관련 개념

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/scikit-learn|scikit-learn]]
- [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]
- [[concepts/classification-evaluation-metrics|분류 성능 평가]]
- [[concepts/clustering-distance-hierarchical-kmeans|군집과 거리·hierarchical clustering·KMeans]]
- [[concepts/neural-network-training-basics|신경망 학습 기초]]
- [[concepts/text-representation-bow-tfidf-word2vec|BoW·TF-IDF·Word2Vec 텍스트 표현]]
- [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]]
- [[concepts/k-fold-cross-validation-generalization|K-fold 교차 검증과 일반화]]
- [[summaries/2026-07-20-machine-learning-regression-svm|2026-07-20 소득 다중회귀와 iris SVM]]
- [[summaries/2026-07-21-machine-learning-knn-cross-validation|2026-07-21 KNN과 K-fold 신경망 평가]]

## 자주 헷갈리는 점

- Pandas의 `.plot()`과 matplotlib는 별개처럼 보이지만, Pandas 그래프는 matplotlib 위에서 그려지는 경우가 많다.
- 그래프가 이상하게 나오면 코드보다 먼저 데이터의 index/columns 구조가 그래프에 맞는지 확인해야 한다.
- 한글 제목·축·범례가 깨질 때는 폰트 설정 문제일 수 있다.
- pie chart는 비율 비교에, scatter는 두 숫자 변수 관계에, box plot은 분포와 이상치에, histogram은 한 변수의 분포에 적합하다.

## 프로젝트/면접에서 설명할 관점

“matplotlib는 탐색·평가 결과를 시각화하지만 `savefig` 호출과 물리 PNG 존재는 다르며, graph 하나가 model 성능·CSV·전체 실행 성공을 대신하지 않는다”고 설명할 수 있다.

## 출처

- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203348.png`
- `raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203436.png`
- `raw/KoreaICT/10. Python/2026.07.03(금)/2026.07.03(금).md`
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md`
