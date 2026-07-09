---
title: 2026-07-01 Python Pandas DataFrame 조회와 입출력
created: 2026-07-01
updated: 2026-07-02
type: summary
tags: [python, study-log]
sources:
  - raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md
status: growing
confidence: high
---

# 2026-07-01 Python Pandas DataFrame 조회와 입출력

## 한 줄 요약

Python 과정에서 [[entities/pandas|Pandas]]의 `DataFrame`/`Series`를 만들고, `loc`/`iloc` 조회·수정, 산술 연산, `reindex`, `drop`, CSV 입출력, 기초 통계와 시각화까지 실습한 날이다.

## 커리큘럼 위치

- 이전 흐름: Java, Oracle, FrontEnd/BackEnd 프로젝트 뒤에 Python 데이터 처리 과정으로 넘어왔다.
- 이날 위치: Pandas를 “표 데이터를 다루는 도구”로 본격 사용하기 시작했다.
- 다음 흐름: 2026-07-02에는 여러 DataFrame을 결합하는 `concat`, `merge`, `pivot` 같은 데이터 재구성으로 이어진다.

## 배운 내용

### 1. DataFrame 생성과 행/열 조회

수업은 `myindex02`, `mycolumns02`, `mylist02`를 준비한 뒤 `np.reshape`로 5×5 형태를 만들고 `pd.DataFrame(...)`으로 표를 구성하는 방식에서 출발했다. 행 이름은 사람 이름, 열 이름은 지역명으로 두어 “영업 사원별 구별 실적”처럼 읽을 수 있는 표를 만들었다. ^[raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md]

핵심 조회 방식은 두 갈래다.

- `iloc`: 숫자 위치 기반 조회
  - 예: `myframe02.iloc[1]`, <code>myframe02.iloc&#91;&#91;1, 3&#93;&#93;</code>, `myframe02.iloc[0::2]`
- `loc`: 라벨 이름 기반 조회
  - 예: `myframe02.loc["연규희"]`, <code>myframe02.loc&#91;&#91;"최유식", "심형식"&#93;&#93;</code>, `myframe02.loc["유관철":"연규희"]`

초보자가 특히 헷갈릴 지점은 “열은 `myframe02["용산구"]`처럼 바로 꺼낼 수 있지만, 행은 보통 `loc`/`iloc`로 꺼낸다”는 차이다.

### 2. 조건 수정과 슬라이싱

조회만 한 것이 아니라 값을 직접 바꾸는 문제를 풀었다.

- 특정 사람들의 특정 열 값 변경: <code>myframe02.loc&#91;&#91;...&#93;, &#91;"용산구"&#93;&#93; = 30</code>
- 이름 범위와 열을 함께 지정: `myframe02.loc["최유식":"심형식", ["노원구"]] = 80`
- 한 사람의 전체 실적 변경: `myframe02.loc["연규희"] = 50`
- 모든 행의 특정 열 변경: `myframe02.loc[:, "은평구"] = 60`
- 조건을 만족하는 행의 일부 열 변경: `myframe02.loc[myframe02["용산구"] <= 50, ["노원구", "은평구"]] = 0`

여기서 `:`는 “모든 행/열”을 뜻하고, boolean 조건식은 “조건을 만족하는 행만 골라내는 마스크(mask)” 역할을 한다.

### 3. DataFrame과 Series 산술

`myframe31.add(myseries31, axis=0)`처럼 `axis`를 지정해 Series의 index를 DataFrame의 어느 축과 맞출지 실습했다.

- `axis=0`: Series의 index를 DataFrame의 행 index와 맞춘다.
- `axis=1`: Series의 index를 DataFrame의 column 이름과 맞춘다.

DataFrame끼리 더할 때는 `myframe31.add(myframe32, fill_value=0)`를 사용했다. 한쪽에만 있는 값은 `fill_value=0`으로 보완할 수 있지만, 서로 모두 없는 위치는 `NaN`으로 남는다.

### 4. reindex와 drop

`reindex`는 행 또는 열의 틀을 새 index/columns 기준으로 다시 맞추는 함수다.

