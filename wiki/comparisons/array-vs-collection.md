---
title: 배열 vs 컬렉션
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

# 배열 vs 컬렉션

## 비교 목적

배열과 컬렉션은 모두 여러 데이터를 하나의 묶음으로 다루기 위한 도구다. 하지만 크기, 타입, 제공 기능이 다르기 때문에 언제 배열을 쓰고 언제 `List`, `Set`, `Map` 같은 컬렉션을 쓸지 구분해야 한다.

## 한눈에 보기

| 항목 | 배열(Array) | 컬렉션(Collection) |
|---|---|---|
| 크기 | 생성할 때 정하면 고정 | 데이터 양에 따라 늘고 줄 수 있음 |
| 저장 타입 | 기본 타입과 객체 모두 가능 | 객체 중심 |
| 접근 방식 | 인덱스 `arr[0]` | `add`, `get`, `put` 등 메서드 |
| 대표 예시 | `int[]`, `String[]`, `Product03[]` | `ArrayList`, `HashSet`, `HashMap` |

## 배열

```java
String[] bts = {"진", "뷔", "정국", "rm", "지민", "슈가", "제이홉"};
```

객체도 배열에 담을 수 있다.

```java
Product03[] productArray = {
    new Product03("쭈쭈바", 1500, "2025/12/25"),
    new Product03("사과", 3000, "2025/06/06")
};
```

배열은 구조가 단순해서 입문 단계에 좋지만, 한 번 만든 뒤 크기를 자유롭게 늘리기 어렵다. ^[raw/Study/1. Java/Java 총정리/Java 총정리.md]

## 컬렉션

| 유형 | 순서 | 중복 | 주요 메서드 | 구현 클래스 예시 |
|---|---|---|---|---|
| List | 있음 | 허용 | `add`, `get`, `size`, `remove`, `set` | `ArrayList`, `LinkedList` |
| Set | 없음 | 허용 안 함 | `add`, `contains`, `size`, `remove` | `HashSet`, `TreeSet` |
| Map | Key 기준 | Key 중복 불가, Value 중복 가능 | `put`, `get`, `containsKey`, `remove` | `HashMap`, `TreeMap` |

## 언제 무엇을 쓰는가

| 상황 | 선택 |
|---|---|
| 개수가 작고 고정되어 있음 | 배열 |
| 데이터가 계속 추가/삭제됨 | `List` |
| 중복이 없어야 함 | `Set` |
| 이름표/키로 값을 찾고 싶음 | `Map` |
| 게시물 목록처럼 순서가 중요함 | `List` |
| 로또 번호처럼 중복이 없어야 함 | `Set` |

## 헷갈리기 쉬운 포인트

배열은 기본 타입만 담는 도구가 아니다. 수업의 `Product03[]`, `Beverage04[]`처럼 객체 참조도 담을 수 있다. 반대로 컬렉션은 무조건 배열의 상위호환이라고만 외우면 부족하다. 데이터가 고정인지, 중복을 허용하는지, 순서가 필요한지, 키로 찾을지를 먼저 봐야 한다.

## 관련 페이지

- [[concepts/java-array|Java 배열]]
- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]

## 출처

- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
