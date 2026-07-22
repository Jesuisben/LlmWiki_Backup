---
title: 군집과 거리·hierarchical clustering·KMeans
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_example.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/mdsAndDendrogram.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_clustering.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/Wholesale customers data.csv
status: growing
confidence: high
---

# 군집과 거리·hierarchical clustering·KMeans

## 정의

군집(clustering)은 정답 label 없이 feature의 유사성·거리 구조를 이용해 비슷한 관측치를 group으로 묶는 비지도 학습이다. 2026-07-13 수업은 Euclidean distance·cosine similarity를 기준으로 hierarchical clustering, MDS, KMeans를 차례로 연결했다.

## 왜 중요한가

분류는 미리 정한 class를 예측하지만, 고객 segment처럼 정답이 없는 데이터에서는 구조부터 찾아야 한다. 다만 algorithm이 만든 cluster는 자연적으로 존재하는 절대 정답이 아니라, 선택한 feature·scale·distance·K·linkage에 따라 달라지는 분석 결과다.

## distance와 similarity

| 기준 | 묻는 질문 | 값 해석 | 주의점 |
|---|---|---|---|
| Euclidean distance | 좌표상 얼마나 가까운가? | 작을수록 가까움 | feature scale과 이상치에 민감 |
| cosine similarity | vector 방향이 얼마나 같은가? | 1에 가까울수록 같은 방향 | 크기 차이를 의도적으로 약화함 |

구매 금액처럼 단위·분산이 크게 다른 feature를 그대로 Euclidean distance에 쓰면 큰 scale의 열이 군집을 지배할 수 있다. 도매 고객 실습이 StandardScaler를 먼저 적용한 이유다.

## hierarchical clustering

처음에는 각 관측치를 하나의 cluster로 두고, linkage 기준에 따라 가장 가까운 cluster를 반복해서 합친다. dendrogram은 어느 거리에서 어떤 cluster가 합쳐졌는지 tree로 보여 준다.

| linkage | 두 cluster 사이 거리 정의 | 성향 |
|---|---|---|
| single | 가장 가까운 두 점의 거리 | 길게 이어지는 chaining 가능 |
| complete | 가장 먼 두 점의 거리 | 비교적 조밀한 cluster 선호 |
| average | 모든 점 쌍 거리의 평균 | single·complete의 중간 성향 |
| Ward | 합친 뒤 cluster 내 제곱오차 증가 | 분산이 작은 cluster 선호 |

수업 source는 음식 5개의 feature로 `pdist` condensed distance vector를 만든 뒤 single linkage와 dendrogram을 사용한다.

## MDS의 책임

MDS(Multidimensional Scaling)는 고차원 관측치 사이 distance를 2D·3D에서 최대한 보존하도록 좌표를 찾는 embedding 기법이다. 관계를 시각화하는 도구이지 자체로 정답 cluster를 생성하는 classifier가 아니다.

음식 실습은 같은 distance matrix를 MDS에 넣어 2차원 위치를 만들고 label을 붙인다. 원문의 거리 표는 “Euclidean”이라고 되어 있지만 값은 source가 별도로 계산한 **squared distance**와 대응한다. MDS code 자체는 제곱 전 distance를 사용한다.

## KMeans

1. K개 중심을 초기화한다.
2. 각 관측치를 가장 가까운 중심에 할당한다.
3. cluster별 평균으로 중심을 갱신한다.
4. 할당·중심이 수렴할 때까지 반복한다.

KMeans는 각 cluster 안의 제곱 거리 합을 줄이는 방향으로 동작한다. 구형에 가까운 cluster와 Euclidean geometry에 잘 맞지만, 임의 모양·밀도 차이·이상치에는 취약할 수 있다.

## 수업 사례

### 2차원 점 10개

초기 중심 두 개를 직접 지정하고 `n_init=1`로 fit해 중심 이동과 cluster 할당을 graph로 그리도록 작성했다. source에는 출력·save 호출이 있지만 물리 PNG는 없다.

### 도매 고객 440개

- 원본: 440행·8열, 결측 0
- 제외: 판매 channel·region
- feature: Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen
- 전처리: StandardScaler
- model: KMeans, K=5, k-means++, `n_init=10`
- 해석: cluster별 평균·행 수·구매액 산점도

`Cluster` 열은 source label이 아니라 `kmeans.labels_`를 붙인 결과다. ID 0과 1을 바꿔도 같은 partition일 수 있으므로 번호 자체에 고정 의미를 부여하지 않는다.

## hierarchical clustering vs KMeans

이 비교는 별도 Comparison 대신 이 Concept에 흡수한다.

| 항목 | hierarchical | KMeans |
|---|---|---|
| K 사전 지정 | dendrogram을 자르는 단계에서 선택 가능 | fit 전에 K 지정 |
| 결과 형태 | 병합 tree와 partition | 중심과 flat partition |
| 반복 계산 | pair/cluster 거리 갱신 | 할당↔중심 갱신 |
| 큰 데이터 | 거리 계산 비용이 커질 수 있음 | 상대적으로 확장하기 쉬움 |
| 해석 | 병합 순서 확인 | cluster center·평균 확인 |

## 자주 헷갈리는 점

- **cluster label vs 정답 label:** cluster ID는 algorithm이 만든 group 식별자이며 실제 class 이름이 아니다.
- **거리와 거리 제곱:** Euclidean distance와 squared Euclidean distance는 값이 다르다. 원문의 음식 표는 후자와 대응한다.
- **scaling과 cluster:** scaling은 단위를 맞추지만 이상치를 제거하지 않는다.
- **MDS와 PCA:** 둘 다 저차원 표현을 만들 수 있지만 MDS는 거리 보존을 중심으로 설계된다.
- **좋은 그림과 좋은 군집:** 2D plot이 분리돼 보이는 것만으로 전체 고차원 cluster 품질이 증명되지 않는다.
- **fit과 artifact:** `fit`, `labels_`, `savefig` code가 있어도 실제 center 출력·PNG 저장 성공은 별도 증거가 필요하다.

## 선행·후속 연결

- 문제 유형: [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- lifecycle 확장: label이 없는 경우를 [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]와 대비
- 수업: [[summaries/2026-07-13-machine-learning-clustering-cnn|2026-07-13 군집과 CNN]]
- 도구: [[entities/scikit-learn|scikit-learn]], [[entities/pandas|Pandas]], [[entities/matplotlib|matplotlib]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.13(월)/2026.07.13(월).md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_example.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/mdsAndDendrogram.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/i.clustering/kmeans_clustering.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/Wholesale customers data.csv`
