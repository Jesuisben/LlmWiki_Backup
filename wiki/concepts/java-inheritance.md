---
title: Java 상속
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 상속

## 정의

상속은 공통 속성과 동작을 부모 클래스(super class)에 두고, 자식 클래스(sub class)가 이를 물려받아 재사용·확장하는 문법이다.

## 왜 중요한가

상속은 중복 코드를 줄이고, 여러 객체를 공통 타입으로 묶어 다형성을 사용할 수 있게 한다. Spring Boot에서도 공통 필드, 추상 클래스, 인터페이스를 이해하는 기반이 된다.

## 핵심 설명

```java
public class Americano03 extends Beverage03 {
    private double waterAmount;
}
```

수업에서는 음료 예제를 통해 공통 필드인 이름과 가격을 `Beverage03`에 두고, `Americano03`, `Espresso03` 같은 하위 클래스가 개별 속성을 추가했다.

## 생성자와 `super`

자식 클래스 생성자의 첫 줄에는 기본적으로 `super();`가 숨어 있다. 부모 클래스에 매개변수 없는 생성자가 없으면 자식 생성자에서 `super(name, price)`처럼 부모 생성자를 명시적으로 호출해야 한다.

수업에서는 `new Americano03("아메리카노", 4000.0, 200.0)`의 값이 자식 생성자에 들어간 뒤, `super(name, price)`를 통해 부모 `Beverage03(String name, double price)` 생성자로 먼저 전달되고, 자식의 `waterAmount`가 이어서 초기화되는 순서를 추적했다. 부모에 매개변수 생성자만 만들자 숨은 `super()`가 호출할 기본 생성자가 사라져 오류가 생기는 경우도 함께 해결했다.

## 접근 지정자

- `private`: 부모 클래스 안에서만 직접 접근 가능
- `protected`: 상속 관계에서 접근 가능
- getter/setter: `private` 필드를 안전하게 읽고 쓰는 통로

## 자주 헷갈리는 점

- 상속받았다고 해서 부모의 `private` 필드를 직접 사용할 수 있는 것은 아니다.
- “일반화”는 여러 하위 클래스의 공통분모를 부모 클래스로 올리는 설계 과정이다.
- Java 클래스 상속은 기본적으로 단일 상속이다. 여러 기능 규격은 인터페이스로 분리한다.

## 학습 연결과 범위

- **선행:** 생성자, `this`, 접근 지정자, 객체 배열.
- **후속:** 부모 타입 배열과 다형성, 추상 클래스와 기능 인터페이스.
- Spring의 공통 기반 클래스는 후속 응용 관점이며, Java 수업 직접 근거는 `Animal`·`Beverage03` 계층과 생성자 호출 실습이다.

## 관련 개념

- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
