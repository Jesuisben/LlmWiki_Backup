---
title: Java 메서드, 생성자, this, 오버로딩
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---
# Java 메서드, 생성자, this, 오버로딩

## 메서드와 반환 타입

메서드는 객체가 할 수 있는 동작이다.

```java
반환타입 메소드이름(매개변수리스트) {
    내가 하고자 하는 일;
    return 반환할값;
}
```

수업에서는 `plus5` 예시로 매개변수와 반환값을 이해했다.

```java
int plus5(int x) {
    int result = x + 5;
    return result;
}
```

호출하는 쪽에서는 반환값을 변수에 받을 수 있다.

```java
int su = 3;
int result = shin.plus5(su);
```

반환할 값이 없으면 `void`를 쓴다.

```java
void display() {
    System.out.println("상품 : " + name);
    System.out.println("단가 : " + price);
    System.out.println("입고 : " + inputdate);
}
```

원본 노트에서는 `void`를 “응대하지 않는, 대답하지 않는” 것으로 이해했다. 즉 메서드가 일을 하긴 하지만 호출한 곳에 결과값을 돌려주지는 않는다는 뜻이다.

## 접근 지정자와 캡슐화

수업 후반에는 접근 지정자와 `private` 필드를 다뤘다.

```java
String name;
private int price;
String inputdate;
```

`private` 필드는 다른 클래스에서 직접 접근할 수 없다. 그래서 getter/setter 메서드를 사용한다.

```java
public int getPrice() {
    return price;
}

public void setPrice(int _price) {
    price = _price;
}
```

이 방식은 **캡슐화(encapsulation)**의 시작이다. 필드를 무조건 공개하지 않고, public 메서드를 통해 읽고 쓰게 한다.

수업에서는 통장 잔액 비유로 이해했다.

- 잔액 조회: getter
- 입금/출금으로 잔액 변경: setter

Java에서는 보통 필드를 `private`으로 만들고 getter/setter를 통해 접근한다.

## 생성자

생성자는 객체 생성 시 딱 한 번 호출되는 특수한 메서드다.

```java
Product03 shin = new Product03();
```

생성자의 목적은 멤버 변수 초기화다.

```java
public Product03(String name, int price, String inputdate) {
    this.name = name;
    this.price = price;
    this.inputdate = inputdate;
}
```

생성자와 일반 메서드의 차이는 다음과 같다.

| 구분 | 생성자 | 메서드 |
|---|---|---|
| 호출 시점 | 객체 생성 시 | 원하는 시점 |
| 호출 횟수 | 객체 생성마다 1번 | 여러 번 가능 |
| 이름 | 클래스 이름과 같음 | 자유롭게 정함 |
| 반환 타입 | 없음, `void`도 쓰지 않음 | 반드시 명시 |
| 목적 | 초기화 | 동작 수행 |

## `this` 키워드

생성자의 매개변수 이름과 멤버 변수 이름이 같으면 구분이 필요하다.

```java
public Product03(String name, int price, String inputdate) {
    this.name = name;
    this.price = price;
    this.inputdate = inputdate;
}
```

`this.name`은 “이 객체가 가진 멤버 변수 `name`”을 뜻한다. 오른쪽의 `name`은 생성자로 들어온 매개변수다.

원본 노트에서는 매개변수가 생성자 구문을 지나면 사라지기 때문에, 그 값을 객체의 멤버 변수에 옮겨 담아야 한다고 이해했다.

## 오버로딩

오버로딩(overloading)은 한 클래스 안에서 이름은 같지만 매개변수의 개수나 타입이 다른 메서드/생성자를 여러 개 만드는 것이다.

```java
public Product03() {
    System.out.println("하하하");
}

public Product03(String name, int price, String inputdate) {
    this.name = name;
    this.price = price;
    this.inputdate = inputdate;
}

public Product03(String name, String inputdate) {
    this.name = name;
    this.inputdate = inputdate;
}
```

오버로딩의 조건은 다음이다.

- 이름은 같아도 된다.
- 매개변수의 개수 또는 타입이 달라야 한다.
- 매개변수 이름만 다른 것은 오버로딩이 아니다.

수업에서는 “더하기를 여러 이름으로 만들지 말고 `add` 하나로 통일하자”는 식으로 목적을 이해했다.

## 관련 페이지

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]

## 출처

- `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
