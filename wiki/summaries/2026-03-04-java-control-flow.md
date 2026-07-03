---
title: 2026-03-04 Java 제어문과 조건문
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md
  - raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-04 Java 제어문과 조건문

## 한 줄 요약

`if`, `if~else`, `else if`, `switch`로 조건에 따라 실행 흐름을 나누는 방법을 배웠다.

## 커리큘럼 위치

- 전날 배운 비교/논리/삼항 연산자의 결과를 실제 실행 분기 조건으로 사용하는 단계다.
- 다음날 [[summaries/2026-03-05-java-for-while|반복문]]과 함께 제어문 전체 구조가 완성된다.

## 배운 내용

- 제어문은 조건문/반복문/보조 제어문으로 나눌 수 있다.
- 단순 `if`: 조건이 참일 때만 실행한다.
- `if~else`: 경우의 수가 둘일 때 사용한다.
- `else if`: 점수 학점처럼 여러 구간 중 하나를 선택할 때 사용한다.
- `switch`: 특정 값에 따라 `case`를 찾아 실행하며, `break`가 없으면 아래 case까지 이어질 수 있다.

## 핵심 실습 / 예제

- 짝수/홀수 판별
- 점수에 따른 A/B/C/D/F 학점 출력
- `switch`에서 `case`, `default`, `break` 흐름 확인

## 헷갈린 점 / 질문

- `else if`는 별도 메서드가 아니라 `else` 뒤에 또 다른 `if`를 붙인 구조로 이해하면 된다.
- `switch`는 맞는 `case`를 찾은 뒤 `break`를 만날 때까지 계속 내려갈 수 있으므로, 의도하지 않은 fall-through를 조심해야 한다.
- 조건식은 최종적으로 `true`/`false`가 되어야 한다.

## 관련 페이지

- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-loop|Java 반복문]]

## 출처

- `raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md`
- `raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
