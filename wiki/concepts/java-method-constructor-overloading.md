---
title: Java 메서드, 생성자, this, 오버로딩
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 메서드, 생성자, this, 오버로딩

## 정의

메서드는 객체의 동작을 담은 실행 블록이고, 생성자는 객체 생성 시 필드를 초기화하는 특수한 블록이다. 오버로딩은 같은 이름을 매개변수 차이로 여러 번 정의하는 문법이다.

## 왜 중요한가

클래스가 단순 데이터 묶음이 아니라 “상태와 동작을 가진 타입”이 되려면 메서드와 생성자를 이해해야 한다. 생성자와 오버로딩은 이후 Entity/DTO 객체 생성 패턴을 이해하는 데도 도움이 된다.

## 핵심 설명

### 메서드

```java
반환타입 메서드이름(매개변수목록) {
    실행문;
}
```

메서드는 값을 반환할 수도 있고, 출력처럼 작업만 수행할 수도 있다.

```java
int plus5(int x) {
    return x + 5;
}

void display() {
    System.out.println(name);
}
```

호출 인수 값이 매개변수라는 지역 이름으로 전달되고, 반환형이 있는 메서드는 `return` 결과가 호출식의 값이 된다. `void` 메서드는 동작은 수행하지만 호출 결과를 값처럼 저장할 수 없다.

### 생성자

```java
public Product03(String name, int price) {
    this.name = name;
    this.price = price;
}
```

- 클래스 이름과 같다.
- 반환 타입이 없다.
- `new`로 객체를 만들 때 한 번 호출된다.
- 개발자가 생성자를 만들면 자동 기본 생성자는 사라진다.

### `this`

`this`는 현재 객체 자신을 가리킨다. 필드명과 매개변수명이 같을 때 `this.name`처럼 필드를 명확히 구분한다.

### 오버로딩

```java
Product03() { }
Product03(String name) { }
Product03(String name, int price) { }
```

같은 이름이라도 매개변수 개수·타입·순서가 다르면 여러 생성자/메서드를 만들 수 있다.

## 수업 실행 흐름

1. 호출자가 `new Product03("신라면", 100, "2026/03/01")`로 값을 전달한다.
2. 같은 구조의 생성자 매개변수가 값을 받는다.
3. `this.name = name`처럼 현재 객체 필드에 초기값을 저장한다.
4. 두 매개변수 생성자와 세 매개변수 생성자를 함께 두면 호출 인수에 따라 알맞은 오버로딩이 선택된다.
5. 생성된 객체는 객체 배열에 들어가고 `display()` 호출로 상태를 출력한다.

## 학습 연결과 범위

- **선행:** [[concepts/java-class-object|클래스·객체·필드·메서드]].
- **후속:** 부모 생성자 호출 `super(...)`와 [[comparisons/overloading-vs-overriding|오버라이딩과의 구분]].
- Entity/DTO 생성 방식과의 연결은 이후 Spring 프로젝트 관점이며, 이 수업의 직접 코드는 `Product03` 생성자와 객체 배열이다.

## 자주 헷갈리는 점

- 생성자는 메서드처럼 생겼지만 반환 타입이 없다.
- 기본 생성자는 자동으로 있는 것처럼 보이지만, 매개변수 생성자를 직접 만들면 필요 시 기본 생성자도 직접 작성해야 한다.
- 오버로딩은 같은 클래스 안의 이름 중복 허용이고, 오버라이딩은 상속받은 메서드 재정의다.
- parameter는 메서드 선언부의 매개변수이고 argument는 호출할 때 넘기는 인수다.
- 생성자는 객체를 만들 때마다 해당 객체에 대해 호출된다. 클래스 전체에서 한 번만 실행되는 블록이 아니다.
- 기본 생성자는 “프로그램 실행 입장권”이 아니라 매개변수 없이 객체를 만들 때 필요한 생성자다.
- 생성자는 상속되거나 오버라이딩되지 않는다.
- 반환 타입만 다르게 한 두 메서드는 오버로딩으로 인정되지 않는다.

## 관련 개념

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-access-modifier-encapsulation|Java 접근 지정자와 캡슐화]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
