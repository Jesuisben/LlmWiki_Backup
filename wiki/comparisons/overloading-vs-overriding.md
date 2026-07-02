---
title: 오버로딩 vs 오버라이딩
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [java]
sources:
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---

# 오버로딩 vs 오버라이딩

## 비교 목적

오버로딩(overloading)과 오버라이딩(overriding)은 이름이 비슷하지만 완전히 다른 상황에서 쓰인다. 하나는 **같은 이름을 여러 방식으로 정의**하는 것이고, 다른 하나는 **부모에게 받은 메서드를 자식에 맞게 재정의**하는 것이다.

## 한눈에 보기

| 항목 | 오버로딩 | 오버라이딩 |
|---|---|---|
| 핵심 의미 | 같은 이름, 다른 매개변수 | 부모 메서드를 자식이 재정의 |
| 발생 위치 | 주로 같은 클래스 안 | 상속 관계의 부모/자식 사이 |
| 조건 | 이름 같고 매개변수 개수 또는 타입이 다름 | 부모 메서드와 선언 형태가 맞아야 함 |
| 수업 예시 | `Product03()` / `Product03(String, int, String)` | `display()`, `toString()`, `drink()` 재정의 |
| 목적 | 이름을 통일해 사용 편의성 증가 | 자식 클래스 상황에 맞는 동작 구현 |

## 오버로딩

```java
public Product03() {}
public Product03(String name, int price, String inputdate) {}
public Product03(String name, String inputdate) {}
```

수업 노트에서는 “더하기는 `add`라는 이름으로 통일하자”처럼, 비슷한 기능의 이름을 여러 개 만들지 않아도 되게 하는 장점으로 이해했다. ^[raw/Study/1. Java/Java 총정리/Java 총정리.md]

## 오버라이딩

```java
@Override
public void display() {
    System.out.println("안내견 여부 : " + guide);
    super.display();
}
```

부모의 기능이 대부분 맞지만 자식에게 맞게 일부를 바꾸거나 추가해야 할 때 사용한다. 숙제에서는 “부모의 기능이 자식에게 100가지 맞아도 1가지는 맞지 않을 수 있기 때문”이라고 정리했다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

## 언제 무엇을 쓰는가

| 상황 | 선택 |
|---|---|
| 같은 기능 이름을 유지하되 입력값 종류가 다름 | 오버로딩 |
| 생성자를 여러 형태로 제공하고 싶음 | 오버로딩 |
| 부모 메서드의 동작을 자식에게 맞게 바꾸고 싶음 | 오버라이딩 |
| 추상 메서드의 구현을 자식이 채워야 함 | 오버라이딩 |
| 다형성에서 실제 객체별 동작이 달라져야 함 | 오버라이딩 |

## 헷갈리기 쉬운 포인트

매개변수 이름만 바꾸는 것은 오버로딩이 아니다. 매개변수의 개수나 타입이 달라야 한다. 오버라이딩은 상속 관계가 전제이며, `@Override`는 컴파일러에게 오버라이딩 여부를 확인시키므로 오타나 선언 실수를 잡는 데 도움이 된다.

## 관련 페이지

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
