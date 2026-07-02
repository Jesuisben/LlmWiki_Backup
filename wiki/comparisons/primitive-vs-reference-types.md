---
title: 기본 자료형 vs 참조 자료형
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [java]
sources:
  - raw/Study/1. Java/2026.02.27(금)/2026.02.27(금).md
  - raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---

# 기본 자료형 vs 참조 자료형

## 비교 목적

Java 입문에서 가장 먼저 헷갈리는 구분 중 하나는 “변수에 값 자체가 들어 있는가, 객체를 가리키는 참조값이 들어 있는가”이다. 이 차이를 알아야 `String`, 배열, 클래스 객체, `null`, `new`, heap/stack 설명이 연결된다.

## 한눈에 보기

| 항목 | 기본 자료형(primitive type) | 참조 자료형(reference type) |
|---|---|---|
| 대표 예시 | `int`, `double`, `char`, `boolean` | `String`, 배열, `Scanner`, 사용자가 만든 클래스 객체 |
| 변수에 담기는 것 | 값 자체 | 객체/배열을 가리키는 참조값 |
| 생성 방식 | 리터럴 대입이 중심 | 대체로 `new` 또는 문자열/배열 초기화 |
| `null` 가능 여부 | 불가능 | 가능 |
| 기본값 예시 | `int`는 0, `double`은 0.0, `boolean`은 false | 클래스/String/배열은 null |

## 수업에서 본 예시

```java
int age = 29;
double average = 74.6666666666666;
boolean result = true;
char ch = 'A';
```

반면 `Scanner`, 배열, 클래스 객체는 참조 자료형이다.

```java
Scanner scan = new Scanner(System.in);
int[] scores = new int[3];
Product shin = new Product();
```

`scan`, `scores`, `shin`에는 객체/배열의 실제 내용이 통째로 들어 있다기보다, heap에 만들어진 대상을 찾아갈 수 있는 참조값이 들어 있다고 이해하면 된다. ^[raw/Study/1. Java/숙제/클래스 숙제 완료.md]

## Stack/Heap 관점

- stack: 메서드 실행 중 쓰이는 지역 변수, 임시 정보가 저장되는 영역으로 이해했다.
- heap: `new`로 만들어진 객체와 배열의 실제 데이터가 저장되는 영역으로 이해했다.
- 참조 변수는 객체의 실제 데이터가 아니라 heap 객체를 가리키는 주소/참조값을 가진다.

## `String`은 자주 쓰이지만 기본 자료형이 아니다

`String name = "이현민";`처럼 너무 자주 쓰여서 기본 자료형처럼 보이지만, `String`은 클래스 기반 참조 자료형이다. 수업 노트에서도 `String`, `Scanner`, `random` 같은 단어를 “타입을 표현하면서 기능도 가지고 있음”으로 설명했다. ^[raw/Study/1. Java/Java 총정리/Java 총정리.md]

## 헷갈리기 쉬운 포인트

`int[]`는 정수들을 담는 배열이지만, 배열이라는 상자 자체는 `new int[3]`으로 만들어지는 객체에 가깝다. 또한 참조 자료형은 `null`일 수 있다. 아직 실제 객체를 가리키지 않는 상태라는 뜻이다.

## 관련 페이지

- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]

## 출처

- `raw/Study/1. Java/2026.02.27(금)/2026.02.27(금).md`
- `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
