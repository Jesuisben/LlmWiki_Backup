---
title: Python 컬렉션과 컴프리헨션
created: 2026-07-03
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md
  - raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md
status: growing
confidence: high
---

# Python 컬렉션과 컴프리헨션

## 정의

Python collection은 여러 값을 하나의 구조로 관리하고, comprehension은 iterable을 순회·변환·필터링해 새 collection을 만드는 표현식이다.

## 왜 중요한가

외부 데이터는 한 값이 아니라 행·열·항목 묶음으로 들어온다. 06-22~23 수업은 list/tuple/dict/set을 사용해 “데이터 모양”을 이해하고, 이후 JSON dict와 Pandas Series/DataFrame으로 이동할 준비를 한다.

## 자료구조 선택

| 타입 | 순서 | 변경 | 중복 | 수업 역할 |
|---|---|---|---|---|
| list | 있음 | 가능 | 가능 | 메뉴·점수·행 목록, 추가·수정·삭제 |
| tuple | 있음 | 불가 | 가능 | 고정된 묶음, `zip` 결과, 함수의 다중 반환 |
| dict | 삽입 순서 유지 | 가능 | key 불가/value 가능 | 품명→가격, 할인율, JSON object |
| set | 위치 기반 순서 없음 | 가능 | 불가 | 중복 제거·집합 검사 |

## 이 수업의 실제 흐름

### list와 tuple

06-22에는 list를 결합하고 `append`·`insert`·index 대입·`remove`·`count`로 바꿨다. 같은 날 tuple은 한 요소 쉼표, indexing/slicing, count/index, list 변환 후 정렬로 다뤘다. immutable은 “읽을 수 없다”가 아니라 “그 tuple의 요소를 직접 대입해 바꿀 수 없다”는 뜻이다. ^[raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md]

### dict와 중첩 list

06-23에는 `dict[key] = value`로 insert/overwrite하고 `in`, `keys`, `values`, `items`, `get`을 사용했다. 중첩 list에서는 바깥 index가 행, 안쪽 index가 열처럼 동작해 학생별 값을 추출·계산했다. 이 구조는 DataFrame 이전의 수동 표 처리다. ^[raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md]

### comprehension

comprehension은 보통 다음 순서로 읽는다.

1. `for` 오른쪽에서 입력 iterable을 확인한다.
2. `if`가 있으면 남길 조건을 확인한다.
3. 맨 앞 표현식이 결과에 어떤 값을 넣는지 확인한다.

수업에서는 평균 이상 점수, 성인 나이, 양수, 짝수, 일정 길이 이상의 이름을 선별했다. 짧게 쓰는 것이 목적이 아니라 “입력 → 조건 → 결과”를 한 표현식으로 나타내는 것이 핵심이다.

Python 문법에는 dict/set comprehension도 있지만, 06-23의 직접 실증 예제는 list comprehension이 중심이다. 이 페이지의 “새 collection” 정의를 모든 comprehension 유형을 당일 실습했다는 의미로 확대하지 않는다.

### 결합·집계·정렬

- `zip`: 같은 위치의 값들을 tuple로 묶고 가장 짧은 iterable에서 멈춘다.
- `sum`·`min`·`max`: 숫자 collection 집계
- `all`·`any`: 조건 결과 전체/일부 판정
- `sorted`: 정렬된 새 list 반환
- list `.sort()`: 원본 list를 제자리에서 변경
- `Counter`: 항목별 빈도를 key-value로 계산

## 대표 데이터 흐름

이름 list와 점수 list를 `zip` → tuple list → `dict`로 바꾸고, `sorted(..., key=dict.get, reverse=True)`로 점수 기준 이름 순서를 만들었다. 이는 여러 열을 같은 행으로 묶고 특정 열 기준으로 정렬하는 표 처리의 축소판이다.

## 자주 헷갈리는 점

- dict의 `get(key, default)`는 default를 반환할 뿐 새 key를 저장하지 않는다.
- loop에서 `for key, value in dict.items()`의 `value` 변수만 바꿔도 dict 원본은 바뀌지 않는다.
- set으로 중복을 제거한 뒤 순서가 필요하면 명시적으로 정렬한다.
- tuple 한 요소는 `(value,)`처럼 쉼표가 필요하다.
- comprehension이 복잡해지면 일반 loop가 더 읽기 쉽다.
- 중첩 list의 위치 숫자는 의미가 드러나지 않으므로 데이터가 커지면 dict·class·DataFrame 같은 이름 기반 구조가 필요하다.

## 선행·후속 연결

- **선행**: [[concepts/python-basic-syntax|Python 기본 문법]]의 반복·조건·slicing
- **다음**: [[concepts/python-functions-modules-packages|Python 함수, 모듈, 패키지]]에서 변환 규칙을 함수로 분리
- **후속**: [[concepts/python-structured-data-xml-json|Python XML/JSON 구조화 데이터 처리]]의 dict/list tree와 [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]의 표 구조

## 관련 수업

- [[summaries/2026-06-22-python-control-flow-collections|2026-06-22 Python 제어문과 컬렉션]]
- [[summaries/2026-06-23-python-dict-comprehension-builtins|2026-06-23 Python dict, comprehension, 내장 함수]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md`
- `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md`
