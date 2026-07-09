---
title: Java 조건 판단
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.03(화)/2026.03.03(화).md
  - raw/KoreaICT/1. Java/2026.03.04(수)/2026.03.04(수).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 조건 판단

## 정의

Java 조건 판단은 비교·논리 연산자와 `if`, `else`, `switch`, 삼항 연산자를 이용해 실행 흐름을 나누는 것이다.

## 왜 중요한가

프로그램은 단순히 위에서 아래로만 실행되지 않는다. 점수가 몇 점인지, 숫자가 짝수인지, 사용자가 어떤 메뉴를 입력했는지에 따라 다른 코드를 실행해야 하므로 조건 판단이 필요하다.

## 핵심 설명

### 조건식

조건식은 최종 결과가 `boolean`인 식이다.

```java
su % 2 == 0
jumsu >= 90
x > y && y > 0
```

### `if` 계열

- 단순 `if`: 참일 때만 실행
- `if~else`: 둘 중 하나 선택
- `else if`: 여러 구간 중 하나 선택

### `switch`

`switch`는 특정 값에 맞는 `case`부터 실행한다. `break`가 없으면 아래 case까지 이어질 수 있다.

### 삼항 연산자

```java
String result = x % 2 == 0 ? "짝수" : "홀수";
```

짧은 값 선택에는 유용하지만, 조건이 복잡하면 `if`가 더 읽기 쉽다.

## 수업 예시

- 두 숫자 중 큰 수 고르기
- 홀짝 판별
- 학점 판정
- `switch`로 특정 값에 따른 출력 분기

## 자주 헷갈리는 점

- `else if`는 별도 메서드가 아니라 `else` 뒤에 `if`가 붙은 구조다.
- `switch`에서 `break`를 빼면 의도하지 않은 case까지 실행될 수 있다.
- 삼항 연산자의 참/거짓 결과값은 대입될 변수 타입과 호환되어야 한다.

## 관련 개념

- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-loop|Java 반복문]]
- [[summaries/2026-03-04-java-control-flow|2026-03-04 Java 제어문과 조건문]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.03(화)/2026.03.03(화).md`
- `raw/KoreaICT/1. Java/2026.03.04(수)/2026.03.04(수).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
