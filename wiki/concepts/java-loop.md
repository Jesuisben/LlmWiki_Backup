---
title: Java 반복문
created: 2026-06-30
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md
  - raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md
  - raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md
status: growing
confidence: high
---

# Java 반복문

## 정의

Java 반복문은 같은 작업을 여러 번 실행하기 위한 제어문이다. 수업에서는 `for`, `while`, 무한 `while`, `break`, 그리고 배열·컬렉션을 순서대로 읽는 향상된 `for`까지 단계적으로 배웠다.

## 왜 중요한가

반복문은 “1부터 10까지 더하기” 같은 계산 연습에서 시작하지만, 실제 프로젝트에서는 배열·목록·DB 조회 결과·장바구니 상품처럼 여러 데이터를 한 번씩 처리할 때 계속 등장한다. 이후 JavaScript의 `forEach`, React의 배열 렌더링, Spring에서 여러 Entity를 DTO로 바꾸는 흐름과도 연결된다.

## 수업에서 배운 흐름

1. `for`로 반복 횟수가 명확한 합계 계산을 했다.
2. `if`와 함께 써서 홀수/짝수 합계를 한 번에 나눴다.
3. `while`로 같은 합계를 다른 형태로 구현했다.
4. `while(true)`와 `break`로 입력 기반 반복을 만들었다.
5. 배열을 배운 뒤 `arr.length`를 조건식에 사용했다.
6. 객체지향 수업에서 향상된 `for`로 배열 안 객체를 순서대로 출력했다.

## 핵심 설명

### for문은 반복 범위가 분명할 때 좋다

수업의 첫 반복문 예제는 1부터 10까지의 합계였다.

```java
int total = 0;

for (int i = 1; i < 11; i++) {
    total += i;
}

System.out.println("총합01 : " + total);
```

여기서 `i`는 제어변수다.

- 초기식: `int i = 1` — 어디서 시작할지 정한다.
- 조건식: `i < 11` — 언제까지 반복할지 정한다.
- 증감식: `i++` — 한 번 반복 후 제어변수를 어떻게 바꿀지 정한다.

수업 노트에서는 `total`과 `i`가 어떻게 변하는지 직접 풀어 써서, 반복문이 “마법처럼 도는 문법”이 아니라 같은 계산을 자동으로 반복하는 구조임을 확인했다. ^[raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md]

### 반복문과 조건문을 합치면 여러 결과를 한 번에 계산할 수 있다

홀수와 짝수의 합을 따로 구할 때, for문 두 개를 쓸 수도 있지만 하나의 for문 안에서 `if`로 나눌 수도 있다.

```java
int odd = 0, even = 0;

for (int i = 1; i < 11; i += 1) {
    if (i % 2 == 0) {
        even += i;
    } else {
        odd += i;
    }
}
```

이 예제는 [[concepts/java-conditional-logic|Java 조건 판단]]과 반복문이 실제로 함께 쓰이는 대표 사례다. ^[raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md]

### while문은 조건을 먼저 보고 계속할지 결정한다

`while`은 초기식, 조건식, 증감식이 한 줄에 모여 있지 않다.

```java
int total = 0;
int i = 1;

while (i < 11) {
    total += i;
    i++;
}
```

그래서 `while`에서는 증감식을 빠뜨리면 무한 반복이 되기 쉽다. 반대로 사용자의 입력처럼 언제 끝날지 코드 작성 시점에 정확히 모르는 상황에는 `while`이 잘 맞는다. ^[raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md]

### 무한 while은 break와 함께 설계해야 한다

숫자 맞히기 실습에서는 `while(true)`로 계속 입력을 받고, 정답을 맞히면 `break`로 반복을 종료했다.

```java
while (true) {
    System.out.println("1부터 100사이의 정수 1개 입력하세요");
    int input = scan.nextInt();

    if (answer == input) {
        System.out.println("정답입니다.");
        break;
    } else if (answer > input) {
        System.out.println(input + "보다 큰 수입니다.");
    } else {
        System.out.println(input + "보다 작은 수입니다.");
    }
}
```

이 구조는 “계속 묻다가 특정 조건이 되면 종료”하는 프로그램의 기본 모양이다. 점수를 계속 입력받다가 음수가 들어오면 종료하고 평균을 계산하는 실습도 같은 패턴이다. ^[raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md]

### 배열과 반복문은 거의 한 세트다

배열은 인덱스가 0부터 시작하므로 반복문 조건에 `배열이름.length`를 자주 쓴다.

```java
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

이 방식은 배열 길이가 바뀌어도 반복 범위를 자동으로 맞출 수 있다. 수업에서는 `int[] arr`, `String[] bts`, 점수 배열을 반복문으로 출력하거나 합산했다. ^[raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md]

### 향상된 for문은 전체를 순서대로 볼 때 간결하다

3월 12일 수업에서는 배열·컬렉션의 요소를 처음부터 끝까지 하나씩 꺼낼 때 향상된 `for`를 사용한다고 정리했다.

```java
for (String item : bts) {
    System.out.println(item);
}
```

일반 `for`는 인덱스 번호가 중요하거나 일부만 건너뛰어야 할 때 유리하고, 향상된 `for`는 전체 요소를 순서대로 읽을 때 간결하다. 이후 객체 배열 `Beverage05[] orderList`를 출력할 때도 같은 방식이 사용됐다. ^[raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md]

## 자주 헷갈리는 점

### `i < 11`과 `i <= 10`은 같은 범위를 만들 수 있다

1부터 10까지 반복할 때 `i < 11`과 `i <= 10`은 결과가 같다. 중요한 것은 시작값, 종료 조건, 증감식이 함께 어떤 숫자들을 만들고 있는지 직접 추적하는 것이다.

### 누적 변수는 반복문 밖에서 초기화한다

합계를 구할 때 `total = 0`을 반복문 안에 두면 매 반복마다 초기화되어 누적이 되지 않는다. 수업에서도 기존 `total`을 재사용할 때는 반복문 전에 다시 `0`으로 초기화했다.

### while에서는 증감식 위치를 놓치기 쉽다

`for`는 증감식이 괄호 안에 있어 눈에 잘 보이지만, `while`은 본문 안에 직접 넣어야 한다. 입력 기반 반복이 아니라 숫자 증가/감소 반복이라면 특히 무한 루프를 조심해야 한다.

## 관련 개념

- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[concepts/java-array|Java 배열]]
- [[summaries/2026-03-04-java-control-flow|2026-03-04 Java 제어문과 조건문]]
- [[summaries/2026-03-05-java-for-while|2026-03-05 Java for문과 while문]]
- [[summaries/2026-03-06-java-while-array|2026-03-06 Java 무한 while과 배열]]
- [[summaries/2026-03-12-java-abstract-interface-static|2026-03-12 Java 추상 클래스, 인터페이스, static/final]]

## 출처

- `raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md`
- `raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md`
- `raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
