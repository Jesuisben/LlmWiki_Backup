---
title: Java 다형성과 참조 형변환
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
# Java 다형성과 참조 형변환

## 참조 형변환과 다형성

### UpCasting

업캐스팅(UpCasting)은 자식 객체를 부모 타입 변수에 담는 것이다.

```java
Beverage04 beverage01 = new Americano04("아메리카노", 4000.0, 250.0);
```

수업 노트에서 중요한 설명은 “본질이 바뀌는 것이 아니라 한시적으로 부모 타입처럼 보이는 것”이다.

- 실제 객체: `Americano04`
- 참조 타입: `Beverage04`
- 사용할 수 있는 메서드: 부모 타입에서 보이는 메서드 중심

업캐스팅은 부모 입장에서 여러 자식 객체를 한꺼번에 관리하기 위해 사용한다.

```java
Beverage04[] beverage = {
    beverage01,
    new Espresso04("마이뿌레소", 2000.0, 1),
    new Latte04("바나나 라떼", 7000.0, "바나나 우유")
};
```

이 배열은 `Americano04`, `Espresso04`, `Latte04`를 모두 `Beverage04` 타입으로 담는다.

### DownCasting

다운캐스팅(DownCasting)은 부모 타입으로 보고 있던 객체를 다시 자식 타입으로 보는 것이다.

```java
Americano04 coffee = (Americano04) beverage01;
coffee.sipAmericano();
```

다운캐스팅은 명시적으로 `(Americano04)`처럼 타입을 적어야 한다.

## `instanceof`

업캐스팅된 배열에서 원래 어떤 자식 객체였는지 확인할 때 `instanceof`를 사용한다.

```java
if (beverage[i] instanceof Americano04) {
    Americano04 ameri = (Americano04) beverage[i];
    ameri.sipAmericano();
} else if (beverage[i] instanceof Espresso04) {
    Espresso04 espre = (Espresso04) beverage[i];
    espre.drinkEspresso();
}
```

원본 노트에서는 `instanceof`를 “너 고향이 어디니?” 같은 느낌으로 이해했다. 즉 이 객체가 처음 어떤 클래스에서 만들어졌는지 확인하는 용도다.

## 오버라이딩과 `toString()`

오버라이딩(overriding)은 부모에게서 물려받은 메서드를 자식 클래스 상황에 맞게 다시 작성하는 것이다.

`System.out.println(객체)`를 하면 내부적으로 `toString()`이 호출된다. 수업에서는 부모와 자식에서 `toString()`을 연속적으로 오버라이딩했다.

```java
@Override
public String toString() {
    String imsi = "상품명 : " + name + ", 단가 : " + price;
    return imsi;
}
```

자식 클래스에서는 부모의 결과에 자기 필드를 덧붙일 수 있다.

```java
@Override
public String toString() {
    String imsi = ", 물의 양 : " + waterAmount;
    return super.toString() + imsi;
}
```

## 숙제에서 보강된 상속 관점

숙제에서는 상속을 “부모 역할의 상위 객체가 자식 역할의 하위 객체에게 필드와 메서드를 물려주어 재사용하게 하는 것”으로 정리했다. 핵심 목적은 두 가지다.

1. **코드 재사용성**: 공통 코드를 부모에 두고 자식은 차이만 추가한다.
2. **유지보수성**: 공통 개념이 바뀌면 부모 쪽 수정이 여러 자식에게 영향을 준다.

예를 들어 “빵”이라는 상위 개념이 바뀌면 소보로빵, 단팥빵, 크림빵을 각각 다시 정의하기보다 부모 개념을 먼저 고치는 식이다. 수업의 음료 예제에서는 `Beverage`가 이 공통 부모 역할을 한다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

### 부모 생성자가 먼저 호출되는 이유

자식 객체가 생성될 때는 부모 부분이 먼저 준비되어야 한다. 그래서 자식 생성자 첫 줄에는 보이지 않는 `super();`가 있고, 필요하면 `super(name, price)`처럼 명시적으로 부모 생성자를 호출한다.

부모에 매개변수 있는 생성자를 직접 만들면 Java가 기본 생성자 `Beverage03()`을 자동으로 만들어 주지 않는다. 이때 다른 자식 생성자의 숨은 `super();`가 호출할 부모 기본 생성자를 찾지 못해 오류가 날 수 있다. 해결은 부모 기본 생성자를 직접 만들거나, 자식 생성자에서 부모의 매개변수 생성자에 맞게 `super(...)`를 호출하는 것이다. ^[raw/Study/1. Java/Java 총정리/Java 총정리.md]

### final 메서드

`final` 메서드는 자식 클래스에서 더 이상 오버라이딩할 수 없는 메서드다. 보안상 바뀌면 안 되는 기능이나, 모든 자식이 동일하게 유지해야 하는 핵심 동작에 사용할 수 있다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

## 관련 페이지

- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]

## 출처

- `raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
