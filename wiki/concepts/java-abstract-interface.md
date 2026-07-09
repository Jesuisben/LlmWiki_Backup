---
title: Java 추상 클래스와 인터페이스
created: 2026-07-02
updated: 2026-07-03
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
public abstract class Beverage {
    public abstract void drink();
}
```

- 직접 객체 생성 불가
- 필드와 일반 메서드를 가질 수 있음
- 추상 메서드는 하위 클래스가 구현해야 함

### 인터페이스

```java
public interface Cookable {
    void cook();
}
```

- 기능 규격 중심
- 클래스는 여러 인터페이스를 `implements`할 수 있음
- Java의 단일 클래스 상속 한계를 기능 조합으로 보완한다.

## 수업 예시

[[summaries/2026-03-12-java-abstract-interface-static|2026-03-12]]에는 음료/가게 예제에서 추상 메서드, 인터페이스, 여러 기능 구현을 함께 다뤘다.

## 자주 헷갈리는 점

- 추상 클래스는 “부모로서 공통 상태와 기본 구현”이 필요할 때 적합하다.
- 인터페이스는 “이 기능을 할 수 있다”는 약속을 여러 클래스에 붙이고 싶을 때 적합하다.
- Java 클래스는 하나만 상속하지만, 인터페이스는 여러 개 구현할 수 있다.

## 관련 개념

- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
