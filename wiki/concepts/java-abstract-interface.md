---
title: Java 추상 클래스와 인터페이스
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---
# Java 추상 클래스와 인터페이스

## 정의

Java에서 **추상 클래스(abstract class)**와 **인터페이스(interface)**는 공통 규격을 만들고, 구체적인 구현은 하위 클래스에 맡기는 객체지향 설계 도구다.

수업에서는 `Beverage05` 추상 클래스와 `WaterAdjustable`, `ShotAddable`, `MilkAddable`, `FoamAddable` 인터페이스를 음료 주문 예제로 배웠다.

## 왜 중요한가

추상 클래스와 인터페이스는 “공통 틀은 공유하고, 세부 구현은 각 클래스가 맡는” 구조를 만든다. 이후 Spring의 interface 기반 Service/Repository 설계와 다형성 이해에 계속 연결된다.

## 추상 클래스 핵심

추상 메서드는 선언만 있고 구현이 없는 메서드다.

```java
public abstract void drink();
```

추상 클래스를 상속받은 일반 클래스는 이 추상 메서드를 반드시 구현해야 한다.

```java
public class Americano05 extends Beverage05 {
    @Override
    public void drink() {
        System.out.println("아메리카노를 마십니다.");
    }
}
```

## 부모 타입 배열과 다형성

부모 타입 배열에는 여러 자식 객체를 함께 담을 수 있다.

```java
Beverage05[] orderList = {
    new Americano05("아메리카노", 4000.0, 200),
    new Espresso05("에스프레소", 3000.0, 1)
};
```

변수 타입은 `Beverage05`여도 실제 객체가 가진 `drink()` 구현이 실행된다.

## 분리된 하위 주제

- [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]] — 기능별 인터페이스, `implements`, `instanceof`, 다운캐스팅
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]] — 둘 중 무엇을 쓸지 비교
- [[concepts/java-memory-static-final|Java 메모리, static, final]] — `static`, `final`의 별도 정리

## 자주 헷갈리는 점

- 추상 클래스는 객체를 직접 만들 수 없다.
- 추상 클래스와 인터페이스는 둘 다 구현 강제성을 줄 수 있지만, 쓰임새가 다르다.
- 인터페이스는 “물 조절 가능”, “샷 추가 가능”처럼 기능 단위로 붙이기 좋다.
- 부모 타입 변수에서는 자식 전용 메서드가 바로 보이지 않는다.

## 관련 페이지

- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
