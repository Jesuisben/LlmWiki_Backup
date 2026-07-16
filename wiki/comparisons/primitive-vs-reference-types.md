---
title: 기본 자료형 vs 참조 자료형
created: 2026-07-02
updated: 2026-07-15
type: comparison
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.02.26(목) - 시작/2026.02.26(목) - 시작.md
  - raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 기본 자료형 vs 참조 자료형

## 비교 목적

Java 초반에는 `char`, `String`, `int`, `double`, `boolean`을 함께 배우지만, 실제로 `String`, 배열, 객체는 기본 자료형이 아니라 참조 자료형이다. 이 구분은 stack/heap, 객체 배열, null 이해로 이어진다.

## 한눈에 보기

| 항목 | 기본 자료형 | 참조 자료형 |
|---|---|---|
| 대표 예 | `int`, `double`, `char`, `boolean` | `String`, 배열, 사용자 정의 클래스 객체 |
| 저장 관점 | 값 자체 | 객체/배열을 가리키는 참조 |
| 기본값 예 | `0`, `0.0`, `false` | `null` |
| 수업 등장 | 점수, 평균, 홀짝 판단 | 문자열, 배열, `Product` 객체 |
| 메모리 감각 | 변수 공간에 값 | 참조 변수와 heap 객체를 구분 |

## 언제 무엇을 쓰는가

1. **점수와 평균 계산:** `int` 점수와 `double` 평균처럼 산술 결과가 필요한 값은 기본 자료형으로 다룬다. 02-27 실습의 점수·평균이 이 상황이다.
2. **상품 한 개 표현:** 이름·가격·입고일과 동작을 함께 가진 상품은 `Product` 객체로 표현하고 `Product shin` 참조가 `new Product()`로 만든 객체를 가리키게 한다.
3. **여러 값 묶기:** `int[]`와 `Product03[]` 모두 참조 자료형이다. 전자는 기본값 배열을, 후자는 객체 참조 배열을 가리킨다는 차이가 있다.

## 관련 수업 예시

`Product03[] itemlist = new Product03[2]`만 실행하면 객체 두 개가 생기는 것이 아니라 `null` 참조 두 칸이 생긴다. 각 칸에 `new Product03(...)`를 넣어야 실제 상품 객체와 연결된다. 이 흐름이 “값 자체”와 “대상을 가리키는 참조”를 구분하는 대표 수업 예시다.

## 헷갈리기 쉬운 포인트

- `String`은 수업 초반에는 문자열형처럼 소개되지만 Java의 primitive type은 아니다.
- 표의 기본값은 **필드나 배열 요소의 자동 기본값** 관점이다. 메서드 안의 지역 변수는 기본값이 자동 배정되지 않아 사용 전에 직접 초기화해야 한다.
- 배열 변수는 배열 전체를 직접 담는 것이 아니라 배열 객체를 가리킨다.
- 객체 변수도 객체 자체가 아니라 heap에 생성된 객체의 참조를 담는다.

## 관련 페이지

- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]

## 출처

- `raw/KoreaICT/1. Java/2026.02.26(목) - 시작/2026.02.26(목) - 시작.md`
- `raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
