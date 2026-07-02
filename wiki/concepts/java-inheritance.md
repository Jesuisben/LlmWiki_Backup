---
title: Java 상속
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---
# Java 상속

## 정의

Java의 **상속(inheritance)**은 기존 클래스의 공통 속성과 동작을 부모 클래스에 두고, 자식 클래스가 그것을 물려받아 확장하는 객체지향 문법이다.

수업에서는 `Beverage03`/`Beverage04`를 부모 클래스로 두고 `Americano03`, `Espresso03`, `Latte03`가 이를 `extends`하는 음료 예제로 배웠다.

## 왜 중요한가

상속은 중복 코드를 줄이고 공통 규칙을 한 곳에 모으기 위해 사용한다. 이후 [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]], 다형성, Spring의 계층 구조 이해로 이어진다.

## 핵심 흐름

- 공통 필드와 메서드는 부모 클래스에 둔다.
- 자식 클래스는 자기에게만 필요한 필드와 동작을 추가한다.
- 부모의 `private` 필드는 자식도 직접 접근할 수 없으므로 getter/setter, `protected`, 생성자 전달을 사용한다.
- 자식 생성자에서는 `super(...)`로 부모 생성자를 먼저 호출한다.

## 대표 예시

```java
public class Americano03 extends Beverage03 {
    private double waterAmount;

    public Americano03(String name, double price, double waterAmount) {
        super(name, price);
        this.waterAmount = waterAmount;
    }
}
```

## 분리된 하위 주제

- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]] — 업캐스팅, 다운캐스팅, `instanceof`, 오버라이딩

## 자주 헷갈리는 점

- 상속은 부모 코드가 자식 파일에 복사되는 것이 아니라 관계를 맺는 것이다.
- `private`은 상속되어도 자식 코드에서 직접 접근할 수 없다.
- 부모 생성자는 자식 객체의 부모 부분을 초기화하기 위해 먼저 호출된다.

## 관련 페이지

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]

## 출처

- `raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
