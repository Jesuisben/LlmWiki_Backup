---
title: Java 인터페이스 기능 설계
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
# Java 인터페이스 기능 설계

## 인터페이스

인터페이스는 특정 기능을 할 수 있다는 규격을 표현한다.

수업에서는 기능별 인터페이스를 만들었다.

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

```java
public interface MilkAddable {
    void changeMilk(String milkType);
}
```

인터페이스 안의 메서드는 기본적으로 추상 메서드처럼 취급된다. 그래서 구현 클래스는 반드시 해당 메서드를 작성해야 한다.

## `extends`와 `implements`

클래스 상속은 `extends`, 인터페이스 구현은 `implements`를 사용한다.

```java
public class Americano05 extends Beverage05 implements WaterAdjustable {
}
```

한 클래스는 부모 클래스 하나만 상속받을 수 있지만, 인터페이스는 여러 개 구현할 수 있다.

```java
public class SpecialCoffee05 extends Beverage05
        implements WaterAdjustable, ShotAddable, MilkAddable {
}
```

이 예시는 스페셜커피가 음료이면서 동시에 물 조절, 샷 추가, 우유 변경 기능을 모두 가진다는 뜻이다.

## `instanceof`와 다운캐스팅

부모 타입 배열로 여러 음료를 관리하다가 특정 기능을 가진 음료만 골라 기능을 실행하려면 `instanceof`와 다운캐스팅이 필요하다.

```java
if (item instanceof Americano05) {
    ((Americano05) item).adjustWater(20);
} else if (item instanceof Espresso05) {
    ((Espresso05) item).addShot(1);
} else if (item instanceof Latte05) {
    ((Latte05) item).changeMilk("아몬드 우유");
}

item.drink();
```

여기서 `item`은 부모 타입이므로 바로 `adjustWater()`를 호출할 수 없다. 실제 타입을 확인하고 자식 타입으로 다운캐스팅한 뒤 호출한다.

## 숙제에서 보강된 추상화 관점

숙제에서는 추상 클래스가 필요한 이유를 “공통적인 특징은 모으되, 구체적인 내용은 자식에게 맡기기 위해서”라고 정리했다. 즉 추상 클래스는 완성품이라기보다 **공통 뼈대 + 구현 강제 규칙**에 가깝다.

추상 클래스를 불완전 클래스라고 부르는 이유는 실행 몸통이 없는 추상 메서드를 포함할 수 있기 때문이다.

```java
public abstract void drink();
```

이 메서드는 `{}` 구현부가 없고 세미콜론으로 끝난다. 따라서 부모가 직접 “어떻게 마실지”를 실행할 수 없고, 자식 클래스가 반드시 오버라이딩해서 완성해야 한다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

| 구분 | 구현부 `{}` | 오버라이딩 | 목적 |
|---|---:|---|---|
| 일반 메서드 | 있음 | 가능 | 공통 기능 제공 |
| final 메서드 | 있음 | 불가능 | 기능 변조 방지, 일관성 유지 |
| 추상 메서드 | 없음 | 반드시 해야 함 | 자식에게 구현 강제 |

인터페이스는 “서로 다른 클래스들에게 공통된 규칙을 적용하기 위한 것”으로 정리했다. 상속이 `A는 B다`에 가깝다면, 인터페이스는 `A는 B 기능을 할 수 있다`에 가깝다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

## 관련 페이지

- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]

## 출처

- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
