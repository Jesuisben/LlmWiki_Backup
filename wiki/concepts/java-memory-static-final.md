---
title: Java 메모리, static, final
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---

# Java 메모리, static, final

## 정의

Java 입문에서 `static`, stack, heap, `final`은 객체가 어디에 만들어지고, 어떤 값이 객체별로 따로 존재하며, 어떤 값이 클래스 전체에서 공유되는지를 이해하기 위한 개념이다.

## 왜 중요한가

객체지향 문법을 배울 때 “객체를 만들지 않고도 쓸 수 있는 값”, “객체마다 따로 있는 값”, “메서드 안에서 잠깐 쓰는 값”이 섞이면 코드 흐름이 헷갈린다.

- `static`: 클래스에 붙어 공유되는 값/메서드
- 인스턴스 변수: 객체마다 따로 가지는 상태
- 지역 변수: 메서드 실행 중 잠깐 쓰는 값
- `final`: 더 이상 바꿀 수 없게 고정한 값 또는 오버라이딩 금지 규칙

## 메모리 영역을 입문 수준으로 이해하기

| 영역 | 입문 단계 이해 | 예시 |
|---|---|---|
| static / method area | 클래스 정보와 static 멤버가 프로그램 동안 올라가는 영역 | `static int count` |
| stack | 메서드 실행 중 쓰이는 지역 변수와 참조 변수 | `int i`, `Product p` 참조 변수 |
| heap | `new`로 생성된 객체와 배열의 실제 데이터 | `new Product()`, `new int[3]` |

```java
Product shin = new Product();
```

입문 단계에서는 `shin`이라는 이름표는 stack 쪽에 있고, 실제 `Product` 객체는 heap에 있다고 비유하면 이해하기 쉽다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

## static 변수와 메서드

`static` 변수는 객체마다 따로 생기는 변수가 아니라 클래스에 하나 붙는 공유 변수다.

```java
public static String STORE_NAME = "G-CAFE";
System.out.println(Beverage05.STORE_NAME);
```

static 메서드도 객체 없이 `클래스명.메서드명()`으로 호출할 수 있다. 객체의 속성과 상관없이 입력값만으로 계산하는 공용 기능이나, 클래스 단위 조회에 어울린다. ^[raw/Study/1. Java/Java 총정리/Java 총정리.md]

## private static과 getter

```java
private static int beverageCount = 0;

public static int getBeverageCount() {
    return beverageCount;
}
```

이 구조는 주문 잔수처럼 클래스 전체가 공유해야 하지만 직접 수정은 막아야 하는 값에 적합하다.

## final 변수와 final 메서드

`final`이 붙은 변수는 한 번 정한 값을 바꿀 수 없다.

```java
public static final String STORE_NAME = "G-CAFE";
```

`final` 메서드는 자식 클래스에서 오버라이딩할 수 없다. 기능 변조를 막거나 모든 자식에서 동일하게 유지해야 하는 핵심 동작에 사용할 수 있다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

## 자주 헷갈리는 점

### static은 객체가 “아예 필요 없다”는 뜻이 아니다

객체마다 달라야 하는 상태는 인스턴스 변수로 두고, 모든 객체가 공유해야 하는 값만 static으로 둔다.

### static 변수와 인스턴스 변수

| 구분 | static 변수 | 인스턴스 변수 |
|---|---|---|
| 생성 기준 | 클래스당 하나 | 객체마다 하나 |
| 접근 | `클래스명.변수명` | `객체명.변수명` |
| 예시 | 카페 이름, 주문 총 개수 | 음료 이름, 가격, 물 양 |

## 관련 개념

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[summaries/2026-03-12-java-abstract-interface-static|2026-03-12 Java 추상 클래스, 인터페이스, static/final]]

## 출처

- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
