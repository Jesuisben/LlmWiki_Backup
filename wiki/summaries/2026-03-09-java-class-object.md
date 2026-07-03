---
title: 2026-03-09 Java 클래스와 객체
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
  - raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-09 Java 클래스와 객체

## 한 줄 요약

`Product` 예제로 클래스 정의, 객체 생성, 멤버 변수, 메서드, 접근 지정자, getter/setter를 배우며 사용자 정의 타입을 만들기 시작했다.

## 커리큘럼 위치

- 배열까지는 같은 타입의 값을 여러 개 담는 방식이었다면, 이날부터는 여러 속성과 동작을 묶은 “객체”를 다룬다.
- 다음날 [[summaries/2026-03-10-java-constructor-overloading-inheritance|생성자·오버로딩·상속 입문]]으로 이어진다.

## 배운 내용

- 클래스: 기존 자료형을 조합해 새로 만드는 사용자 정의 타입
- 객체: 클래스로부터 만들어진 구체적인 대상
- 멤버 변수/필드: 객체의 속성 데이터
- 메서드: 객체가 수행할 동작 또는 값을 반환하는 실행 블록
- 접근 지정자: 특히 `private`을 통해 외부 직접 접근을 막고 getter/setter를 사용한다.
- 클래스 이름은 관례적으로 첫 글자를 대문자로 쓴다.

## 핵심 실습 / 예제

- `Product` 클래스에 `name`, `price`, `inputdate` 필드를 정의했다.
- `Product shin = new Product();`로 객체를 생성했다.
- `shin.name = "신라면"`처럼 객체의 필드에 값을 넣고 출력했다.
- `Product03` 등으로 접근 지정자와 getter/setter 실습을 진행했다.

## 헷갈린 점 / 질문

- 클래스는 “붕어빵 틀”, 객체는 “만들어진 붕어빵” 비유로 이해할 수 있지만, 실제 Java에서는 클래스가 타입 역할도 한다.
- 지역 변수는 메서드 실행이 끝나면 사라지지만, 필드는 객체가 살아 있는 동안 객체와 함께 유지된다.
- `private` 필드는 상속이나 다른 클래스에서 직접 접근할 수 없으므로 메서드로 접근해야 한다.

## 관련 페이지

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]

## 출처

- `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
- `raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
