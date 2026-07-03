---
title: Java 객체 배열과 메모리 관점
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
status: stable
confidence: high
---

# Java 객체 배열과 메모리 관점

## 정의

객체 배열은 같은 클래스 타입의 객체 참조를 여러 개 담는 배열이다. 배열 칸에는 객체 자체가 아니라 heap에 만들어진 객체를 가리키는 참조값이 들어간다.

## 왜 중요한가

Java 수업은 기본 배열에서 객체 배열로 넘어가며 “값을 여러 개 담는다”에서 “객체를 여러 개 관리한다”로 발전했다. 이 흐름은 이후 상품 목록, 회원 목록, 장바구니 목록 같은 백엔드/프론트엔드 데이터 구조와 연결된다.

## 핵심 설명

```java
Product03[] products = new Product03[3];
products[0] = new Product03("신라면", 1000);
products[1] = new Product03("새우깡", 1500);
```

- `products` 배열 자체는 참조 변수다.
- 각 칸도 `Product03` 객체를 가리키는 참조를 담는다.
- 객체는 heap 영역에 만들어지고, 지역 변수/참조 변수는 stack 관점에서 이해할 수 있다.

## 수업 예시

[[summaries/2026-03-10-java-constructor-overloading-inheritance|2026-03-10]]에는 `Product` 객체 여러 개를 배열에 담고 반복문으로 처리하는 예제가 등장했다. [[summaries/2026-03-11-java-inheritance-polymorphism|2026-03-11]]에는 부모 타입 배열에 여러 자식 객체를 담는 다형성 예제로 확장되었다.

## 자주 헷갈리는 점

- `Product03[] products = new Product03[3]`은 객체 3개를 자동 생성하는 것이 아니다. 객체 참조를 담을 칸 3개를 만드는 것이다.
- 각 칸에 `new Product03(...)`를 대입해야 실제 객체가 연결된다.
- 부모 타입 배열에 자식 객체를 담을 수 있는 이유는 업캐스팅 때문이다.

## 관련 개념

- [[concepts/java-array|Java 배열]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]

## 출처

- `raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
