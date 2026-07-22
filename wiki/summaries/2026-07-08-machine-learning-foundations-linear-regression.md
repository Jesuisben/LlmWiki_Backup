---
title: 2026-07-08 Machine Learning 기초와 선형회귀
created: 2026-07-22
updated: 2026-07-22
type: summary
tags: [python, curriculum, study-log]
sources:
  - raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/auto-mpg.csv
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf
  - raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(실습).pdf
status: growing
confidence: high
---

# 2026-07-08 Machine Learning 기초와 선형회귀

## 한 줄 요약

Python 과목을 마친 뒤 AI·Machine Learning·Deep Learning의 범위를 구분하고, `auto-mpg` 데이터를 전처리해 단순·다중 선형회귀의 feature/label 분리부터 학습·예측·평가까지 첫 모델 흐름을 작성했다.

## 전체 교시·학습 순서

| 교시 | 학습 흐름 | 역할 |
|---|---|---|
| 1~2교시 | Python 공부 | 같은 날짜의 Python 마무리 구간이며 ML 본문과 합치지 않는다. |
| 3교시 | AI·ML·DL 관계 → 지도·비지도·강화 학습 → 회귀·분류·군집 | 어떤 문제를 어떤 학습 방식으로 푸는지 큰 지도를 세웠다. |
| 4교시 | Python으로 ML 공부하기, `a.basic` 자습 안내 | 이론을 Python source 실습으로 옮길 준비를 했다. |
| 5~6교시 | `auto-mpg` 탐색·전처리 → 단순 선형회귀 → 다중 선형회귀 | 데이터에서 모델과 평가 지표까지 한 번 연결했다. |
| 7~8교시 | 자습 | 추가 실행 결과나 별도 artifact는 기록되지 않았다. |

## 왜 이 흐름으로 배웠는가

먼저 [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]으로 회귀·분류·군집의 출력 차이를 구분해야 `mpg`처럼 연속 숫자를 예측하는 문제가 왜 회귀인지 판단할 수 있다. 그다음 이전 [[entities/pandas|Pandas]] 학습에서 익힌 표 조회·결측 처리·시각화를 입력 준비에 사용하고, [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]의 split→fit→predict→evaluate를 처음 적용했다. 이 구조는 다음 날 SVM·KNN·Decision Tree 분류에서도 모델만 바뀐 채 반복된다.

## 핵심 개념

- AI는 인간 지능을 모방하는 가장 넓은 범위이고, ML은 데이터에서 패턴을 학습하는 AI의 하위 범위이며, DL은 다층 신경망을 사용하는 ML의 하위 범위다.
- 지도 학습은 feature와 정답 label을 함께 사용한다. 회귀는 연속 숫자, 분류는 범주를 예측한다.
- 비지도 학습은 정답 label 없이 구조를 찾으며, 이날 대표 문제로 군집을 구분했다.
- 강화 학습은 환경과 상호작용하며 reward를 최대화하는 행동 정책을 학습한다.
- 단순 선형회귀는 feature 하나, 다중 선형회귀는 여러 feature로 하나의 연속 label을 예측한다.

## 대표 입력 → 처리 → 결과

### `auto-mpg` 단순 선형회귀

1. **입력:** header가 없는 398행·9열 `auto-mpg.csv`를 읽고 열 이름을 지정했다.
2. **탐색:** 자료형·요약 통계·결측 후보·상관계수와 그래프 코드를 통해 데이터 구조를 살폈다.
3. **전처리:** `horsepower`의 `?`를 결측값으로 바꾸고 실수형으로 변환한 뒤 평균으로 채웠다.
4. **선택:** `weight`를 feature, `mpg`를 label로 정하고 7:3 train/test로 분리했다.
5. **학습·예측:** `LinearRegression.fit()`으로 계수와 절편을 학습하고 test feature에 `predict()`를 호출했다.
6. **평가:** test set의 $R^2$와 실제값-예측값의 MSE를 계산하도록 작성했다.

### 다중 선형회귀

같은 데이터에서 `cylinders`, `horsepower`, `weight`를 feature로 묶고 `mpg`를 label로 유지했다. 다시 7:3 분할한 뒤 다중 회귀 모델의 계수·절편·$R^2$·예측값과 변수별 그래프를 만들도록 확장했다. 단일 원인으로 설명하던 단계에서 여러 feature의 동시 관계를 보는 단계로 이동한 것이다.

