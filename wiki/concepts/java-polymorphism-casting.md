---
title: Java 다형성과 참조 형변환
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 다형성과 참조 형변환

## 정의

다형성은 하나의 부모 타입으로 여러 자식 객체를 다룰 수 있는 객체지향 특성이다. 참조 형변환은 자식 객체를 부모 타입으로 보거나, 다시 자식 타입으로 좁혀 보는 과정이다.

## 왜 중요한가

수업의 음료 예제처럼 `Beverage03` 배열에 `Americano03`, `Espresso03` 객체를 함께 담을 수 있으면 반복문으로 공통 처리를 할 수 있다. 이후 Spring에서 인터페이스 타입으로 구현체를 다루는 흐름과도 연결된다.

## 핵심 설명

### 업캐스팅

```java
Beverage03 drink = new Americano03(...);
```

자식 객체를 부모 타입 참조로 바라보는 것이다. 보통 자동으로 가능하다.

### 다운캐스팅

```java
if (drink instanceof Americano03) {
    Americano03 americano = (Americano03) drink;
}
```

부모 타입 참조를 다시 자식 타입으로 좁히는 것이다. 실제 객체 타입이 맞는지 확인해야 안전하다.

### 오버라이딩과 다형성

부모 타입으로 호출해도 실제 객체가 자식이면 자식이 재정의한 메서드가 실행된다. 그래서 `toString()` 같은 메서드를 각 클래스 상황에 맞게 재정의할 수 있다.

## 수업 예시

- `Beverage04[]`에 `Espresso04`, `Latte04` 객체를 함께 저장하고 반복문에서 공통 `showInfo()` 호출.
- `beverage[i] instanceof Americano04`처럼 실제 생성 타입을 확인한 뒤 자식 기능을 호출하기 위한 다운캐스팅 수행.
- `Object → Animal → Dog` 또는 음료 계층에서 `toString()`을 재정의하고 실제 객체의 메서드가 선택되는 흐름 확인.

## 학습 연결과 범위

- **선행:** [[concepts/java-inheritance|상속]]과 [[concepts/java-object-array-memory|객체 배열]].
- **후속:** 추상 클래스·인터페이스 타입으로 여러 구현 객체를 다루는 설계.
- Spring에서 인터페이스 타입으로 구현체를 다루는 설명은 후속 확장이며, 직접 수업 근거는 음료 배열·`instanceof`·다운캐스팅이다.

## 자주 헷갈리는 점

- 업캐스팅은 안전하지만, 부모 타입으로 보이는 동안 자식 전용 메서드는 바로 호출할 수 없다.
- 다운캐스팅은 실제 객체 타입이 맞을 때만 안전하다.
- `instanceof`는 “이 참조가 실제로 해당 타입 객체를 가리키는가”를 확인하는 도구다.
- 업캐스팅은 객체 자체를 부모 객체로 바꾸는 것이 아니라 같은 객체를 부모 타입 관점으로 참조하는 것이다.
- 호출 가능한 멤버는 컴파일 시 참조 타입이 제한하지만, 오버라이딩된 메서드의 실제 구현은 런타임 객체 타입에 따라 선택된다.

## 관련 개념

- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
