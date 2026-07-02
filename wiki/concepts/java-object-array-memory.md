---
title: Java 객체 배열과 메모리 관점
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
# Java 객체 배열과 메모리 관점

## 객체 배열

클래스도 사용자가 만든 타입이므로 배열로 만들 수 있다.

```java
Product03[] itemlist = new Product03[size];

itemlist[0] = new Product03("소이조이", 2000, "2025/08/15");
itemlist[1] = new Product03("맥심커피", "2025/07/17");
```

초기화 기법도 가능하다.

```java
Product03[] productArray = {
    new Product03("쭈쭈바", 1500, "2025/12/25"),
    new Product03("사과", 3000, "2025/06/06"),
    new Product03("오징어땅콩", "2025/07/17")
};
```

이 부분은 이후 Spring에서 `List<Product>`, `Page<Product>`처럼 객체 묶음을 다루는 흐름과 연결된다.

## 클래스 숙제에서 보강된 관점

`클래스 숙제 완료.md`는 클래스/객체를 단순 문법이 아니라 **메모리와 책임 분리** 관점으로 다시 정리한다.

- 클래스는 객체를 만들기 위한 설계도이자 사용자 정의 타입이다.
- 객체는 `new`를 통해 실제 메모리에 만들어지는 인스턴스다.
- 필드(field)는 객체가 살아 있는 동안 상태를 보관하고, 지역 변수는 메서드 실행 중 잠깐 쓰이다 사라진다.
- 메서드는 객체의 동작이며, 필드를 읽거나 바꾸고 다른 객체와 데이터를 주고받는 통로가 된다.
- 생성자는 객체가 만들어질 때 초기 상태를 잡아 주는 특별한 블록이다.

이 관점은 이후 [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]를 볼 때 중요하다. Entity/DTO/Service도 결국 “어떤 상태와 동작을 가진 클래스를 왜 나누는가”의 문제이기 때문이다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

### Stack/Heap 관점으로 보는 객체

```java
Product shin = new Product();
```

- `shin`이라는 참조 변수는 stack 쪽의 지역 변수로 이해할 수 있다.
- `new Product()`로 만들어진 실제 객체 데이터는 heap에 올라간다.
- `shin`에는 객체 자체가 통째로 들어 있는 것이 아니라 heap 객체를 가리키는 참조값이 들어 있다.

그래서 [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]에서 `int age = 29`와 `Product shin = new Product()`는 메모리에 저장되는 느낌이 다르다.

## 관련 페이지

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]

## 출처

- `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
