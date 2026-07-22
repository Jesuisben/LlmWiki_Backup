---
title: Machine Learning 재고도화 재고 및 실행 계획
created: 2026-07-22
updated: 2026-07-22
type: meta
tags: [study-log, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/2026.07.09(목)/2026.07.09(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.10(금)/2026.07.10(금).md
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.14(화)/2026.07.14(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.15(수)/2026.07.15(수).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.20(월)/2026.07.20(월).md
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/2026.07.21(화).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/Pasted image 20260716124822.png
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721120235.png
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721121821.png
  - raw/KoreaICT/11. Machine Learning/2026.07.21(화)/첨부파일/Pasted image 20260721130355.png
  - raw/KoreaICT/11. Machine Learning/Machine Learning 총정리/Machine Learning 총정리.md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(실습).pdf
status: stable
confidence: high
---

# Machine Learning 재고도화 재고 및 실행 계획

## 범위와 강제 경계

- Agent 직접 조사 범위: 2026-07-08 시작일부터 2026-07-21까지 날짜 수업 9개
- 직접 확인 첨부: 2026-07-16 이미지 5개, 2026-07-21 이미지 3개
- 보조 재고 범위: `raw/KoreaICT/11. Machine Learning/교육 자료/` 전체와 0바이트 총정리 파일
- 완전 제외: `raw/KoreaICT/11. Machine Learning/2026.07.22(수)` 폴더 전체
- 제외 범위에는 파일 열람, 내용 검색, hash, manifest, wiki 근거, 수정 후보 판정이 모두 포함된다.
- `Machine Learning 총정리.md`는 0바이트이므로 본문 ingest를 보류한다.
- `2026.00.00(00)`은 8교시 heading만 있는 날짜 template이다. 실제 수업 Summary로 만들지 않는다.

이 문서는 고정 재고와 실행 계획, 날짜별 완료 인계를 함께 보존한다. ML-1~4에서 RML01~RML09의 날짜별 Summary·Concept·Entity ingest를 완료했고, ML-5에서 과목 전체 고정점까지 통과해 단계 11을 최종 완료했다.

## raw 단위 식별자와 manifest

| ID | 범위 | 파일 수 | bytes | 정렬 SHA-256 digest |
|---|---|---:|---:|---|
| RML01 | 2026-07-08 시작 | 1 | 19,133 | `696dd2d3d2fd954b25729754051f3db84c67028999b7589b0a279d103e9baf05` |
| RML02 | 2026-07-09 | 1 | 42,187 | `8e9773c8759144900dd8ae33018d943d10ab91b1fb36e4542d5da075667702e1` |
| RML03 | 2026-07-10 | 1 | 25,407 | `7d909b0a95f3a81d95175fee03aeb88f26e610c6ffe6953c7ddff031bd475af2` |
| RML04 | 2026-07-13 | 1 | 34,066 | `24595238a332d9ddea0ffe3aa3dd2d519bd7405bafd074d6577e8de3f2e0a847` |
| RML05 | 2026-07-14 | 1 | 22,704 | `8a5693a707f58880e66b914ab5002af8f76cf013099688192b10235b7186605f` |
| RML06 | 2026-07-15 | 1 | 15,772 | `2d0739adfe93fc2c2a3f0a3d8337f4c8c3d177ace88075019e36f9910b4d621d` |
| RML07 | 2026-07-16 + 첨부 5개 | 6 | 264,331 | `66075e526963cfa324f37ab8e399d194797208cde0dffb2da450fe17db322324` |
| RML08 | 2026-07-20 | 1 | 12,040 | `ae5f3b5f318589ce64e2f4600d2ef49551d399df6cf5c16fe7c25b9dc74c53aa` |
| RML09 | 2026-07-21 + 첨부 3개 | 4 | 229,343 | `24fbd2559403d8672e95b7068c0420c67bacd2f106a586c7383bed232f6313b5` |
| ML-TOTAL | 0바이트 총정리 | 1 | 0 | `70ec72757a03a7d2b8cf1ef8611c61e05edfb1ad0720657d572928b64bf16bb6` |
| ML-EDU | 교육 자료 전체 | 4,158 | 120,322,346 | `0f31b55ba79f122f783c4d73ebe5318c425c06072db86cdf2f8ee818738f1559` |

Machine Learning 전체 허용 manifest는 4,176개, 120,987,329 bytes이며 digest는 `8d861452dda8eecc0019ae19e339717b3aeabb4e4b56ffafab1883f5a157962d`다. 이 digest에는 RML01~RML09, 첨부 8개, 0바이트 총정리, 교육 자료만 포함되고 2026-07-22와 `2026.00.00(00)`은 포함되지 않는다. 단위별 시작·종료 digest도 전부 동일했다.

## 교육자료 확장자 재고

| 확장자 | 파일 수 | bytes | 역할 |
|---|---:|---:|---|
| `.jpg` | 4,026 | 91,593,922 | 고양이/강아지 dataset 4,020개와 VGG16 입력 3개, 날짜 결과 graph 3개 |
| `.png` | 6 | 489,491 | VGG16 입력 1개와 날짜 첨부 diagram·결과 graph |
| `.py` | 90 | 254,211 | 기초·회귀·분류·군집·CNN·NLP 실습 source |
| `.csv` | 21 | 10,978,851 | 회귀·분류·군집·text dataset |
| `.txt` | 6 | 825,384 | 소설 corpus, 사용자 사전, 요구사항·환경 자료 |
| `.pdf` | 2 | 16,517,328 | 이론 342쪽, 실습 163쪽 교안 |
| `.xlsx` | 1 | 60,825 | Sheet1 `A1:T416` 교육 dataset |
| `.xml` | 8 | 51,108 | IDE project metadata |
| `.iml` | 2 | 688 | IDE module metadata |
| `.pyc` | 1 | 10,036 | `keras_graph_util` bytecode, import/compile 흔적 |
| `.bak` | 1 | 3,246 | requirements backup |
| 확장자 없음 | 2 | 287 | IDE metadata |
| `.md` | 10 | 201,952 | 날짜 MD 9개와 0바이트 총정리 1개 |

확장자 합계는 4,176개로 전체 manifest 파일 수와 일치한다. 교육 자료 root 자체는 4,158개이며, 나머지 18개는 날짜 MD·첨부와 총정리다.

## 0바이트·중복·metadata

- 0바이트 2개: 총정리 MD와 교육 source `k.national/aaa.py`
- byte hash 중복 group 23개, 중복으로 추가된 file 23개
- 중복 구성: dataset과 `dataIn/img` 사이의 cat 10개·dog 10개, IDE profile XML 1개, `requirements.txt`와 `.bak` 1개, 0바이트 2개 1group
- `.idea`·`.iml` 등 IDE metadata: 12개, 52,083 bytes. 학습 내용 근거가 아니라 개발환경 흔적이다.
- `.pyc` 1개는 source module이 한 번 compile/import되었을 가능성을 보여 주지만 전체 program 실행 성공이나 특정 model 학습을 증명하지 않는다.

## 대량 image dataset 단위 재고

| 단위 | class | 수 | bytes | digest/비고 |
|---|---|---:|---:|---|
| `datasets/cats_and_dogs` | cat | 2,000 | dataset 합계에 포함 | 파일명 prefix 기준 |
| `datasets/cats_and_dogs` | dog | 2,000 | dataset 합계에 포함 | 파일명 prefix 기준 |
| `datasets/cats_and_dogs` 전체 | 2 class | 4,000 | 90,897,189 | `fafbfed8b8f8709029c504f1fa023126f262e4d11076edd5dc9ad1755b2e4292` |
| `dataIn/img/cat` | cat sample | 10 | 173,298 | dataset의 동일 파일과 hash 중복 |
| `dataIn/img/dog` | dog sample | 10 | 200,781 | dataset의 동일 파일과 hash 중복 |
| `dataIn/img` 전체 | 2 class | 20 | 374,079 | `97f11dcbd7cab8eee492ed79f446b0b0c040b2b3f7f43ac857e11f2c9a0ab74b` |
| `dataIn/image` | VGG16 prediction input | 4 | 349,114 | `54960a33d9be1c6b086c89fdbc1dd276ed435dd708b564b8235a5f631ea73170` |

대표 pixel 표본으로 `cat.0.jpg`와 `dog.0.jpg`를 확인했다. 전자는 실내에서 사람이 잡고 있는 주황색 고양이로 motion blur와 복잡한 배경이 있고, 후자는 침구 위 검은 소형견으로 flash eye·리드줄·배경 물체가 있다. 이는 class와 실제 촬영 variation을 확인하는 표본일 뿐 전체 4,000개의 label 품질·중복·학습 적합성을 대표하지 않는다.

## source·CSV·TXT·XLSX·PDF 역할

### Python source

- `.py` 90개를 import하지 않고 `ast.parse()`로 검사했다.
- 90개 모두 parse 성공했다. 0바이트 `aaa.py`도 문법적으로는 parse 가능하나 학습 내용은 없다.
- 상위 역할은 `a.basic` 기초 통계·전처리, `b.linear` 회귀, `c~g` 분류 알고리즘, `h.softmax` Keras/MNIST, `i.clustering` 군집, `j.cnn` CNN/VGG16, `k.national` NLP·Word2Vec·Bayesian filter다.
- AST 성공은 문법 구조만 증명한다. dependency 설치, dataset 경로, JVM, model download, fit/evaluate/predict, 파일 저장 성공은 증명하지 않는다.

### 표·text dataset

- CSV 21개는 1~103,904 data row, 1~61 columns 범위다. 모두 row 폭이 일정했다.
- `Salary_dataset.csv`만 빈 header column 1개가 있다. 다른 CSV는 빈 header column이 없다.
- UTF-8 계열 19개, CP949 2개이며 ragged CSV는 0개다.
- TXT 6개에는 5,882줄 소설 corpus, 700줄 유방암 dataset, 소규모 text·사용자 사전, requirements, 399줄 dataset 제작 안내가 있다.
- XLSX 1개는 package 설치 없이 ZIP/XML metadata로 확인했으며 Sheet1 하나, 범위 `A1:T416`이다. cell 결측·자료형 정밀 검사는 실제 ingest 시 수행한다.

### PDF

- 이론 교안: 342쪽, 9,914,711 bytes
- 실습 교안: 163쪽, 6,602,617 bytes
- `pdftotext` 추출은 두 파일 모두 성공했으며 각각 71,345 bytes, 41,823 bytes의 non-empty text가 나왔다.
- 날짜 MD는 PDF page 범위를 이론 설명·실습 code의 보조 provenance로 가리킨다. PDF 전체를 날짜 수업의 직접 실행 증거로 사용하지 않는다.

## 날짜 MD와 첨부 8개 대응

| 날짜 | 첨부 | MD 위치·역할 | pixel 판독과 증거 경계 |
|---|---|---|---|
| 07-16 | `Pasted image 20260716124822.png` | 사전 학습 model 설명 직후 | 강아지·고양이 labeled image → 사전 학습 → model diagram. 이론 설명 image이며 VGG16 download·prediction 실행을 증명하지 않는다. |
| 07-16 | `probability_cat.jpg` | VGG16 top-10 graph 결과 | `cat.jpg` 분류 chart, top class는 tiger cat 약 30%, Egyptian cat 약 25%, tabby 약 16%. 입력 cat pixel과 filename이 대응한다. |
| 07-16 | `probability_fox.jpg` | VGG16 top-10 graph 결과 | `fox.jpg` 분류 chart, red fox 약 95%가 가장 높다. 입력 fox pixel과 filename이 대응한다. |
| 07-16 | `probability_mydog.png` | VGG16 top-10 graph 결과 | `mydog.png` 분류 chart, Labrador retriever 약 65%, kuvasz 약 26%가 상위다. |
| 07-16 | `probability_myrabbit.jpg` | VGG16 top-10 graph 결과 | `myrabbit.jpg` 분류 chart, hare 약 98%가 가장 높다. |
| 07-21 | `Pasted image 20260721120235.png` | KNN 동작 원리 직후 | 구매자·비구매자 점과 새 녹색 point 주변 원으로 최근접 이웃 vote를 설명한다. 실제 KNN 실행 결과는 아니다. |
| 07-21 | `Pasted image 20260721121821.png` | sonar model topology table 직후 | 입력 2개, hidden layer 2개, ReLU, sigmoid output diagram. code는 60 features와 24/10 units이므로 개념 축약도이며 정확한 node 수 diagram은 아니다. |
| 07-21 | `Pasted image 20260721130355.png` | K-fold 일반화 설명 직후 | 5-fold에서 orange test fold를 순환하고 5개 결과를 평균하는 교육 diagram. 이날 code의 `n_splits=10`과는 fold 수가 다르며 절차 설명용이다. |

07-16 결과 graph 4개는 입력 filename, top-10 class label, y축 0~100, code의 chart title·probability×100 흐름과 대응한다. 이는 VGG16 prediction 결과 graph가 실제 저장되었다는 강한 artifact 증거다. 하지만 model download 시점, 전체 console output, `prediction_result.csv`, 모든 source image의 저장 copy, 재실행 가능성은 증명하지 않는다.

## 날짜별 전체 학습 주제

| ID | 날짜 | 학습 흐름 | 본문 ingest 시 핵심 경계 |
|---|---|---|---|
| RML01 | 07-08 | AI/ML/DL 관계 → 지도·비지도·강화 → 회귀·분류·군집 → auto-mpg 단순·다중 선형회귀 | Python 복습 2교시와 ML 시작을 구분. `fit`·metric·save code와 실제 artifact를 구분 |
| RML02 | 07-09 | confusion matrix·accuracy/precision/recall/F1 → SVM/ROC/AUC → KNN·overfitting → Decision Tree·ensemble | 노트의 bagging/boosting/voting 표 label과 설명이 서로 어긋나는 후보를 검토 |
| RML03 | 07-10 | CountVectorizer·Naive Bayes spam → logistic regression iris → Keras·MNIST·gradient descent·activation | embedded sparse output과 실제 run을 구분. 개인 Java 경로 재출력 금지 |
| RML04 | 07-13 | clustering distance·linkage·MDS·KMeans → CNN·pooling·padding → Dropout | graph save code와 physical result 부재, 이론 code fence 오분류 후보 주의 |
| RML05 | 07-14 | NLP·morphology·stopword·tokenization → BoW/CBOW/Word2Vec/N-gram/TF-IDF → sentiment MLP → Toji preprocessing | Word2Vec 저장 부분은 주석 처리 상태이므로 model 생성 성공으로 쓰지 않음 |
| RML06 | 07-15 | Toji token/model 생성 code → 유사도·WordCloud → Bayesian filter 초안 | `toji.model` 등 physical artifact 부재. Bayesian filter는 `pass`가 남은 미완성 단계 |
| RML07 | 07-16 | Bayesian filter 완성 → pretrained model/VGG16 prediction | 출력 text와 graph 4개는 확인. prediction CSV는 없음 |
| RML08 | 07-20 | data collection 복습 → income multiple regression → iris SVM → OCR 실습 과제 | OCR은 풀이·결과 없이 “실습 해보기” 단계 |
| RML09 | 07-21 | KNN preference → KNN·K-fold diagram → sonar 10-fold neural network | diagram의 5-fold와 code의 10-fold 구분, loss/accuracy graph artifact 부재 |

## code·output·model·dataset·artifact 증거 경계

1. code fence는 작성된 source를 증명한다. import·dataset read·fit·predict·save 성공을 자동 증명하지 않는다.
2. 노트 안 text output은 특정 실행 정황이지만 실행 시점·환경·code version이 완전히 연결되지 않을 수 있다.
3. Traceback 또는 오류 설명은 실패 원인 후보를 증명하며 수정 후 성공을 증명하지 않는다.
4. `model.fit()` 호출은 학습 시도 code다. 학습 history·metric·model file·재현 실행이 없으면 완료 model로 확대하지 않는다.
5. source dataset 물리 파일은 입력 가능성을 증명한다. 해당 날짜 code가 실제로 그 파일을 끝까지 처리했다는 증거는 아니다.
6. confusion matrix·ROC·probability graph는 해당 결과 artifact의 존재를 증명한다. train/test leakage·일반화·model 전체 품질은 별도 검증한다.
7. `to_csv`, `savefig`, `model.save` 호출은 저장 의도다. 물리 file 확인 전에는 결과 artifact로 분류하지 않는다.
8. `.pyc`는 compile/import 흔적일 뿐 model training artifact가 아니다.

## raw↔기존 wiki 대응

- ML-4 완료 시점에 Machine Learning raw를 frontmatter `sources`에 직접 선언한 지식 페이지는 `summary 9 / concept 13 / entity 8 / comparison 0 / query 0`, 총 30개다.
- 날짜 Summary는 RML01~RML09 9개가 모두 완료됐고 과목 통합 검증 ML-5만 남았다.
- ML-1~4에서 신규 Concept 12개와 scikit-learn·Keras·Gensim·VGG16 Entity를 만들고, 기존 한국어 text pipeline까지 ML 직접 source로 보강했다.
- 선행 공유 page는 [[entities/python|Python]], [[entities/pandas|Pandas]], [[entities/jupyter-notebook|Jupyter Notebook]], [[entities/matplotlib|matplotlib]], [[entities/konlpy|KoNLPy]], [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]]이다.
- 이들 공유 page는 Python 선행 학습을 보존하고 있다. 다음 ingest에서 실제 ML 날짜 source를 추가할 때만 ML 학습 이력을 부분 보강한다.
- 직접 source 수는 완료된 RML01~RML09 범위의 현재 상태다. 0바이트 총정리나 제외한 2026-07-22를 ingest한 것으로 간주하지 않는다.

## 신규 페이지 후보와 책임 판단

### 날짜 Summary 후보

9개 날짜 모두 학습 주제가 독립적이고 시간 흐름 복원이 필요하므로 날짜 Summary 후보로 유지한다.

- `2026-07-08-machine-learning-foundations-linear-regression.md`
- `2026-07-09-machine-learning-classification-evaluation.md`
- `2026-07-10-machine-learning-text-classification-neural-network.md`
- `2026-07-13-machine-learning-clustering-cnn.md`
- `2026-07-14-machine-learning-nlp-vectorization.md`
- `2026-07-15-machine-learning-word2vec-bayesian-filter.md`
- `2026-07-16-machine-learning-bayesian-filter-pretrained-model.md`
- `2026-07-20-machine-learning-regression-svm.md`
- `2026-07-21-machine-learning-knn-cross-validation.md`

### Concept 후보

독립 검색 가치와 반복 횟수가 높은 후보만 유지한다.

- Machine Learning 지도·비지도 학습과 회귀·분류·군집
- feature/label, train/test split, 전처리, model fit/predict/evaluate lifecycle
- 선형회귀와 R²·MSE
- confusion matrix와 accuracy·precision·recall·F1·ROC/AUC
- SVM·KNN·Decision Tree의 분류 원리
- 과적합·일반화·K-fold cross validation
- clustering distance·hierarchical·KMeans·MDS
- text tokenization·BoW·TF-IDF·Word2Vec
- Keras Dense network·activation·loss·optimizer
- CNN·pooling·padding·Dropout·pretrained model

### Entity 후보

- scikit-learn: 전처리·split·회귀·분류·군집·metric의 공통 toolkit
- Keras/TensorFlow: MNIST·Dense·CNN·VGG16 실습 framework
- VGG16: 07-16 사전 학습 image prediction의 식별 가능한 model
- Gensim: 07-15 Word2Vec model build/load library

### Comparison 후보

- 회귀 vs 분류 vs 군집
- 표준화 vs Min-Max 정규화
- SVM vs KNN vs Decision Tree
- BoW vs TF-IDF vs Word2Vec
- train/test split vs K-fold cross validation
- 학습 model vs 사전 학습 model

### Query 후보

- 왜 scaler는 train에 `fit_transform`, test에는 `transform`만 하는가
- confusion matrix에서 FP와 FN 중 무엇을 더 줄여야 하는가
- save/fit/predict code와 실제 model·graph artifact를 어떻게 구분하는가
- 07-09 ensemble 표의 bagging·boosting·voting 설명이 왜 어긋나는가

## 기존 페이지 처리 분류

| 분류 | 페이지/범위 | 판단 |
|---|---|---|
| 유지 | Python 06-19~07-08 완료 Summary·core Concept | ML 본문을 덮어쓰지 않고 선행 링크로 사용 |
| 부분 보강 | Python·Pandas·Jupyter·matplotlib·KoNLPy Entity | ML 날짜에서 실제 사용된 이력만 source와 함께 누적 |
| 부분 보강 | 한국어 text mining pipeline | 07-10~16 vectorization·Word2Vec·Bayesian filter와 연결하되 Python 07-08 책임 유지 |
| 신규 필요 | 날짜 Summary 9개와 반복 Concept | 직접 source가 0개이므로 실제 ingest에서 생성 |
| 통합 후보 | regression/SVM/KNN 반복 설명 | 날짜 Summary에 흐름, Concept에 재사용 원리를 분리 |
| 근거 부족 | 0바이트 총정리·OCR 과제 결과·저장 파일 없는 model/graph | 완료·성공으로 쓰지 않음 |
| needs-review | 07-09 ensemble 표, 07-14 주석 처리 Word2Vec, 07-15 미완 Bayesian filter | 오류·중간 상태를 그대로 보존 |

## 날짜 순 실행 분할안

### ML-1: RML01~RML02 — 07-08~07-09

- Summary 2개 작성
- ML 기초, 회귀 lifecycle, classification metric Concept의 초기 책임 확정
- scikit-learn Entity 생성 여부 판단
- 07-09 ensemble 표의 용어 오류를 PDF와 대조
- 완료 조건: 두 날짜 전체 흐름·code/output 경계·sources·links·index/log·scoped manifest 검증

### ML-2: RML03~RML04 — 07-10~07-13

- **2026-07-22 완료:** Summary 2개, text vectorization·신경망 학습·clustering·CNN Concept 4개, Keras Entity 1개를 신설했다.
- model lifecycle·문제 유형·분류 평가와 scikit-learn·Python·Pandas·matplotlib에는 ML-2에서 실제 발전한 부분만 누적했다.
- dataset·embedded output·metric/history·메모리 model·graph/CSV save call·물리 artifact를 분리했고, `dataOut` 결과 0개를 성공으로 확대하지 않았다.
- CountVectorizer→Naive Bayes, iris logistic regression→MNIST Dense, 거리→hierarchical/MDS/KMeans, Dense→CNN/Dropout 흐름과 frontmatter·link·manifest 고정점을 통과했다.

### ML-3: RML05~RML07 — 07-14~07-16

- **2026-07-22 완료:** Summary 3개와 text representation·pretrained VGG16 Concept 2개, Gensim·VGG16 Entity 2개를 신설했다.
- Korean text pipeline·Naive Bayes·lifecycle·CNN과 KoNLPy·Keras·Python·Pandas·matplotlib에는 ML-3에서 실제 발전한 책임만 누적했다.
- 07-14 주석 처리 Word2Vec, 07-15 Bayesian `pass` 초안·model artifact 부재, 07-16 완성본·VGG16 graph 4개를 증거 단계별로 구분했다.
- 07-16 첨부 5개와 입력 image 4개를 실제 픽셀·MD 문맥으로 5/5·4/4 대응했고 graph 존재를 download·CSV·전체 재현 성공으로 확대하지 않았다.

### ML-4: RML08~RML09 — 07-20~07-21

- **2026-07-22 완료:** Summary 2개와 KNN distance·voting, K-fold cross-validation·generalization Concept 2개를 신설했다.
- model lifecycle·회귀/분류 평가·신경망 학습과 scikit-learn·Keras·Python·Pandas·matplotlib에는 ML-4에서 실제 발전한 책임만 누적했다.
- income 회귀와 iris SVM의 holdout·train-only scaling, preference KNN의 전체-data Min-Max leakage·test 선택 편향, sonar 10-fold의 fold 내부 preprocessing 원칙을 구분했다.
- 07-21 첨부 3개를 실제 픽셀·MD 문맥으로 3/3 대응하고, 5-fold 도식/10-fold code와 축약 topology/실제 60-24-10-1 구조를 분리했다.
- OCR은 풀이·출력 없는 과제, graph·CSV는 save call만 있고 물리 artifact 0개로 유지했다. TensorFlow Entity·Comparison·Query는 각각 독립 책임·별도 검색 책임·실제 질문이 부족해 만들지 않았다.

### ML-5: 과목 통합 고정점

- **2026-07-22 완료:** 날짜 Summary 9개와 직접 source Concept 14개·Entity 8개·Comparison 1개, 총 32개를 재집계하고 책임 중복·누락과 source union을 교차 검증했다.
- Summary의 세션 한정 문구와 `.py` 개수, 07-14 CountVectorizer+MLPClassifier, 주석 처리된 persistence, 07-15 Word2Vec 생성자 학습·Bayesian `pass`, 07-16 Bayesian 완성·VGG16 graph filename 경계를 source와 다시 동기화했다.
- 반복된 SVM margin/kernel/C/gamma 책임은 `svm-margin-kernel-classification` Concept로, StandardScaler/Min-Max 선택 책임은 `standardization-vs-minmax-scaling` Comparison으로 독립시켰다. 나머지 후보는 기존 Concept가 소유하고 실제 사용자 질문이 없어 Query 0개를 유지했다.
- 직접 source는 `summary 9 / concept 14 / entity 8 / comparison 1 / query 0`, 총 32개이며 RML01~RML09 날짜·첨부 source union 17/17을 유지한다.
- frontmatter·허용 tag·source 실경로와 본문 동기화·broken/ambiguous link·index·고립·중복 title·200줄 초과·placeholder·credential 값·fence 오류 0개, 실제 page 수와 index `Total pages` 312/312를 통과했다.
- Python·ML 허용 범위·ML-1~4 manifest와 scoped raw Git 상태는 기준선과 동일하다. 총정리 0바이트는 계속 보류했고 지정 제외 날짜는 별도 사용자 지시 전까지 완전 제외한다.

## 각 실행 세션 공통 완료 조건

1. 할당 날짜 MD를 처음부터 끝까지 대조한다.
2. 날짜 첨부는 실제 pixel과 MD 앞뒤 문맥을 대응한다.
3. 직접 사용한 교육 source만 보조 provenance에 추가한다.
4. code·output·Traceback·수정·재실행·dataset·model·metric·plot·prediction artifact를 구분한다.
5. 원본에 없는 성공·수치·질문을 만들지 않는다.
6. 개인 환경 경로·credential·API 식별값을 재출력하지 않는다.
7. 새 페이지는 index에 등록하고 의미 있는 작업은 log에 기록한다.
8. scoped `git diff --check`와 시작/종료 manifest 동일성을 확인한다.
9. 2026-07-22가 검색·hash·manifest·source에 포함되지 않았는지 확인한다.
10. 실패·미분류·충돌 후보가 남으면 해당 실행 단위를 완료로 선언하지 않는다.

## 다음 세션 인계

### 2026-07-22 ML-1 완료 상태

- 직접 범위: RML01~RML02 2/2를 처음부터 끝까지 대조했다. ML-1 시작 manifest는 2개·61,320 bytes·`6f5368a7d6bf21bc8df9ca7889da6635391d7a708fa971f15c5d8e712e53d38a`다.
- 신규 Summary 2개: `2026-07-08-machine-learning-foundations-linear-regression`, `2026-07-09-machine-learning-classification-evaluation`
- 신규 Concept 4개: 문제 유형, model lifecycle, 선형회귀 평가, 분류 평가
- 신규 Entity 1개: `scikit-learn`. Python·Pandas·matplotlib Entity에는 실제 ML-1 날짜 이력만 부분 보강했고, 날짜 원문에 독립 Notebook 근거가 없어 Jupyter Notebook은 수정하지 않았다.
- 직접 source 지식 페이지는 `summary 2 / concept 4 / entity 4 / comparison 0 / query 0`, 총 10개로 늘었다. Entity 4개는 Python·Pandas·matplotlib·scikit-learn이다.
- Comparison 판단: 회귀/분류/군집과 분류 지표 비교는 각 overview Concept에 흡수했다. SVM/KNN/Tree는 첫날 알고리즘 개요로 Summary에 흡수하고 후속 반복 뒤 독립 분리를 재판정한다. scaler train/test 비교는 lifecycle의 leakage 책임에 흡수했다.
- Query 판단: 실제 사용자 질문 기록이 없어 0개를 유지했다. ensemble 표 불일치는 07-09 Summary에서 원본 표기·현재 판단·이론 교안 근거를 나눠 교정했다.
- 증거 경계: ML-1 source 4개 AST 오류 0개, `auto-mpg` 398행·9열, 유방암 dataset 700줄·11열과 `?` 16개를 확인했다. `dataOut`의 해당 저장 결과는 0개이므로 fit·metric·save code를 실제 model·graph artifact 성공으로 확대하지 않았다.
- 정확성 교정: 07-09 세 분류 source의 scaler-before-split leakage, StandardScaler의 이상치 설명, 07-08 교육 source의 test 개수 출력 오류, $R^2$ 음수 가능성을 raw 수정 없이 wiki 판단으로 구분했다.

### 2026-07-22 ML-2 완료 상태

- 직접 범위: RML03~RML04 2/2를 처음부터 끝까지 대조했다. ML-2 manifest는 2개·59,473 bytes·`13076df2af3906fe8e2d0291bfd807c0cc6292f46cb17ff882969a3ae11e20f9`다.
- 신규 Summary 2개: `2026-07-10-machine-learning-text-classification-neural-network`, `2026-07-13-machine-learning-clustering-cnn`
- 신규 Concept 4개: text vectorization·Naive Bayes, 신경망 학습 기초, clustering·distance, CNN·Dropout
- 신규 Entity 1개: `Keras`. TensorFlow는 날짜 원문에서 독립 framework 책임이 충분히 분리되지 않아 별도 생성하지 않았다.
- 기존 흡수: logistic regression은 문제 유형·분류 평가·lifecycle에, hierarchical vs KMeans는 군집 Concept에, Dense vs CNN과 padding vs pooling은 CNN Concept에 흡수했다.
- Comparison·Query는 실제 반복 혼동을 Concept가 소유하고 사용자 질문 기록이 없어 각각 0개를 유지했다.
- 증거 경계: 관련 Python source 12개 AST 12/12 통과, mail 86행·iris 150행·도매 고객 440행의 구조를 정적으로 확인했다. embedded output·metric/history code·메모리 model·save call과 물리 CSV·PNG·model artifact를 구분했다.
- 정확성 교정: 음식 거리 표의 squared distance, MNIST 744/784 주석, 결과 CSV 이름 불일치, KMeans cluster ID와 정답 label 차이, Dropout inference 설명, 이론 text의 Python fence 오분류를 raw 수정 없이 wiki에서 구분했다.

다음 세션은 ML-3의 RML05~RML07(2026-07-14·07-15·07-16)만 수행한다. ML-1~2를 중복 재작성하거나 전체 교육자료 재고를 다시 계산하지 않는다. 2026-07-22와 ML-4 이후는 자동으로 시작하지 않는다.

### 2026-07-22 ML-3 완료 상태

- 직접 범위: RML05~RML07 날짜 MD 3개와 RML07 첨부 5개를 대조했다. ML-3 manifest는 8개·302,807 bytes·`6db65866df112202276c0d9988d50d3ebf047c2dcffde7bddbb2437e2cc0b03d`다.
- 신규 Summary 3개: `2026-07-14-machine-learning-nlp-vectorization`, `2026-07-15-machine-learning-word2vec-bayesian-filter`, `2026-07-16-machine-learning-bayesian-filter-pretrained-model`
- 신규 Concept 2개: BoW·TF-IDF·Word2Vec text representation, pretrained model·VGG16 inference
- 신규 Entity 2개: Gensim, VGG16. TensorFlow는 독립 API·runtime 학습 근거가 충분하지 않아 만들지 않았다.
- 기존 흡수: tokenization/stopword는 Korean text pipeline·KoNLPy에, Bayesian 초안→완성은 기존 Naive Bayes Concept에, build/save/load code와 artifact 차이는 lifecycle에 흡수했다.
- BoW·TF-IDF·Word2Vec 비교는 새 Concept가 표와 선택 축을 소유하며 별도 Comparison은 만들지 않았다. Query도 실제 사용자 질문 기록이 없어 0개를 유지했다.
- 증거 경계: Python source AST 7/7, movie review 30행·mail 40행, 《토지》 5,882줄을 정적으로 확인했다. `toji.model`·prediction CSV·WordCloud PNG는 없고 probability graph 4개만 물리 artifact로 확인됐다.

ML-3 인계는 완료됐고 ML-4에서 RML08~RML09를 처리했다. ML-1~4의 완료 페이지를 중복 재작성하지 않는다.

### 2026-07-22 ML-4 완료 상태

- 직접 범위: RML08 날짜 MD 1개와 RML09 날짜 MD·첨부 3개를 대조했다. canonical manifest는 RML08 1개·12,040 bytes·`ae5f3b5f318589ce64e2f4600d2ef49551d399df6cf5c16fe7c25b9dc74c53aa`, RML09 4개·229,343 bytes·`24fbd2559403d8672e95b7068c0420c67bacd2f106a586c7383bed232f6313b5`로 계획 기준선과 일치했다. 같은 formula의 ML-4 통합 manifest도 시작·종료 모두 5개·241,383 bytes·`4084e6c2985e0f732a57c9f18e3c73c5c2f355b71f01ee01496ec4f4db6f34e8`이다.
- 신규 Summary 2개: `2026-07-20-machine-learning-regression-svm`, `2026-07-21-machine-learning-knn-cross-validation`
- 신규 Concept 2개: KNN distance·voting, K-fold cross-validation·generalization
- 기존 흡수: multiple regression·SVM 재방문은 회귀 평가·분류 평가·lifecycle에, sonar topology·fold evaluation은 신경망·Keras에, graph code/artifact는 matplotlib·lifecycle에 누적했다.
- Comparison 후보인 holdout/K-fold, 5/10-fold, metric/평균, 전처리 시점, KNN/SVM은 두 신규 Concept와 lifecycle·평가 페이지가 선택 기준을 소유하므로 별도 생성하지 않았다. Query는 실제 사용자 질문이 없어 0개를 유지했다.
- TensorFlow는 날짜 code의 Keras import를 넘어 독립 API·runtime 책임이 충분하지 않아 Entity를 만들지 않았다. OCR도 풀이·실행 결과 없는 과제여서 독립 Concept로 만들지 않았다.
- 증거 경계: Python source AST 4/4, income 20행·iris 150행·preference 14행·sonar 208행·surgery 470행 구조를 정적으로 확인했다. 실제 metric·History·직렬화 model·CSV·PNG는 없고 07-21 첨부 3개는 교육 개념도다.

### 2026-07-22 ML-5 완료 상태

- 날짜 Summary 9개의 학습 순서·이전/다음 연결·입력→처리→결과와 code/output/metric/History/model/artifact 경계를 과목 전체 흐름으로 교차 검증했다.
- Concept 14개는 문제 유형·lifecycle·회귀/분류 평가·SVM·text·군집·신경망/CNN·KNN/K-fold·pretrained inference 책임을, Entity 8개는 언어·표·시각화·형태소·전통 ML·deep learning·embedding·식별 model의 학습 이력을 각각 소유하도록 확정했다.
- 직접 source 32개, 날짜·첨부 source union 17/17, 구조 오류 0개, page count 312/312, code fence 0개를 확인했다.
- Python 72개·19,361,756 bytes, ML 허용 범위 4,176개·120,987,329 bytes와 ML-1~4 digest가 모두 기준선과 일치하고 scoped raw status/diff도 0건이다.
- StandardScaler와 Min-Max 선택을 독립 검색할 Comparison 1개를 만들고 Query는 0개를 유지했다. 0바이트 총정리는 ingest하지 않았으며 단계 11 Machine Learning은 최종 완료했고 단계 12는 자동으로 시작하지 않았다.

다음 세션은 단계 12 전체 통합 품질 검증만 수행한다. 새 날짜 ingest나 지정 제외 날짜 자료는 별도 사용자 지시 없이 시작하지 않는다.

## 출처

- RML01~RML09의 날짜 MD 9개
- RML07 첨부 이미지 5개와 RML09 첨부 이미지 3개
- `raw/KoreaICT/11. Machine Learning/Machine Learning 총정리/Machine Learning 총정리.md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/` 전체 재고
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(실습).pdf`
