---
title: Java 클래스와 객체
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---
# Java 클래스와 객체

## 정의

Java에서 **클래스(class)**는 객체를 만들기 위한 사용자 정의 타입이고, **객체(object)**는 그 클래스를 바탕으로 실제로 생성된 구체적인 값이다.

수업에서는 클래스는 붕어빵 틀·스포츠라는 범주·시계 설계 정보, 객체는 만들어진 붕어빵·축구/야구/농구·실제 시계 하나로 비유했다.

## 왜 중요한가

Java 이후의 Spring Boot 학습은 대부분 객체지향 위에서 돌아간다. Entity, DTO, Controller, Service, Repository, Bean은 모두 클래스/객체 개념과 연결된다.

## 핵심 흐름

1. 클래스는 기존 타입을 조합해 만든 사용자 정의 타입이다.
2. 객체는 `new 클래스명()`으로 heap에 생성된다.
3. 필드는 객체의 상태, 메서드는 동작, 생성자는 초기화를 담당한다.
4. 캡슐화를 위해 필드는 `private`으로 두고 getter/setter로 접근하는 경우가 많다.

자세한 문법과 예제는 다음 하위 페이지로 나눴다.

- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]] — 메서드, 접근 지정자, 생성자, `this`, 오버로딩
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]] — 객체 배열, stack/heap 관점, 클래스 숙제 보강

## 수업 예시

```java
Product shin = new Product();
shin.name = "신라면";
shin.price = 1000;
```

`Product`는 사용자가 만든 타입이고, `shin`은 그 타입으로 생성한 객체다. `.`은 객체 안의 멤버에 접근하는 연산자다.

## 자주 헷갈리는 점

- 클래스는 설계도이고 객체는 실제 생성물이다.
- 멤버 변수는 객체에 속하고, 지역 변수는 메서드 실행 중 잠시 사용된다.
- 메서드는 동작이고 생성자는 객체 초기화 문법이다.
- `private`은 감추기만 하는 것이 아니라 잘못된 접근을 줄이는 캡슐화 장치다.

## 관련 페이지

- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]

## 출처

- `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
