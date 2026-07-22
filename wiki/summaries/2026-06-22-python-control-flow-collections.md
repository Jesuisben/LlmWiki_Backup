---
title: 2026-06-22 Python 제어문과 컬렉션
created: 2026-07-03
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md
status: growing
confidence: high
---

# 2026-06-22 Python 제어문과 컬렉션

## 한 줄 요약

조건과 반복으로 실행 순서를 만들고, list·tuple에 여러 값을 담아 조회·변경·누적하는 단계까지 확장했다.

## 배운 내용

1. `if`·`elif`·`else`로 홀짝, 성인 여부, 가중 점수, 학점을 판정했다.
2. `range(stop)`, `range(start, stop)`, `range(start, stop, step)`을 `for`와 결합해 정해진 횟수를 반복했다.
3. `while True`·`break`로 정답을 맞힐 때까지 반복하는 흐름과, 재고가 0이 될 때까지 판매하는 상태 기반 반복을 연습했다.
4. list의 결합·반복·추가·삽입·수정·삭제·검색·빈도 계산을 수행하고 `Counter`로 항목별 횟수를 셌다.
5. tuple의 생성 방식, 한 요소 tuple의 쉼표, 불변성, indexing/slicing, 다중 할당과 swap을 배웠다.
6. 마지막에는 `split` → list 순회·수정 → `join`과 list/tuple 문제로 제어문과 컬렉션을 함께 사용했다.

수업은 “한 값에 대한 분기”에서 “여러 값에 같은 규칙을 반복 적용”하는 방향으로 진행되었다. 이는 다음 날 dict·중첩 list·comprehension으로 이어지는 기반이다. ^[raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md]

## 대표 실습

### 커피 재고 판매

- **입력**: 남은 잔 수와 단가를 둔 뒤 반복마다 입금액을 받는다.
- **처리**: 금액이 단가보다 큰지·같은지·작은지에 따라 거스름돈, 판매, 판매 불가를 나눈다.
- **상태 변화**: 판매가 성립한 경우에만 재고를 1 감소시킨다.
- **종료**: 재고가 0이 되면 `while` 조건이 거짓이 되어 종료 문구로 이동한다.

### 문자열을 list로 바꿔 가공하기

- **입력**: 공백으로 구분된 문장을 `split()`해 list로 만든다.
- **처리**: 위치가 짝수인 단어는 대문자, 홀수인 단어는 소문자로 바꾼다.
- **결과**: `"#".join(...)`으로 다시 하나의 문자열로 조립한다.

### list와 tuple의 역할 비교

커피 list는 `append`, `insert`, index 대입, `remove`로 상태를 바꿨다. 빵 tuple은 직접 수정하지 않고 slicing한 결과를 list로 변환해 정렬했다. “순서가 있다”는 공통점과 “직접 변경 가능한가”라는 차이를 같은 데이터로 확인한 흐름이다.

## 실행·결과 근거

- 각 문제에는 코드와 출력 결과가 함께 있으나 대부분 교안형 결과 블록이므로 독립 실행 성공으로 일괄 판정하지 않는다.
- 무작위 숫자 맞히기는 code가 존재하지만 특정 실행 transcript는 보존되지 않았다.
- list 검색의 `ValueError`는 `try/except`로 처리하는 작성 코드가 있으며, 예외 처리는 06-26에 독립 주제로 다시 학습한다.
- 시험 점수·문자열을 함께 다룬 ForAndList 구간은 “불합격자를 `continue`로 건너뛰어 합격자만 출력한” 결과 블록이 있지만 뒤의 현재 code에는 그 반복문이 없다. 결과를 현재 code의 실행 산출물로 확정하지 않는다.

## 헷갈린 점 / 질문

- `range`의 stop은 포함되지 않는다. 합계에서 끝값을 포함하려면 `stop + 1`이 필요하다.
- list는 mutable, tuple은 immutable이다. tuple 한 요소는 `("값",)`처럼 쉼표가 필요하다.
- `while True` 자체는 종료 조건이 아니므로 내부의 `break`나 상태 변화가 반드시 필요하다.
- `continue`는 현재 반복만 건너뛰고 반복문 전체를 끝내지 않는다.
- “`for`는 횟수가 정해졌을 때, `while`은 정해지지 않았을 때”는 선택 경향을 설명한 것이지 문법적 제한은 아니다.
- 원본 문제 중 “3의 배수인 위치와 1번째 요소”는 중복 여부를 별도로 판단해야 한다. 요구 문장과 결과 list를 함께 확인해야 한다.

## 이전·다음 수업 연결

- **이전**: [[summaries/2026-06-19-python-setup-basic-syntax|06-19]]의 입력·형변환·연산을 조건과 반복 안에 배치했다.
- **다음**: [[summaries/2026-06-23-python-dict-comprehension-builtins|06-23]]에서 key-value, 중첩 list, comprehension과 정렬·집계를 다룬다.
- **후속**: list/tuple의 순회와 boolean 조건은 Series filtering과 DataFrame 행 처리로 확장된다.

## 관련 페이지

- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md`
