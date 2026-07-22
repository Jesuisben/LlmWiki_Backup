---
title: 2026-07-16 Bayesian filter 완성과 사전 학습 모델
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/Pasted image 20260716124822.png
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/bayes_test.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/pretrainedModel.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mail_data.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/cat.jpg
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/fox.jpg
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/mydog.png
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/myrabbit.jpg
status: growing
confidence: high
---

# 2026-07-16 Bayesian filter 완성과 사전 학습 모델

## 한 줄 요약

전날 tokenization·`fit()` 골격과 `pass`로 남았던 Bayesian filter에 word/category count와 score·predict를 채워 text 분류 흐름을 완성하고, ImageNet 사전 학습 VGG16으로 네 입력 image의 top class probability graph를 만드는 추론 단계로 확장했다.

## 전체 교시·학습 순서

1. Bayesian filter의 단어·category count 복습
2. Laplace smoothing을 포함한 category별 score 계산
3. 입력 text의 category prediction 완성
4. `mail_data.csv`로 train하고 새 문장 예측
5. 사전 학습 model과 transfer learning 개념
6. VGG16·ImageNet class 구조
7. image load→224×224 resize→array→batch→`preprocess_input`
8. `predict`→`decode_predictions`→top class·probability
9. top-10 막대그래프와 prediction CSV 저장 code
10. 첨부 graph 4개와 실제 입력 image 4개 대응

## 왜 이 흐름으로 배웠는가

07-15는 token embedding과 Bayesian classifier 초안까지 진행했다. 이날 첫 부분은 직접 구현 classifier의 반환 경로를 완성해 “count가 어떻게 prediction이 되는가”를 닫는다. 이후에는 [[concepts/cnn-convolution-pooling-dropout|직접 topology를 작성한 CNN]]에서 한 단계 나아가, 이미 대규모 dataset으로 학습된 parameter를 가져와 preprocessing·prediction·해석에 집중했다.

## Bayesian filter: 07-15 초안 → 07-16 완성

| 단계 | 07-15 | 07-16 |
|---|---|---|
| tokenization·`fit()` 골격 | 구현 | 유지 |
| token count | `increase_word()`가 `pass` | category별 count와 전체 vocabulary 누적 |
| category count | 미구현 | 문서 category count 누적 |
| category score | 미구현 | prior와 token likelihood를 log로 누적 |
| predict | 미구현 | 모든 category score 중 최대값 반환 |

`mail_data.csv`는 40행·2열이고 `광고`/`일반` label이 20개씩이다. Laplace smoothing은 train에서 보지 못한 token 때문에 전체 probability가 0이 되는 것을 막지만, 작은 dataset의 일반화 성능을 보장하지 않는다. 원문은 예측 text를 포함하지만 별도 accuracy·confusion matrix는 없다.

## VGG16 입력 → 처리 → 결과

- **입력:** RGB image 한 장.
- **구조:** 원래 크기와 무관하게 224×224×3으로 맞추고 batch 차원을 더해 1×224×224×3 tensor로 변환.
- **전처리:** VGG16 학습 조건에 맞는 `preprocess_input` 적용.
- **prediction:** 1,000개 ImageNet class에 대한 score vector 생성.
- **해석:** `decode_predictions`로 class label과 probability를 얻고 top-10 graph 구성.
- **저장 의도:** graph file과 누적 prediction CSV.

## 첨부 5개와 실제 픽셀 대응

### 개념 도식 1개

`Pasted image 20260716124822.png`는 강아지·고양이 labeled image가 “사전 학습” 단계를 거쳐 model로 이어지는 993×255 도식이다. 개념 설명 근거이지 VGG16 download·실행 결과는 아니다.

### 입력 4개 ↔ 결과 graph 4개