- 행 추가/재배열: `myframe04.reindex(index=newindex04, fill_value=50)`
- 열 추가/재배열: `myframe04.reindex(columns=newcolumn04, fill_value=40)`

새로 추가된 행/열에는 원래 데이터가 없으므로 기본적으로 `NaN`이 생긴다. `fill_value`를 주면 빈 값을 지정한 값으로 채울 수 있다.

`drop`은 행 또는 열을 제거할 때 사용했다.

- 행 삭제: `drop(["김영민"], axis=0)` 또는 `axis="index"`
- 열 삭제: `drop(["출장기간"], axis="columns")`

### 5. CSV 입출력과 Faker 더미 데이터

후반부에는 `Faker('ko_KR')`로 한국어 더미 데이터를 만들고, `to_csv()`로 저장한 뒤 `read_csv()`로 다시 읽었다.

- 저장: `myframe01.to_csv(filename, encoding=myencoding, mode='w', index=True)`
- 읽기: `pd.read_csv(filename, index_col=0, encoding=myencoding)`

원본 노트에서는 Excel 호환을 고려해 `CP949` 인코딩을 명시했다. Windows/한국어 CSV 실습에서는 UTF-8뿐 아니라 CP949도 자주 등장한다는 점이 중요하다.

### 6. Series 속성, 통계, 누락값

`payment01.csv`를 읽은 뒤 열 하나를 꺼내면 `Series`가 된다는 점을 확인했다.

- 대괄호 추출: `payment['교통비']`
- 점 표기 추출: `payment.교통비`
- 크기/형태/개수: `size`, `shape`, `len()`, `count()`
- 데이터 타입과 결측: `dtype`, `hasnans`, `isnull()`, `notnull()`
- 기초 통계: `quantile()`, `min()`, `max()`, `mean()`, `median()`, `std()`, `sum()`, `describe()`
- 빈도수: `value_counts()`, `value_counts(normalize=True)`

`business > business.mean()`처럼 Series에 비교 연산을 적용하면 boolean Series가 만들어지고, 이를 다시 필터로 사용할 수 있다.

### 7. set_index, rename, 파생 컬럼, Pie 차트

마지막 흐름에서는 `set_index('사원명')`으로 기존 열을 행 색인으로 옮기고, `rename(index=..., columns=...)`으로 행/열 이름을 변경했다. 또한 scalar 값을 넣어 전체 열을 만들거나, 기존 열을 계산해 파생 컬럼을 만들었다.

- 전체 열 생성: `payment['차량 지원'] = '지원'`
- 파생 컬럼 생성: `payment['최종 식비'] = payment['식비'] + 100`
- Pie 차트: `chartdata01.plot(kind='pie', ...)`

## 핵심 개념

- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]: 행/열 표 데이터를 만들고 조회·수정·계산하는 핵심 자료구조
- [[entities/pandas|Pandas]]: CSV, Series, DataFrame, 통계, 시각화 흐름을 담당한 Python 라이브러리
- [[entities/jupyter-notebook|Jupyter Notebook]]: 코드를 셀 단위로 실행하며 표와 그래프 결과를 바로 확인한 학습 환경

## 헷갈린 점 / 질문

- `loc`와 `iloc`는 둘 다 행/열을 고르지만, `loc`는 라벨 이름 기준이고 `iloc`는 숫자 위치 기준이다.
- `myframe["열이름"]`은 열 선택이지만, 행을 선택할 때는 보통 `loc`/`iloc`를 쓴다.
- `axis=0`과 `axis=1`은 함수마다 “방향”을 떠올리기 어렵다. Pandas에서는 보통 `axis=0`이 행 index 방향, `axis=1`이 columns 방향이라는 기준으로 외워야 한다.
- `NaN`은 단순히 글자가 아니라 “값이 없음/결측”을 나타내며, 계산·통계에서 별도 처리가 필요하다.
- `to_csv`/`read_csv`에서 인코딩을 맞추지 않으면 한글이 깨질 수 있다.

## 관련 페이지

- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[summaries/2026-07-02-python-pandas-reshape-merge|2026-07-02 Python Pandas 데이터 결합과 재구조화]]

## 출처

- `raw/KoreaICT/10. Python/2026.07.01(수)/2026.07.01(수).md`
