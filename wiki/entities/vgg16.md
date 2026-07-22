---
title: VGG16
created: 2026-07-22
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/Pasted image 20260716124822.png
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png
  - raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/pretrainedModel.py
status: growing
confidence: high
---

# VGG16

## 무엇인가

VGG16은 작은 3×3 convolution을 여러 층 쌓은 대표 CNN architecture다. 이 위키에서는 Keras application의 ImageNet 사전 학습 weight를 불러와 네 image를 1,000개 class 중 하나로 분류하는 model로 2026-07-16에 등장했다.

## 이 위키에서의 맥락

07-13에는 `Conv2D`·Pooling·Flatten·Dense로 CNN topology를 직접 작성했다. 07-16에는 학습을 처음부터 수행하지 않고 VGG16의 기존 parameter와 class vocabulary를 이용해 input preprocessing→prediction→decoding→graph 저장 흐름을 배웠다.

## 날짜별 학습 이력

### 2026-07-16 — 사전 학습 추론

- Keras application에서 VGG16 load
- 224×224 RGB input으로 resize
- batch tensor와 전용 preprocessing 구성
- 1,000-class prediction과 top label decode
- cat·fox·dog·rabbit 입력의 top-10 probability graph 작성
- DataFrame으로 prediction 결과를 누적해 CSV로 저장하도록 code 작성

## 입력·출력 계약

| 항목 | 수업 기준 |
|---|---|
| 입력 | RGB image, 224×224×3로 변환 |
| batch | 단일 image도 1×224×224×3 |
| preprocessing | VGG16 전용 `preprocess_input` |
| 출력 | ImageNet 1,000-class score vector |
| 해석 | `decode_predictions`의 class ID·label·probability |

model 구조가 맞아도 preprocessing convention이 다르면 prediction 해석이 달라질 수 있다.

## 첨부 artifact

실제 probability graph 네 개와 입력 image는 4/4 대응한다. graph별 class·확률 해석과 artifact 증거 한계는 [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]]이 소유하고, 이 Entity는 VGG16의 architecture·입출력 contract·날짜별 사용 이력을 소유한다.

## framework·model 책임 구분

- [[entities/keras|Keras]]: model load·image utility·decode API를 제공하는 framework 계층
- VGG16: 선택한 architecture와 pretrained parameter·입출력 contract
- [[entities/python|Python]]: file loop와 처리 절차를 조립
- [[entities/pandas|Pandas]]: prediction row를 표로 누적
- [[entities/matplotlib|matplotlib]]: top-10 graph 생성

원문은 TensorFlow를 독립 runtime·API 학습 주제로 분리하지 않는다. 따라서 ML-3에서도 TensorFlow Entity를 별도로 만들지 않는다.

## 실행·artifact 경계

VGG16 load·predict 호출은 model 사용 절차를 증명한다. 물리 graph와 code·CSV·재현 실행의 세부 증거 판정은 Concept에 위임하며, weight file과 prediction CSV는 저장소에서 확인되지 않는다.

## 관련 개념

- [[concepts/pretrained-model-vgg16-inference|사전 학습 모델과 VGG16 추론]]
- [[concepts/cnn-convolution-pooling-dropout|CNN과 convolution·pooling·Dropout]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|2026-07-16 Bayesian filter 완성과 사전 학습 모델]]
- [[entities/keras|Keras]]

## 프로젝트/면접에서 설명할 관점

“VGG16은 3×3 convolution을 깊게 쌓은 CNN이며, 수업에서는 ImageNet pretrained model의 입력 contract에 image를 맞춘 뒤 top class를 추론했다. graph artifact와 전체 실행·CSV·재현성은 별도 증거로 관리했다”고 설명할 수 있다.

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/Pasted image 20260716124822.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/pretrainedModel.py`
