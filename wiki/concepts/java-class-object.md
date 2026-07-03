---
title: Java 클래스와 객체
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 클래스와 객체

## 정의

클래스는 객체를 만들기 위한 사용자 정의 타입이자 설계도이고, 객체는 그 클래스를 바탕으로 만들어진 구체적인 대상이다.

## 왜 중요한가

Java는 객체지향 언어다. Spring Boot의 Entity, DTO, Service, Controller도 결국 클래스와 객체를 이용해 구성된다. 따라서 Java 초반의 `Product` 예제는 이후 백엔드 학습의 출발점이다.

## 핵심 설명

수업에서는 `Product`를 예로 들었다.

```java
public class Product {
    String name;
    int price;
    String inputdate;
}
```

이 클래스는 상품명, 단가, 입고일자를 가진 새로운 타입이다.

```java
Product shin = new Product();
shin.name = "신라면";
```

`shin`은 `Product` 클래스로 만든 객체를 가리키는 참조 변수다.

## 클래스의 3요소

- 필드/멤버 변수: 객체의 상태 데이터
- 메서드: 객체의 동작
- 생성자: 객체 생성 시 초기화 담당

숙제 정리에서는 지역 변수와 필드의 차이도 함께 다뤘다. 지역 변수는 메서드 실행 중에만 사용되고, 필드는 객체가 살아 있는 동안 유지된다.

## 자주 헷갈리는 점

- 클래스는 추상적인 설계이고, 객체는 메모리에 만들어진 구체적인 인스턴스다.
- 클래스 이름은 관례적으로 대문자로 시작한다.
- `private` 필드는 객체 내부 데이터 보호를 위해 직접 접근을 막고 getter/setter로 접근한다.

## 관련 개념

- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[concepts/java-inheritance|Java 상속]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]

## 출처

- `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
