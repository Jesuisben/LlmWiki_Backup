---
title: 2026-06-25 Python 표준 라이브러리와 객체지향
created: 2026-07-03
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md
status: growing
confidence: high
---

# 2026-06-25 Python 표준 라이브러리와 객체지향

## 한 줄 요약

직접 만든 module에서 Python 표준 library 사용으로 확장하고, class·상속·Has-A로 데이터와 동작을 객체 단위로 묶었다.

## 배운 내용

1. 이전 날 만든 문자열 분리/결합 함수를 다른 module에서 import해 사용했다.
2. `zfill`, `os.path`, `random`, `datetime`으로 경로·무작위·날짜/시간 데이터를 처리했다.
3. `class`, `__init__`, `self`, class variable, instance variable, method를 배웠다.
4. `Person`을 `Employee`·`Student`·`Teacher`가 상속하고 `super()`로 부모 초기화·메서드를 재사용했다.
5. `Bag`-`Dosirak`, `Sales`-`Fruit` 예제로 한 객체가 다른 객체를 포함하는 Has-A 관계를 실습했다.
6. 다음 날 배울 예외 처리로 이어질 것을 마지막에 예고했다.

표준 module 실습은 “이미 만들어진 기능을 조합하는 법”, 객체지향 실습은 “내 프로그램의 상태와 동작을 구조화하는 법”을 각각 담당한다. ^[raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md]

## 대표 실습

### 경로를 조립해 디렉터리 생성

- **입력**: 상위 경로와 새 폴더 이름
- **처리**: `os.path.isdir`로 존재 여부를 확인하고 `os.path.join`으로 경로를 조립한다.
- **결과 의도**: `os.mkdir`로 상위·하위 폴더를 만든다.

code와 “폴더가 생성됨”이라는 서술은 있지만 생성된 폴더 artifact가 이번 raw 범위에 보존된 것은 아니므로, 파일 시스템 실습 작성 근거로 구분한다.

### random의 중복 정책 비교

`randint`·`choice`는 한 값, `choices`는 중복 허용 복수 선택, `sample`은 중복 없는 표본, `shuffle`은 기존 순서를 제자리에서 섞는 역할로 나눴다. 로또·조 편성·발표 순서·팀 추출 문제에서 같은 list를 서로 다른 정책으로 처리했다.

### 상속과 Has-A

- **상속(Is-A)**: 공통 이름·나이·성별은 `Person`에 두고 자식이 추가 상태와 동작을 확장한다.
- **포함(Has-A)**: `Bag`가 `Dosirak` 객체를 보관하거나 `Sales`가 `Fruit` 객체를 만들어 사용한다.

이 구분은 Java에서 배운 상속·객체 포함을 Python 문법으로 다시 확인한 것이다.

## 원본에서 확인된 주의점

- `random.choices()` 설명 중 “중복 없이”라는 표현과 바로 뒤의 “중복 허용” 설명이 충돌한다. 실제 구분은 `choices` 중복 허용, `sample` 중복 비허용이다.
- `Bag.dosirak`과 `isOpened`가 class variable로 선언되어 여러 `Bag` 인스턴스가 상태를 공유할 수 있다. 인스턴스별 가방 상태라면 `__init__`에서 만들어야 한다.
- `Sales` 예제는 반복마다 `self.fruit`를 덮어쓰므로 마지막 객체만 속성으로 남는다. 수업의 Has-A 개념과 장기 보관 구조는 분리해 이해한다.
- 소멸자 `__del__`은 개념으로 소개되었지만, 실행 시점을 자원 해제의 유일한 보장으로 사용하지 않는다.

## 실행·결과 근거

- 여러 문제의 code와 출력 예시는 남아 있으나 전체 `.py` 실행 transcript는 없다.
- random 결과는 실행마다 달라질 수 있으므로 원본의 숫자·명단을 고정 결과로 취급하지 않는다.
- 경로 생성 code는 쓰기 side effect가 있어 이번 재고도화에서는 실행하지 않았다.

## 헷갈린 점 / 질문

- `self`는 호출할 때 직접 쓰지 않지만 instance method 정의의 첫 매개변수로 필요하다.
- class variable은 모든 instance가 공유하고 instance variable은 객체별로 분리된다.
- Python은 생성자 overloading을 여러 개 정의하기보다 기본 인수·가변 인수 등으로 설계한다.
- overriding은 자식이 같은 이름의 method를 다시 정의하는 것이고 `super()`는 부모 구현을 재사용한다.

## 이전·다음 수업 연결

- **이전**: [[summaries/2026-06-24-python-functions-modules|06-24]]의 함수·module 재사용을 표준 library와 class로 확장했다.
- **다음**: [[summaries/2026-06-26-python-exception-file-regex|06-26]]에서 실패를 처리하고 외부 파일을 읽고 쓰는 흐름으로 이동한다.
- **선행 연결**: [[concepts/java-class-object|Java 클래스와 객체]], [[concepts/java-inheritance|Java 상속]]과 문법·실행 모델을 비교한다.

## 관련 페이지

- [[concepts/python-oop-basics|Python 객체지향 기본]]
- [[concepts/python-functions-modules-packages|Python 함수, 모듈, 패키지]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md`
