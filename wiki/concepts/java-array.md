---
title: Java 배열
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 배열

## 정의

배열(array)은 같은 타입의 여러 값을 하나의 이름으로 묶어 저장하는 고정 크기 자료구조다.

## 왜 중요한가

점수 여러 개, 이름 여러 개, 상품 객체 여러 개처럼 반복 처리할 값들을 개별 변수로 하나씩 만들면 관리가 어렵다. 배열은 반복문과 함께 여러 값을 순서대로 다룰 수 있게 해준다.

## 핵심 설명

배열의 3요소는 이름, 타입, 요소 개수다.

```java
int[] arr = new int[3];
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
```

- 인덱스는 0부터 시작한다.
- 요소 개수는 `arr.length`로 확인한다.
- 값이 이미 명확하면 초기화 기법을 쓴다.

```java
String[] bts = {"RM", "진", "슈가"};
```

## 객체 배열

[[summaries/2026-03-10-java-constructor-overloading-inheritance|2026-03-10]]에는 `Product[]`처럼 객체를 배열에 담는 예제가 등장했다. 이때 배열 칸에는 객체 자체가 아니라 객체를 가리키는 참조가 들어간다.

## 자주 헷갈리는 점

- `new int[3]`은 3칸을 만든다는 뜻이지, 인덱스 3번까지 쓸 수 있다는 뜻이 아니다. 사용 가능한 인덱스는 `0`, `1`, `2`다.
- 배열은 크기가 고정된다. 크기가 자주 변하는 데이터는 [[comparisons/array-vs-collection|배열 vs 컬렉션]] 기준으로 컬렉션을 고려한다.
- 향상된 for문은 전체 조회에는 편하지만, 인덱스 번호가 필요한 경우 일반 for문이 더 적합하다.

## 관련 개념

- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[comparisons/array-vs-collection|배열 vs 컬렉션]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
