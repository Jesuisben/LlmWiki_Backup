---
title: 2026-06-23 Python dict, comprehension, 내장 함수
created: 2026-07-03
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md
status: growing
confidence: high
---

# 2026-06-23 Python dict, comprehension, 내장 함수

## 한 줄 요약

순서형 list/tuple에서 key-value dict와 set으로 자료구조를 넓히고, 중첩 데이터·comprehension·내장 함수로 필터링·집계·결합·정렬하는 흐름을 만들었다.

## 배운 내용

1. dict의 key 중복 불가와 대입 시 덮어쓰기, `in`, `keys`, `values`, `items`, `get`, `clear`를 학습했다.
2. key가 없을 때 `KeyError`를 처리하거나 `get(key, default)`로 안전하게 읽는 두 방식을 비교했다.
3. 중첩 list에서 `행[열]` 형태로 값을 읽고 수정한 뒤 반복문으로 각 행을 계산했다.
4. list comprehension으로 범위 생성, 배수 변환, 조건 필터링, 평균 이상 점수·성인·양수·짝수·이름 길이 선별을 수행했다.
5. `sum`·`min`·`max`·`set`·`all`·`any`·`ord`·`chr`·`pow` 등 내장 함수로 반복 코드를 줄였다.
6. `zip`으로 여러 iterable을 같은 위치끼리 묶고, `sorted`의 `key`·`reverse`로 dict key/value 기준 정렬을 연습했다.

이날의 핵심 전환은 “자료를 저장하는 법”에서 “자료의 모양을 바꾸고 필요한 것만 고르는 법”으로 이동한 것이다. 이후 함수·모듈과 Pandas가 이 패턴을 재사용한다. ^[raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md]

## 대표 실습

### 빵 가격 dict 갱신

- **입력**: 품명 → 가격 dict, 신규 품명 list, 조회 대상 list를 준비한다.
- **처리**: 없는 key 추가, 기존 가격 수정, value 존재 여부 확인, 반복 추가, 예외 처리, `get` 기본값, `items` 순회를 차례로 적용한다.
- **결과**: 마지막에는 특정 품목만 가격을 조정해 출력한다. loop의 지역 변수 `value`만 바꾸면 원본 dict가 바뀌지 않는다는 점은 이후 실제 갱신 코드에서 다시 확인해야 한다.

### 중첩 list를 행 데이터처럼 처리

학생별 `[이름, 식별 문자열, 점수...]` list를 하나의 상위 list에 담고, 각 행에서 필요한 위치를 꺼내 연도·연령대·성별·총점·평균·학점을 계산했다. 개인 식별 형식은 slicing 교육용 원본 데이터이므로 위키에는 실제 값을 옮기지 않는다.

### `zip` → list → dict → 정렬

- **입력**: 이름 list와 점수 list
- **처리**: `zip`으로 `(이름, 점수)` tuple들을 만들고 `dict()`로 변환
- **결과**: `sorted(mydict, key=mydict.get, reverse=True)`로 높은 점수의 이름부터 정렬

이 흐름은 여러 열을 묶어 표 구조로 만드는 Pandas 학습의 선행 경험이다.

## 실행·결과 근거

- 코드와 예상/기록 출력이 풍부하지만 별도 실행 artifact는 없다. 출력 블록을 모든 예제의 성공 증거로 확대하지 않는다.
- 중첩 list의 예상 출력에서 몇 번째 요소라고 적은 label과 실제 code의 위치 label이 일관되지 않는다. 학점 조건도 `>` 경계를 사용해 정확히 경계값인 점수는 한 단계 낮게 분류될 수 있으므로, 해당 결과를 검증 완료로 보지 않는다.
- 일부 결과 문구와 code 변수명에는 오탈자가 있으므로, 학습 개념은 원본 요구·코드·결과를 함께 읽어 판정했다.
- `eval()`은 문자열을 코드로 실행하므로 신뢰하지 않는 입력에는 사용하지 않는다는 보안 경계를 함께 기억해야 한다.

## 헷갈린 점 / 질문

- `dict[key]`는 key 부재 시 예외, `dict.get(key, default)`는 기본값 반환이며 dict에 새 항목을 저장하지는 않는다.
- comprehension은 `[표현식 for 변수 in 반복가능객체 if 조건]` 순서로 읽는다.
- `set`은 중복을 제거하지만 순서 기반 결과가 필요하면 다시 정렬해야 한다.
- 빈 `{}`는 dict이고 빈 set은 `set()`으로 만든다. truthiness도 숫자 1만 참인 것이 아니라 0은 falsy, 0이 아닌 숫자는 일반적으로 truthy다.
- `zip`은 가장 짧은 iterable 길이까지만 묶는다.
- `sorted()`는 새 list를 반환하고, list의 `.sort()`는 원본 list를 제자리에서 바꾼다.

## 이전·다음 수업 연결

- **이전**: [[summaries/2026-06-22-python-control-flow-collections|06-22]]의 list/tuple과 반복문을 확장했다.
- **다음**: [[summaries/2026-06-24-python-functions-modules|06-24]]에서 반복되는 처리 로직을 함수·lambda·module로 분리한다.
- **후속**: dict는 JSON 객체, 중첩 list는 DataFrame 행, comprehension은 전처리 filter의 감각으로 이어진다.

## 관련 페이지

- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-functions-modules-packages|Python 함수, 모듈, 패키지]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md`
