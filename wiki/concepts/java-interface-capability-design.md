---
title: Java 인터페이스 기능 설계
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
status: stable
confidence: high
---

# Java 인터페이스 기능 설계

## 정의

인터페이스 기능 설계는 클래스의 부모-자식 계층과 별개로 “어떤 기능을 수행할 수 있는가”를 작은 규격으로 나누어 붙이는 방식이다.

## 왜 중요한가

상속은 “무엇인가”의 관계를 표현하는 데 좋지만, 기능은 여러 방향으로 섞일 수 있다. Java는 클래스 다중 상속을 허용하지 않으므로 여러 기능 조합에는 인터페이스가 필요하다.

## 핵심 설명

```java
public interface Iceable {
    void addIce();
}

public interface Cookable {
    void cook();
}

public class Americano extends Beverage implements Iceable {
    public void addIce() { }
}
```

이런 식으로 음료가 공통적으로 `Beverage` 계열에 속하면서도, 얼음 추가·조리·포장 같은 기능은 인터페이스로 따로 표현할 수 있다.

## 수업 예시

[[summaries/2026-03-12-java-abstract-interface-static|2026-03-12]]에는 한 개의 수퍼클래스와 여러 인터페이스를 함께 사용하는 예제가 등장했다. 이는 기능을 수평적으로 붙이는 연습이었다.

## 자주 헷갈리는 점

- 인터페이스는 “부모 클래스가 여러 개”라는 의미라기보다 “여러 기능 계약을 구현한다”는 의미로 이해하는 편이 안전하다.
- 인터페이스 타입으로 바라보면 그 인터페이스에 선언된 기능만 바로 사용할 수 있다.
- 실제 구현 클래스의 고유 기능이 필요하면 타입 확인과 형변환이 필요할 수 있다.

## 관련 개념

- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
