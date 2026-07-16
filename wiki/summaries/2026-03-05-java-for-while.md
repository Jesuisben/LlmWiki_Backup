---
title: 2026-03-05 Java for문과 while문
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.03.05(목)/2026.03.05(목).md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-05 Java for문과 while문

## 한 줄 요약

`for`와 `while` 반복문을 이용해 1부터 10까지 합계, 홀수/짝수 합계, 반복 조건을 직접 계산했다.

## 커리큘럼 위치

- [[summaries/2026-03-04-java-control-flow|조건문]]에 이어 제어문 중 반복문을 배운 날이다.
- 다음날 [[summaries/2026-03-06-java-while-array|무한 while, Scanner, 배열]]에서 입력 반복과 배열 처리로 확장된다.

## 배운 내용

- `for(초기식; 조건식; 증감식)` 구조
- 제어변수 `i`, 누적 변수 `total`, 초기화의 의미
- `while(조건식)` 구조와 초기식/증감식이 빠지면 무한 반복이 될 수 있다는 점
- 반복문 안에서 `if`를 함께 사용해 홀수/짝수를 나누는 방식

## 핵심 실습 / 예제

- `total = 0`에서 시작해 `i = 1`부터 `10`까지 `total += i`를 반복하고 `55`를 출력했다. 이 실습으로 **초기화 → 조건 검사 → 누적 → 증감 → 종료** 순서를 확인했다.
- 1부터 100까지 3씩 증가한 합계는 `1717`, 97부터 2까지 5씩 감소한 합계는 `990`이 나오는 것을 `for`와 `while`로 각각 확인했다.
- 홀수/짝수 합계는 두 개의 `for`로 따로 계산하는 방식과, 하나의 `for` 안에서 `i % 2`를 `if`로 판정해 `odd`·`even`에 나누어 누적하는 방식을 비교했다.

## 헷갈린 점 / 질문

- `for`의 세미콜론 위치가 중요하다.
- 반복문 안에서 선언한 제어변수는 반복문이 끝나면 사용할 수 없다.
- 누적 변수는 재사용 전에 0 등으로 다시 초기화해야 이전 계산 결과가 섞이지 않는다.

## 관련 페이지

- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[summaries/2026-03-06-java-while-array|2026-03-06 Java 무한 while과 배열]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.05(목)/2026.03.05(목).md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
