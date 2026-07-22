---
title: 사전 학습 모델과 VGG16 추론
created: 2026-07-22
updated: 2026-07-22
type: concept
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

# 사전 학습 모델과 VGG16 추론

## 정의

사전 학습 모델(pretrained model)은 대규모 dataset에서 이미 parameter를 학습한 model이다. 2026-07-16 수업에서는 ImageNet class를 학습한 VGG16을 불러와 새 image를 전처리하고 class probability를 예측했다.

## 왜 중요한가

모든 image task를 처음부터 대규모로 학습하려면 많은 data·연산·시간이 필요하다. 사전 학습 parameter를 사용하면 이미 배운 edge·texture·shape 표현을 추론이나 새 task의 출발점으로 재사용할 수 있다. 다만 다른 class 체계와 domain에 그대로 맞는지는 별도 평가가 필요하다.

## pretrained inference와 transfer learning

| 단계 | parameter 변경 | 수업 범위 |
|---|---|---|
| pretrained inference | 없음 | VGG16을 불러와 ImageNet 1,000 class prediction |
| feature extraction | backbone은 동결, 새 head 학습 | 개념 연결 가능, 직접 학습 결과 없음 |
| fine-tuning | 일부 pretrained layer도 추가 학습 | 후속 확장, 직접 수행 근거 없음 |
| from-scratch training | 모든 parameter를 현재 data로 학습 | 07-13 CNN topology의 별도 흐름 |

따라서 이날 code는 “사전 학습 model을 활용한 추론”이 직접 책임이다. transfer learning은 상위 개념이지만 새 classifier 학습·fine-tuning 성공까지 확대하지 않는다.

## VGG16 image 처리 구조

1. image를 RGB로 읽는다.
2. VGG16 입력 크기인 224×224로 resize한다.
3. pixel을 array로 바꾸고 batch 차원을 추가한다.
4. `preprocess_input`으로 model 학습 조건에 맞춘다.
5. `predict`로 1×1000 score를 얻는다.
6. `decode_predictions`로 class label과 probability를 읽는다.
7. top class를 console text·DataFrame·top-10 graph로 표현한다.

입력 원본의 실제 크기는 cat 1024×768, fox 420×277, mydog 349×333, myrabbit 420×287이다. resize는 shape를 맞추지만 원본 종횡비 변화가 prediction에 영향을 줄 수 있다.

## 수업 graph 네 개의 해석

- 주황색 고양이: tiger cat·Egyptian cat·tabby가 상위
- 눈밭의 여우: red fox가 약 95%
- 흰 어린 강아지: Labrador retriever·kuvasz가 상위
- 흰 토끼: hare가 약 98%

이는 model의 ImageNet class vocabulary 안에서 계산된 결과다. 실제 animal의 정확한 품종·종 label, calibration, 일반화 성능을 보증하지 않는다. 특히 rabbit image를 hare로 분류한 것은 시각적 관련성은 있지만 두 명칭이 동일 정답이라는 뜻은 아니다.

## graph·prediction·artifact 증거

첨부 graph 네 개는 실제 픽셀로 확인되며 입력 filename·top-10 label·확률 축이 원문 맥락과 4/4 대응한다. graph artifact는 prediction 결과를 시각화한 파일이 남았음을 강하게 뒷받침한다.

그러나 다음은 미확정이다.

- VGG16 weight의 실제 download 시점과 cache
- source 전체의 오류 없는 end-to-end 실행
- graph를 만든 정확한 source version
- `prediction_result.csv` 저장 성공
- 모든 console output과 현재 환경 재현

probability graph의 `savefig` 이름은 첨부 filename 4개와 일치한다. 별도의 `pretrained_model_<입력명>` 호출은 resize된 입력 image 재저장용이며 해당 artifact는 확인되지 않았다. graph가 존재해도 전체 loop·CSV·현재 재현 성공은 별도 검증 대상이다.

## 자주 헷갈리는 점

- **model load와 model training:** weight를 불러오는 것은 현재 data로 parameter를 학습하는 `fit`이 아니다.
- **prediction score와 정확도:** 한 image의 class probability와 dataset 전체 accuracy는 다르다.
- **top-1과 top-10:** top-1은 가장 큰 하나, top-10 graph는 후보 분포를 보여 준다.
- **preprocessing:** image 파일을 읽었다고 바로 model 입력이 되는 것이 아니라 shape·batch·pixel convention을 맞춰야 한다.
- **graph 저장과 CSV 저장:** 하나의 artifact가 존재해도 다른 저장 호출의 성공을 대신하지 않는다.

## 선행·후속 연결

- CNN 선행: [[concepts/cnn-convolution-pooling-dropout|CNN과 convolution·pooling·Dropout]]
- framework: [[entities/keras|Keras]]
- model: [[entities/vgg16|VGG16]]
- lifecycle: [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- 수업: [[summaries/2026-07-16-machine-learning-bayesian-filter-pretrained-model|2026-07-16 Bayesian filter 완성과 사전 학습 모델]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/2026.07.16(목).md`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/Pasted image 20260716124822.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_cat.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_fox.jpg`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_mydog.png`
- `raw/KoreaICT/11. Machine Learning/2026.07.16(목)/첨부파일/probability_myrabbit.jpg`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/j.cnn/pretrainedModel.py`
