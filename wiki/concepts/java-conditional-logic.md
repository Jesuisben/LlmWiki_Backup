---
title: Java 조건 판단
created: 2026-06-30
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md
  - raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md
status: growing
confidence: high
---

# Java 조건 판단

## 정의

Java 조건 판단은 프로그램이 상황에 따라 다른 코드를 실행하도록 만드는 방식이다. 수업에서는 먼저 비교 연산자와 논리 연산자로 `true`/`false`를 만드는 법을 배우고, 그 결과를 삼항 연산자, `if`, `if~else`, `else if`, `switch`에 연결했다.

## 왜 중요한가

개발에서 조건 판단은 “사용자가 어떤 값을 입력했는가”, “로그인한 사용자가 관리자인가”, “점수가 어느 구간에 속하는가”, “상품이 품절인가”처럼 거의 모든 로직의 갈림길이 된다. 이 수업에서는 단순히 문법을 외우기보다, 조건식이 실행 흐름을 어떻게 바꾸는지 확인하는 데 초점이 있었다.

## 수업에서 배운 흐름

1. `4 < 5`, `3 != 6`처럼 비교 연산자로 boolean 결과를 만든다.
2. `&&`, `||`, `!`로 여러 조건을 조합한다.
3. 삼항 연산자로 “값 하나를 선택”한다.
4. `if`로 조건이 참일 때만 실행한다.
5. `if~else`로 두 갈래 중 하나를 고른다.
6. `else if`로 여러 구간 중 하나를 고른다.
7. `switch`로 특정 값에 따른 분기를 만든다.

## 핵심 설명

### 조건식은 boolean으로 끝난다

조건식은 결국 `true` 또는 `false`가 되는 식이다. 예를 들어 3월이 봄인지 판단하는 실습에서는 다음처럼 범위를 조건식으로 만들었다.

```java
int month = 3;
boolean result = month >= 3 && month <= 5;
System.out.println("result : " + result);
```

여기서 `month >= 3`과 `month <= 5`가 둘 다 참이어야 봄이라고 판단한다. 즉 `&&`는 “둘 다 참”이라는 조건을 만든다. ^[raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md]

### 삼항 연산자는 실행문보다 “값 선택”에 가깝다

수업에서는 큰 수 고르기, 홀짝 판단, 3의 배수 처리, 계절 판단을 삼항 연산자로 연습했다.

```java
int x = 10, y = 20;
int result = x >= y ? x : y;

String 홀짝 = (x % 2) == 0 ? "짝수" : "홀수";
```

중요한 점은 `?` 뒤의 참일 때 값과 `:` 뒤의 거짓일 때 값이 결국 변수에 들어간다는 것이다. 그래서 대입받는 변수의 타입과 두 결과 값의 타입이 맞아야 한다. ^[raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md]

### if는 “조건이 참이면 실행”이다

`if`의 중괄호 안 코드는 조건식이 참일 때만 실행된다. 수업에서는 `su % 2 == 0`으로 짝수를 판단했다.

```java
int su = 4;

if (su % 2 == 0) {
    System.out.println(su + "는 짝수입니다.");
}

System.out.println("나는 무조건 실행 됩니다.");
```

마지막 출력문은 `if` 바깥에 있으므로 조건과 상관없이 실행된다. 이 예제는 중괄호 안과 밖의 차이를 보여준다. ^[raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md]

### else if는 위에서부터 처음 맞는 조건 하나만 고른다

학점 매기기 예제에서는 점수 구간을 높은 점수부터 검사했다.

```java
int jumsu = 75;

if (jumsu >= 90) {
    System.out.println("A 학점");
} else if (jumsu >= 80) {
    System.out.println("B 학점");
} else if (jumsu >= 70) {
    System.out.println("C 학점");
} else if (jumsu >= 60) {
    System.out.println("D 학점");
} else {
    System.out.println("F 학점");
}
```

`75`는 `>= 70`에서 처음 참이 되므로 `C 학점`만 출력된다. 뒤의 조건은 더 이상 검사하지 않는다. ^[raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md]

### switch는 break가 없으면 아래 case까지 계속 흐른다

수업에서 강조한 차이는 `if`는 조건 하나를 만족하면 해당 블록만 실행하지만, `switch`는 맞는 `case`를 만난 뒤 `break`가 없으면 아래 case까지 이어질 수 있다는 점이다.

```java
switch (su) {
    case 1:
    case 3:
    case 5:
        System.out.println("홀수");
        break;
    case 2:
    case 4:
    case 6:
        System.out.println("짝수");
        break;
    default:
        System.out.println("잘못된 숫자 형식입니다.");
}
```

같은 결과를 내는 여러 `case`를 묶을 수 있지만, 의도적으로 이어지게 하는 경우가 아니라면 `break`를 빠뜨리지 않는 것이 중요하다. ^[raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md]

## 자주 헷갈리는 점

### `==`와 `=`는 다르다

- `=`는 값을 대입한다.
- `==`는 두 값이 같은지 비교한다.

조건식 안에서는 보통 비교가 필요하므로 `==`, `!=`, `<`, `>=` 같은 비교 연산자를 써야 한다.

### 삼항 연산자와 if는 용도가 다르다

삼항 연산자는 간단히 값 하나를 고를 때 적합하다.

```java
String result = x % 2 == 0 ? "짝수" : "홀수";
```

반대로 여러 문장을 실행하거나 로직이 길어지면 `if~else`가 더 읽기 좋다.

### switch의 `default`는 if의 `else`와 비슷하지만 break 흐름을 함께 봐야 한다

`default`는 어떤 `case`에도 맞지 않을 때 실행되는 기본 분기다. 다만 `switch` 전체에서는 `case`와 `break`의 흐름이 중요하므로, `default`만 if의 `else`처럼 외우면 부족하다.

## 이전/이후 학습과의 연결

- 이전: [[concepts/java-operators|Java 연산자]]에서 비교·논리·조건 연산자를 배웠다.
- 같은 흐름: [[concepts/java-loop|Java 반복문]]에서는 조건식이 반복 지속 여부를 결정한다.
- 이후: Spring/React 프로젝트에서는 로그인 권한, 관리자 버튼 표시, 재고 검증 같은 로직이 모두 조건 판단으로 구현된다.

## 관련 개념

- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-loop|Java 반복문]]
- [[summaries/2026-03-03-java-logic-ternary|2026-03-03 Java 논리 연산자와 조건 연산자]]
- [[summaries/2026-03-04-java-control-flow|2026-03-04 Java 제어문과 조건문]]

## 출처

- `raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md`
- `raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md`
