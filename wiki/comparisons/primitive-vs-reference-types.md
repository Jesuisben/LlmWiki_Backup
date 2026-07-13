---
title: 기본 자료형 vs 참조 자료형
created: 2026-07-02
updated: 2026-07-13
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

- 숫자 계산, 참/거짓 판단처럼 값 자체가 필요한 경우 기본 자료형을 쓴다.
- 여러 글자, 여러 값 묶음, 속성과 동작이 있는 대상을 표현할 때 참조 자료형을 쓴다.

## 헷갈리기 쉬운 포인트

- `String`은 수업 초반에는 문자열형처럼 소개되지만 Java의 primitive type은 아니다.
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
