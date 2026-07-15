---
title: 2026-02-27 Java 기본 자료형과 연산자
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md
  - raw/KoreaICT/1. Java/2026.02.27(금)/1번 문제.png
  - raw/KoreaICT/1. Java/2026.02.27(금)/2번 문제.png
  - raw/KoreaICT/1. Java/2026.02.27(금)/3번 문제.png
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-02-27 Java 기본 자료형과 연산자

## 한 줄 요약

Java의 변수, `char`/`String`/`int`/`double`/`boolean`, 산술·대입·복합 대입·증감 연산자를 배우고 문제 이미지로 계산 결과 예측을 연습했다.

## 커리큘럼 위치

- 전날의 “출력하는 프로그램”에서 한 단계 나아가, 값을 저장하고 계산하는 프로그램을 만들기 시작한 날이다.
- 다음 수업 [[summaries/2026-03-03-java-logic-ternary|2026-03-03 논리 연산자와 조건 연산자]]에서 비교·논리·삼항 연산자로 확장된다.

## 배운 내용

- 변수 선언: `데이터타입 변수명;`
- 변수 대입: `변수명 = 값;`
- 동시 선언: `int age, time;`
- 주요 타입: `char`, `String`, `int`, `double`, `boolean`
- 산술 연산자: `+`, `-`, `*`, `/`, `%`
- 대입/복합 대입: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- 증감 연산자: `++`, `--`, 전위/후위 위치에 따른 실행 시점 차이

## 핵심 실습 / 예제

문제 이미지에서 확인한 대표 실습은 다음과 같다.

- `Add2.java`: `a=3`, `b=4`, `c=5`일 때 `2*a + 3*b - c = 13`을 계산해 출력한다.
- `ShowJumsu.java`: 이름, 국어 점수, 영어 점수를 출력하고 평균 `41.5`를 계산한다.
- `PlusMinus02.java`: `x++`, `--y`, `--x`, `y++`처럼 전위/후위 증감 연산이 섞인 코드의 출력 결과를 예측한다.

`PlusMinus02`에서는 한 줄을 통째로 외우지 않고 다음 순서로 값을 추적했다.

```java
int x = 3, y = 5, z;
z = x++ + --y;       // 계산 뒤 x=4, y=4, z=7
z += --x + y++;      // 계산 뒤 x=3, y=5, z=14
```

전위 증감 반영 → 현재 식 계산 → 대입 → 후위 증감 완료 순서로 표를 그리면 값 변화를 놓치기 어렵다.

## 헷갈린 점 / 질문

- `/`는 정수끼리 계산하면 몫만 남는다. 평균처럼 소수점이 필요하면 `double`을 사용하거나 형변환을 고려해야 한다.
- `++x`는 먼저 증가하고 식에 참여하지만, `x++`는 현재 값을 먼저 사용한 뒤 증가한다.
- `String`은 수업 초반에는 “문자열형”으로 다루지만, 실제로는 객체/참조 자료형이다.
- `++x`와 `x++`를 단독문으로 쓰면 최종값은 같지만, 다른 연산식 안에서는 **식에 사용되는 값의 시점**이 다르다.
- 복합 대입은 기존 값을 읽어 계산한 뒤 같은 변수에 다시 쓰는 연산이다.

## 관련 페이지

- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-operators|Java 연산자]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]

## 출처

- `raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md`
- `raw/KoreaICT/1. Java/2026.02.27(금)/1번 문제.png`
- `raw/KoreaICT/1. Java/2026.02.27(금)/2번 문제.png`
- `raw/KoreaICT/1. Java/2026.02.27(금)/3번 문제.png`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
