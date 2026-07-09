---
title: Java 메모리, static, final
created: 2026-07-02
updated: 2026-07-03
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
private static int coffeeCount;
```

### `final`

`final`은 변경을 막는 키워드다.

- 변수: 한 번 대입 후 변경 불가, 상수처럼 사용
- 메서드: 오버라이딩 불가
- 클래스: 상속 불가

## 수업 예시

[[summaries/2026-03-12-java-abstract-interface-static|2026-03-12]]에는 가게 이름이나 커피 잔수처럼 여러 객체가 공유해야 하는 값을 `static`으로 두는 흐름이 등장했다. 숙제에서는 static/method area, stack, heap 차이를 조사했다.

## 자주 헷갈리는 점

- `static`은 “편하게 아무 데서나 쓰는 것”이 아니라 “객체가 아니라 클래스에 속한다”는 의미다.
- `final` 변수는 상수처럼 쓰지만, 참조 자료형에서는 참조 변경과 객체 내부 상태 변경을 구분해야 한다.
- 객체마다 달라져야 하는 값은 `static`으로 두면 안 된다.

## 관련 개념

- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[concepts/java-class-object|Java 클래스와 객체]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
