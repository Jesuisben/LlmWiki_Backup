---
title: Java 반복문
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.05(목)/2026.03.05(목).md
  - raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java 반복문

## 정의

반복문은 같은 코드를 조건이 만족되는 동안 여러 번 실행하는 제어문이다. 수업에서는 `for`, `while`, `while(true)`, 향상된 for문을 순서대로 배웠다.

## 왜 중요한가

합계 계산, 입력 반복, 배열 전체 출력처럼 같은 동작을 여러 번 수행해야 하는 상황은 거의 모든 프로그램에서 반복된다.

## 핵심 설명

### `for`

```java
for (int i = 1; i < 11; i++) {
    total += i;
}
```

초기식, 조건식, 증감식이 한 줄에 모여 있어 반복 횟수가 비교적 명확할 때 좋다.

### `while`

```java
while (i < 11) {
    total += i;
    i++;
}
```

조건이 참인 동안 반복한다. 초기식과 증감식 위치를 직접 관리해야 한다.

### 무한 반복과 `break`

`while(true)`는 입력을 계속 받다가 정답을 맞히거나 음수 입력 같은 종료 조건을 만나면 `break`로 빠져나오는 방식으로 사용했다.

### 향상된 for

```java
for (String item : bts) {
    System.out.println(item);
}
```

배열/컬렉션의 모든 요소를 순서대로 볼 때 간결하다.

## 수업 예시

- 1부터 10까지 `total += i`로 누적해 `55` 출력.
- 배열에 입력받은 정수를 홀수/짝수로 나누어 각각 누적.
- `while(true)`에서 숫자를 입력받아 정답이면 `break`, 아니면 크다/작다 힌트 출력.
- 음수 입력 전까지 점수를 누적한 뒤 개수로 나누어 평균 계산.
- `for (Beverage05 item : orderList)`로 부모 타입 객체 배열을 순회하고 실제 객체의 `drink()` 호출.

## 자주 헷갈리는 점

- 반복문 안에서 선언한 변수는 반복문 밖에서 사용할 수 없다.
- 누적 변수는 재사용 전 초기화해야 한다.
- 향상된 for문은 인덱스가 필요 없는 조회에 적합하고, 특정 인덱스 수정에는 일반 for문이 적합하다.
- `for` 안의 `i`를 밖에서 못 쓰는 이유는 반복이 끝나서가 아니라 블록 scope 안에 선언했기 때문이다.
- 무한 반복에는 도달 가능한 종료 조건이 있어야 한다. 점수 입력이 한 번도 성공하지 않은 상태라면 평균 계산 전에 개수가 0인지도 확인해야 한다.
- 향상된 for는 모든 요소를 순회하는 문법이지 FIFO 자료구조를 구현하는 문법이 아니다.
- `do-while`, `continue`는 이 과목 raw에서 직접 학습한 중심 범위가 아니므로 본 수업 실습처럼 확대하지 않는다.

## 관련 개념

- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[comparisons/array-vs-collection|배열 vs 컬렉션]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.05(목)/2026.03.05(목).md`
- `raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
