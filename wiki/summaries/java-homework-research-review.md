---
title: Java 클래스 숙제와 사전조사 정리
created: 2026-07-15
updated: 2026-07-15
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: medium
---

# Java 클래스 숙제와 사전조사 정리

## 한 줄 요약

날짜별 직접 수업과 별도로 수행한 클래스 숙제를 객체·접근 제어·상속·추상화 복습과 메모리·컬렉션·제네릭 사전조사로 구분해 정리한다.

## 자료의 위치와 역할

이 원본에는 날짜가 명시되지 않았으므로 특정 수업일 summary로 귀속하지 않는다. 03-09~03-12 직접 수업과 겹치는 복습도 있지만, 날짜별 노트에서 실행을 확인할 수 없는 조사 답안도 함께 있다.

## 직접 수업 복습

- 클래스·객체·인스턴스, 필드·지역 변수·메서드·생성자 구분
- `private` 필드와 getter/setter, `this`
- 상속, 오버라이딩, 업캐스팅·다운캐스팅
- 추상 클래스와 인터페이스, 클래스 단일 상속과 여러 인터페이스 구현

이 항목들은 [[summaries/2026-03-09-java-class-object|03-09 클래스와 객체]], [[summaries/2026-03-10-java-constructor-overloading-inheritance|03-10 생성자·상속]], [[summaries/2026-03-11-java-inheritance-polymorphism|03-11 다형성]], [[summaries/2026-03-12-java-abstract-interface-static|03-12 추상화·인터페이스]]의 실행 기록과 함께 봐야 한다.

## 숙제 사전조사

### 메모리와 변수 생명주기

- stack, heap, static/method area의 입문용 구분
- 지역 변수, 인스턴스 변수, static 변수의 생성·사용 범위
- 이 구분은 학습용 모델이며 실제 JVM 구현과 최적화 전체를 설명하는 사양은 아니다.

### 컬렉션

| 종류 | 순서 | 중복 | 대표 연산 | 조사한 구현 예 |
|---|---|---|---|---|
| `List` | 있음 | 허용 | `add`, `get`, `size`, `remove`, `set` | `ArrayList`, `LinkedList` |
| `Set` | 인덱스 순서 기준 없음 | 허용하지 않음 | `add`, `contains`, `size`, `remove` | `HashSet`, `TreeSet` |
| `Map` | 키 기반 | 키 중복 불가 | `put`, `get`, `containsKey`, `remove` | `HashMap`, `TreeMap` |

숙제에서는 게시물 목록은 `List`, 중복 없는 번호 집합은 `Set`, 이름표가 붙은 값은 `Map`처럼 선택 상황을 조사했다. 이는 날짜별 Java 수업에서 컬렉션 구현 코드를 실행한 기록이 아니라 사전조사다.

### 제네릭

제네릭(generic)은 클래스나 컬렉션이 사용할 데이터 타입을 외부에서 지정해 타입 안정성을 높이는 문법으로 조사했다. 예를 들어 `List<String>`은 문자열 요소를 다룬다는 계약을 표현한다. 제네릭의 실제 구현 실습은 이 과목 날짜별 raw에서 확인되지 않는다.

## 원천 답안 검증이 필요한 부분

- “인터페이스의 모든 메서드는 반드시 추상 메서드”라는 답은 이날 학습 범위에는 맞지만 현대 Java 전체 규칙은 아니다. `default`, `static`, `private` 메서드가 있다.
- stack에는 기본형만, heap에는 참조형만 저장된다는 식의 이분법은 입문용 단순화다.
- `static`을 전역 변수와 완전히 같은 개념으로 보면 클래스 소속이라는 의미를 놓친다.
- 컬렉션을 모두 가변 배열처럼 이해하면 `List`, `Set`, `Map`의 순서·중복·키 구조 차이를 놓친다.

## 헷갈린 점 / 질문

- **직접 수업인가?** 날짜별 코드에서 실행을 확인한 내용과 숙제에서 조사만 한 내용을 구분한다.
- **배열과 컬렉션은 같은가?** 배열은 고정 크기 문법이고 컬렉션은 목적별 자료구조를 제공하는 라이브러리다.
- **getter/setter가 있으면 무조건 캡슐화인가?** 공개 범위와 변경 규칙을 설계해야 하며 메서드를 자동 생성하는 것만으로 충분하지 않다.

## 다음에 볼 것

- [[concepts/java-access-modifier-encapsulation|Java 접근 지정자와 캡슐화]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]
- [[comparisons/array-vs-collection|배열 vs 컬렉션]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 관련 페이지

- [[entities/java|Java]]
- [[summaries/2026-03-13-java-subject-review|Java 총정리]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]

## 출처

- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
