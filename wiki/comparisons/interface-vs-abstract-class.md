---
title: 인터페이스 vs 추상 클래스
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md
status: growing
confidence: high
---

# 인터페이스 vs 추상 클래스

## 비교 목적

추상 클래스와 인터페이스는 둘 다 “하위 클래스가 반드시 구현해야 할 규칙”을 만들 수 있다. 그래서 처음 배울 때 둘의 차이가 헷갈리기 쉽다.

2026-03-12 수업에서는 카페 음료 예제로 이 차이를 배웠다.

- 추상 클래스: `Beverage05`
- 인터페이스: `WaterAdjustable`, `ShotAddable`, `MilkAddable`, `FoamAddable`

## 한눈에 보기

| 항목 | 추상 클래스 | 인터페이스 |
|---|---|---|
| 핵심 의미 | 공통 부모 클래스 | 기능 규격 |
| 키워드 | `abstract class` | `interface` |
| 연결 방식 | `extends` | `implements` |
| 다중 적용 | 클래스 상속은 1개만 | 여러 인터페이스 구현 가능 |
| 필드/생성자 | 공통 필드와 생성자 사용 가능 | 주로 기능 메서드 규격 |
| 수업 예시 | `Beverage05` | `WaterAdjustable`, `ShotAddable` |

## 추상 클래스는 “공통 뼈대”에 가깝다

`Beverage05`는 모든 음료의 공통 부모 역할을 했다.

```java
public abstract class Beverage05 {
    private String name;
    private double price;

    public abstract void drink();

    public Beverage05(String name, double price) {
        this.name = name;
        this.price = price;
    }
}
```

여기에는 음료 이름, 가격, 생성자, `toString()`, `getName()` 같은 공통 요소가 들어갈 수 있다. 동시에 `drink()`처럼 모든 음료가 반드시 구현해야 할 추상 메서드도 둘 수 있다.

## 인터페이스는 “기능 규격”에 가깝다

인터페이스는 어떤 기능을 할 수 있다는 약속이다.

```java
public interface WaterAdjustable {
    void adjustWater(double amount);
}
```

```java
public interface ShotAddable {
    void addShot(int count);
}
```

아메리카노는 물 조절 기능이 필요하고, 에스프레소는 샷 추가 기능이 필요하다. 이런 기능을 클래스 계층 전체에 넣기보다 인터페이스로 분리하면 필요한 클래스에만 붙일 수 있다.

## 같이 쓰는 예시

```java
public class Americano05 extends Beverage05 implements WaterAdjustable {
    @Override
    public void drink() {
        // 아메리카노 마시기 구현
    }

    @Override
    public void adjustWater(double amount) {
        // 물 조절 구현
    }
}
```

`Americano05`는 다음 두 가지 의미를 가진다.

- `Beverage05`를 상속받았으므로 음료다.
- `WaterAdjustable`을 구현했으므로 물 조절이 가능하다.

여러 기능을 동시에 붙일 수도 있다.

```java
public class SpecialCoffee05 extends Beverage05
        implements WaterAdjustable, ShotAddable, MilkAddable {
}
```

## 언제 무엇을 쓰는가

| 상황 | 선택 |
|---|---|
| 여러 클래스가 공통 필드/생성자/일반 메서드를 공유해야 한다 | 추상 클래스 |
| 모든 자식이 반드시 구현해야 할 대표 동작이 있다 | 추상 클래스 또는 인터페이스 |
| 기능을 선택적으로 여러 클래스에 붙이고 싶다 | 인터페이스 |
| 한 클래스에 여러 기능 규격을 동시에 붙이고 싶다 | 인터페이스 |
| “이것은 무엇인가” 관계를 표현하고 싶다 | 추상 클래스/상속 |
| “이것은 무엇을 할 수 있는가”를 표현하고 싶다 | 인터페이스 |

## 헷갈리기 쉬운 포인트

### 둘 다 추상 메서드를 가질 수 있다

그래서 “추상 메서드가 있으면 무조건 추상 클래스”라고 외우면 부족하다. 인터페이스의 메서드도 기본적으로 구현을 강제하는 규격이다.

### 클래스 상속은 하나만, 인터페이스는 여러 개

Java에서 한 클래스는 부모 클래스를 하나만 상속받는다. 하지만 인터페이스는 여러 개 구현할 수 있다.

### 카페 예제로 기억하기

- `Beverage05`: 모든 음료의 공통 뼈대
- `drink()`: 모든 음료가 해야 하는 기본 동작
- `WaterAdjustable`: 물 조절 기능
- `ShotAddable`: 샷 추가 기능
- `MilkAddable`: 우유 변경 기능
- `FoamAddable`: 거품 추가 기능

즉 “음료다”는 상속, “무엇을 조절할 수 있다”는 인터페이스로 이해하면 좋다.

## 관련 페이지

- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[summaries/2026-03-12-java-abstract-interface-static|2026-03-12 Java 추상 클래스, 인터페이스, static/final]]

## 출처

- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
