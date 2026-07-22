---
title: 2026-06-30 Python Pandas Series와 DataFrame 입문
created: 2026-07-03
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md
  - raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203348.png
  - raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203436.png
status: growing
confidence: high
---

# 2026-06-30 Python Pandas Series와 DataFrame 입문

## 한 줄 요약

Jupyter에서 1차원 Series의 label·position·value를 읽고 계산·필터링·시각화한 뒤, 마지막에 2차원 DataFrame의 행·열 구조로 진입했다.

## 배운 내용

1. Jupyter의 code/Markdown 셀, `Ctrl + Enter`·`Shift + Enter`, notebook 저장 흐름을 확인했다.
2. range·list·dict로 Series를 만들고 `index`, `name`, `values`, `dtype`, `to_frame`을 읽었다.
3. label 조회, list 형태 다중 조회, label slicing, `loc`·`iloc`, position slicing을 구분했다.
4. 대입과 boolean indexing으로 일부 값을 선택·수정했다.
5. scalar 연산과 Series 간 index 정렬 연산, `NaN`, `fill_value`를 배웠다.
6. `unique`, `value_counts(normalize=True)`, `isin`으로 유일값·빈도·조건 포함 여부를 계산했다.
7. 국가별 Series를 선그래프와 막대그래프로 표현하고 실제 PNG 결과 두 개를 노트에 연결했다.
8. 오후 시험·Series 정리 뒤 DataFrame의 `index`·`columns`·`values`·전치와 NumPy `reshape`를 소개했다.

학습의 중심은 단순 list의 position 접근에서, 데이터에 붙은 label을 기준으로 정렬·연산하는 Pandas 사고로 이동하는 것이다. Oracle의 행·열 표 감각을 Python 메모리 객체에 옮겼지만 DB table과 동일한 것은 아니다. ^[raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md]

## 대표 실습

### Series 생성과 label 부여

- **입력**: 국가 list와 신용도 숫자 list 또는 key-value dict
- **처리**: `pd.Series(data=..., index=...)`로 value와 label을 대응시키고 index/Series 이름을 지정한다.
- **결과**: label별 값을 가진 1차원 표와 `dtype`이 노트에 출력 형태로 기록되어 있다.

### 조회·수정·필터링

- 단일 label은 scalar, label list는 Series를 반환한다.
- label slicing은 끝 label을 포함하지만 position slicing은 끝 위치를 포함하지 않는다.
- 비교식은 value마다 True/False인 boolean Series를 만들고, 이를 다시 indexing해 참인 행만 선택한다.
- boolean mask는 대상 Series와 index가 대응해야 한다.

### index 정렬 연산

두 Series를 더할 때 같은 index끼리 계산하고 한쪽에만 있는 index는 `NaN`이 된다. 산술 method의 `fill_value`는 한쪽 결측을 임시 값으로 보완하지만 양쪽 모두 결측이면 결과도 결측으로 남는다.

### 그래프 artifact

- 선그래프 PNG: 7개 국가 label과 값, x축 국가명·y축 신용도는 plotting 문맥과 대응한다. 그러나 code 제목, 노트의 text 반환값, PNG 픽셀 제목의 띄어쓰기·철자가 서로 달라 현재 보이는 code cell의 정확한 실행 결과라고 단정할 수 없다.
- 막대그래프 PNG: 같은 7개 범주·값을 색이 반복되는 막대로 표시하며 제목·축 label도 인접 code·text 결과와 대체로 대응한다. 그래도 실행 시점과 notebook 상태는 확인되지 않는다.

두 파일은 그래프 결과가 물리적으로 저장되어 있고 실제 픽셀을 확인했다는 강한 artifact 근거다. 그러나 이 사실만으로 전체 notebook의 모든 셀, 모든 Pandas 실습, 현재 code의 재현 실행이 성공했다고 확대하지 않는다.

## 실행·결과 근거

- Series 표와 연산 결과는 노트에 embedded output으로 다수 보존되어 있다.
- 그래프 PNG 2개는 직접 확인한 physical artifact다. 막대그래프는 인접 code와 대응도가 높지만 선그래프 제목은 code·text·PNG 사이에 불일치가 있어 동일 cell의 정확한 산출물 여부는 미확정이다.
- notebook 파일 자체는 raw 재고에 없으므로 cell 실행 순서·전체 재실행 성공은 검증할 수 없다.
- 오후 “Python 시험”은 시간표 표기만 있고 문제·점수·결과가 없으므로 시험 성취를 추정하지 않는다.

## 헷갈린 점 / 질문

- Series의 index(label)와 내부 position은 독립 개념이다. 정수 label일 때는 `loc`와 `iloc`로 명시한다.
- label slice는 끝 포함, `iloc`/position slice는 끝 미포함이다.
- 단일 label 선택은 scalar를 반환하고, label을 list 형태로 감싼 선택은 Series를 반환한다.
- `NaN`이 들어오면 정수 Series의 연산 결과가 `float64`로 보일 수 있다.
- `to_frame()`은 새 DataFrame을 반환하며 원본 Series 자체를 바꾸지 않는다.
- 막대그래프 code의 y축 상한은 다른 Series 변수의 `max()`를 참조한다. 현재 그림은 만들어졌지만 독립 재실행에서는 의도한 Series를 참조하는지 확인해야 한다.

## 이전·다음 수업 연결

- **이전**: [[summaries/2026-06-29-python-regex-xml-json-jupyter|06-29]]에서 Pandas 설치와 Jupyter 실행 환경을 준비했다.
- **당일 후반**: Series 하나에서 DataFrame의 행·열·2차원 array로 이동했다.
- **다음**: 2026-07-01 이후 DataFrame 조회·입출력 심화는 사용자 수정 및 후속 Agent 범위이므로 이번 페이지에서 재해석하지 않는다.

## 관련 페이지

- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[entities/matplotlib|matplotlib]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.30(화)/2026.06.30(화).md`
- `raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203348.png`
- `raw/KoreaICT/10. Python/2026.06.30(화)/첨부파일/Pasted image 20260715203436.png`
