---
title: 2026-03-04 Java 제어문과 조건문
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.03.04(수)/2026.03.04(수).md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-04 Java 제어문과 조건문

## 한 줄 요약

`if`, `else if`, `switch`로 실행 흐름을 나누고, `printf`의 서식 지정자로 조건 판단 결과를 한 문장에 출력했다.

## 커리큘럼 위치

- 전날 배운 비교/논리/삼항 연산자의 결과를 실제 실행 분기 조건으로 사용하는 단계다.
- 다음날 [[summaries/2026-03-05-java-for-while|반복문]]과 함께 제어문 전체 구조가 완성된다.

## 배운 내용

- 제어문은 조건문/반복문/보조 제어문으로 나눌 수 있다.
- 단순 `if`: 조건이 참일 때만 실행한다.
- `if~else`: 경우의 수가 둘일 때 사용한다.
- `else if`: 점수 학점처럼 여러 구간 중 하나를 선택할 때 사용한다.
- `switch`: 특정 값에 따라 `case`를 찾아 실행하며, `break`가 없으면 아래 case까지 이어질 수 있다.
- `printf`: `%s`, `%d`, `%f`, `%.3f`처럼 값의 출력 형식을 지정하며 자동 줄바꿈은 하지 않는다.

## 핵심 실습 / 예제

대표 학점 실습은 `jumsu = 75`를 입력값처럼 두고 `90 → 80 → 70 → 60` 순서로 조건을 검사해 처음 참이 되는 `C 학점`을 출력했다. 조건 범위를 위에서 아래로 좁혀 가기 때문에 순서를 바꾸면 판정이 달라질 수 있다.

`switch` 실습은 `su = 5`에 맞는 `case 5`에서 `홀수`를 출력하고 `break`로 종료했다. 이어 `case 1: case 3: case 5:`를 한 실행문에 묶어 여러 값이 같은 결과로 합류하는 흐름도 확인했다.

오후 종합 문제는 이름·과목 점수 → 총점·평균 계산 → `if/else if`로 학점 결정 → `switch`로 학점별 메시지나 경품 결정 → `printf`로 결과 출력 순서로 오전의 분기 문법과 출력 형식을 결합했다. `average = 74.666...`을 `%f`로 출력하면 `74.666667`, `%.3f`로 출력하면 `74.667`이 되는 것도 확인했다.

## 헷갈린 점 / 질문

- `else if`는 별도 메서드가 아니라 `else` 뒤에 또 다른 `if`를 붙인 구조로 이해하면 된다.
- `switch`는 맞는 `case`를 찾은 뒤 `break`를 만날 때까지 계속 내려갈 수 있으므로, 의도하지 않은 fall-through를 조심해야 한다.
- 조건식은 최종적으로 `true`/`false`가 되어야 한다.
- `if`, `switch`, `break`는 메서드가 아니라 각각 조건/선택/보조 제어문에 쓰이는 문법과 키워드다.
- `println`은 출력 후 줄바꿈하고, `printf`는 형식 지정 출력이지만 줄바꿈 문자를 직접 넣지 않으면 다음 출력이 이어진다.

## 관련 페이지

- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-loop|Java 반복문]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.04(수)/2026.03.04(수).md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
