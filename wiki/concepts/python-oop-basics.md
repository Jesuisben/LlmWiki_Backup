---
title: Python 객체지향 기본
created: 2026-07-03
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md
status: growing
confidence: high
---

# Python 객체지향 기본

## 정의

Python 객체지향은 class를 설계도로 삼아 instance별 상태와 method를 묶고, 상속(Is-A)과 포함(Has-A)으로 객체 관계를 표현하는 방식이다.

## 왜 중요한가

06-25 수업은 Java 객체지향에서 익힌 class·생성자·상속을 Python 문법으로 다시 구성했다. 같은 개념의 공통점과 Python 특유의 `self`, `__init__`, class variable을 함께 보면 framework와 library의 객체 API를 읽기 쉬워진다.

## class와 instance

### `__init__`와 `self`

`__init__`은 instance 생성 직후 초기 상태를 설정하는 특별 method다. 첫 매개변수 `self`는 호출 대상 instance를 가리킨다. 호출할 때 직접 전달하지 않지만 method 정의에는 필요하다.

수업의 계좌·원 예제는 다음 흐름을 반복했다.

1. 생성자 인수를 받는다.
2. `self.속성`에 저장해 instance variable을 만든다.
3. instance method가 `self.속성`을 읽어 출력·계산한다.

### class variable과 instance variable

- class variable: class body에 선언되어 instance들이 공유한다.
- instance variable: 보통 `__init__`에서 `self`에 저장해 객체별로 분리한다.

계좌의 거래처명처럼 공통 값은 class variable로 설명할 수 있다. 반대로 가방의 열림 상태와 내용물처럼 객체마다 달라야 하는 값을 class variable로 두면 여러 instance가 공유할 수 있으므로 주의한다. ^[raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md]

## 상속과 overriding

`Employee(Person)`·`Student(Person)`·`Teacher(Person)`는 공통 이름·나이·성별을 부모에 두고 자식별 상태와 행동을 추가했다.

- `super().__init__(...)`: 부모 초기화 재사용
- 같은 이름의 method 재정의: overriding
- `super().method()`: 부모 동작을 먼저 실행한 뒤 자식 동작 추가

상속은 “자식은 부모의 한 종류다”라는 Is-A 관계일 때 자연스럽다.

## Has-A 포함 관계

`Bag`가 `Dosirak`을 담고 `Sales`가 `Fruit`을 사용한 예제는 한 객체가 다른 객체를 구성요소로 가지는 Has-A 관계다. 상속으로 공통 타입을 만들 필요가 없고, 역할을 조합할 때 사용한다.

수업 code의 `Sales`는 반복마다 `self.fruit`를 새 객체로 덮어쓴다. 이는 객체를 “사용했다”는 Has-A 예시는 되지만, 판매 과일 전체를 보존하려면 list 같은 별도 collection이 필요하다.

## Java와 비교

| 항목 | Python 수업 | Java 선행 학습 |
|---|---|---|
| 생성 초기화 | `__init__` | class 이름과 같은 생성자 |
| 현재 객체 | `self`를 정의에 명시 | `this`는 필요 시 사용 |
| 상속 | `class Child(Parent)` | `extends` |
| 부모 호출 | `super()` | `super` |
| 생성자 다형식 | 기본/가변 인수 등으로 설계 | overloading 가능 |
| 타입 선언 | runtime 값 중심 | field/parameter type 명시 |

## 자주 헷갈리는 점

- `self`는 생성자 표시가 아니라 현재 instance 참조다.
- `__init__`을 여러 번 정의하면 마지막 정의가 앞 정의를 덮어쓰므로 Java식 constructor overloading이 되지 않는다.
- class variable의 mutable list는 instance 전체가 공유할 수 있다.
- overriding과 overloading은 다르다.
- Has-A는 class를 다른 class 안에 “문법적으로 선언”하는 것보다, 실제 객체를 속성·collection으로 보유하는 관계가 핵심이다.
- `__del__`의 호출 시점은 확정적 자원 해제 수단으로 의존하지 않는다. 파일은 `with` 같은 context manager를 사용한다.

## 선행·후속 연결

- **선행**: [[concepts/java-class-object|Java 클래스와 객체]], [[concepts/java-inheritance|Java 상속]], [[concepts/python-functions-modules-packages|Python 함수, 모듈, 패키지]]
- **당일**: [[summaries/2026-06-25-python-standard-library-oop|2026-06-25 Python 표준 라이브러리와 객체지향]]
- **후속**: [[concepts/python-exception-handling|Python 예외 처리]]와 file context manager, Pandas의 Series/DataFrame 객체 method 사용

## 관련 개념

- [[entities/python|Python]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md`