## code·output·metric·model·artifact 증거 경계

| 증거 | 확인된 범위 | 확인되지 않은 범위 |
|---|---|---|
| 날짜 MD와 독립 `.py` | 데이터 읽기·전처리·split·fit·predict·score·MSE·save 호출이 작성됨 | 현재 환경에서 처음부터 끝까지 재실행 성공했는지 |
| `auto-mpg.csv` | 398행·9열 물리 입력이 존재하고 행 폭이 일정함 | 이날 수업에서 모든 행이 정상 처리되었는지 |
| triple-quoted 설명 | 예시 계수·절편·$R^2$ 해석이 source에 기록됨 | 실행 직후 stdout으로 생성된 결과인지 |
| `LinearRegression` 객체 | 학습을 시도하는 code가 존재함 | 직렬화된 물리 model artifact가 존재하는지 |
| `to_csv`·`savefig` | CSV·그래프 저장 의도가 작성됨 | `dataOut`에는 해당 결과 파일이 없어 실제 저장 성공은 미확정 |

`fit()` 호출은 학습 code이고, 모델 파일 저장과는 다르다. 이날 source에는 별도의 model 직렬화 호출도 없다.

## 실제 오류·불일치·미확정 실행

- 날짜 MD의 test 개수 출력은 `len(x_test)`로 맞지만 독립 교육 source는 test 개수에도 `len(x_train)`을 사용한다. 원본 source의 출력 label/값 불일치이며 raw는 수정하지 않았다.
- 날짜 설명의 “실제 작업에서는 random seed를 빼야 한다”는 절대 규칙이 아니다. 실험 재현과 모델 비교에는 고정 seed가 유용하고, 분할 변화에 대한 안정성은 여러 seed나 cross-validation로 별도 확인한다.
- 날짜와 source에 계수·절편·약 68.9% 설명력 문장이 있지만 실행 stdout이나 결과 artifact가 아니다. 현재 code와 같은 데이터·버전에서 다시 얻었다고 단정하지 않는다.
- 저장 메시지를 `print`하는 것은 파일 생성 성공 검증이 아니다. 실제 경로의 파일 존재·크기·내용 확인이 별도로 필요하다.

## 헷갈린 점과 정확한 구분 기준

- **feature와 label:** 모델에 넣는 설명 변수는 feature, 맞히려는 정답은 label이다. `weight → mpg`에서 `weight`가 feature다.
- **상관관계와 회귀:** 음의 상관은 두 변수가 반대 방향으로 움직인다는 관찰이고, 회귀 모델의 test 성능이나 인과관계를 자동으로 보장하지 않는다.
- **$R^2$와 MSE:** $R^2$는 평균 예측 기준과 비교한 설명력이고 높을수록 좋다. MSE는 오차 제곱 평균이므로 낮을수록 좋으며 label 단위의 제곱에 영향을 받는다.
- **학습 모델과 저장 artifact:** 메모리의 학습 객체, metric 출력, CSV·PNG, 직렬화 model file은 서로 다른 결과물이다.

## 이전·다음 학습 연결

- 이전: [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 Python 한국어 텍스트 마이닝]]까지 축적한 Python·Pandas 데이터 처리 능력이 전처리와 결과표 작성에 사용됐다. 같은 날짜라도 Python Summary와 ML Summary의 과목 책임은 분리한다.
- 다음: 2026-07-09에는 연속값 회귀에서 범주 분류로 이동해 confusion matrix, SVM, ROC/AUC, KNN, Decision Tree를 배운다.

## 관련 페이지

- [[concepts/machine-learning-problem-types|Machine Learning 문제 유형]]
- [[concepts/machine-learning-model-lifecycle|Machine Learning 모델 생명주기]]
- [[concepts/linear-regression-evaluation|선형회귀와 R²·MSE]]
- [[entities/scikit-learn|scikit-learn]]
- [[entities/pandas|Pandas]]

## 출처

- `raw/KoreaICT/11. Machine Learning/2026.07.08(수) - 시작/2026.07.08(수) - 시작.md`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/b.linear/simple_linear_regression.py`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신러닝/dataIn/auto-mpg.csv`
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(이론).pdf` — ML 기초·split·회귀·MSE·$R^2$ 보조
- `raw/KoreaICT/11. Machine Learning/교육 자료/머신 러닝 교안(실습).pdf` — 선형회귀 실습 source 위치 보조
