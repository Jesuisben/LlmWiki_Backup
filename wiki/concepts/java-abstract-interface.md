---
title: Java 추상 클래스와 인터페이스
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 추상 클래스와 인터페이스

## 정의

추상 클래스는 공통 상태와 일부 구현을 가진 부모 설계도이고, 인터페이스는 클래스가 반드시 제공해야 할 기능 규격이다.

## 왜 중요한가

객체지향 설계에서는 “공통으로 가져야 하는 것”과 “할 수 있어야 하는 기능”을 구분해야 한다. 수업의 음료 예제에서 추상 클래스와 인터페이스는 상속만으로 해결하기 어려운 기능 분리를 설명하는 도구였다.

## 핵심 설명

### 추상 클래스

```java
public abstract class Beverage05 {
    public abstract void drink();
}
```

- 직접 객체 생성 불가
- 필드와 일반 메서드를 가질 수 있음
- 추상 메서드는 하위 클래스가 구현해야 함

### 인터페이스

```java
public interface WaterAdjustable {
    void adjustWater(double amount);
}
```

- 기능 규격 중심
- 클래스는 여러 인터페이스를 `implements`할 수 있음
- Java의 단일 클래스 상속 한계를 기능 조합으로 보완한다.

## 수업 예시

[[summaries/2026-03-12-java-abstract-interface-static|2026-03-12]]에는 `Beverage05`가 `drink()`를 추상 메서드로 선언하고, `WaterAdjustable`, `ShotAddable`, `MilkAddable`이 물 조절·샷 추가·우유 추가/변경 기능을 각각 규격으로 분리하는 음료 예제가 등장했다. 하위 클래스는 공통 음료 상태는 상속받고, 실제로 제공하는 기능만 인터페이스로 골라 구현했다.

## 학습 연결과 범위

- **Java 수업에서 직접 학습:** 추상 클래스의 직접 생성 금지, 추상 메서드 구현 강제, 클래스 단일 상속, 여러 인터페이스 구현, 음료 기능 분리.
- **이후 확장 관점:** Spring에서 인터페이스 타입으로 구현체를 다루는 방식과 연결할 수 있지만, 이는 Java 수업의 음료 코드 다음에 배우는 응용 관점이다.
- **현대 Java 경계:** 이날 인터페이스에는 추상 기능 계약만 작성했다. 현대 Java 인터페이스는 `default`, `static`, `private` 메서드도 가질 수 있으므로 “모든 인터페이스 메서드는 언제나 구현이 없다”로 일반화하지 않는다.

## 자주 헷갈리는 점

- 추상 클래스는 “부모로서 공통 상태와 기본 구현”이 필요할 때 적합하다.
- 인터페이스는 “이 기능을 할 수 있다”는 약속을 여러 클래스에 붙이고 싶을 때 적합하다.
- Java 클래스는 하나만 상속하지만, 인터페이스는 여러 개 구현할 수 있다.
- 추상 클래스는 추상 메서드가 없어도 선언할 수 있고, 일반 필드·생성자·구현된 메서드를 가질 수 있다.

## 관련 개념

- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
