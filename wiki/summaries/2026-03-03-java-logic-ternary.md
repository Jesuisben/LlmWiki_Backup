---
title: 2026-03-03 Java 논리 연산자와 조건 연산자
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md
  - raw/Study/1. Java/2026.03.03(화)/1번 문제.png
  - raw/Study/1. Java/2026.03.03(화)/2번 문제.png
  - raw/Study/1. Java/2026.03.03(화)/3번 문제.png
  - raw/Study/1. Java/2026.03.03(화)/연산자 마무리 문제.png
  - raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-03 Java 논리 연산자와 조건 연산자

## 한 줄 요약

산술·증감 연산자 복습 뒤 비교, 논리, 부정, 삼항 연산자를 배우며 “계산”에서 “판단”으로 넘어갔다.

## 커리큘럼 위치

- [[summaries/2026-02-27-java-basic-types-operators|기본 연산자]]를 조건 판단의 재료로 확장한 날이다.
- 다음날 [[summaries/2026-03-04-java-control-flow|if/switch 제어문]]에서 실제 실행 흐름을 나누는 문법으로 이어진다.

## 배운 내용

- 연산자 우선순위: 단항 → 산술 → 관계 → 비트 → 논리 → 조건 → 대입 순으로 큰 흐름을 확인했다.
- 관계/비교 연산자: `<`, `<=`, `>`, `>=`, `==`, `!=`
- 논리 연산자: `&&`, `||`
- 부정 연산자: `!`
- 조건 연산자/삼항 연산자: `조건식 ? 참일 때 값 : 거짓일 때 값`
- 변수 타입은 한 번 선언하면 바꿀 수 없다는 점을 강조했다.

## 핵심 실습 / 예제

- 두 숫자 중 큰 수 고르기: `x >= y ? x : y`
- 홀짝 판별: `(x % 2) == 0 ? "짝수" : "홀수"`
- 문제 이미지의 마무리 문제: 복합 대입 연산자는 값을 덮어쓰는 것이 아니라 기존 값에 누적 계산해 다시 대입한다. 문자열과 숫자의 `+`는 덧셈 또는 문자열 연결로 다르게 해석된다.

## 헷갈린 점 / 질문

- `=`는 대입이고 `==`는 비교다.
- 숫자 비교 결과와 논리 연산 결과는 `boolean`이다.
- 삼항 연산자의 `참일 때 값`과 `거짓일 때 값`은 최종적으로 같은 변수에 들어가므로 타입 호환성을 생각해야 한다.

## 관련 페이지

- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]

## 출처

- `raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md`
- `raw/Study/1. Java/2026.03.03(화)/연산자 마무리 문제.png`
- `raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