| 입력 pixel | 결과 graph | top class | 판정 |
|---|---|---|---|
| 실내의 주황색 줄무늬 어린 고양이 | `probability_cat.jpg` | tiger cat 약 30%, Egyptian cat 약 25%, tabby 약 16% | 고양이 입력·ImageNet 고양이 class가 의미상 대응 |
| 눈밭의 붉은 여우 | `probability_fox.jpg` | red fox 약 95% | 입력 대상과 직접 대응 |
| 흰색·크림색 어린 강아지 얼굴 | `probability_mydog.png` | Labrador retriever 약 65%, kuvasz 약 26% | 강아지 입력과 견종 class가 의미상 대응하나 실제 품종 정답은 미확정 |
| 손 위의 흰 토끼 | `probability_myrabbit.jpg` | hare 약 98% | 토끼류 입력과 의미상 대응하지만 rabbit와 hare는 생물학적으로 동일 label이 아님 |

네 graph는 모두 1000×800 top-10 bar chart이고, filename·title·확률×100 흐름이 원문 code 및 입력 파일과 대응한다.

## graph artifact가 증명하는 범위

- graph 네 파일이 실제 존재하고 top class·probability가 픽셀로 읽힌다.
- 입력 filename과 graph filename이 4/4 대응한다.
- 이는 적어도 prediction 결과를 graph로 만든 artifact가 남았다는 강한 근거다.
- 하지만 model weight download 시점, 전체 source의 오류 없는 end-to-end 실행, console output 전부, `prediction_result.csv`, graph를 만든 정확한 code version, 현재 환경 재현 성공은 증명하지 않는다.
- resize된 입력 image 재저장용 `pretrained_model_<입력명>` artifact는 확인되지 않았다. probability graph의 `savefig` filename은 `probability_<입력명>`으로 첨부 4개와 일치하지만, 이것만으로 전체 loop·CSV·현재 재현 성공까지 확정하지 않는다.

## code·output·metric·model·prediction·artifact 경계

| 층 | 이번 날짜 근거 |
|---|---|
| source code | Bayesian 완성본과 VGG16 load/preprocess/predict/save 절차 |
| dataset | mail CSV와 입력 image 4개 |
| embedded output | text prediction·class probability text |
| model | VGG16 load call; 별도 weight file은 저장소에 없음 |
| prediction | decoded top class와 score text·graph |
| graph artifact | 날짜 첨부 probability graph 4개 |
| CSV artifact | 저장 code만 있고 물리 파일 없음 |
| 재현 실행 | 수행하지 않아 미확정 |

## 헷갈린 점 / 질문

- **직접 학습 vs pretrained:** 직접 학습은 현재 dataset으로 parameter를 fit하고, pretrained는 다른 대규모 학습에서 얻은 parameter를 불러온다.
- **pretrained inference vs transfer learning:** 그대로 predict하면 feature reuse 기반 inference이고, 새 task에 맞게 layer를 교체·동결·fine-tune해야 transfer learning 학습 단계가 생긴다.
- **probability와 정답:** 높은 score는 model의 class 분포이며 실제 품종·종 정답을 자동 보증하지 않는다.
- **graph 존재와 전체 실행:** 저장 결과 일부가 있어도 CSV·download·전체 loop·재현성은 각각 확인해야 한다.

## 이전·다음 연결

- 이전: [[summaries/2026-07-15-machine-learning-word2vec-bayesian-filter|2026-07-15 Word2Vec과 Bayesian filter 초안]]
- text 분류: [[concepts/text-vectorization-naive-bayes-classification|텍스트 벡터화와 Naive Bayes 분류]]
- image 개념: [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]], [[entities/vgg16|VGG16]]
- framework: [[entities/keras|Keras]]
- 후속: [[summaries/2026-07-20-machine-learning-regression-svm|07-20 회귀·SVM 재방문]]과 [[summaries/2026-07-21-machine-learning-knn-cross-validation|07-21 KNN·K-fold 일반화]]로 이어진다.

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/Pasted image 20260716124822.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/k.national/bayes_test.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/pretrainedModel.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/mail_data.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/cat.jpg`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/fox.jpg`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/mydog.png`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/image/myrabbit.jpg`
