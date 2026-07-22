---
title: 2026-06-24 Python 함수, 람다, 모듈·패키지
created: 2026-07-03
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md
status: growing
confidence: high
---

# 2026-06-24 Python 함수, 람다, 모듈·패키지

## 한 줄 요약

반복되던 처리 로직을 함수로 묶고, 인수 전달·lambda·고차 함수에서 모듈/패키지 import까지 코드 재사용 범위를 넓혔다.

## 배운 내용

1. `enumerate`로 iterable의 위치와 값을 함께 받았다.
2. `def`·`return`, 기본 매개변수, 위치 인수와 키워드 인수를 학습했다.
3. 일반 매개변수 → `*args` → `**kwargs` 순서와 tuple/dict로 모이는 가변 인수를 확인했다.
4. `lambda`를 comprehension·`filter`·`map`에 전달해 선택과 변환을 함수로 표현했다.
5. `__name__ == "__main__"`으로 직접 실행과 import 실행을 구분했다.
6. 파일 하나를 module, module을 묶는 디렉터리를 package로 보고 여섯 가지 import 형태와 별칭을 비교했다.

수업 순서는 “함수를 정의한다 → 함수를 값처럼 다른 함수에 넘긴다 → 다른 파일의 함수를 불러온다”로 확장된다. 이 흐름은 외부 library를 import하는 06-29 수업의 직접 선행이다. ^[raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md]

## 대표 실습

### 가변 인수로 여러 모양의 입력 받기

- **입력**: category 하나, 여러 위치 값, 여러 key=value를 한 함수에 전달한다.
- **처리**: 위치 값은 tuple, keyword 값은 dict로 받은 뒤 각각 순회한다.
- **결과**: 카테고리 아래 항목과 key/value 정보를 출력하는 code가 기록되어 있다.

### lambda + filter/map

- **입력**: 정수 list와 “3의 배수인가”를 반환하는 lambda
- **처리**: comprehension은 각 요소를 boolean으로 변환하고, `filter`는 참인 원소만 남기며, `map`은 모든 원소를 새 값으로 바꾼다.
- **결과**: 비율 계산·배수 선별·일괄 값 변경의 세 역할을 비교했다.

### 직접 실행과 import

한 module에서 함수를 정의하고 `__name__` 값에 따라 직접 실행용 code를 분기했다. 다른 파일이 그 함수를 import하면 module top-level code도 실행된다는 점을 기록했다. 이후 package 경로에서 module 전체·별칭·함수 직접 import를 차례로 사용했다.

## 원본에서 확인된 불일치

- 기본값이 있는 덧셈 함수 예제에서는 설명 주석과 실제 함수 시그니처가 맞지 않는 부분이 있다. 호출 code상 기본값이 존재하므로 “필수 인수가 누락되어 항상 오류”라고 단정하지 않는다.
- 성적 함수의 `else` 분기와 마지막 호출 값에는 요구사항·출력 예시와 맞지 않는 부분이 있다. 따라서 모든 출력 예시를 현재 code의 실행 결과로 취급하지 않는다.
- 전역 list를 두 함수가 함께 사용하는 최솟값/최댓값 예제는 재호출할수록 상태가 누적된다. 함수의 입력만으로 결과가 결정되는 구조와 비교할 필요가 있다.

## 실행·결과 근거

- module/package code와 교육 자료의 독립 `.py` 파일이 보조 근거로 존재하지만, 이번 summary는 날짜 노트의 학습 흐름을 우선한다.
- 출력 블록은 수업상 기대/기록 결과이며 전체 module 테스트 성공을 의미하지 않는다.
- import로 생성된 bytecode가 있더라도 특정 호출·분기·결과의 정확성까지 증명하지 않는다.

## 헷갈린 점 / 질문

- 위치 인수는 keyword 인수보다 앞에 둔다.
- `*args`는 tuple, `**kwargs`는 dict지만 이름 `args`·`kwargs` 자체는 관례다.
- `map(func, data)`에는 실행 결과 `func()`가 아니라 함수 객체 `func`를 전달한다.
- module은 `.py` 파일, package는 module을 묶는 디렉터리다.
- import 순간 module의 top-level code가 실행될 수 있으므로 실행 진입점을 분리한다.

## 이전·다음 수업 연결

- **이전**: [[summaries/2026-06-23-python-dict-comprehension-builtins|06-23]]의 반복·필터·dict 처리를 재사용 가능한 함수로 묶었다.
- **다음**: [[summaries/2026-06-25-python-standard-library-oop|06-25]]에서 표준 module을 사용하고 class로 상태와 동작을 함께 묶는다.
- **후속**: [[summaries/2026-06-29-python-regex-xml-json-jupyter|06-29]]의 `re`, `json`, XML module과 외부 Pandas import로 이어진다.

## 관련 페이지

- [[concepts/python-functions-modules-packages|Python 함수, 모듈, 패키지]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md`
