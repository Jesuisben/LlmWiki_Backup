---
title: Java 기본 자료형
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.02.26(목)/2026.02.26(목).md
  - raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 기본 자료형

## 정의

Java 기본 자료형(primitive type)은 값 자체를 변수 공간에 저장하는 타입이다. 수업에서는 `char`, `int`, `double`, `boolean`을 중심으로 배우고, 문자열 처리를 위해 `String`도 함께 다뤘다.

## 왜 중요한가

변수 타입은 어떤 값을 담을 수 있는지, 어떤 연산이 가능한지, 계산 결과가 어떻게 나오는지를 결정한다. 예를 들어 `int / int`는 정수 나눗셈이 되고, 평균처럼 소수점이 필요한 계산에는 `double`을 고려해야 한다.

## 핵심 설명

| 수업에서 다룬 타입 | 의미 | 예시 | 주의 |
|---|---|---|---|
| `char` | 문자 1개 | `'A'` | 작은따옴표 사용 |
| `String` | 문자열 | `"hello"` | 기본형이 아니라 참조 자료형 |
| `int` | 정수 | `10` | 정수 나눗셈 주의 |
| `double` | 실수 | `41.5` | 평균·소수 계산에 사용 |
| `boolean` | 참/거짓 | `true`, `false` | 비교/논리 연산 결과 |

## 수업 예시

- [[summaries/2026-02-27-java-basic-types-operators|2026-02-27]] 문제 이미지에서는 이름, 국어/영어 점수, 평균을 출력하면서 `String`, `int`, `double`이 함께 등장했다.
- [[summaries/2026-03-03-java-logic-ternary|2026-03-03]]에는 비교 연산의 결과가 `boolean`이 된다는 흐름이 이어졌다.

## 자주 헷갈리는 점

- `String`은 교안과 노트에서 문자열형처럼 함께 배우지만, Java의 8개 기본 자료형에는 속하지 않는다.
- 변수 타입은 선언 후 바꿀 수 없다. `int age`로 선언한 변수를 다시 `String age`로 재정의할 수 없다.
- 문자 `char`는 한 글자, 문자열 `String`은 0개 이상의 문자 묶음이다.

## 관련 개념

- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]
- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-class-object|Java 클래스와 객체]]

## 출처

- `raw/KoreaICT/1. Java/2026.02.26(목)/2026.02.26(목).md`
- `raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
