---
title: Java 메모리, static, final
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 메모리, static, final

## 정의

Java 학습에서 stack, heap, static 영역은 값과 객체가 어디에 놓이는지 이해하기 위한 메모리 관점이고, `static`과 `final`은 멤버의 소속과 변경 가능성을 제어하는 키워드다.

## 왜 중요한가

기본 자료형과 참조 자료형, 객체 배열, 클래스 변수, 상수를 이해하려면 “값 자체”, “객체”, “공유 멤버”가 서로 다르다는 감각이 필요하다.

## 핵심 설명

### stack

메서드 실행 중 생기는 지역 변수, 매개변수, 참조 변수 등이 놓이는 영역으로 이해했다. 실행이 끝나면 사라지는 임시 공간에 가깝다.

### heap

`new`로 생성한 객체가 놓이는 영역이다. 참조 변수는 stack에 있고, 실제 객체는 heap에 있다고 구분하면 객체 배열과 참조 자료형을 이해하기 쉽다.

### static 영역

클래스 자체에 속하는 멤버가 놓이는 영역으로 이해했다. 객체마다 따로 생기는 값이 아니라 클래스 차원에서 공유되는 값이다.

```java
private static int beverageCount;
```

### `final`

`final`은 변경을 막는 키워드다.

- 변수: 한 번 대입 후 변경 불가, 상수처럼 사용
- 메서드: 오버라이딩 불가
- 클래스: 상속 불가

## 수업 예시

[[summaries/2026-03-12-java-abstract-interface-static|2026-03-12]]에는 `public static final String STORE_NAME`으로 가게 이름을 상수화하고, `private static int beverageCount`를 부모 생성자에서 증가시켜 생성된 음료 수를 클래스 전체가 공유하는 흐름이 등장했다. 숙제에서는 static/method area, stack, heap 차이를 조사했다.

```java
public Beverage05(String name, double price) {
    this.name = name;
    this.price = price;
    beverageCount++;
}
```

## 학습 연결과 범위

- **Java 수업에서 직접 실행:** 클래스가 공유하는 값에 `static`을 사용하고, 변경을 막을 값·메서드·클래스에 `final`을 적용하는 흐름.
- **직접 실행 범위 보정:** 이날 중심 실습은 `static final` 상수와 static 카운터다. final 메서드·final 클래스는 숙제 조사와 Java 일반 규칙으로 구분한다.
- **숙제로 조사:** stack/heap/static(method area) 구분과 지역·인스턴스·정적 변수의 생명주기.
- **정확성 경계:** 이 페이지의 메모리 구분은 입문 수업용 모델이다. 실제 JVM 메모리 구조와 가비지 컬렉션의 세부 구현을 완전히 설명하는 사양 문서로 해석하지 않는다.
- **후속:** 객체 배열의 참조와 클래스 공용 설정을 이해한 뒤 Spring Bean·정적 유틸리티와의 차이를 공부할 기반이 된다.

## 자주 헷갈리는 점

- `static`은 “편하게 아무 데서나 쓰는 것”이 아니라 “객체가 아니라 클래스에 속한다”는 의미다.
- `final` 변수는 상수처럼 쓰지만, 참조 자료형에서는 참조 변경과 객체 내부 상태 변경을 구분해야 한다.
- 객체마다 달라져야 하는 값은 `static`으로 두면 안 된다.
- `static`을 “Java의 전역 변수 이름”으로만 이해하면 객체 소속과 클래스 소속의 차이를 놓친다.
- `final` 참조는 다른 객체를 다시 가리키는 일을 막지만, 그 객체 내부 상태까지 자동으로 불변으로 만들지는 않는다.

## 관련 개념

- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[concepts/java-class-object|Java 클래스와 객체]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
